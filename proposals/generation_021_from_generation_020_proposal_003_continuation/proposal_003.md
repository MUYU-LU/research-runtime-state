# Proposal 003: Higher-Cap Vector-Norm Energy Residual

- family: atomwise_energy_residual
- phase: 4
- jump_type: exploit
- budget_class: small
- expected_capability_gain: Test whether the direct residual needs the evidence-recommended upper cap of 0.05 to escape the undertrained muted-mixer regime.

## one_sentence_hypothesis
A bounded beta<=0.05 atomwise residual on `[scalar_state, vector_norm]` should produce a larger positive G_delta than the source if generation_020 failed mainly from excessive residual attenuation.

## mechanism_refs
- GEN021-M01-atomwise-energy-residual-calibration

## evidence_refs
- evidence_brief_20260501T011417Z.md
- mechanism_cards.json::GEN021-M01-atomwise-energy-residual-calibration beta <=0.02 or 0.05
- patch_blueprints.json::GEN021-M01-atomwise-energy-residual-calibration
- generation_summaries/generation_020.json::proposal_003 scalar_scale approx 1.24e-4 and vector_scale approx 2.28e-5 diagnosis
- paper_artifact:paper_001 force accuracy alone not enough
- repo_artifact:repo_001 Atomwise.forward and Forces.forward

## historical_relation
- source_unit: generation_020/proposal_003
- relation_to_source: exploit
- not_a_duplicate_of: proposal_001 uses the safer 0.02 cap; this variant intentionally tests the evidence-allowed 0.05 cap for under-attenuation.
- why_not_duplicate: generation_020 hidden mixer cap was tiny in effective scale; this uses zero-output residual with a larger direct energy scale, not a new hidden mixer.
- lesson_used: the best child was neutral with Q_total=4.04784 and ISO17 gap_penalty=0.14068; stronger direct energy calibration may be needed to clear the 0.03 margin.

## benchmark_rationale
Discuss expected effects on all relevant benchmark signals, not force-only:
- capacity/scaling hypothesis, if any: small readout capacity increase only; no interaction-depth or basis scaling.
- rmd17 energy: may improve mixed_energy_mae if residual captures final calibration; cap raises overfit risk.
- rmd17 force: higher risk than proposal_001 because larger residual gradients can perturb forces.
- rmd17 gap / Q: require Q_rmd17 not to lose more than energy/gap gain; gap_penalty should not exceed source materially.
- iso17 energy: stronger primary target; expected lower mixed_energy_mae if source is under-corrected.
- iso17 force: monitor mixed_force_mae for regression from residual gradients.
- iso17 gap / Q: should lower gap_penalty and increase Q_iso17 enough to justify larger beta.
- training stability / runtime risk: low runtime, moderate objective tradeoff risk.
- control comparison expectation: must beat proposal_001 or produce Q_total G_delta > +0.03; otherwise prefer lower cap.

- validation terms: energy, force, gap penalty, Q_rmd17, Q_iso17, Q_total, and G_delta are the selection-facing signals.

## files_to_edit
- `model/model.py`
- `model/train.py` if needed, otherwise `none`
- never `config.json` for MLIP-quality changes

## code_insertion_points
- `model/model.py::EvolutionMLIP.__init__`: add residual head identical to proposal_001 but with scale cap 0.05.
- `model/model.py::EvolutionMLIP.forward_energy`: add residual from `[scalar_state, vector_norm]` after readout normalization and before final energy return.
- `model/train.py::train/run_epoch`: none.
- code-level MLIP knobs may include `EvolutionMLIP.__init__` defaults, `MODEL_*` constants, or `TRAIN_*` constants when present

## minimal_edit_plan
1. Implement the same invariant residual data flow as GEN021-M01.
2. Use beta cap 0.05 while keeping final projection zero-initialized.
3. Do not change loss weights or scheduler so beta-cap effect is isolated.

## implementation_checklist
- [ ] Preserve `E = sum_i E_i` and force-from-energy contract.
- [ ] Preserve benchmark metric field names and runnable entrypoint contract.
- [ ] Modify only the allowed target unit files.
- [ ] Do not edit `config.json`; change MLIP knobs in `model/model.py` or `model/train.py`.
- [ ] Keep tensor shapes compatible with current dataloader and model forward.
- [ ] Add no unbounded cubic neighbor/triplet loops unless explicitly justified by budget.
- [ ] Call `mark_unit_implemented.py --unit generation_021/proposal_003 --actor implementation_subagent` after edits.

## expected_benchmark_effect
- primary expected gain: larger ISO17 energy/gap improvement and positive Q_total/G_delta.
- expected tradeoff: force and RMD17 Q regression risk if beta over-corrects.
- failure signal that would falsify this proposal: Q_iso17 rises but Q_rmd17 falls enough to keep Q_total within neutral variance or negative G_delta.

## ablation_or_control
- required control or comparison: compare to proposal_001 low-cap residual and unchanged control.
- optional zero-gate / source-fallback / readout-only ablation: initialize final residual output to zero so source fallback is exact at construction.

## implementation_notes_for_subagent
This is the intentionally stronger sibling of proposal_001; do not combine it with loss reweighting because attribution must stay on residual scale.
