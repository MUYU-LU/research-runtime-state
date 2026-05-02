# Proposal 003: Trainable fitted atomref safeguard

- family: trainable_lstsq_atomref
- phase: 1
- jump_type: exploit
- budget_class: tiny
- expected_capability_gain: Isolate whether proposal_007's frozen fitted composition offset caused energy/Q regression by allowing the fitted atomref to adapt during training.

## one_sentence_hypothesis
Keeping least-squares atomref initialization but removing the hard freeze should improve ISO17/RMD17 energy calibration if the frozen baseline was mismatched to benchmark train/validation distributions.

## mechanism_refs
- GEN014-M02-atomref-energy-safeguard

## evidence_refs
- mechanism_cards.json::GEN014-M02-atomref-energy-safeguard
- patch_blueprints.json::GEN014-M02-atomref-energy-safeguard
- repo:ACEsuit/mace#99833dea34c0::AtomicEnergiesBlock/E0 handling
- benchmark_diagnosis.json::proposal_007::mixed_energy_mae_regression

## historical_relation
- source_unit: generation_013/proposal_007
- relation_to_source: exploit
- not_a_duplicate_of: generation_013/proposal_001 because this starts from scalar-only proposal_007 and changes only the atomref freeze, without restoring vector readout.
- why_not_duplicate: proposal_007 froze fitted atomref; this is the one-factor unfreeze ablation required by M02.
- lesson_used: Generation_013 atomref-freeze variants were mostly neutral, but proposal_007 combined freeze with scalar-only readout and regressed energy/Q.

## benchmark_rationale
- rmd17 energy: Expected improvement if hard-frozen E0 is slightly biased.
- rmd17 force: Mostly neutral because atomref is position-independent; force changes occur through rebalanced residual training.
- rmd17 gap / Q: Q improves only if energy gain exceeds any force tradeoff.
- iso17 energy: Primary target due to proposal_007 ISO17 mixed_energy_mae regression.
- iso17 force: Neutral to small indirect change.
- iso17 gap / Q: May improve other/within energy gap calibration.
- training stability / runtime risk: Very low; removes a freeze line and keeps current optimizer.
- control comparison expectation: If energy improves with force neutral, freeze should not be reused blindly.

## files_to_edit
- `model/train.py`

## code_insertion_points
- `model/train.py::train`: remove or disable the `if atomref_fitted: model.atomref.weight.requires_grad_(False)` block after `initialize_atomref_lstsq`.
- `model/train.py::run_epoch`: none.
- `model/model.py::EvolutionMLIP`: none.

## minimal_edit_plan
1. Preserve `initialize_atomref_lstsq` and the fitted initialization.
2. Remove the hard freeze so `model.atomref.weight` remains trainable.
3. Keep optimizer construction over `model.parameters()` unchanged.

## implementation_checklist
- [ ] Preserve `E = sum_i E_i` and force-from-energy contract.
- [ ] Preserve benchmark metric field names and runnable entrypoint contract.
- [ ] Modify only the allowed target unit files.
- [ ] Keep tensor shapes compatible with current dataloader and model forward.
- [ ] Add no unbounded cubic neighbor/triplet loops unless explicitly justified by budget.
- [ ] Call `mark_unit_implemented.py --unit <UNIT> --actor implementation_subagent` after edits.
- [ ] Do not change readout width or vector path in this unit.

## expected_benchmark_effect
- primary expected gain: Better mixed_energy_mae and Q_total than proposal_007.
- expected tradeoff: Could worsen composition baseline stability if atomref drifts too much.
- failure signal that would falsify this proposal: Energy/Q remain worse than source or atomref training destabilizes validation energy.

## ablation_or_control
- required control or comparison: Exact proposal_007 frozen-atomref scalar-only control.
- optional zero-gate / source-fallback / readout-only ablation: Later soft-regularized atomref if fully trainable drift is harmful.

## implementation_notes_for_subagent
This is a one-factor train.py edit. Do not add regularizers, parameter groups, or architecture changes.
