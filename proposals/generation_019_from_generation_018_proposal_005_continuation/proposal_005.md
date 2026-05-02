# Proposal 005: CACE ν=2 descriptor consistency side branch

- family: cace_nu2_descriptor_consistency
- phase: 3
- jump_type: jump
- budget_class: small
- expected_capability_gain: Tighten the existing body-order side branch into a CACE-consistent ν=2 invariant descriptor while preserving the TP main path.

## one_sentence_hypothesis
A formula-grounded CACE A/B descriptor in BodyOrderMessageBranch can reduce ISO17 energy/gap errors as a small invariant residual without disturbing the scalar-vector TP force mechanism.

## mechanism_refs
- GEN019-M02-cace-nu2-ab-consistency

## evidence_refs
- mechanism_cards.json::GEN019-M02-cace-nu2-ab-consistency
- paper_artifact:paper_002 CACE A/B ν=2 basis extraction
- repo_artifact:repo_002 cace/modules/angular.py product_basis.py symmetrize_basis.py interaction.py
- repo_artifact:repo_003 mace/modules/symmetric_contraction.py
- benchmark_diagnosis.json current ISO17 gap headroom

## historical_relation
- source_unit: generation_018/proposal_005
- relation_to_source: jump
- not_a_duplicate_of: Not generation_018/proposal_003, which inserted a learned symmetric contraction against generation_016/proposal_002; this starts from proposal_005 and explicitly preserves its winning TPInteractionBranch while tightening the already-present body_order branch.
- lesson_used: Product-basis contraction was a partial frontier win but energy remained high; keep it smaller, documented, and residual rather than letting it dominate the TP path.

## why_not_duplicate
Not generation_018/proposal_003, which inserted a learned symmetric contraction against generation_016/proposal_002; this starts from proposal_005 and explicitly preserves its winning TPInteractionBranch while tightening the already-present body_order branch. The source unit is already a frontier win, so this proposal is deliberately scoped around preserving its explicit scalar-vector tensor-product signal unless the proposal is the exact control or backward-simplification branch.

## benchmark_rationale
Current source generation_018/proposal_005 is the best-known unit: Q_total=4.049988, Q_rmd17=4.199739, Q_iso17=3.771881, G_delta=+0.107440 over generation_016/proposal_002. RMD17 is already strong (mixed_energy_mae=0.029077, mixed_force_mae=0.060116, gap_penalty=0.007114). ISO17 remains the main headroom (mixed_energy_mae=0.244736, mixed_force_mae=0.149781, gap_penalty=0.145198). Generation_018/proposal_003 showed a nearby product-basis branch can approach the frontier (Q_total=4.025879) mostly through ISO17 force/geometry, while first-layer-only TP and RoPE variants regressed Q_total. The control from generation_018/proposal_008 reached Q_total=3.931143, so small gains must clear source variance rather than only beat the old parent.
- capacity/scaling hypothesis, if any: Small descriptor change; preserves hidden_dim=96, num_interactions=2, num_rbf=32.
- rmd17 energy: Source mixed_energy_mae is 0.029077 with improving train/val energy; proposal should not regress this beyond neutral variance.
- rmd17 force: Source mixed_force_mae is 0.060116 and is the strongest part of the branch; any force regression must be treated as a failure unless Q_total improves clearly and gap is controlled.
- rmd17 gap / Q: Source gap_penalty is 0.007114 and Q_dataset/Q_rmd17 is 4.199739; preserve this as the benchmark anchor.
- iso17 energy: Source mixed_energy_mae is 0.244736 with within/other energy split 0.212976/0.265909; this is the main improvement target.
- iso17 force: Source mixed_force_mae is 0.149781; keep neutral-to-positive force behavior and avoid force-only gains that worsen energy.
- iso17 gap / Q: Source gap_penalty is 0.145198 and Q_dataset/Q_iso17 is 3.771881; useful proposals should lower gap or raise Q_iso17 without harming Q_rmd17.
- training stability / runtime risk: Primary target is ISO17 mixed_energy_mae=0.244736 and gap_penalty=0.145198; expected force effect is neutral-to-positive if residual remains damped.
- control comparison expectation: Compare against proposal_008 exact source replicate and the source metrics above; Q_total must be interpreted relative to control variance, not force-only ranking.

