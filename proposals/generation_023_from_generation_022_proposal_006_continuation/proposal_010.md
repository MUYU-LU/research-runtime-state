# Proposal 010: Energy-balanced training objective control

- family: energy_gap_training_control
- phase: 3
- jump_type: control
- budget_class: tiny
- expected_capability_gain: Diagnose whether the source's ISO17 energy/gap weakness is training-weight balance rather than another architecture mechanism

## one_sentence_hypothesis
A small code-level shift toward energy loss during the existing warmup schedule may reduce ISO17 energy/gap error while preserving most of the source's force quality.

## mechanism_refs
- []

## evidence_refs
- current source unit: generation_022/proposal_006
- benchmark_diagnosis.json: ISO17 mixed_energy_mae=0.2627397479531607, other_energy_mae=0.28307091346153845, gap_penalty=0.1536659406879372, val energy trend worsening while force trend improves
- benchmark_diagnosis.json: RMD17 mixed_force_mae=0.060482785477710424 and mixed_energy_mae=0.02897457275390625 show the source is already strong locally, so this is a bounded objective-control rather than a model-family rewrite
- proposal_format.md: training-objective evolution may change loss weights in `model/train.py` while benchmark data, split semantics, metric names, and launch protocol stay fixed
- proposal_constraints.json: no external mechanism is claimed; this proposal is diagnosis-driven/control and therefore uses `mechanism_refs: []`

## historical_relation
- source_unit: generation_022/proposal_006
- relation_to_source: control
- not_a_duplicate_of: Not a duplicate of proposal_006 because it is not an exact source replicate; it changes only training loss weights/schedule in code. Not a duplicate of proposals_001-005 or _007-_009 because it adds no LES tail, no distance kernel, no charge normalization, and no model architecture branch. It tests whether the source architecture was underweighted for energy/gap rather than missing another charge mechanism.
- lesson_used: The source's ISO17 force trend is improving but validation energy is worsening; before attributing all ISO17 gap to long-range architecture, run one tiny objective-control that increases energy pressure without changing benchmark evaluation semantics.

## why_not_duplicate
This is the only generation_023 proposal that edits `model/train.py` instead of adding an LES real-space branch or copying the source. It is intentionally diagnosis-driven: if it improves ISO17 energy/gap, later LES proposals should be judged against an energy-balanced source baseline; if it fails, objective balance is unlikely to explain the gap.

## benchmark_rationale
- capacity/scaling hypothesis, if any: none; hidden dimension, cutoff, basis count, and architecture stay unchanged.
- rmd17 energy: may improve slightly or stay near source because RMD17 already has low mixed_energy_mae=0.0289746.
- rmd17 force: primary tradeoff risk; reducing force dominance can worsen mixed_force_mae=0.0604828, so the weight shift must be modest.
- rmd17 gap / Q: should remain within source/control variance; reject if force degradation raises gap/Q penalty without ISO17 compensation.
- iso17 energy: primary target; a higher energy weight and less force-heavy early schedule may reduce mixed_energy_mae=0.2627397 and other_energy_mae=0.2830709.
- iso17 force: expected to remain acceptable because force weight is still high and the force-from-energy contract is unchanged.
- iso17 gap / Q: target gap_penalty=0.1536659 and Q_iso17=3.7576871 by improving energy consistency rather than adding a new physics branch.
- training stability / runtime risk: tiny; no O(N^2) branch, no extra parameters, same optimizer/scheduler and epoch count.
- control comparison expectation: compare against proposal_006 exact source replicate and the LES proposals; this control tells whether energy weighting alone competes with mechanism edits.

## files_to_edit
- `model/train.py`
- none (`model/model.py` unchanged)
- never `config.json` for MLIP-quality changes

## code_insertion_points
- `model/train.py::code-level defaults`: change `TRAIN_ENERGY_WEIGHT` from `1.0` to `1.35` and `TRAIN_FORCE_WEIGHT` from `20.0` to `18.0`; leave learning rate, weight decay, epoch count, dataset loading, and metric computation unchanged.
- `model/train.py::train`: replace the existing warmup factors `epoch_energy_weight = energy_weight * (0.6 + 0.4 * warmup_ratio)` and `epoch_force_weight = force_weight * (1.1 - 0.1 * warmup_ratio)` with a bounded energy-balanced schedule such as `epoch_energy_weight = energy_weight * (0.8 + 0.3 * warmup_ratio)` and `epoch_force_weight = force_weight * (1.05 - 0.05 * warmup_ratio)`.
- `model/model.py`: no change.

## minimal_edit_plan
1. Edit only the code-level training constants in `model/train.py` to modestly increase energy pressure and modestly reduce force dominance.
2. Adjust only the existing per-epoch warmup multipliers; do not change the loss formula, optimizer family, scheduler type, epochs, dataloaders, metrics, or launch protocol.
3. Keep `model/model.py` byte-identical to the source architecture so any benchmark difference is attributable to objective balance.

## implementation_checklist
- [ ] Preserve `E = sum_i E_i` and force-from-energy contract by leaving `model/model.py` unchanged.
- [ ] Preserve benchmark metric field names, split semantics, dataset semantics, and runnable entrypoint contract.
- [ ] Modify only `model/train.py`; do not edit `model/model.py` unless required by materialization boilerplate.
- [ ] Do not edit `config.json`; loss weights are code-level MLIP knobs in `model/train.py`.
- [ ] Keep tensor shapes and dataloader behavior unchanged.
- [ ] Add no all-pair, cubic, PBC, Ewald, cell, or charge-label logic.
- [ ] Keep optimizer, scheduler, training epoch count, and batch protocol unchanged.
- [ ] Call `mark_unit_implemented.py --unit <UNIT> --actor implementation_subagent` after edits.

## expected_benchmark_effect
- primary expected gain: improved ISO17 energy/gap/Q from less force-dominated training, without needing a new architecture branch.
- expected tradeoff: possible RMD17/ISO17 force MAE regression because the force loss remains high but no longer dominates as strongly.
- failure signal that would falsify this proposal: ISO17 energy/gap does not improve or force degradation reduces Q_total below the source/control band.

## ablation_or_control
- required control or comparison: compare directly with proposal_006 exact source replicate and generation_022/proposal_006 source metrics; interpret as an objective-control, not external mechanism evidence.
- optional zero-gate / source-fallback / readout-only ablation: none; source fallback is proposal_006, while this proposal changes only training weights.

## implementation_notes_for_subagent
Do not claim GEN023-M01 or any external LES mechanism here. This proposal is intentionally diagnosis-driven and uses `mechanism_refs: []`. Preserve fixed benchmark semantics: no dataset changes, no metric changes, no launch changes, no config quality knobs. The concrete code handoff is limited to `model/train.py`: set `TRAIN_ENERGY_WEIGHT=1.35`, `TRAIN_FORCE_WEIGHT=18.0`, and make the existing warmup less force-heavy by using energy multiplier `0.8 + 0.3*warmup_ratio` and force multiplier `1.05 - 0.05*warmup_ratio`. Keep `run_epoch` loss structure `energy_weight * loss_energy + force_weight * loss_force` and all history fields unchanged so downstream collectors continue to read the same schema.
