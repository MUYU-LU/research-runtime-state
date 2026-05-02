# Proposal 010: Rank-2 gate with late training warmup

- family: rank2_gate_training_warmup
- phase: 4
- jump_type: wildcard
- budget_class: small
- expected_capability_gain: Stabilize the rank-2 TP sibling by coupling its residual gate to a conservative training warmup.

## one_sentence_hypothesis
If rank-2 angular features are useful but early force training is sensitive, a source-recoverable S-channel with delayed/lower initial gate should improve ISO17 Q while protecting RMD17 force.

## mechanism_refs
- GEN019-M01-rank2-cartesian-tp-sibling

## evidence_refs
- mechanism_cards.json::GEN019-M01-rank2-cartesian-tp-sibling
- patch_blueprints.json::GEN019-M01-rank2-cartesian-tp-sibling
- benchmark_diagnosis.json train histories: both datasets improve late, ISO17 val energy volatile
- research-skill training-objective policy allowing bounded schedules

## historical_relation
- source_unit: generation_018/proposal_005
- relation_to_source: jump
- not_a_duplicate_of: Not proposal_001 because it adds a bounded train.py warmup for the new rank2 gate; not proposal_009 because it includes a concrete evidence-backed rank2 mechanism.
- lesson_used: Added branches can regress energy if active too early; near-zero residuals worked for TP, so rank2 should be even more conservatively warmed.

## why_not_duplicate
Not proposal_001 because it adds a bounded train.py warmup for the new rank2 gate; not proposal_009 because it includes a concrete evidence-backed rank2 mechanism. The source unit is already a frontier win, so this proposal is deliberately scoped around preserving its explicit scalar-vector tensor-product signal unless the proposal is the exact control or backward-simplification branch.

## benchmark_rationale
Current source generation_018/proposal_005 is the best-known unit: Q_total=4.049988, Q_rmd17=4.199739, Q_iso17=3.771881, G_delta=+0.107440 over generation_016/proposal_002. RMD17 is already strong (mixed_energy_mae=0.029077, mixed_force_mae=0.060116, gap_penalty=0.007114). ISO17 remains the main headroom (mixed_energy_mae=0.244736, mixed_force_mae=0.149781, gap_penalty=0.145198). Generation_018/proposal_003 showed a nearby product-basis branch can approach the frontier (Q_total=4.025879) mostly through ISO17 force/geometry, while first-layer-only TP and RoPE variants regressed Q_total. The control from generation_018/proposal_008 reached Q_total=3.931143, so small gains must clear source variance rather than only beat the old parent.
- capacity/scaling hypothesis, if any: Small mechanism plus schedule; no hidden_dim/depth/RBF increase.
- rmd17 energy: Source mixed_energy_mae is 0.029077 with improving train/val energy; proposal should not regress this beyond neutral variance.
- rmd17 force: Source mixed_force_mae is 0.060116 and is the strongest part of the branch; any force regression must be treated as a failure unless Q_total improves clearly and gap is controlled.
- rmd17 gap / Q: Source gap_penalty is 0.007114 and Q_dataset/Q_rmd17 is 4.199739; preserve this as the benchmark anchor.
- iso17 energy: Source mixed_energy_mae is 0.244736 with within/other energy split 0.212976/0.265909; this is the main improvement target.
- iso17 force: Source mixed_force_mae is 0.149781; keep neutral-to-positive force behavior and avoid force-only gains that worsen energy.
- iso17 gap / Q: Source gap_penalty is 0.145198 and Q_dataset/Q_iso17 is 3.771881; useful proposals should lower gap or raise Q_iso17 without harming Q_rmd17.
- training stability / runtime risk: Expected to reduce ISO17 gap without destabilizing RMD17 force; runtime similar to proposal_001 but optimization risk lower.
- control comparison expectation: Compare against proposal_008 exact source replicate and the source metrics above; Q_total must be interpreted relative to control variance, not force-only ranking.

## files_to_edit
- `model/model.py`
- `model/train.py`
- never `config.json` for MLIP-quality changes

## code_insertion_points
- `model/model.py::TPInteractionBranch.__init__/forward`: add rank2 S-channel and expose a scalar `rank2_residual_logit`/cap initialized near -7 or -6.
- `model/model.py::EvolutionMLIP`: optionally provide a method or attribute for rank2 warmup multiplier defaulting to 1.0 in eval.
- `model/train.py::train/run_epoch`: during training epochs 1-2 keep rank2 multiplier lower or leave the logit very negative; after warmup allow normal trainable gate. Must preserve eval metric semantics.
- `model/train.py`: preserve energy/force weights except any tiny logged warmup constant.

## minimal_edit_plan
1. Implement the rank2 S-channel as in proposal_001 but initialize more conservatively.
2. Add a simple epoch-dependent multiplier in training only if it can be done without changing model forward contract; otherwise set initial logit lower and skip schedule plumbing.
3. Keep all scalar-vector TP and body-order source paths unchanged.
4. Log or keep constants obvious so implementation_report captures the training behavior.

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
- primary expected gain: Primary expected gain is safer Q_iso17 improvement than proposal_001; tradeoff is that rank2 may remain too inactive in 8 epochs. Falsified if no measurable difference from source or if training schedule changes obscure mechanism attribution.
- expected tradeoff: Runtime, memory, or optimization risk must be judged against Q_dataset/Q_rmd17/Q_iso17/Q_total, not a single force metric. For tiny/control proposals the tradeoff should be interpretability rather than capacity.
- failure signal that would falsify this proposal: Q_total below the source/control envelope, RMD17 force or energy regression beyond neutral variance, ISO17 gap_penalty worse without compensating Q gain, smoke/runtime failure, or loss of force-from-energy behavior.

## ablation_or_control
- required control or comparison: Compare exact source, proposal_001 rank2 without training warmup, and zero-gate rank2. If gains require warmup, future rounds can tune gate schedule.
- optional zero-gate / source-fallback / readout-only ablation: Keep every new residual source-recoverable by a zero/very-negative gate when the proposal includes a branch; for control, no ablation beyond exact copy is needed.

## implementation_notes_for_subagent
This wildcard intentionally crosses mechanism and objective axes but keeps both bounded and source-recoverable. Implement only inside the materialized target unit. Do not edit global round state, proposal files, selection files, benchmark data, evaluator code, or `config.json` for MLIP quality. Preserve the generation_018/proposal_005 tensor shapes: scalar_state `[N,H]`, vector_state `[N,H,3]`, edge basis `[E,num_rbf]`, energy scalar, forces `[N,3]` by autograd.
