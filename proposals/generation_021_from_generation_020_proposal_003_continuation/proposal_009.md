# Proposal 009: Nonzero LR Tail Training Control

- family: training_schedule_control
- phase: 4
- jump_type: control
- budget_class: tiny
- expected_capability_gain: Test whether the new/source residual pathways are undertrained because cosine annealing drives LR to zero by epoch 8.

## one_sentence_hypothesis
Keeping a small nonzero LR tail should improve energy/gap/Q learning under the fixed 8-epoch budget without changing architecture or benchmark semantics.

## mechanism_refs
- []

## evidence_refs
- evidence_brief_20260501T011417Z.md::diagnosis that generation_020 PaiNN-style mixer was likely too muted under 8 epochs with LR reaching zero
- mechanism_cards.json::GEN021-M01-atomwise-energy-residual-calibration diagnosis paragraphs
- current source model/train.py::CosineAnnealingLR T_max=max(epochs,1)
- generation_summaries/generation_020.json::neutral_variance best child below 0.03 margin

## historical_relation
- source_unit: generation_020/proposal_003
- relation_to_source: control
- not_a_duplicate_of: GEN021-M02 loss rebalancing changes objective allocation; this proposal changes only optimizer schedule tail.
- why_not_duplicate: it is diagnosis-driven training control with mechanism_refs empty because the evidence package's strong training mechanism is loss allocation, not LR scheduling.
- lesson_used: under an 8-epoch budget, a zero LR endpoint may freeze tiny residual paths before they affect energy/gap/Q.

## benchmark_rationale
Discuss expected effects on all relevant benchmark signals, not force-only:
- capacity/scaling hypothesis, if any: none.
- rmd17 energy: may improve if late learning continues rather than annealing fully to zero.
- rmd17 force: could improve or regress depending on late optimizer noise; grad_clip unchanged.
- rmd17 gap / Q: expected small Q_rmd17 movement; must stay within stable range.
- iso17 energy: target improvement by giving energy calibration more late updates.
- iso17 force: expected neutral; no loss reweight change.
- iso17 gap / Q: target lower gap_penalty if undertraining was bottleneck.
- training stability / runtime risk: no runtime cost; mild risk of overfitting or noisy final epoch.
- control comparison expectation: positive Q_total G_delta would support schedule-tail diagnosis; neutral result says LR tail is not enough.

- validation terms: energy, force, gap penalty, Q_rmd17, Q_iso17, Q_total, and G_delta are the selection-facing signals.

## files_to_edit
- `model/model.py` if needed, otherwise `none`
- `model/train.py`
- never `config.json` for MLIP-quality changes

## code_insertion_points
- `model/train.py::train`: change scheduler construction from `CosineAnnealingLR(optimizer, T_max=max(epochs,1))` to the same scheduler with a code-level `eta_min = learning_rate * 0.1` or equivalent small nonzero floor.
- `model/train.py::run_epoch`: none.
- `model/model.py::EvolutionMLIP`: none.
- code-level MLIP knobs may include `EvolutionMLIP.__init__` defaults, `MODEL_*` constants, or `TRAIN_*` constants when present

## minimal_edit_plan
1. Add a local code constant such as `TRAIN_LR_ETA_MIN_FRACTION = 0.1` in train.py.
2. Pass `eta_min=learning_rate * TRAIN_LR_ETA_MIN_FRACTION` to CosineAnnealingLR.
3. Leave loss weights, model architecture, epochs, data, metrics, and config unchanged.

## implementation_checklist
- [ ] Preserve `E = sum_i E_i` and force-from-energy contract.
- [ ] Preserve benchmark metric field names and runnable entrypoint contract.
- [ ] Modify only the allowed target unit files.
- [ ] Do not edit `config.json`; change MLIP knobs in `model/model.py` or `model/train.py`.
- [ ] Keep tensor shapes compatible with current dataloader and model forward.
- [ ] Add no unbounded cubic neighbor/triplet loops unless explicitly justified by budget.
- [ ] Call `mark_unit_implemented.py --unit generation_021/proposal_009 --actor implementation_subagent` after edits.

## expected_benchmark_effect
- primary expected gain: modest Q_total and G_delta improvement if undertraining, not architecture, limited source performance.
- expected tradeoff: possible slight overfit/noisy force or energy at final epochs.
- failure signal that would falsify this proposal: no energy/gap improvement or negative Q_total due to noisier optimization.

## ablation_or_control
- required control or comparison: compare to exact source control and loss-rebalance proposals.
- optional zero-gate / source-fallback / readout-only ablation: not applicable; this is a training schedule control.

## implementation_notes_for_subagent
This proposal is intentionally diagnosis-driven with no strong mechanism_refs. Keep the change minimal and code-level; do not change epochs or config.json.