## files_to_edit
- `model/model.py`
- `model/train.py` if needed, otherwise `none`
- never `config.json` for MLIP-quality changes

## code_insertion_points
- `model/model.py::BodyOrderMessageBranch._angular_monomials`: explicitly document/order [1,x,y,z,x²,y²,z²,xy,xz,yz].
- `model/model.py::BodyOrderMessageBranch._symmetrize`: replace ad-hoc slices with CACE ν=1/ν=2 contractions and project back to descriptor_dim=128 if shape changes.
- `model/model.py::BodyOrderMessageBranch.forward`: keep edge_a and index_add flow; optionally add a tiny product-basis projection after atom_a normalization.
- `model/model.py::EvolutionMLIP.forward_energy`: keep `body_order_multiplier = 0.05*sigmoid(body_order_scale)` or smaller; do not change TP branches.

## minimal_edit_plan
1. Audit angular monomial order and l2 weighting.
2. Implement a bounded ν=2 descriptor using existing atom_a tensor, no explicit triplet enumeration.
3. If descriptor_dim changes, insert a near-zero/identity-style projection back to the old size for readout compatibility.
4. Leave TPInteractionBranch, readout_scalar_update, optimizer, and loss schedule unchanged.

## implementation_checklist
- [ ] Preserve `E = sum_i E_i` and force-from-energy contract.
- [ ] Preserve benchmark metric field names and runnable entrypoint contract.
- [ ] Modify only the allowed target unit files.
- [ ] Do not edit `config.json`; change MLIP knobs in `model/model.py` or `model/train.py`.
- [ ] Keep tensor shapes compatible with current dataloader and model forward.
- [ ] Add no unbounded cubic neighbor/triplet loops unless explicitly justified by budget.
- [ ] Preserve the existing scalar-vector `TPInteractionBranch` path unless this proposal is the explicit control/simplification case.
- [ ] Call `mark_unit_implemented.py --unit <UNIT> --actor implementation_subagent` after edits.

## expected_benchmark_effect
- primary expected gain: Expected Q_iso17 gain through energy/gap improvement; Q_rmd17 should remain near source. Runtime low-to-moderate because existing atom_a is reused. Falsified by repeating body-order tradeoffs: worse RMD17 force/energy or lower Q_total despite lower ISO17 gap.
- expected tradeoff: Runtime, memory, or optimization risk must be judged against Q_dataset/Q_rmd17/Q_iso17/Q_total, not a single force metric. For tiny/control proposals the tradeoff should be interpretability rather than capacity.
- failure signal that would falsify this proposal: Q_total below the source/control envelope, RMD17 force or energy regression beyond neutral variance, ISO17 gap_penalty worse without compensating Q gain, smoke/runtime failure, or loss of force-from-energy behavior.

## ablation_or_control
- required control or comparison: Disable product-basis projection while keeping angular audit to distinguish bug/consistency from expressivity; compare to source and generation_018/proposal_003 outcome.
- optional zero-gate / source-fallback / readout-only ablation: Keep every new residual source-recoverable by a zero/very-negative gate when the proposal includes a branch; for control, no ablation beyond exact copy is needed.

## implementation_notes_for_subagent
No e3nn/MACE import. Use pure torch `einsum` or tensor products over small radial/type/angular dims only. Implement only inside the materialized target unit. Do not edit global round state, proposal files, selection files, benchmark data, evaluator code, or `config.json` for MLIP quality. Preserve the generation_018/proposal_005 tensor shapes: scalar_state `[N,H]`, vector_state `[N,H,3]`, edge basis `[E,num_rbf]`, energy scalar, forces `[N,3]` by autograd.
