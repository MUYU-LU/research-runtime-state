# Proposal 009: Force-stable ISO17 energy tail schedule

- family: training_objective_energy_tail
- phase: 2
- jump_type: wildcard
- budget_class: tiny
- expected_capability_gain: Test whether ISO17 energy/gap headroom is partly an objective-schedule issue while keeping the TP architecture fixed.

## one_sentence_hypothesis
A slightly longer, force-stable energy warmup/tail weighting can reduce ISO17 mixed_energy_mae and gap_penalty without changing benchmark semantics or weakening force supervision.

## mechanism_refs
- []

## evidence_refs
- benchmark_diagnosis.json: ISO17 val energy remains high while train energy improves; source train.py warmup uses 3 epochs
- research-skill training-objective policy
- generation_017/proposal_010 training diagnostic was not frontier, so this must be tiny and architecture-preserving
- current_code_profile.json train.py constants

## historical_relation
- source_unit: generation_018/proposal_005
- relation_to_source: ablation
- not_a_duplicate_of: Not a repeat of broad training-objective attempts because it is paired with the proven TP architecture and changes only a tiny schedule constant/weight curve; no model.py mechanism changes.
- lesson_used: Training-only changes are historically weak, but ISO17 energy/gap remains the main bottleneck; include exactly one small diagnostic wildcard.

## why_not_duplicate
Not a repeat of broad training-objective attempts because it is paired with the proven TP architecture and changes only a tiny schedule constant/weight curve; no model.py mechanism changes. The source unit is already a frontier win, so this proposal is deliberately scoped around preserving its explicit scalar-vector tensor-product signal unless the proposal is the exact control or backward-simplification branch.

## benchmark_rationale
Current source generation_018/proposal_005 is the best-known unit: Q_total=4.049988, Q_rmd17=4.199739, Q_iso17=3.771881, G_delta=+0.107440 over generation_016/proposal_002. RMD17 is already strong (mixed_energy_mae=0.029077, mixed_force_mae=0.060116, gap_penalty=0.007114). ISO17 remains the main headroom (mixed_energy_mae=0.244736, mixed_force_mae=0.149781, gap_penalty=0.145198). Generation_018/proposal_003 showed a nearby product-basis branch can approach the frontier (Q_total=4.025879) mostly through ISO17 force/geometry, while first-layer-only TP and RoPE variants regressed Q_total. The control from generation_018/proposal_008 reached Q_total=3.931143, so small gains must clear source variance rather than only beat the old parent.
- capacity/scaling hypothesis, if any: No architecture capacity change; training objective only.
- rmd17 energy: Source mixed_energy_mae is 0.029077 with improving train/val energy; proposal should not regress this beyond neutral variance.
- rmd17 force: Source mixed_force_mae is 0.060116 and is the strongest part of the branch; any force regression must be treated as a failure unless Q_total improves clearly and gap is controlled.
- rmd17 gap / Q: Source gap_penalty is 0.007114 and Q_dataset/Q_rmd17 is 4.199739; preserve this as the benchmark anchor.
- iso17 energy: Source mixed_energy_mae is 0.244736 with within/other energy split 0.212976/0.265909; this is the main improvement target.
- iso17 force: Source mixed_force_mae is 0.149781; keep neutral-to-positive force behavior and avoid force-only gains that worsen energy.
- iso17 gap / Q: Source gap_penalty is 0.145198 and Q_dataset/Q_iso17 is 3.771881; useful proposals should lower gap or raise Q_iso17 without harming Q_rmd17.
- training stability / runtime risk: Targets ISO17 mixed_energy_mae/gap; RMD17 force must not degrade because force_weight remains high and metric semantics are fixed.
- control comparison expectation: Compare against proposal_008 exact source replicate and the source metrics above; Q_total must be interpreted relative to control variance, not force-only ranking.

## files_to_edit
- `model/train.py`
- `model/model.py` if only needed to expose an optional aux loss; otherwise `none`
- never `config.json` for MLIP-quality changes

## code_insertion_points
- `model/train.py::train`: replace hard dependency on `CONFIG.get("energy_warmup_epochs",3)` with a code-level constant such as `TRAIN_ENERGY_WARMUP_EPOCHS=4` or a bounded epoch_energy_weight tail.
- `model/train.py::run_epoch`: preserve loss definition fields and metric names; do not alter evaluator metrics.
- `model/model.py`: no architecture changes; preserve TPInteractionBranch.

## minimal_edit_plan
1. Add explicit code-level constant `TRAIN_ENERGY_WARMUP_EPOCHS = 4` or equivalent in train.py.
2. Keep `TRAIN_FORCE_WEIGHT=20.0`; optionally use energy_weight tail of 1.05 only after warmup, capped and logged.
3. Ensure history still logs `energy_weight`, `force_weight`, `learning_rate`, and `grad_clip`.
4. Do not edit config.json or dataset/eval semantics.

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
- primary expected gain: Expected small ISO17 energy/gap improvement; possible tradeoff is worse force MAE or RMD17 Q if energy is overweighted. Falsified if Q_total falls, force metrics regress, or train instability appears.
- expected tradeoff: Runtime, memory, or optimization risk must be judged against Q_dataset/Q_rmd17/Q_iso17/Q_total, not a single force metric. For tiny/control proposals the tradeoff should be interpretability rather than capacity.
- failure signal that would falsify this proposal: Q_total below the source/control envelope, RMD17 force or energy regression beyond neutral variance, ISO17 gap_penalty worse without compensating Q gain, smoke/runtime failure, or loss of force-from-energy behavior.

## ablation_or_control
- required control or comparison: Compare to exact source control; if selected with architecture proposals, treat as diagnostic rather than mechanism evidence.
- optional zero-gate / source-fallback / readout-only ablation: Keep every new residual source-recoverable by a zero/very-negative gate when the proposal includes a branch; for control, no ablation beyond exact copy is needed.

## implementation_notes_for_subagent
Keep this train.py-only unless adding a tiny aux scalar is strictly necessary; avoid any dataset-specific branch. Implement only inside the materialized target unit. Do not edit global round state, proposal files, selection files, benchmark data, evaluator code, or `config.json` for MLIP quality. Preserve the generation_018/proposal_005 tensor shapes: scalar_state `[N,H]`, vector_state `[N,H,3]`, edge basis `[E,num_rbf]`, energy scalar, forces `[N,3]` by autograd.
