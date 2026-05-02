# Proposal 004: Mild Late Energy-Force Loss Rebalance

- family: loss_rebalance
- phase: 4
- jump_type: control
- budget_class: tiny
- expected_capability_gain: Diagnose whether the force-dominated MAE objective is suppressing energy/gap improvements under the fixed 8-epoch budget.

## one_sentence_hypothesis
Reducing late force domination from 20x to about 18x while raising energy weight to 1.25 should improve ISO17 energy/gap and Q_iso17 without sacrificing Q_rmd17 enough to hurt Q_total.

## mechanism_refs
- GEN021-M02-energy-force-loss-rebalancing-control

## evidence_refs
- evidence_brief_20260501T011417Z.md
- mechanism_cards.json::GEN021-M02-energy-force-loss-rebalancing-control
- patch_blueprints.json::GEN021-M02-energy-force-loss-rebalancing-control
- generation_summaries/generation_020.json::ISO17 energy/gap remain under-improved while force trend improves
- repo_artifact:repo_001 SchNetPack md17.yaml separate energy and forces loss weights
- paper_artifact:paper_001 Forces Are Not Enough

## historical_relation
- source_unit: generation_020/proposal_003
- relation_to_source: control
- not_a_duplicate_of: generation_020/proposal_005/006 combined model and train edits; this is train-only and bounded for attribution.
- why_not_duplicate: it leaves architecture unchanged and changes only epoch weights after warmup, directly testing GEN021-M02.
- lesson_used: source loss contribution is roughly energy 0.217*1 vs force 0.133*20, so energy/gap metrics may be underweighted.

## benchmark_rationale
Discuss expected effects on all relevant benchmark signals, not force-only:
- capacity/scaling hypothesis, if any: none; pure training-objective control.
- rmd17 energy: may improve slightly by emphasizing scalar energy.
- rmd17 force: primary risk is force MAE worsening; force weight remains high at >=18.
- rmd17 gap / Q: should remain close to source Q_rmd17=4.19815; reject if force regression dominates.
- iso17 energy: primary target is lower mixed_energy_mae and validation energy transfer.
- iso17 force: expected small regression or neutral; force still dominates total loss.
- iso17 gap / Q: expected lower gap_penalty and higher Q_iso17.
- training stability / runtime risk: no runtime cost; very low implementation risk.
- control comparison expectation: if Q_total G_delta is positive but small, use as diagnostic; if >+0.03, objective allocation is a real bottleneck.

- validation terms: energy, force, gap penalty, Q_rmd17, Q_iso17, Q_total, and G_delta are the selection-facing signals.

## files_to_edit
- `model/model.py` if needed, otherwise `none`
- `model/train.py`
- never `config.json` for MLIP-quality changes

## code_insertion_points
- `model/train.py::train`: after warmup, set `epoch_energy_weight = energy_weight * 1.25` and `epoch_force_weight = force_weight * 0.9`; preserve current warmup for epochs <= energy_warmup_epochs.
- `model/train.py::run_epoch`: keep loss_energy/loss_force definitions unchanged; only consume passed weights.
- `model/model.py::EvolutionMLIP.forward`: none; preserve force-from-energy autograd.
- code-level MLIP knobs may include `EvolutionMLIP.__init__` defaults, `MODEL_*` constants, or `TRAIN_*` constants when present

## minimal_edit_plan
1. Leave model.py unchanged.
2. Modify only the epoch weight schedule in train.py after warmup.
3. Keep force_weight floor >=18 and energy_weight exactly 1.25 late for a mild diagnostic.

## implementation_checklist
- [ ] Preserve `E = sum_i E_i` and force-from-energy contract.
- [ ] Preserve benchmark metric field names and runnable entrypoint contract.
- [ ] Modify only the allowed target unit files.
- [ ] Do not edit `config.json`; change MLIP knobs in `model/model.py` or `model/train.py`.
- [ ] Keep tensor shapes compatible with current dataloader and model forward.
- [ ] Add no unbounded cubic neighbor/triplet loops unless explicitly justified by budget.
- [ ] Call `mark_unit_implemented.py --unit generation_021/proposal_004 --actor implementation_subagent` after edits.

## expected_benchmark_effect
- primary expected gain: ISO17 energy/gap and Q_iso17 improvement through better objective allocation.
- expected tradeoff: possible force MAE regression, especially RMD17.
- failure signal that would falsify this proposal: energy improves but Q_total/G_delta is neutral or negative due to force/Q_rmd17 degradation.

## ablation_or_control
- required control or comparison: compare to unchanged source/control and proposal_005 stronger reweighting.
- optional zero-gate / source-fallback / readout-only ablation: not applicable; train-only control.

## implementation_notes_for_subagent
Do not edit architecture, model defaults, config.json, datasets, metrics, or evaluation; this is a bounded training-objective control only.
