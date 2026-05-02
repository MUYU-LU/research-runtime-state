# Proposal 006: Exact source replicate variance control

- family: source_variance_control
- phase: 0
- jump_type: control
- budget_class: tiny
- expected_capability_gain: Calibrate generation_023 variance before attributing small LES-tail gains to mechanism edits

## one_sentence_hypothesis
An exact copy of generation_022/proposal_006 establishes whether small Q_total, energy, force, or gap changes in this continuation exceed run-to-run variance.

## mechanism_refs
- []

## evidence_refs
- current source unit: generation_022/proposal_006
- context.md: source Q_total=4.042395946355124, Q_rmd17=4.195700703172324, Q_iso17=3.7576871122660367
- generation_022/proposal_007 control replicate: Q_total=4.052381423761268, showing variance can beat the mechanism source
- round policy control requirement for source fallback / variance control

## historical_relation
- source_unit: generation_022/proposal_006
- relation_to_source: control
- not_a_duplicate_of: This is intentionally an exact duplicate of source code for variance calibration; it is not a mechanism proposal and must not be interpreted as fresh evidence.
- lesson_used: proposal_006 was below the best generation_022 control replicate, so generation_023 needs a source/control anchor before selecting tiny LES-tail effects.

## why_not_duplicate
Clear control/ablation rationale: this file is an exact/source variance-control proposal. It should be materialized only as a control replicate and not counted as a new mechanism.

## benchmark_rationale
- capacity/scaling hypothesis, if any: none.
- rmd17 energy: expected to match source mixed_energy_mae=0.0289746 within variance.
- rmd17 force: expected to match source mixed_force_mae=0.0604828 within variance.
- rmd17 gap / Q: expected near source gap_penalty=0.010653 and Q_rmd17=4.195701, with variance potentially approaching control Q_rmd17=4.221827.
- iso17 energy: expected near source mixed_energy_mae=0.262740.
- iso17 force: expected near source mixed_force_mae=0.148905.
- iso17 gap / Q: expected near source gap_penalty=0.153666 and Q_iso17=3.757687.
- training stability / runtime risk: lowest risk; no code changes.
- control comparison expectation: any LES proposal should beat this replicate and the generation_022/proposal_007 control band before being treated as real progress.

## files_to_edit
- none
- never `config.json` for MLIP-quality changes

## code_insertion_points
- none
- `model/model.py`: no change
- `model/train.py`: no change

## minimal_edit_plan
1. Exact copy of generation_022/proposal_006 source unit.
2. Do not edit `model/model.py`.
3. Do not edit `model/train.py`.

## implementation_checklist
- [ ] Do not change `model/model.py`.
- [ ] Do not change `model/train.py`.
- [ ] Preserve benchmark metric field names and runnable entrypoint contract.
- [ ] Mark implemented as a control/source replicate if required by workflow.
- [ ] Call `mark_unit_implemented.py --unit <UNIT> --actor implementation_subagent` after confirming no edits.

## expected_benchmark_effect
- primary expected gain: none; variance calibration only.
- expected tradeoff: consumes one benchmark slot but improves interpretability.
- failure signal that would falsify this proposal: smoke or benchmark failure despite exact source copy, indicating workflow/runtime rather than model issue.

## ablation_or_control
- required control or comparison: compare all LES-tail proposals against this exact source replicate and generation_022/proposal_007.
- optional zero-gate / source-fallback / readout-only ablation: none; this is the source fallback itself.

## implementation_notes_for_subagent
Clear control/ablation rationale: materialize as an exact copy of generation_022/proposal_006. Do not add the GEN023-M01 LES tail here; the absence of `GEN023-M01-les-realspace-latent-charge-tail` is intentional because this is a variance/source control.
