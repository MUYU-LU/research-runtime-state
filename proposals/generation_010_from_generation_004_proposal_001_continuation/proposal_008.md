# Proposal 008: Exact source control replicate

- family: balanced_local_equivariant_control
- phase: 4
- jump_type: control
- budget_class: tiny
- expected_capability_gain: none, this is a variance anchor.

## one_sentence_hypothesis
An exact source replicate is required to interpret whether any tiny exploit or jump beats the parent rather than benchmark noise.

## mechanism_refs
- []

## evidence_refs
- current source unit generation_004/proposal_001
- round policy control requirement
- generation_memory.json

## historical_relation
- source_unit: generation_004/proposal_001
- relation_to_source: control
- not_a_duplicate_of: prior controls because a fresh control in this round is required for attribution under continuing variance.
- lesson_used: no child in recent generations beat the source, so a clean variance anchor remains mandatory.

## benchmark_rationale
Discuss expected effects on all relevant benchmark signals, not force-only:
- rmd17 energy: should match source distribution within run variance.
- rmd17 force: should match source distribution within run variance.
- rmd17 gap / Q: baseline for interpretation, not a capability attempt.
- iso17 energy: should match source distribution within run variance.
- iso17 force: should match source distribution within run variance.
- iso17 gap / Q: baseline for interpretation.
- training stability / runtime risk: lowest possible.
- control comparison expectation: all other proposals should be judged against this anchor.

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
- failure signal that would falsify this proposal: a large drop from source would indicate substantial variance or hidden implementation drift in the workflow.

## ablation_or_control
- required control or comparison: this proposal is the required control.
- optional zero-gate / source-fallback / readout-only ablation: none.

## implementation_notes_for_subagent
Do not change `model/model.py` or `model/train.py`. Mark the unit as a control replicate if the workflow expects that metadata.
