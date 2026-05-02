# Proposal 002: One-step body-order message residual

- family: body_order_message_residual
- phase: 3
- jump_type: jump
- budget_class: medium
- expected_capability_gain: Test whether message-passed invariant descriptors improve ISO17 cross-conformer energy beyond a static body-order branch.

## one_sentence_hypothesis
Adding one bounded message update over compact A/B body-order descriptors will change the message passing path enough to improve ISO17 gap while retaining the source scalar/vector backbone as a stable fallback.

## mechanism_refs
- GEN016-M01-cace-shadow-body-order-representation

## evidence_refs
- paper_artifact:paper_001
- repo_artifact:repo_001
- mechanism_cards.json::GEN016-M01-cace-shadow-body-order-representation repo_code_trace MessageBchi/MessageAr
- patch_blueprints.json::GEN016-M01-cace-shadow-body-order-representation
- benchmark_diagnosis.json::generation_015/proposal_004 ISO17 mixed_energy_mae=0.29388116803717634, gap_penalty=0.09986681269946639
- current_code_profile.json::model/model.py current neighbor list and edge basis

## historical_relation
- source_unit: generation_015/proposal_004
- relation_to_source: jump
- not_a_duplicate_of: The source and recent generation_015 proposals adjust the local scalar/vector block or readout; this proposal adds a separate invariant descriptor message path before residual energy.
- lesson_used: Static local updates gave good force trends but did not stabilize ISO17 energy; a bounded message-passed descriptor may improve conformer transfer without a full rewrite.

## why_not_duplicate
Unlike proposal_001, this proposal is not just a static B-head. It adds a single descriptor-level edge message: source atom B/A features condition an edge projection that is scatter-added and re-normalized before the residual energy head.

## benchmark_rationale
- rmd17 energy: Expected mostly preserved by small residual scale.
- rmd17 force: Slightly higher risk than static branch because descriptor messages add edge-dependent gradients.
- rmd17 gap / Q: Should remain within tolerance if residual scale is damped.
- iso17 energy: May improve conformer calibration by letting body-order descriptors communicate across bonded/local neighborhoods.
- iso17 force: Potential improvement from better angular sensitivity; reject if force MAE worsens despite energy gains.
- iso17 gap / Q: Primary target is Q_iso17 via lower energy/gap penalties.
- training stability / runtime risk: Medium; use one message layer only and neighbor-count normalization.
- control comparison expectation: Should outperform static/no-message control if message-passed descriptors are useful.

## files_to_edit
- `model/model.py`
- `model/train.py`: none expected
- never `config.json` for MLIP-quality changes

## code_insertion_points
- `model/model.py::new BodyOrderMessageBranch`: create compact A/B features, edge MLP conditioned by sender descriptor, scatter message to receiver descriptor, normalize, and recompute/normalize B-like features.
- `model/model.py::EvolutionMLIP.__init__`: add branch, descriptor message MLP, residual readout, and damped scale after RBF setup/readout modules.
- `model/model.py::EvolutionMLIP.forward_energy`: compute branch after neighbor/RBF tensors are available and add residual scalar after source per-atom energy.
- `model/train.py::none`: keep current energy/force weights and optimizer defaults.

## minimal_edit_plan
1. Reuse compact angular/RBF/type edge features from the M01 blueprint to form atom-centered descriptors.
2. Add one edge message step where sender descriptor features pass through a small MLP, multiply by cutoff, scatter to receivers, and combine with original descriptors under LayerNorm.
3. Read out per-atom residual energy with near-zero scale and preserve all source model behavior when scale is zero.

## implementation_checklist
- [ ] Preserve `E = sum_i E_i` and force-from-energy contract.
- [ ] Preserve benchmark metric field names and runnable entrypoint contract.
- [ ] Modify only the allowed target unit files.
- [ ] Do not edit `config.json`; change MLIP knobs in `model/model.py` or `model/train.py`.
- [ ] Keep tensor shapes compatible with current dataloader and model forward.
- [ ] Add no unbounded cubic neighbor/triplet loops; descriptor message pass must be O(E * Bdim).
- [ ] Normalize by neighbor count to avoid molecule-size scale blow-up.
- [ ] Call `mark_unit_implemented.py --unit <UNIT> --actor implementation_subagent` after edits.

## expected_benchmark_effect
- primary expected gain: ISO17 energy/gap gains over the source and over static body-order residual if descriptor communication matters.
- expected tradeoff: More runtime and higher force-gradient risk than proposal_001.
- failure signal that would falsify this proposal: Runtime blow-up, unstable residual scale, or ISO17 force/energy both worse than source.

## ablation_or_control
- required control or comparison: Compare to source control and, if selected together, proposal_001 static branch.
- optional zero-gate / source-fallback / readout-only ablation: Set descriptor message MLP output to zero while retaining static B features.

## implementation_notes_for_subagent
Keep the message update one layer and local to the new branch. Do not alter `BalancedInteractionBlock`; the point is a parallel message path with an easy source fallback.
