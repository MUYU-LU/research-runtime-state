# Proposal 006: Tiny Energy Residual Plus Mild Loss Rebalance

- family: residual_plus_objective
- phase: 4
- jump_type: exploit
- budget_class: small
- expected_capability_gain: Combine the direct residual mechanism with a very mild objective shift so the new energy path receives enough scalar supervision within 8 epochs.

## one_sentence_hypothesis
A beta<=0.01 atomwise residual paired with late 1.2/19 energy-force weights should improve energy/gap/Q more reliably than either factor alone while keeping runtime and force risk bounded.

## mechanism_refs
- GEN021-M01-atomwise-energy-residual-calibration
- GEN021-M02-energy-force-loss-rebalancing-control

## evidence_refs
- evidence_brief_20260501T011417Z.md
- mechanism_cards.json::GEN021-M01-atomwise-energy-residual-calibration
- mechanism_cards.json::GEN021-M02-energy-force-loss-rebalancing-control
- patch_blueprints.json::GEN021-M01-atomwise-energy-residual-calibration
- patch_blueprints.json::GEN021-M02-energy-force-loss-rebalancing-control
- generation_summaries/generation_020.json::neutral_variance best child below margin
- repo_artifact:repo_001 Atomwise and energy/forces loss traces

## historical_relation
- source_unit: generation_020/proposal_003
- relation_to_source: exploit
- not_a_duplicate_of: generation_020/proposal_005/006 combined edits but not this direct residual mechanism; proposals_001 and_004 are single-factor siblings.
- why_not_duplicate: uses lower beta and lower loss shift than standalone variants to bound two-factor risk.
- lesson_used: the prior mixer was physically legal but too muted under 8 epochs and force-dominated loss; combine a direct path with just enough energy emphasis.

## benchmark_rationale
Discuss expected effects on all relevant benchmark signals, not force-only:
- capacity/scaling hypothesis, if any: one tiny residual head; no interaction or basis scaling.
- rmd17 energy: expected neutral-to-better from residual and mild energy weight.
- rmd17 force: force risk bounded by beta<=0.01 and force_weight>=19.
- rmd17 gap / Q: should preserve Q_rmd17 close to source; reject if RMD17 collapses.
- iso17 energy: primary target from both model path and objective allocation.
- iso17 force: expected neutral-to-slight regression; force remains dominant.
- iso17 gap / Q: target gap_penalty reduction and Q_iso17 lift.
- training stability / runtime risk: small runtime cost; moderate attribution complexity because two factors change.
- control comparison expectation: should exceed both unchanged source and single-factor proposal expectations with Q_total G_delta > +0.03; otherwise split factors are preferable.

- validation terms: energy, force, gap penalty, Q_rmd17, Q_iso17, Q_total, and G_delta are the selection-facing signals.

## files_to_edit
- `model/model.py`
- `model/train.py`
- never `config.json` for MLIP-quality changes

## code_insertion_points
- `model/model.py::EvolutionMLIP.__init__`: add small zero-output residual head on `[scalar_state, vector_norm]` with beta cap 0.01.
- `model/model.py::EvolutionMLIP.forward_energy`: add residual energy before return, preserving autograd forces.
- `model/train.py::train`: after warmup use `epoch_energy_weight = energy_weight * 1.2` and `epoch_force_weight = force_weight * 0.95`.
- code-level MLIP knobs may include `EvolutionMLIP.__init__` defaults, `MODEL_*` constants, or `TRAIN_*` constants when present

## minimal_edit_plan
1. Implement GEN021-M01 residual with beta cap 0.01.
2. Implement mild GEN021-M02 post-warmup weight schedule 1.2 energy / 19 force.
3. Leave optimizer, scheduler, dataset, metrics, and config unchanged.

## implementation_checklist
- [ ] Preserve `E = sum_i E_i` and force-from-energy contract.
- [ ] Preserve benchmark metric field names and runnable entrypoint contract.
- [ ] Modify only the allowed target unit files.
- [ ] Do not edit `config.json`; change MLIP knobs in `model/model.py` or `model/train.py`.
- [ ] Keep tensor shapes compatible with current dataloader and model forward.
- [ ] Add no unbounded cubic neighbor/triplet loops unless explicitly justified by budget.
- [ ] Call `mark_unit_implemented.py --unit generation_021/proposal_006 --actor implementation_subagent` after edits.

## expected_benchmark_effect
- primary expected gain: positive G_delta through ISO17 energy/gap/Q lift without RMD17 force collapse.
- expected tradeoff: attribution is less clean than single-factor controls; slight force regression possible.
- failure signal that would falsify this proposal: neither Q_iso17 nor Q_total beats single-factor controls, or Q_rmd17 drops materially.

## ablation_or_control
- required control or comparison: compare to proposal_001 residual-only and proposal_004 loss-only.
- optional zero-gate / source-fallback / readout-only ablation: beta zero with the same weights would isolate loss effect if needed later.

## implementation_notes_for_subagent
Use conservative constants; do not escalate beta or loss weights beyond this proposal because this is the bounded combined test.
