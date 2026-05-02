# Proposal 008: Exact source control replicate

- family: balanced_source_control
- phase: 3
- jump_type: control
- budget_class: tiny
- expected_capability_gain: none, this is the attribution anchor for the new continuation source.

## one_sentence_hypothesis
An exact replicate of generation_010/proposal_007 is required to tell whether any small exploit or jump is genuinely better than source-level variance.

## mechanism_refs
- []

## evidence_refs
- current source unit generation_010/proposal_007
- round policy control requirement
- benchmark_diagnosis.json

## historical_relation
- source_unit: generation_010/proposal_007
- relation_to_source: control
- not_a_duplicate_of: prior controls because this round needs a fresh control for a different continuation source.
- lesson_used: all candidate gains in this round are expected to be small, so attribution depends on a clean source replicate.

## benchmark_rationale
Discuss expected effects on all relevant benchmark signals, not force-only:
- rmd17 energy: should match source within run variance.
- rmd17 force: should match source within run variance.
- rmd17 gap / Q: baseline for comparison.
- iso17 energy: should match source within run variance.
- iso17 force: should match source within run variance.
- iso17 gap / Q: baseline for comparison.
- training stability / runtime risk: lowest possible.
- control comparison expectation: all other proposals should be judged relative to this anchor.

## files_to_edit
- `none`

## code_insertion_points
- `none`

## minimal_edit_plan
1. Exact copy of source unit.

## implementation_checklist
- [ ] Preserve `E = sum_i E_i` and force-from-energy contract.
- [ ] Preserve benchmark metric field names and runnable entrypoint contract.
- [ ] Modify only the allowed target unit files.
- [ ] Keep tensor shapes compatible with current dataloader and model forward.
- [ ] Add no unbounded cubic neighbor/triplet loops unless explicitly justified by budget.
- [ ] Call `mark_unit_implemented.py --unit <UNIT> --actor implementation_subagent` after edits.

## expected_benchmark_effect
- primary expected gain: none, this is for attribution.
- expected tradeoff: consumes one slot.
- failure signal that would falsify this proposal: a large drop from source would indicate workflow variance or hidden drift.

## ablation_or_control
- required control or comparison: this proposal is the required control.
- optional zero-gate / source-fallback / readout-only ablation: none.

## implementation_notes_for_subagent
Do not change `model/model.py` or `model/train.py`. Mark the unit as a control replicate if the workflow expects that metadata.
