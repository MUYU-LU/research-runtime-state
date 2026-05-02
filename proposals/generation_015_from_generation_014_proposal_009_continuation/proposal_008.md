# Proposal 008: Exact source control replicate

- family: source_control_replicate
- phase: 0
- jump_type: control
- budget_class: tiny
- expected_capability_gain: Measure run variance for generation_014/proposal_009 before attributing small generation_015 changes to real mechanism gains.

## one_sentence_hypothesis
An exact replicate of the current best unit provides the required control baseline for Q_total, ISO17 energy/gap volatility, and remote runtime variance.

## mechanism_refs
- []

## evidence_refs
- current source unit generation_014/proposal_009
- round policy control requirement
- context.md::generation_014/proposal_009::Q_total=3.8988711909426823
- context.md::generation_014/proposal_009::run_state=terminal_success::remote_smoke_passed=true

## historical_relation
- source_unit: generation_014/proposal_009
- relation_to_source: control
- not_a_duplicate_of: all mechanism proposals because this intentionally makes no MLIP-quality edit and exists only to estimate variance.
- why_not_duplicate: Control replicas are required comparison artifacts, not mechanism claims.
- lesson_used: Several prior generations show control variance and family-history ambiguity; source-level variance must be measured before selecting small readout-gate wins.

## benchmark_rationale
- rmd17 energy: Expected to match source within run variance.
- rmd17 force: Expected to match source within run variance.
- rmd17 gap / Q: Expected to match source Q_rmd17=4.054452.
- iso17 energy: Expected to expose whether source ISO17 validation energy volatility is reproducible.
- iso17 force: Expected to match source within run variance.
- iso17 gap / Q: Expected to match source Q_iso17=3.609935 within variance.
- training stability / runtime risk: Lowest; no code edit beyond materialization bookkeeping.
- control comparison expectation: Mechanism proposals should beat this control on Q_total or show a targeted ISO17 energy/gap improvement with acceptable tradeoff.

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
- [ ] Preserve `E = sum_i E_i` and force-from-energy contract by leaving source code intact.
- [ ] Mark implemented as a control replicate if required by workflow.
- [ ] Call `mark_unit_implemented.py --unit <UNIT> --actor implementation_subagent` after materialization/status handling.

## expected_benchmark_effect
- primary expected gain: No mechanism gain; variance baseline only.
- expected tradeoff: Consumes one run slot but prevents over-selection of noise.
- failure signal that would falsify this proposal: Smoke/runtime failure or metrics far from source, indicating reproducibility/runtime variance that must be considered.

## ablation_or_control
- required control or comparison: This is the control.
- optional zero-gate / source-fallback / readout-only ablation: Compare against fixed damping and scalar low-start gate.

## implementation_notes_for_subagent
Do not edit any runnable-unit code for this proposal. The implementation step should only record control status according to workflow scripts.
