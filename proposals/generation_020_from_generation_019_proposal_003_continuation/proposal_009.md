# Proposal 009: Training-only ISO17 energy-tail diagnostic

- family: energy_gap_objective_diagnostic
- phase: 2
- jump_type: wildcard
- budget_class: tiny
- expected_capability_gain: Test whether the source's ISO17 energy/gap weakness is partly an objective schedule issue rather than an architecture issue.

## one_sentence_hypothesis
A tiny late-epoch energy emphasis in train.py, with model.py unchanged, may reduce ISO17 energy/gap error while exposing whether architecture changes are necessary.

## mechanism_refs
- []

## evidence_refs
- benchmark_diagnosis.json ISO17 mixed_energy_mae=0.252341, gap_penalty=0.144950, final validation energy worse than early best
- current_code_profile.json train schedule energy_weight warms to 1.0 and force_weight to 20.0
- proposal_format.md training-objective proposal guidance
- mechanism_cards.json warning that success must be judged on energy/gap/Q, not force-only rank

## historical_relation
- source_unit: generation_019/proposal_003
- relation_to_source: ablation
- not_a_duplicate_of: This is model.py-identical and does not use GEN020-M01; it isolates training objective behavior from architecture changes.
- lesson_used: ISO17 force improves while energy/gap remain weak, suggesting a possible late force-dominance/energy-calibration issue.

## why_not_duplicate
Unlike proposal_006, this contains no PaiNN mixer. It is a wildcard diagnostic to decide whether the active source can improve through objective weighting alone.

## benchmark_rationale
- capacity/scaling hypothesis, if any: None; training-only.
- rmd17 energy: Monitor mixed_energy_mae=0.031769 for energy overemphasis side effects.
- rmd17 force: Main risk is degradation of mixed_force_mae=0.060948 if force_weight is reduced too much.
- rmd17 gap / Q: Preserve Q_rmd17=4.166948 and gap_penalty=0.010551.
- iso17 energy: Primary target mixed_energy_mae=0.252341 and other_energy_mae=0.279956; schedule should reduce late energy drift.
- iso17 force: Preserve mixed_force_mae=0.149767; do not accept force collapse.
- iso17 gap / Q: Success requires lower gap_penalty=0.144950 or higher Q_iso17=3.764325 and Q_total.
- training stability / runtime risk: No architecture/runtime overhead; risk is objective tradeoff and prior schedule diagnostics may be weak.
- control comparison expectation: Compare to exact control and proposal_006 to separate training-only from mechanism-plus-training effects.

## files_to_edit
- `model/model.py` none
- `model/train.py`
- never `config.json` for MLIP-quality changes

## code_insertion_points
- `model/train.py::train_model` epoch loop: keep existing warmup but add a late small energy multiplier, e.g. after midpoint interpolate energy_weight to 1.10-1.15 while keeping force_weight >=19.
- `model/train.py::history logging`: preserve existing field names for energy_weight, force_weight, learning_rate, grad_clip.
- `model/model.py`: no changes.

## minimal_edit_plan
1. Leave `model/model.py` byte-for-byte unchanged after materialization if possible.
2. Modify only the code-level train constants/schedule for a modest late energy emphasis.
3. Keep epoch count, optimizer, scheduler shape, grad_clip, data, evaluator, and metrics unchanged.
4. Ensure logged weights make the diagnostic interpretable.

## implementation_checklist
- [ ] Preserve `E = sum_i E_i` and force-from-energy contract.
- [ ] Preserve benchmark metric field names and runnable entrypoint contract.
- [ ] Modify only the allowed target unit files.
- [ ] Do not edit `config.json`; change MLIP knobs in `model/model.py` or `model/train.py`.
- [ ] Keep tensor shapes compatible with current dataloader and model forward.
- [ ] Do not change architecture, direct force heads, dataset splits, or eval formulas.
- [ ] Keep objective schedule bounded and documented in history fields.
- [ ] Call `mark_unit_implemented.py --unit <UNIT> --actor implementation_subagent` after edits.

## expected_benchmark_effect
- primary expected gain: Small ISO17 energy/gap/Q improvement if the source was underweighted for energy late in training.
- expected tradeoff: Possible force degradation; acceptable only if Q_total improves and gap does not worsen.
- failure signal that would falsify this proposal: Worse force/Q_total or no ISO17 energy/gap improvement, indicating architecture/path changes are needed.

## ablation_or_control
- required control or comparison: Exact control proposal_008 and mechanism-plus-schedule proposal_006.
- optional zero-gate / source-fallback / readout-only ablation: Not applicable; model code is the ablation boundary.

## implementation_notes_for_subagent
Treat this as diagnosis-driven with `mechanism_refs: []`. Do not add GEN020-M01 code here.
