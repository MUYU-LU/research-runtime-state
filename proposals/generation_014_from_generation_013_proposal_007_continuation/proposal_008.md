# Proposal 008: Exact source control replicate

- family: source_control_replicate
- phase: 1
- jump_type: control
- budget_class: tiny
- expected_capability_gain: Provide a same-generation stochastic/control baseline for judging whether generation_014 repairs beat proposal_007 rather than run variance.

## one_sentence_hypothesis
An exact copy of generation_013/proposal_007 establishes the control distribution for scalar-only frozen-atomref behavior under the same generation_014 workflow.

## mechanism_refs
- []

## evidence_refs
- current source unit: generation_013/proposal_007
- round policy control requirement
- benchmark_diagnosis.json::proposal_007 terminal_success metrics

## historical_relation
- source_unit: generation_013/proposal_007
- relation_to_source: control
- not_a_duplicate_of: repair proposals because it intentionally changes no mechanism and serves only as a comparator.
- why_not_duplicate: Control replicate is required to separate real gains from run variance; it is not a competing mechanism proposal.
- lesson_used: Generation_013 outcomes include neutral variance around parent; generation_014 needs a same-source reference.

## benchmark_rationale
- rmd17 energy: Expected to match proposal_007 within training variance.
- rmd17 force: Expected to match proposal_007 within training variance.
- rmd17 gap / Q: Expected to reproduce proposal_007 gap/Q behavior.
- iso17 energy: Expected to reproduce proposal_007 energy regression baseline.
- iso17 force: Expected to reproduce proposal_007 force behavior.
- iso17 gap / Q: Expected to establish current scalar-only Q baseline.
- training stability / runtime risk: Minimal.
- control comparison expectation: Any selected repair should beat this on Q_total to be meaningful.

## files_to_edit
- none

## code_insertion_points
- none

## minimal_edit_plan
1. Exact copy of source unit.
2. Do not edit `model/model.py`.
3. Do not edit `model/train.py`.

## implementation_checklist
- [ ] Do not change `model/model.py`.
- [ ] Do not change `model/train.py`.
- [ ] Preserve benchmark metric field names and runnable entrypoint contract.
- [ ] Mark implemented as control replicate if required by workflow.
- [ ] Call `mark_unit_implemented.py --unit <UNIT> --actor implementation_subagent` after control setup.

## expected_benchmark_effect
- primary expected gain: No scientific gain; provides baseline variance.
- expected tradeoff: Consumes one run slot.
- failure signal that would falsify this proposal: Metrics materially differ from proposal_007 beyond normal variance or smoke fails.

## ablation_or_control
- required control or comparison: This is the required control.
- optional zero-gate / source-fallback / readout-only ablation: Exact source fallback.

## implementation_notes_for_subagent
Do not make any code edits. Only complete the workflow-required implementation marker for a control unit.
