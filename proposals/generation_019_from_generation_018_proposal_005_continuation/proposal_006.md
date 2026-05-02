# Proposal 006: Radial-resolution and rank2 bottleneck test

- family: tp_radial_resolution_scaling
- phase: 4
- jump_type: jump
- budget_class: medium
- expected_capability_gain: Test whether the frontier TP branch is limited by radial/angular resolution rather than only mechanism form.

## one_sentence_hypothesis
A bounded code-level increase from num_rbf=32 to 40 with the rank-2 TP sibling can improve ISO17 gap/Q if the current scalar-vector TP under-resolves distance-dependent angular coupling.

## mechanism_refs
- GEN019-M01-rank2-cartesian-tp-sibling

## evidence_refs
- proposal_format.md capacity scaling policy
- current capacity knobs in context: MODEL_NUM_RBF=32, hidden_dim=96, num_interactions=2
- mechanism_cards.json::GEN019-M01-rank2-cartesian-tp-sibling
- benchmark_diagnosis.json source train trends and ISO17 headroom

## historical_relation
- source_unit: generation_018/proposal_005
- relation_to_source: jump
- not_a_duplicate_of: Not proposal_001 because it also tests a radial-resolution bottleneck through code-level defaults; not a config edit because the change belongs in model/train constants.
- lesson_used: The first-layer TP probe regressed while full TP won, suggesting representation resolution may matter; keep scaling bounded and falsifiable.

## why_not_duplicate
Not proposal_001 because it also tests a radial-resolution bottleneck through code-level defaults; not a config edit because the change belongs in model/train constants. The source unit is already a frontier win, so this proposal is deliberately scoped around preserving its explicit scalar-vector tensor-product signal unless the proposal is the exact control or backward-simplification branch.

## benchmark_rationale
Current source generation_018/proposal_005 is the best-known unit: Q_total=4.049988, Q_rmd17=4.199739, Q_iso17=3.771881, G_delta=+0.107440 over generation_016/proposal_002. RMD17 is already strong (mixed_energy_mae=0.029077, mixed_force_mae=0.060116, gap_penalty=0.007114). ISO17 remains the main headroom (mixed_energy_mae=0.244736, mixed_force_mae=0.149781, gap_penalty=0.145198). Generation_018/proposal_003 showed a nearby product-basis branch can approach the frontier (Q_total=4.025879) mostly through ISO17 force/geometry, while first-layer-only TP and RoPE variants regressed Q_total. The control from generation_018/proposal_008 reached Q_total=3.931143, so small gains must clear source variance rather than only beat the old parent.
- capacity/scaling hypothesis, if any: Capacity/resolution hypothesis: increase `MODEL_NUM_RBF`/`num_rbf` from 32 to 40 only, optionally add rank2 S-channel; no hidden_dim/depth increase.
- rmd17 energy: Source mixed_energy_mae is 0.029077 with improving train/val energy; proposal should not regress this beyond neutral variance.
- rmd17 force: Source mixed_force_mae is 0.060116 and is the strongest part of the branch; any force regression must be treated as a failure unless Q_total improves clearly and gap is controlled.
- rmd17 gap / Q: Source gap_penalty is 0.007114 and Q_dataset/Q_rmd17 is 4.199739; preserve this as the benchmark anchor.
- iso17 energy: Source mixed_energy_mae is 0.244736 with within/other energy split 0.212976/0.265909; this is the main improvement target.
- iso17 force: Source mixed_force_mae is 0.149781; keep neutral-to-positive force behavior and avoid force-only gains that worsen energy.
- iso17 gap / Q: Source gap_penalty is 0.145198 and Q_dataset/Q_iso17 is 3.771881; useful proposals should lower gap or raise Q_iso17 without harming Q_rmd17.
- training stability / runtime risk: Could improve ISO17 Q by resolving distance-dependent angular anisotropy, but may increase runtime/memory and overfit RMD17 energy.
- control comparison expectation: Compare against proposal_008 exact source replicate and the source metrics above; Q_total must be interpreted relative to control variance, not force-only ranking.

## files_to_edit
- `model/model.py`
- `model/train.py`
- never `config.json` for MLIP-quality changes

## code_insertion_points
- `model/train.py::MODEL_NUM_RBF`: change code-level default from 32 to 40.
- `model/model.py::EvolutionMLIP.__init__`: ensure default `num_rbf` also matches 40 if constructor default is used directly.
- `model/model.py::TPInteractionBranch`: add proposal_001 rank-2 S-channel or keep hooks compatible with `num_rbf=40`.
- `model/train.py::train`: preserve learning rate, weights, epochs, scheduler, and logging.

## minimal_edit_plan
1. Update code-level num_rbf defaults in model.py/train.py only.
2. Verify all edge MLPs consume `num_rbf` constructor argument, not hard-coded 32.
3. Add the rank-2 branch only with a very small gate; do not increase hidden_dim or depth.
4. Document runtime/OOM risk and leave benchmark config unchanged.

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
- primary expected gain: Expected primary gain is Q_iso17 via lower gap_penalty; RMD17 may improve or stay neutral if radial basis was a bottleneck. Tradeoff is more edge MLP parameters and runtime. Falsified if runtime rises materially without Q_total gain or RMD17 energy regresses.
- expected tradeoff: Runtime, memory, or optimization risk must be judged against Q_dataset/Q_rmd17/Q_iso17/Q_total, not a single force metric. For tiny/control proposals the tradeoff should be interpretability rather than capacity.
- failure signal that would falsify this proposal: Q_total below the source/control envelope, RMD17 force or energy regression beyond neutral variance, ISO17 gap_penalty worse without compensating Q gain, smoke/runtime failure, or loss of force-from-energy behavior.

## ablation_or_control
- required control or comparison: Compare to proposal_001 at num_rbf=32 and exact source; if 40-RBF helps only with rank2 disabled, future selection can separate capacity from mechanism.
- optional zero-gate / source-fallback / readout-only ablation: Keep every new residual source-recoverable by a zero/very-negative gate when the proposal includes a branch; for control, no ablation beyond exact copy is needed.

## implementation_notes_for_subagent
This is a bounded scaling jump, not a general hyperparameter sweep. Implement only inside the materialized target unit. Do not edit global round state, proposal files, selection files, benchmark data, evaluator code, or `config.json` for MLIP quality. Preserve the generation_018/proposal_005 tensor shapes: scalar_state `[N,H]`, vector_state `[N,H,3]`, edge basis `[E,num_rbf]`, energy scalar, forces `[N,3]` by autograd.
