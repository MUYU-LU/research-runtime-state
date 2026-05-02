# Proposal 007: Exact Source Control Replicate

- family: source_control
- phase: 4
- jump_type: control
- budget_class: tiny
- expected_capability_gain: Estimate generation_020/proposal_003 variance under the same benchmark before attributing small G_delta to new mechanisms.

## one_sentence_hypothesis
An unchanged replicate of generation_020/proposal_003 establishes whether observed Q_rmd17, Q_iso17, Q_total, gap penalty, and G_delta shifts exceed neutral run variance.

## mechanism_refs
- []

## evidence_refs
- current source unit generation_020/proposal_003
- generation_summaries/generation_020.json::proposal_008 control_replicate Q_total=3.9806335007424267
- evidence_brief_20260501T011417Z.md::generation_020 best child neutral_variance
- round policy control requirement

## historical_relation
- source_unit: generation_020/proposal_003
- relation_to_source: control
- not_a_duplicate_of: this intentionally duplicates source code but not as a mechanism proposal; it is the required variance/control anchor.
- why_not_duplicate: exact-copy controls are allowed as controls and must be labeled as such with mechanism_refs empty.
- lesson_used: generation_020 best child was below margin, so small Q changes need a fresh control comparison.

## benchmark_rationale
Discuss expected effects on all relevant benchmark signals, not force-only:
- capacity/scaling hypothesis, if any: none.
- rmd17 energy: expected to reproduce source mixed_energy_mae near 0.02895 within variance.
- rmd17 force: expected to reproduce source mixed_force_mae near 0.06032 within variance.
- rmd17 gap / Q: expected Q_rmd17 near 4.19815 and gap_penalty near 0.00828 within variance.
- iso17 energy: expected mixed_energy_mae near 0.26482 within variance.
- iso17 force: expected mixed_force_mae near 0.14660 within variance.
- iso17 gap / Q: expected Q_iso17 near 3.76869 and gap_penalty near 0.14068 within variance.
- training stability / runtime risk: no new risk beyond source.
- control comparison expectation: G_delta should be interpreted as variance baseline; new proposals should beat this by Q_total margin >0.03.

- validation terms: energy, force, gap penalty, Q_rmd17, Q_iso17, Q_total, and G_delta are the selection-facing signals.

## files_to_edit
- none
- never `config.json` for MLIP-quality changes

## code_insertion_points
- none

## minimal_edit_plan
1. Exact copy of source unit.

## implementation_checklist
- [ ] Do not change `model/model.py`.
- [ ] Do not change `model/train.py`.
- [ ] Mark implemented as control replicate if required by workflow.
- [ ] Preserve benchmark metric field names and runnable entrypoint contract.
- [ ] Do not edit `config.json`; change MLIP knobs in `model/model.py` or `model/train.py` only when a proposal requires them.

## expected_benchmark_effect
- primary expected gain: none; this is a variance/control baseline.
- expected tradeoff: consumes one benchmark slot but prevents over-interpreting neutral Q_total/G_delta shifts.
- failure signal that would falsify this proposal: code differs from generation_020/proposal_003 or metrics are used as mechanism evidence.

## ablation_or_control
- required control or comparison: compare all mechanism proposals against this exact-copy result.
- optional zero-gate / source-fallback / readout-only ablation: not applicable.

## implementation_notes_for_subagent
Materialize as an exact copy only. Do not edit model.py, train.py, config.json, or any benchmark semantics; if the workflow requires marking implementation, mark it as a control replicate for generation_021/proposal_007.
