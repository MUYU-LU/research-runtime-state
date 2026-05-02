# Proposal 003: Separated scalar/vector TP scale calibration

- family: tp_scale_calibration
- phase: 4
- jump_type: exploit
- budget_class: tiny
- expected_capability_gain: Improve the existing TP branch by calibrating scalar and vector residual magnitudes without new mechanism complexity.

## one_sentence_hypothesis
The current scalar-vector TP branch is strong but may have suboptimal fixed 0.1 scale caps; per-layer bounded calibration can preserve RMD17 force quality and reduce ISO17 energy/gap mismatch.

## mechanism_refs
- GEN019-M01-rank2-cartesian-tp-sibling

## evidence_refs
- current_code_profile.json::TPInteractionBranch residual_scales
- benchmark_diagnosis.json source metrics
- generation_018_summary: proposal_005 frontier win, proposal_006 first-layer TP tradeoff
- proposal_constraints.json allowed mechanism GEN019-M01

## historical_relation
- source_unit: generation_018/proposal_005
- relation_to_source: exploit
- not_a_duplicate_of: Not a new tensor-product variant; it exploits exactly generation_018/proposal_005 by only changing residual scale parameterization and optional rank2 gate defaults. It is not proposal_001 because no S-channel is required.
- lesson_used: The full TP path won while smaller first-layer TP regressed; this suggests the signal is real but scale placement matters, so calibration is a low-risk exploit.

## why_not_duplicate
Not a new tensor-product variant; it exploits exactly generation_018/proposal_005 by only changing residual scale parameterization and optional rank2 gate defaults. It is not proposal_001 because no S-channel is required. The source unit is already a frontier win, so this proposal is deliberately scoped around preserving its explicit scalar-vector tensor-product signal unless the proposal is the exact control or backward-simplification branch.

## benchmark_rationale
Current source generation_018/proposal_005 is the best-known unit: Q_total=4.049988, Q_rmd17=4.199739, Q_iso17=3.771881, G_delta=+0.107440 over generation_016/proposal_002. RMD17 is already strong (mixed_energy_mae=0.029077, mixed_force_mae=0.060116, gap_penalty=0.007114). ISO17 remains the main headroom (mixed_energy_mae=0.244736, mixed_force_mae=0.149781, gap_penalty=0.145198). Generation_018/proposal_003 showed a nearby product-basis branch can approach the frontier (Q_total=4.025879) mostly through ISO17 force/geometry, while first-layer-only TP and RoPE variants regressed Q_total. The control from generation_018/proposal_008 reached Q_total=3.931143, so small gains must clear source variance rather than only beat the old parent.
- capacity/scaling hypothesis, if any: No capacity increase; only scalar parameters or small gates.
- rmd17 energy: Source mixed_energy_mae is 0.029077 with improving train/val energy; proposal should not regress this beyond neutral variance.
- rmd17 force: Source mixed_force_mae is 0.060116 and is the strongest part of the branch; any force regression must be treated as a failure unless Q_total improves clearly and gap is controlled.
- rmd17 gap / Q: Source gap_penalty is 0.007114 and Q_dataset/Q_rmd17 is 4.199739; preserve this as the benchmark anchor.
- iso17 energy: Source mixed_energy_mae is 0.244736 with within/other energy split 0.212976/0.265909; this is the main improvement target.
- iso17 force: Source mixed_force_mae is 0.149781; keep neutral-to-positive force behavior and avoid force-only gains that worsen energy.
- iso17 gap / Q: Source gap_penalty is 0.145198 and Q_dataset/Q_iso17 is 3.771881; useful proposals should lower gap or raise Q_iso17 without harming Q_rmd17.
- training stability / runtime risk: Expected to protect RMD17 mixed_force_mae=0.060116 and mixed_energy_mae=0.029077 while testing whether ISO17 Q can improve by reducing over/under-coupled vector residuals.
- control comparison expectation: Compare against proposal_008 exact source replicate and the source metrics above; Q_total must be interpreted relative to control variance, not force-only ranking.

## files_to_edit
- `model/model.py`
- `model/train.py` if needed, otherwise `none`
- never `config.json` for MLIP-quality changes

## code_insertion_points
- `model/model.py::TPInteractionBranch.__init__`: replace shared hard-coded `0.1*sigmoid(logit)` cap with per-layer/per-channel `scalar_scale_cap`, `vector_scale_cap`, or learned low-rank channel gate initialized to the current value.
- `model/model.py::TPInteractionBranch.residual_scales`: return bounded per-channel or per-layer scales, clamped/capped so source behavior is recoverable.
- `model/model.py::EvolutionMLIP.forward_energy`: preserve existing combination order `next_state + scale*delta`; do not add new branches.
- `model/train.py`: no metric/objective change.

## minimal_edit_plan
1. Keep TPInteractionBranch messages exactly as in source.
2. Make residual scales more expressive but bounded: e.g. per-channel vectors initialized so mean scale equals current scalar/vector scale.
3. Optionally add a scalar_state-conditioned gate with final layer initialized to zero and cap at current 0.1.
4. Do not alter BodyOrderMessageBranch or readout except for shape-compatible scale plumbing.

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
- primary expected gain: Primary gain would be small Q_total improvement by lowering ISO17 force/energy gap without hurting RMD17; runtime essentially unchanged. Falsified if the added calibration causes training instability or worse Q_rmd17.
- expected tradeoff: Runtime, memory, or optimization risk must be judged against Q_dataset/Q_rmd17/Q_iso17/Q_total, not a single force metric. For tiny/control proposals the tradeoff should be interpretability rather than capacity.
- failure signal that would falsify this proposal: Q_total below the source/control envelope, RMD17 force or energy regression beyond neutral variance, ISO17 gap_penalty worse without compensating Q gain, smoke/runtime failure, or loss of force-from-energy behavior.

## ablation_or_control
- required control or comparison: Compare to source with all scale parameters initialized to current constants; report learned average scalar/vector scales after training if available.
- optional zero-gate / source-fallback / readout-only ablation: Keep every new residual source-recoverable by a zero/very-negative gate when the proposal includes a branch; for control, no ablation beyond exact copy is needed.

## implementation_notes_for_subagent
This is a low-risk exploit suitable for variance measurement around the winning mechanism. Implement only inside the materialized target unit. Do not edit global round state, proposal files, selection files, benchmark data, evaluator code, or `config.json` for MLIP quality. Preserve the generation_018/proposal_005 tensor shapes: scalar_state `[N,H]`, vector_state `[N,H,3]`, edge basis `[E,num_rbf]`, energy scalar, forces `[N,3]` by autograd.
