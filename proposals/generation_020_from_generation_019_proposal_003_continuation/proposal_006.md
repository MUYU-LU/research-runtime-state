# Proposal 006: PaiNN mixer with late energy-weight stabilization

- family: painn_energy_schedule_probe
- phase: 5
- jump_type: jump
- budget_class: small
- expected_capability_gain: Test whether vector-norm mixing needs a slightly less force-dominated late objective to reduce ISO17 energy/gap error.

## one_sentence_hypothesis
A bounded M01 mixer paired with a small code-level late energy-weight lift should improve ISO17 energy/gap without changing benchmark metrics or the force-from-energy contract.

## mechanism_refs
- GEN020-M01-painn-intra-layer-vector-norm-mixing

## evidence_refs
- mechanism_cards.json expected effect targets ISO17 mixed_energy_mae/gap and warns against force-only interpretation
- proposal_format.md training-objective proposal guidance
- current_code_profile.json train schedule energy_weight warms 0.733->1.0 and force_weight 21.333->20.0
- benchmark_diagnosis.json ISO17 best val energy=0.550456 early while final energy worsens, final force improves

## historical_relation
- source_unit: generation_019/proposal_003
- relation_to_source: jump
- not_a_duplicate_of: Unlike proposals 001-005, this changes train.py objective schedule in addition to M01; unlike prior training-only diagnostics, it remains mechanism-centric and uses the strong insertion point.
- lesson_used: ISO17 force trend improves while energy/gap remain weak, so a tiny objective adjustment may be needed to let scalar feedback optimize the right signal.

## why_not_duplicate
This is not a force-only or schedule-only proposal. The training tweak is explicitly bounded and tied to GEN020-M01's energy/gap target.

## benchmark_rationale
- capacity/scaling hypothesis, if any: No model capacity scaling; objective-shape probe.
- rmd17 energy: Energy weight lift should not hurt mixed_energy_mae=0.031769; monitor because RMD17 is already strong.
- rmd17 force: Slight risk to mixed_force_mae=0.060948 if force weight is reduced too much; keep force_weight near 20.
- rmd17 gap / Q: Preserve gap_penalty=0.010551 and Q_rmd17=4.166948.
- iso17 energy: Primary target mixed_energy_mae=0.252341 and final val energy instability; late energy emphasis may reduce within/other energy split.
- iso17 force: Preserve mixed_force_mae=0.149767; do not trade large force loss for small energy gain.
- iso17 gap / Q: Lower gap_penalty=0.144950 and raise Q_iso17=3.764325; Q_total must improve, not just energy alone.
- training stability / runtime risk: No architectural extra beyond M01; objective change risk is interpretability and force tradeoff.
- control comparison expectation: Compare to proposal_001 to separate mechanism from objective schedule.

## files_to_edit
- `model/model.py`
- `model/train.py`
- never `config.json` for MLIP-quality changes

## code_insertion_points
- `model/model.py::TPInvariantPaiNNMixing` and `EvolutionMLIP.forward_energy`: implement bounded per-layer M01 mixer.
- `model/train.py::train_model` epoch loop: after warmup, use a modest late energy multiplier such as 1.10-1.20 while keeping force_weight >=18-20.
- `model/train.py::history logging`: continue logging energy_weight, force_weight, grad_clip with existing field names.

## minimal_edit_plan
1. Implement source-recoverable M01 mixer.
2. Keep early epochs as source schedule; in late epochs only, modestly raise energy_weight or reduce force_weight no more than about 10%.
3. Preserve optimizer, scheduler, epochs, data, eval, and metric names.
4. Make constants code-local and easy to revert.

## implementation_checklist
- [ ] Preserve `E = sum_i E_i` and force-from-energy contract.
- [ ] Preserve benchmark metric field names and runnable entrypoint contract.
- [ ] Modify only the allowed target unit files.
- [ ] Do not edit `config.json`; change MLIP knobs in `model/model.py` or `model/train.py`.
- [ ] Keep tensor shapes compatible with current dataloader and model forward.
- [ ] Do not add direct force losses beyond the existing force-from-energy objective.
- [ ] Keep objective schedule bounded and logged.
- [ ] Call `mark_unit_implemented.py --unit <UNIT> --actor implementation_subagent` after edits.

## expected_benchmark_effect
- primary expected gain: ISO17 mixed_energy_mae/gap and Q_iso17 improvement when M01 scalar feedback is optimized with slightly better energy emphasis.
- expected tradeoff: Possible small force regression; unacceptable if Q_total or gap worsens.
- failure signal that would falsify this proposal: It underperforms proposal_001 or produces force degradation exceeding energy/gap benefit.

## ablation_or_control
- required control or comparison: Compare to pure M01 proposal_001 and training-only wildcard proposal_009.
- optional zero-gate / source-fallback / readout-only ablation: Zero M01 mixer leaves a schedule diagnostic but not an external-mechanism win.

## implementation_notes_for_subagent
Keep the schedule tweak tiny and documented. Do not change benchmark formulas, split semantics, epoch count, or config.
