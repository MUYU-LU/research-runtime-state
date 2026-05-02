# Proposal 008: Replace Muted Final Mixer With Direct Energy Residual

- family: residual_simplify
- phase: 4
- jump_type: backward-simplify
- budget_class: small
- expected_capability_gain: Test whether removing the underpowered final PaiNN-style mixer and adding a direct energy residual improves Q_total with cleaner attribution.

## one_sentence_hypothesis
If the final TPInvariantPaiNNMixing is too muted to help under 8 epochs, disabling it while adding a beta<=0.02 atomwise energy residual should improve energy/gap/Q and avoid hidden-state noise.

## mechanism_refs
- GEN021-M01-atomwise-energy-residual-calibration

## evidence_refs
- evidence_brief_20260501T011417Z.md
- mechanism_cards.json::GEN021-M01-atomwise-energy-residual-calibration muted final mixer diagnosis
- patch_blueprints.json::GEN021-M01-atomwise-energy-residual-calibration
- generation_summaries/generation_020.json::proposal_003 neutral_variance and source final mixer
- current source model.py::TPInvariantPaiNNMixing residual_scales scalar 0.05*sigmoid(-6), vector 0.025*sigmoid(-7)

## historical_relation
- source_unit: generation_020/proposal_003
- relation_to_source: simplify
- not_a_duplicate_of: proposal_001 leaves the final mixer active; this removes or bypasses it to test backward simplification.
- why_not_duplicate: it is not just an energy residual but a replacement of the muted hidden mixer with a direct scalar route.
- lesson_used: hidden-state vector mixer was likely too weakly coupled; direct energy path should be easier to train and evaluate.

## benchmark_rationale
Discuss expected effects on all relevant benchmark signals, not force-only:
- capacity/scaling hypothesis, if any: net capacity roughly neutral because one muted mixer is bypassed and one small residual head is added.
- rmd17 energy: may improve if final hidden mixer noise is removed; could regress if mixer supplied useful calibration.
- rmd17 force: should be stable because residual is conservative and capped; removal may reduce vector-gradient noise.
- rmd17 gap / Q: expect Q_rmd17 neutral; any large loss means final mixer was helpful despite small scale.
- iso17 energy: target lower mixed_energy_mae through direct residual.
- iso17 force: monitor for residual-induced regression.
- iso17 gap / Q: target gap_penalty reduction and Q_iso17 lift.
- training stability / runtime risk: slightly lower or equal runtime; low implementation risk.
- control comparison expectation: should beat source and proposal_001 if final mixer is harmful; otherwise proposal_001 is preferred. Require Q_total G_delta > +0.03 for clear win.

- validation terms: energy, force, gap penalty, Q_rmd17, Q_iso17, Q_total, and G_delta are the selection-facing signals.

## files_to_edit
- `model/model.py`
- `model/train.py` if needed, otherwise `none`
- never `config.json` for MLIP-quality changes

## code_insertion_points
- `model/model.py::EvolutionMLIP.__init__`: replace `self.final_tp_invariant_mixer = TPInvariantPaiNNMixing(...)` with `nn.Identity()`-style bypass or a flagless no-op wrapper, and add GEN021-M01 residual head beta<=0.02.
- `model/model.py::EvolutionMLIP.forward_energy`: skip final mixer application or have it return unchanged states; add residual energy after readout normalization.
- `model/train.py::train/run_epoch`: none.
- code-level MLIP knobs may include `EvolutionMLIP.__init__` defaults, `MODEL_*` constants, or `TRAIN_*` constants when present

## minimal_edit_plan
1. Make the final mixer a no-op without changing other interaction/TP branches.
2. Add the invariant atomwise energy residual from `[scalar_state, vector_norm]` with zero final output and beta<=0.02.
3. Keep training weights and optimizer unchanged.

## implementation_checklist
- [ ] Preserve `E = sum_i E_i` and force-from-energy contract.
- [ ] Preserve benchmark metric field names and runnable entrypoint contract.
- [ ] Modify only the allowed target unit files.
- [ ] Do not edit `config.json`; change MLIP knobs in `model/model.py` or `model/train.py`.
- [ ] Keep tensor shapes compatible with current dataloader and model forward.
- [ ] Add no unbounded cubic neighbor/triplet loops unless explicitly justified by budget.
- [ ] Call `mark_unit_implemented.py --unit generation_021/proposal_008 --actor implementation_subagent` after edits.

## expected_benchmark_effect
- primary expected gain: cleaner ISO17 energy/gap and Q_total/G_delta by replacing a muted indirect path.
- expected tradeoff: if final mixer was subtly beneficial, Q_rmd17 or Q_iso17 may fall.
- failure signal that would falsify this proposal: worse Q_total than source/control or residual-only proposal_001.

## ablation_or_control
- required control or comparison: compare to proposal_001, which keeps final mixer; compare to exact source control.
- optional zero-gate / source-fallback / readout-only ablation: residual beta=0 with mixer disabled would isolate mixer removal in a future round.

## implementation_notes_for_subagent
Do not delete the TPInvariantPaiNNMixing class if unnecessary; a no-op bypass at the call site is sufficient and safer for implementation.
