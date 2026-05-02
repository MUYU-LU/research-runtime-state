# Proposal 010: Diagnosis-driven ISO17 energy-stability warmup

- family: energy_stability_training_probe
- phase: 3
- jump_type: wildcard
- budget_class: tiny
- expected_capability_gain: Test whether the source architecture's ISO17 late energy worsening is partly a training-weight schedule issue rather than a representation issue.

## one_sentence_hypothesis
A slightly longer and stronger energy warmup in `model/train.py` may reduce ISO17 mixed_energy_mae/gap for the source architecture while preserving the force-from-energy model and fixed benchmark metrics.

## mechanism_refs
- []

## evidence_refs
- benchmark_diagnosis.json::generation_016/proposal_002 ISO17 energy_trend=worsening, best_val_energy_mae=0.3720703125, last_val_energy_mae=0.9840494791666666
- benchmark_diagnosis.json::generation_016/proposal_002 ISO17 force_trend=improving, mixed_force_mae=0.17568934841089728
- mechanism_cards.json::GEN017-M01 patch blueprint says keep train weights unchanged for primary ablation, so this is diagnosis-driven wildcard not strong mechanism
- generation_016 selection memory: prior training-target probe existed, but not as a source-only schedule probe on generation_016/proposal_002's body-order message branch

## historical_relation
- source_unit: generation_016/proposal_002
- relation_to_source: ablation
- not_a_duplicate_of: generation_016/proposal_007 combined minimal body-order residual with code-level reweighting from a different source; this proposal keeps the current source architecture exact and changes only a small training schedule knob in code.
- lesson_used: Source ISO17 force improves while validation energy worsens late, suggesting a small objective-schedule probe is useful even though external mechanism evidence is architecture-focused.

## why_not_duplicate
This is not an architecture proposal and not a force-only tweak. It is a bounded train.py-only diagnostic for the current best body-order message source, with all benchmark/eval semantics unchanged.

## benchmark_rationale
- rmd17 energy: May improve slightly or stay stable if energy supervision is emphasized longer.
- rmd17 force: Risk of modest force degradation if energy weight competes with force weight.
- rmd17 gap / Q: Success requires no large Q_rmd17 loss.
- iso17 energy: Primary target is reducing late validation energy drift and mixed_energy_mae.
- iso17 force: Should remain close if force weight remains high.
- iso17 gap / Q: Gain expected only if mixed_energy_mae/gap improve more than any force tradeoff.
- training stability / runtime risk: Same runtime; small risk of under-training forces under 8 epochs.
- control comparison expectation: Should be interpreted against exact source control and M01 architecture proposals.

## files_to_edit
- `model/model.py`: none expected
- `model/train.py`
- never `config.json` for MLIP-quality changes

## code_insertion_points
- `model/train.py::TRAIN_ENERGY_WEIGHT/TRAIN_FORCE_WEIGHT`: optionally set `TRAIN_ENERGY_WEIGHT = 1.15` and `TRAIN_FORCE_WEIGHT = 19.0`, or leave constants and change warmup only if preferred by implementer.
- `model/train.py::train`: set `energy_warmup_epochs` effective default to 5 instead of 3 when config does not override, and use a gentler force taper such as `epoch_force_weight = force_weight * (1.05 - 0.05 * warmup_ratio)`.
- `model/model.py::none`: keep source architecture unchanged.

## minimal_edit_plan
1. Do not touch `model/model.py`.
2. In `model/train.py`, adjust only code-level training defaults or schedule math to modestly emphasize energy for more epochs while keeping force weight high.
3. Keep optimizer, dataloaders, metric names, epoch count, CUDA requirement, and force-from-energy behavior unchanged.

## implementation_checklist
- [ ] Preserve `E = sum_i E_i` and force-from-energy contract.
- [ ] Preserve benchmark metric field names and runnable entrypoint contract.
- [ ] Modify only the allowed target unit files.
- [ ] Do not edit `config.json`; change MLIP knobs in `model/model.py` or `model/train.py`.
- [ ] Keep tensor shapes compatible with current dataloader and model forward.
- [ ] Add no unbounded cubic neighbor/triplet loops unless explicitly justified by budget.
- [ ] Do not change dataset splits, eval formulas, output keys, or epoch count.
- [ ] Avoid large force-weight reductions; this is an energy-stability probe, not force de-prioritization.
- [ ] Call `mark_unit_implemented.py --unit <UNIT> --actor implementation_subagent` after edits.

## expected_benchmark_effect
- primary expected gain: Lower ISO17 mixed_energy_mae/gap and less late validation energy worsening.
- expected tradeoff: Possible small force MAE regression, especially on RMD17.
- failure signal that would falsify this proposal: Force degradation dominates Q or ISO17 energy still worsens late.

## ablation_or_control
- required control or comparison: Exact source control with unchanged train schedule.
- optional zero-gate / source-fallback / readout-only ablation: Revert `model/train.py` constants/schedule to source values.

## implementation_notes_for_subagent
This is diagnosis-driven and has no strong external mechanism refs. Keep the change tiny, code-level, and reversible; do not edit `config.json` or model architecture.
