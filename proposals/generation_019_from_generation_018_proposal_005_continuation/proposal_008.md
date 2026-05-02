# Proposal 008: Exact source replicate control

- family: control_replicate
- phase: 0
- jump_type: control
- budget_class: tiny
- expected_capability_gain: Measure run variance for generation_018/proposal_005 before attributing small generation_019 deltas to mechanisms.

## one_sentence_hypothesis
An unchanged copy of the source should reproduce the frontier envelope and anchor whether proposal deltas over Q_total=4.049988 are meaningful.

## mechanism_refs
- []

## evidence_refs
- generation_018/proposal_005 current source unit
- benchmark_diagnosis.json source metrics
- round policy control requirement
- generation_018/proposal_008 control replicate variance: Q_total=3.931143 from older parent

## historical_relation
- source_unit: generation_018/proposal_005
- relation_to_source: control
- not_a_duplicate_of: This is intentionally an exact replicate of generation_018/proposal_005, not a new mechanism; it is required to interpret small gains/losses.
- lesson_used: Prior control replicates show nontrivial variance; a source-specific control is needed because the continuation source changed to proposal_005.

## why_not_duplicate
This is intentionally an exact replicate of generation_018/proposal_005, not a new mechanism; it is required to interpret small gains/losses. The source unit is already a frontier win, so this proposal is deliberately scoped around preserving its explicit scalar-vector tensor-product signal unless the proposal is the exact control or backward-simplification branch.

## benchmark_rationale
Current source generation_018/proposal_005 is the best-known unit: Q_total=4.049988, Q_rmd17=4.199739, Q_iso17=3.771881, G_delta=+0.107440 over generation_016/proposal_002. RMD17 is already strong (mixed_energy_mae=0.029077, mixed_force_mae=0.060116, gap_penalty=0.007114). ISO17 remains the main headroom (mixed_energy_mae=0.244736, mixed_force_mae=0.149781, gap_penalty=0.145198). Generation_018/proposal_003 showed a nearby product-basis branch can approach the frontier (Q_total=4.025879) mostly through ISO17 force/geometry, while first-layer-only TP and RoPE variants regressed Q_total. The control from generation_018/proposal_008 reached Q_total=3.931143, so small gains must clear source variance rather than only beat the old parent.
- capacity/scaling hypothesis, if any: No capacity or objective change.
- rmd17 energy: Source mixed_energy_mae is 0.029077 with improving train/val energy; proposal should not regress this beyond neutral variance.
- rmd17 force: Source mixed_force_mae is 0.060116 and is the strongest part of the branch; any force regression must be treated as a failure unless Q_total improves clearly and gap is controlled.
- rmd17 gap / Q: Source gap_penalty is 0.007114 and Q_dataset/Q_rmd17 is 4.199739; preserve this as the benchmark anchor.
- iso17 energy: Source mixed_energy_mae is 0.244736 with within/other energy split 0.212976/0.265909; this is the main improvement target.
- iso17 force: Source mixed_force_mae is 0.149781; keep neutral-to-positive force behavior and avoid force-only gains that worsen energy.
- iso17 gap / Q: Source gap_penalty is 0.145198 and Q_dataset/Q_iso17 is 3.771881; useful proposals should lower gap or raise Q_iso17 without harming Q_rmd17.
- training stability / runtime risk: Expected to match source energy/force/gap/Q within run variance; any large deviation flags training/runtime variance rather than mechanism effect.
- control comparison expectation: Compare against proposal_008 exact source replicate and the source metrics above; Q_total must be interpreted relative to control variance, not force-only ranking.

## files_to_edit
- none

## code_insertion_points
- none

## minimal_edit_plan
1. Exact copy of source unit generation_018/proposal_005.
2. Do not edit `model/model.py`.
3. Do not edit `model/train.py`.
4. Mark implemented as a control replicate if required by workflow.

## implementation_checklist
- [ ] Do not change `model/model.py`.
- [ ] Do not change `model/train.py`.
- [ ] Preserve benchmark metric field names and runnable entrypoint contract.
- [ ] Mark implemented as a control replicate if required by workflow.
- [ ] Call `mark_unit_implemented.py --unit <UNIT> --actor implementation_subagent` after control materialization.

## expected_benchmark_effect
- primary expected gain: Primary expected result is a variance anchor near Q_rmd17=4.199739, Q_iso17=3.771881, Q_total=4.049988. Falsified only as a control if smoke/launch fails or metrics drift far from source.
- expected tradeoff: Runtime, memory, or optimization risk must be judged against Q_dataset/Q_rmd17/Q_iso17/Q_total, not a single force metric. For tiny/control proposals the tradeoff should be interpretability rather than capacity.
- failure signal that would falsify this proposal: Q_total below the source/control envelope, RMD17 force or energy regression beyond neutral variance, ISO17 gap_penalty worse without compensating Q gain, smoke/runtime failure, or loss of force-from-energy behavior.

## ablation_or_control
- required control or comparison: This is the required control for all rank2/CACE/scaling/training proposals.
- optional zero-gate / source-fallback / readout-only ablation: Keep every new residual source-recoverable by a zero/very-negative gate when the proposal includes a branch; for control, no ablation beyond exact copy is needed.

## implementation_notes_for_subagent
No file edits. Implementation subagent should only perform the workflow marking needed for a control replicate. Implement only inside the materialized target unit. Do not edit global round state, proposal files, selection files, benchmark data, evaluator code, or `config.json` for MLIP quality. Preserve the generation_018/proposal_005 tensor shapes: scalar_state `[N,H]`, vector_state `[N,H,3]`, edge basis `[E,num_rbf]`, energy scalar, forces `[N,3]` by autograd.
