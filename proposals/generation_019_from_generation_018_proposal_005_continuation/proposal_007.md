# Proposal 007: TP-only body-order simplification control

- family: tp_only_body_simplify
- phase: 3
- jump_type: backward-simplify
- budget_class: tiny
- expected_capability_gain: Isolate how much of the frontier win comes from scalar-vector TP by reducing the body-order side branch influence.

## one_sentence_hypothesis
If generation_018/proposal_005 is mainly a TP win, shrinking or source-fallbacking the body-order readout should preserve much of Q_total and may reduce ISO17 energy/gap overfitting.

## mechanism_refs
- []

## evidence_refs
- benchmark_diagnosis.json source metrics
- generation_018_summary: proposal_005 TP frontier vs proposal_003 product-basis near-frontier
- tree_state family stats: low_rank_tensor_product_interaction one strong positive; body/product simplify neutral
- round policy requires backward-simplify axis

## historical_relation
- source_unit: generation_018/proposal_005
- relation_to_source: simplify
- not_a_duplicate_of: Not exact control because it changes only body_order residual influence; not generation_018/proposal_009 because it starts from the TP-winning source rather than simplifying the older parent body branch.
- lesson_used: Local many-body/body-order families have many mixed or negative outcomes; isolate the new TP signal before adding more body-order capacity.

## why_not_duplicate
Not exact control because it changes only body_order residual influence; not generation_018/proposal_009 because it starts from the TP-winning source rather than simplifying the older parent body branch. The source unit is already a frontier win, so this proposal is deliberately scoped around preserving its explicit scalar-vector tensor-product signal unless the proposal is the exact control or backward-simplification branch.

## benchmark_rationale
Current source generation_018/proposal_005 is the best-known unit: Q_total=4.049988, Q_rmd17=4.199739, Q_iso17=3.771881, G_delta=+0.107440 over generation_016/proposal_002. RMD17 is already strong (mixed_energy_mae=0.029077, mixed_force_mae=0.060116, gap_penalty=0.007114). ISO17 remains the main headroom (mixed_energy_mae=0.244736, mixed_force_mae=0.149781, gap_penalty=0.145198). Generation_018/proposal_003 showed a nearby product-basis branch can approach the frontier (Q_total=4.025879) mostly through ISO17 force/geometry, while first-layer-only TP and RoPE variants regressed Q_total. The control from generation_018/proposal_008 reached Q_total=3.931143, so small gains must clear source variance rather than only beat the old parent.
- capacity/scaling hypothesis, if any: Simplification: no new capacity; may reduce active residual contribution.
- rmd17 energy: Source mixed_energy_mae is 0.029077 with improving train/val energy; proposal should not regress this beyond neutral variance.
- rmd17 force: Source mixed_force_mae is 0.060116 and is the strongest part of the branch; any force regression must be treated as a failure unless Q_total improves clearly and gap is controlled.
- rmd17 gap / Q: Source gap_penalty is 0.007114 and Q_dataset/Q_rmd17 is 4.199739; preserve this as the benchmark anchor.
- iso17 energy: Source mixed_energy_mae is 0.244736 with within/other energy split 0.212976/0.265909; this is the main improvement target.
- iso17 force: Source mixed_force_mae is 0.149781; keep neutral-to-positive force behavior and avoid force-only gains that worsen energy.
- iso17 gap / Q: Source gap_penalty is 0.145198 and Q_dataset/Q_iso17 is 3.771881; useful proposals should lower gap or raise Q_iso17 without harming Q_rmd17.
- training stability / runtime risk: Expected to preserve RMD17 force if TP is sufficient. It may hurt ISO17 energy if body_order residual was necessary, which would be an informative falsification.
- control comparison expectation: Compare against proposal_008 exact source replicate and the source metrics above; Q_total must be interpreted relative to control variance, not force-only ranking.

## files_to_edit
- `model/model.py`
- `model/train.py` if needed, otherwise `none`
- never `config.json` for MLIP-quality changes

## code_insertion_points
- `model/model.py::EvolutionMLIP.__init__`: initialize `body_order_scale` lower (e.g. -6 or -7) or add a tiny learned cap for body_order_multiplier.
- `model/model.py::EvolutionMLIP.forward_energy`: keep body_order_descriptor computation for shape compatibility but multiply residual by the smaller cap; do not alter TP branches.
- `model/train.py`: no objective change.

## minimal_edit_plan
1. Keep `TPInteractionBranch` exactly as source.
2. Lower only `body_order_scale`/cap or introduce a source-fallback flag that makes body_order residual near zero at initialization.
3. Do not delete BodyOrderMessageBranch unless implementation can guarantee shape and smoke compatibility.
4. Measure whether Q_rmd17/Q_iso17 remain close to source despite lower body-order contribution.

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
- primary expected gain: If TP is dominant, Q_total should stay close to 4.049988 with possibly lower runtime/readout variance. If ISO17 Q drops, the body-order branch is still necessary. Falsified by clear regression in Q_rmd17, Q_iso17, or gap_penalty.
- expected tradeoff: Runtime, memory, or optimization risk must be judged against Q_dataset/Q_rmd17/Q_iso17/Q_total, not a single force metric. For tiny/control proposals the tradeoff should be interpretability rather than capacity.
- failure signal that would falsify this proposal: Q_total below the source/control envelope, RMD17 force or energy regression beyond neutral variance, ISO17 gap_penalty worse without compensating Q gain, smoke/runtime failure, or loss of force-from-energy behavior.

## ablation_or_control
- required control or comparison: Compare exact source and proposal_005 CACE enhancement; this is the low-complexity backward branch for interpretation.
- optional zero-gate / source-fallback / readout-only ablation: Keep every new residual source-recoverable by a zero/very-negative gate when the proposal includes a branch; for control, no ablation beyond exact copy is needed.

## implementation_notes_for_subagent
Because this is a bounded simplification, mechanism_refs is intentionally empty; it is diagnosis/control driven. Implement only inside the materialized target unit. Do not edit global round state, proposal files, selection files, benchmark data, evaluator code, or `config.json` for MLIP quality. Preserve the generation_018/proposal_005 tensor shapes: scalar_state `[N,H]`, vector_state `[N,H,3]`, edge basis `[E,num_rbf]`, energy scalar, forces `[N,3]` by autograd.
