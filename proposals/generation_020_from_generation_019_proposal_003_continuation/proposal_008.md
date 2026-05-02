# Proposal 008: Exact source replicate control

- family: source_control_replicate
- phase: 0
- jump_type: control
- budget_class: tiny
- expected_capability_gain: Calibrate generation_020 run variance against the current source before attributing small Q changes to edits.

## one_sentence_hypothesis
An exact copy of generation_019/proposal_003 is required to interpret whether proposed changes beat source/control variance on Q_total, energy, force, and gap metrics.

## mechanism_refs
- []

## evidence_refs
- current source unit generation_019/proposal_003
- benchmark_diagnosis.json Q_total=4.026030, Q_rmd17=4.166948, Q_iso17=3.764325, G_delta=-0.023958
- round policy control requirement from proposal_format.md
- generation_019/proposal_008 prior control Q_total=4.023487

## historical_relation
- source_unit: generation_019/proposal_003
- relation_to_source: control
- not_a_duplicate_of: This is intentionally an exact duplicate control, not a research mechanism.
- lesson_used: Generation_019 outcomes were close enough that variance calibration is mandatory before declaring small gains.

## why_not_duplicate
It is a duplicate by design and should be selected/used only as the control anchor. It must not be described as a new mechanism or improvement.

## benchmark_rationale
- capacity/scaling hypothesis, if any: None.
- rmd17 energy: Expected to reproduce mixed_energy_mae=0.031769 within run variance.
- rmd17 force: Expected to reproduce mixed_force_mae=0.060948.
- rmd17 gap / Q: Expected Q_rmd17 around 4.166948 and gap_penalty around 0.010551.
- iso17 energy: Expected mixed_energy_mae around 0.252341.
- iso17 force: Expected mixed_force_mae around 0.149767.
- iso17 gap / Q: Expected Q_iso17 around 3.764325 and gap_penalty around 0.144950.
- training stability / runtime risk: Same as source; any deviation is variance or environment.
- control comparison expectation: All non-control proposals should beat this control, not just the stale source metrics.

## files_to_edit
- none

## code_insertion_points
- none

## minimal_edit_plan
1. Exact copy of source unit generation_019/proposal_003.
2. Do not change `model/model.py`.
3. Do not change `model/train.py`.
4. Mark implemented as a control replicate if required by workflow.

## implementation_checklist
- [ ] Do not change `model/model.py`.
- [ ] Do not change `model/train.py`.
- [ ] Do not edit `config.json`.
- [ ] Preserve benchmark metric field names and runnable entrypoint contract.
- [ ] Preserve source outputs semantics: scalar energy sum and autograd forces.
- [ ] Mark implemented as control replicate if required by workflow.
- [ ] Call `mark_unit_implemented.py --unit <UNIT> --actor implementation_subagent` after materialization/control copy handling.

## expected_benchmark_effect
- primary expected gain: No gain expected; provides the variance baseline.
- expected tradeoff: Consumes one slot but makes Q_total interpretation reliable.
- failure signal that would falsify this proposal: Any nontrivial code delta from source or failure to run.

## ablation_or_control
- required control or comparison: This is the required control.
- optional zero-gate / source-fallback / readout-only ablation: Not applicable.

## implementation_notes_for_subagent
Do not edit model code. If the workflow materializes this unit, keep it as an exact source copy and mark it as control according to available helper scripts.
