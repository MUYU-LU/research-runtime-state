# Proposal 005: Fixed offset with energy-balanced loss schedule

- family: frozen_offset_energy_balance
- phase: 3
- jump_type: jump
- budget_class: small
- expected_capability_gain: Pair frozen atomref with a less force-dominant late loss schedule to address energy drift while preserving conservative force learning.

## one_sentence_hypothesis
Freezing atomref removes offset drift, and modestly increasing late energy weight should further improve ISO17 energy/gap without changing model capacity or evaluation semantics.

## mechanism_refs
- MATERIALIZED-FROZEN-LSTSQ-ATOMREF-OFFSET-001

## evidence_refs
- paper_artifact:paper_002::Forces Are Not Enough energy-stability warning
- repo_artifact:repo_001::src/schnetpack/configs/experiment/md17.yaml
- /home/lmy/.openclaw/workspace/research_runtime/ledger/frontier.jsonl::generation_012/proposal_005
- /home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/evidence_run_20260428T152307Z/proposal_constraints.json

## historical_relation
- source_unit: generation_012/proposal_005
- relation_to_source: jump
- not_a_duplicate_of: Proposal 001 because this changes training loss weights in addition to offset freezing.
- lesson_used: Source train history shows force-heavy training and ISO17 validation energy worsening despite force improvement; energy must be protected explicitly.

## benchmark_rationale
- rmd17 energy: Higher late energy weight may preserve or improve the already strong RMD17 energy.
- rmd17 force: Slight force tradeoff is possible but should be bounded because force_weight remains high.
- rmd17 gap / Q: If energy improves more than force regresses, Q_rmd17 remains strong.
- iso17 energy: Primary target is lower mixed_energy_mae and reduced validation energy drift.
- iso17 force: Expected small degradation at worst; monitor mixed_force_mae.
- iso17 gap / Q: Expected gain if energy/gap penalties dominate current ISO17 weakness.
- training stability / runtime risk: No architecture runtime change; only scalar weights.
- control comparison expectation: Should outperform source on energy/gap; pure freeze controls whether schedule change is necessary.

## files_to_edit
- `model/train.py`
- `model/model.py` none

## code_insertion_points
- `model/model.py::EvolutionMLIP.forward_energy`: no change.
- `model/train.py::train`: freeze fitted atomref before optimizer creation; adjust `epoch_energy_weight`/`epoch_force_weight` schedule to end at slightly higher energy emphasis, e.g. source defaults with `energy_weight * (0.8 + 0.4 * warmup_ratio)` and `force_weight * (1.05 - 0.05 * warmup_ratio)`.

## minimal_edit_plan
1. Capture and freeze the fitted atomref as in Proposal 001.
2. Modify only the deterministic epoch weight formulas; keep history keys `energy_weight` and `force_weight` unchanged.
3. Preserve epoch count, optimizer type, scheduler, dataloaders, and eval code.

## implementation_checklist
- [ ] Preserve `E = sum_i E_i` and force-from-energy contract.
- [ ] Preserve benchmark metric field names and runnable entrypoint contract.
- [ ] Modify only the allowed target unit files.
- [ ] Keep tensor shapes compatible with current dataloader and model forward.
- [ ] Add no unbounded cubic neighbor/triplet loops unless explicitly justified by budget.
- [ ] Call `mark_unit_implemented.py --unit <UNIT> --actor implementation_subagent` after edits.
- [ ] Do not introduce early stopping or validation-dependent loss changes.

## expected_benchmark_effect
- primary expected gain: Better ISO17 energy/gap and possibly RMD17 energy while retaining most force performance.
- expected tradeoff: Force MAE may regress if energy weight becomes too strong.
- failure signal that would falsify this proposal: Q_total falls because force degradation exceeds energy/gap improvement.

## ablation_or_control
- required control or comparison: Compare against Proposal 001 pure freeze and source control.
- optional zero-gate / source-fallback / readout-only ablation: Keep config keys available so default values can fall back to source if constants are not changed.

## implementation_notes_for_subagent
Use fixed constants only. Do not inspect validation metrics to adapt training; benchmark semantics and split usage must remain fixed.
