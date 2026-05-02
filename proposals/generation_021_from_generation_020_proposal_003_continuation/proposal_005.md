# Proposal 005: Stronger Late Energy Emphasis Schedule

- family: loss_rebalance
- phase: 4
- jump_type: exploit
- budget_class: tiny
- expected_capability_gain: Test a stronger but bounded energy-weight schedule for ISO17 gap recovery while keeping force supervision dominant.

## one_sentence_hypothesis
A late ramp to energy_weight=1.5 and force_weight=16 should reveal whether current Q_total is limited by underweighted energy/gap terms rather than architecture.

## mechanism_refs
- GEN021-M02-energy-force-loss-rebalancing-control

## evidence_refs
- evidence_brief_20260501T011417Z.md
- mechanism_cards.json::GEN021-M02-energy-force-loss-rebalancing-control
- patch_blueprints.json::GEN021-M02-energy-force-loss-rebalancing-control
- generation_summaries/generation_020.json::proposal_003 ISO17 gap_penalty=0.14068 and Q_iso17=3.76869
- repo_artifact:repo_001 SchNetPack separate energy/force ModelOutput loss weights
- paper_artifact:paper_002 SchNet combined energy-force loss form

## historical_relation
- source_unit: generation_020/proposal_003
- relation_to_source: exploit
- not_a_duplicate_of: proposal_004 is mild 1.25/18; this is the upper bounded loss-rebalance sibling.
- why_not_duplicate: it changes only training weights but explores the stronger evidence-suggested range where force still dominates at >=16.
- lesson_used: neutral generation_020 children suggest small architecture edits are insufficient unless the objective rewards energy/gap calibration.

## benchmark_rationale
Discuss expected effects on all relevant benchmark signals, not force-only:
- capacity/scaling hypothesis, if any: none.
- rmd17 energy: expected improvement or neutral as scalar energy receives more gradient.
- rmd17 force: higher force-regression risk than proposal_004 because final force weight is 16.
- rmd17 gap / Q: Q_rmd17 may fall if force degradation dominates; acceptable only if Q_total rises.
- iso17 energy: primary target; energy MAE should improve if objective allocation is bottleneck.
- iso17 force: monitor closely; force loss remains much larger than energy but less dominant.
- iso17 gap / Q: target lower gap_penalty and meaningful Q_iso17 increase.
- training stability / runtime risk: no runtime increase; scientific risk is force-energy tradeoff.
- control comparison expectation: should deliver larger Q_total G_delta than proposal_004; if not, strong reweighting is too aggressive.

- validation terms: energy, force, gap penalty, Q_rmd17, Q_iso17, Q_total, and G_delta are the selection-facing signals.

## files_to_edit
- `model/model.py` if needed, otherwise `none`
- `model/train.py`
- never `config.json` for MLIP-quality changes

## code_insertion_points
- `model/train.py::train`: after warmup, linearly ramp epochs 4-8 from current weights to `epoch_energy_weight = energy_weight * 1.5` and `epoch_force_weight = force_weight * 0.8`.
- `model/train.py::run_epoch`: no loss formula changes; consume epoch weights.
- `model/model.py::EvolutionMLIP.forward`: none.
- code-level MLIP knobs may include `EvolutionMLIP.__init__` defaults, `MODEL_*` constants, or `TRAIN_*` constants when present

## minimal_edit_plan
1. Leave architecture unchanged.
2. Replace post-warmup constant weights with a bounded late ramp to 1.5 energy and 16 force.
3. Log weights in the existing history row as before; do not change eval semantics.

## implementation_checklist
- [ ] Preserve `E = sum_i E_i` and force-from-energy contract.
- [ ] Preserve benchmark metric field names and runnable entrypoint contract.
- [ ] Modify only the allowed target unit files.
- [ ] Do not edit `config.json`; change MLIP knobs in `model/model.py` or `model/train.py`.
- [ ] Keep tensor shapes compatible with current dataloader and model forward.
- [ ] Add no unbounded cubic neighbor/triplet loops unless explicitly justified by budget.
- [ ] Call `mark_unit_implemented.py --unit generation_021/proposal_005 --actor implementation_subagent` after edits.

## expected_benchmark_effect
- primary expected gain: Q_iso17 and Q_total lift through ISO17 energy/gap improvement.
- expected tradeoff: RMD17/ISO17 mixed_force_mae may worsen; Q_rmd17 could fall.
- failure signal that would falsify this proposal: positive energy movement with negative Q_total or G_delta because force penalties dominate.

## ablation_or_control
- required control or comparison: compare to proposal_004 mild loss rebalance and unchanged control.
- optional zero-gate / source-fallback / readout-only ablation: not applicable; train-only schedule.

## implementation_notes_for_subagent
Keep this as a clean objective-only exploit. Do not change optimizer, LR scheduler, model capacity, or config.json.
