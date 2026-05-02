# Proposal 002: Iso17-friendly loss schedule exploit

- family: balanced_training_schedule
- phase: 3
- jump_type: exploit
- budget_class: tiny
- expected_capability_gain: improve iso17 energy calibration through training schedule changes while keeping the source architecture untouched.

## one_sentence_hypothesis
The source architecture may already be near the right structure, so a gentler early force emphasis and slightly longer energy warmup can lift iso17 energy and overall Q without changing message passing.

## mechanism_refs
- []

## evidence_refs
- benchmark_diagnosis.json
- current_code_profile.json
- proposal_constraints.json
- evidence_quality.json
- mechanism_cards.json::HYP-B001

## historical_relation
- source_unit: generation_010/proposal_007
- relation_to_source: exploit
- not_a_duplicate_of: prior architectural exploit proposals because this is train-only and isolates whether the remaining deficit is optimization rather than representation.
- lesson_used: the source already completed cleanly with improving trends on both datasets, so a schedule-only exploit is a low-risk way to probe undertraining or misweighted energy-force balance.

## benchmark_rationale
Discuss expected effects on all relevant benchmark signals, not force-only:
- rmd17 energy: likely neutral to slight downside if the schedule becomes too iso17-friendly.
- rmd17 force: should stay similar if force weight remains dominant.
- rmd17 gap / Q: low movement expected.
- iso17 energy: main upside via smoother calibration.
- iso17 force: should stay close to source.
- iso17 gap / Q: could improve if the source was still slightly force-overweighted.
- training stability / runtime risk: very low.
- control comparison expectation: if this beats control, the loop learns that optimization is the bottleneck more than architecture.

## files_to_edit
- `model/model.py`: none
- `model/train.py`

## code_insertion_points
- `model/train.py::train`: adjust warmup, epoch-wise energy/force weighting, and optionally minimum learning-rate floor without touching dataloading or benchmark outputs.
- `model/model.py::<none>`: none

## minimal_edit_plan
1. Keep the model definition identical to the source.
2. Modify the epoch weighting schedule to ramp energy slightly longer and reduce the early force overweight.
3. Keep optimizer, outputs, and training history structure compatible with the current workflow.

## implementation_checklist
- [ ] Preserve `E = sum_i E_i` and force-from-energy contract.
- [ ] Preserve benchmark metric field names and runnable entrypoint contract.
- [ ] Modify only the allowed target unit files.
- [ ] Keep tensor shapes compatible with current dataloader and model forward.
- [ ] Add no unbounded cubic neighbor/triplet loops unless explicitly justified by budget.
- [ ] Call `mark_unit_implemented.py --unit <UNIT> --actor implementation_subagent` after edits.

## expected_benchmark_effect
- primary expected gain: iso17 mixed energy MAE reduction with similar force quality.
- expected tradeoff: a small rmd17 force regression if the schedule weakens force pressure too much.
- failure signal that would falsify this proposal: both datasets stay flat or worsen, implying optimization is not the limiting factor.

## ablation_or_control
- required control or comparison: proposal_008 exact source replicate.
- optional zero-gate / source-fallback / readout-only ablation: none, this is already a train-only ablation.

## implementation_notes_for_subagent
Do not rewrite the training loop. Keep the exact output schema and only alter scalar schedule constants or the simple schedule formula inside `train`.
