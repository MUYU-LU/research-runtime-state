# Proposal 009: Exact source control replicate

- family: source_control
- phase: 2
- jump_type: control
- budget_class: tiny
- expected_capability_gain: Provide a variance/control baseline for generation_016 selection and benchmarking.

## one_sentence_hypothesis
An exact copy of generation_015/proposal_004 will quantify benchmark variance and protect interpretation of architecture-departure proposals.

## mechanism_refs
- []

## evidence_refs
- current source unit: generation_015/proposal_004
- benchmark_diagnosis.json::generation_015/proposal_004 Q_total=3.9176951158891966
- proposal_format.md::control proposal requirement
- research_skill round policy control requirement

## historical_relation
- source_unit: generation_015/proposal_004
- relation_to_source: control
- not_a_duplicate_of: It is intentionally a duplicate control, not a candidate mechanism; selection should treat it as a baseline replicate.
- lesson_used: The source unit is the current continuation point and has mixed strengths; all larger jumps need a same-source control comparison.

## why_not_duplicate
This is deliberately a duplicate only in the statistical/control sense. It must not be interpreted as a new mechanism or selected as an architecture departure.

## benchmark_rationale
- rmd17 energy: Should reproduce source within run variance.
- rmd17 force: Should reproduce source within run variance.
- rmd17 gap / Q: Baseline for generation_016.
- iso17 energy: Should reproduce source energy weakness/variance.
- iso17 force: Should reproduce source force trend/variance.
- iso17 gap / Q: Baseline for assessing energy/gap proposals.
- training stability / runtime risk: Lowest risk.
- control comparison expectation: Architecture proposals should exceed this control in Q_total or explain tradeoffs.

## files_to_edit
- none

## code_insertion_points
- none

## minimal_edit_plan
1. Exact copy of source unit.
2. Do not change `model/model.py`.
3. Do not change `model/train.py`.

## implementation_checklist
- [ ] Do not change `model/model.py`.
- [ ] Do not change `model/train.py`.
- [ ] Preserve benchmark metric field names and runnable entrypoint contract.
- [ ] Do not edit `config.json`.
- [ ] Mark implemented as a control replicate if required by workflow.
- [ ] Call `mark_unit_implemented.py --unit <UNIT> --actor implementation_subagent` after control materialization.

## expected_benchmark_effect
- primary expected gain: None; variance estimate and baseline.
- expected tradeoff: Consumes one run slot if selected.
- failure signal that would falsify this proposal: Metrics deviate outside expected run variance or smoke fails despite no code changes.

## ablation_or_control
- required control or comparison: This is the required control.
- optional zero-gate / source-fallback / readout-only ablation: Not applicable.

## implementation_notes_for_subagent
Do not edit code. The only implementation action after materialization should be marking the unit implemented as a control according to workflow expectations.
