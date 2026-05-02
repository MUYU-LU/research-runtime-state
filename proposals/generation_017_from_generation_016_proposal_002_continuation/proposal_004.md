# Proposal 004: Body-order-conditioned scalar-state PaiNN update

- family: painn_body_to_scalar_update
- phase: 4
- jump_type: jump
- budget_class: small
- expected_capability_gain: Move the vector-conditioned body-order signal into the final scalar state so both the main readout and body-order residual can improve ISO17 energy calibration.

## one_sentence_hypothesis
A single near-zero scalar-state update from `[scalar_state, body_order_descriptor, ||Vv||, <Uv,Vv>]` will couple explicit body-order geometry with learned vector context more effectively than leaving body-order as a side residual only.

## mechanism_refs
- GEN017-M01-painn-style-scalar-vector-mixing-gate

## evidence_refs
- mechanism_cards.json::GEN017-M01 formula_derivation maps PaiNN scalar update to current vector contractions
- mechanism_cards.json::GEN017-M01 data_flow says new gate can read vector_state through scalar contractions while preserving invariance
- patch_blueprints.json::GEN017-M01 implementation-ready target files and insertion points
- benchmark_diagnosis.json::source Q_total=3.9425481167873127 and ISO17 energy_trend=worsening
- evidence_provenance.json::repo_artifact:repo_002 SchNetPack PaiNNMixing.forward code trace

## historical_relation
- source_unit: generation_016/proposal_002
- relation_to_source: jump
- not_a_duplicate_of: Source appends body-order as a separate residual after the main scalar readout; this injects a bounded body/vector-conditioned update into `scalar_state` before the final source readout.
- lesson_used: A side branch alone produced neutral variance; a stronger but still local jump tests whether the main energy readout needs access to the explicit body-order/vector coupling.

## why_not_duplicate
This is not an electrostatic/nonlocal jump from generation_016, not a new CACE tensor hierarchy, and not the exploit descriptor gate. It changes the integration point: body-order/vector features update `scalar_state` before `readout_scalar_update`/`readout`, with near-zero initialization.

## benchmark_rationale
- rmd17 energy: Moderate risk because main scalar readout is touched; near-zero initialization should protect source behavior.
- rmd17 force: Risk is higher than proposals 001-003 but still bounded and conservative through energy.
- rmd17 gap / Q: Expected neutral if the update remains small; reject if RMD17 Q falls outside control variance.
- iso17 energy: May improve more than residual-only gates by letting final scalar energy use body-order context directly.
- iso17 force: Could improve if scalar state learns smoother geometry; could regress if update overfits energy.
- iso17 gap / Q: Main target is lower mixed_energy_mae and gap penalty.
- training stability / runtime risk: Small/medium overhead; no new edge loops.
- control comparison expectation: Should outperform residual-only gates only if side-readout isolation was the bottleneck.

## files_to_edit
- `model/model.py`
- `model/train.py`: none expected
- never `config.json` for MLIP-quality changes

## code_insertion_points
- `model/model.py::EvolutionMLIP.__init__`: add optional `body_descriptor_to_hidden = nn.Linear(descriptor_dim, hidden_dim)` and `scalar_body_vector_update` MLP from `[scalar_state, projected_body, norm_v, dot_uv]` to hidden_dim plus a small learnable scale.
- `model/model.py::EvolutionMLIP.forward_energy`: after interactions and vector contractions, before the existing `vector_norm = ...` readout block, add `scalar_state = readout_norm(scalar_state + small_scale * delta_scalar)`.
- `model/train.py::none`: do not alter loss weights or warmup.

## minimal_edit_plan
1. Project `body_order_descriptor` to hidden_dim and compute M01 vector invariants after interaction blocks.
2. Build a near-zero scalar update MLP and add it to `scalar_state` before the existing readout scalar update.
3. Keep the original `body_order_readout` residual path unchanged so the jump is only the added scalar-state coupling.

## implementation_checklist
- [ ] Preserve `E = sum_i E_i` and force-from-energy contract.
- [ ] Preserve benchmark metric field names and runnable entrypoint contract.
- [ ] Modify only the allowed target unit files.
- [ ] Do not edit `config.json`; change MLIP knobs in `model/model.py` or `model/train.py`.
- [ ] Keep tensor shapes compatible with current dataloader and model forward.
- [ ] Add no unbounded cubic neighbor/triplet loops unless explicitly justified by budget.
- [ ] Initialize the scalar update as a near no-op.
- [ ] Do not change body-order descriptor size or training objective.
- [ ] Call `mark_unit_implemented.py --unit <UNIT> --actor implementation_subagent` after edits.

## expected_benchmark_effect
- primary expected gain: Larger ISO17 energy/gap improvement than residual-only gating.
- expected tradeoff: Greater chance of perturbing RMD17 energy/force because the main readout path changes.
- failure signal that would falsify this proposal: RMD17 Q regression without clear ISO17 Q gain, especially compared with proposals 001-003.

## ablation_or_control
- required control or comparison: Exact source and at least one residual-only gate if selected.
- optional zero-gate / source-fallback / readout-only ablation: Set scalar update scale to zero.

## implementation_notes_for_subagent
Keep the jump one update layer only. Do not rewrite `BalancedInteractionBlock`; this is a post-interaction scalar-state adapter using existing descriptor/vector tensors.
