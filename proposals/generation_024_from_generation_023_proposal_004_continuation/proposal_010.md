# Proposal 010: Pure energy-weight stabilization for source tail

- family: energy_weight_stabilization_source_tail
- phase: 2
- jump_type: wildcard
- budget_class: tiny
- expected_capability_gain: Improve ISO17 energy/gap by modestly rebalancing code-level loss weights without changing proposal_004 architecture.

## one_sentence_hypothesis
A small code-level increase in energy loss weight can test whether proposal_004's ISO17 gap is partly an objective-balance issue rather than a missing SOG mechanism.

## mechanism_refs
- []

## evidence_refs
- benchmark_diagnosis.json: ISO17 last-epoch val energy is unstable/high while best_val_energy_mae was much lower; source mixed_energy_mae=0.2679998259591584 and gap_penalty=0.1531424820304152
- context.md current training knobs: `TRAIN_ENERGY_WEIGHT=1.0`, `TRAIN_FORCE_WEIGHT=20.0`, learning_rate=0.001, weight_decay=1e-05
- proposal_format.md: training-objective evolution is valid as code-level defaults when benchmark metrics/splits remain fixed
- generation_023_summary.json: proposal_004 has best generation Q_total but ISO17 is not generation-best, so a tiny objective probe is useful
- lineage_stats.json: mechanism families have mixed outcomes; objective control helps separate training balance from architecture changes.

## historical_relation
- source_unit: generation_023/proposal_004
- relation_to_source: ablation
- not_a_duplicate_of: Not a duplicate of proposal_006 because it changes only training loss weights and no SOG/architecture code; not a duplicate of source because optimization objective changes.
- lesson_used: Source force trends are improving and energy trends differ by dataset; a bounded pure objective probe can identify whether energy/gap weakness is trainable without new mechanisms.

## why_not_duplicate
This is the pure-training counterpart to the SOG+objective proposal. It should keep `model/model.py` identical to source and edit only `model/train.py` code-level constants, enabling a clean objective ablation.

## benchmark_rationale
- capacity/scaling hypothesis, if any: none; training-objective hypothesis only.
- rmd17 energy: expected improvement or stability from energy_weight increase.
- rmd17 force: possible mild degradation if energy competes with force; keep force_weight unchanged at 20.0 to minimize this.
- rmd17 gap / Q: source gap is already strong, so changes should be modest.
- iso17 energy: primary target; higher energy weight may reduce mixed_energy_mae and last-epoch energy drift.
- iso17 force: expected neutral-to-slight degradation; acceptable only if Q_total improves.
- iso17 gap / Q: expected gain if gap_penalty is partly energy calibration rather than representation.
- training stability / runtime risk: tiny; no architecture or runtime complexity changes.
- control comparison expectation: if this matches SOG+objective, objective balance may be the key; if it fails while SOG succeeds, mechanism dominates.

## files_to_edit
- none (`model/model.py` unchanged)
- `model/train.py`
- never `config.json` for MLIP-quality changes

## code_insertion_points
- `model/train.py::MLIP code-level defaults`: change `TRAIN_ENERGY_WEIGHT = 1.0` to a bounded value such as `1.25` or `1.5`; leave `TRAIN_FORCE_WEIGHT = 20.0` unless a very small adjustment to `18.0` is explicitly documented.
- `model/train.py::run_epoch`: no semantic change; continue computing the same energy and force losses and metrics.
- `model/model.py`: no change.

## minimal_edit_plan
1. Edit only `TRAIN_ENERGY_WEIGHT` in `model/train.py` to a modest value, preferably `1.25` for lower force-regression risk.
2. Leave force weight, learning rate, weight decay, epoch loop, dataloader, and evaluation untouched.
3. Add a short comment that this is a pure objective ablation for ISO17 energy/gap stability.

## implementation_checklist
- [ ] Preserve `E = sum_i E_i` and force-from-energy contract.
- [ ] Preserve benchmark metric field names and runnable entrypoint contract.
- [ ] Modify only the allowed target unit files.
- [ ] Do not edit `config.json`; change MLIP knobs in `model/model.py` or `model/train.py`.
- [ ] Keep tensor shapes compatible with current dataloader and model forward.
- [ ] Add no unbounded cubic neighbor/triplet loops unless explicitly justified by budget.
- [ ] Do not change `model/model.py` for this proposal.
- [ ] Do not change dataset, split, evaluation, metric names, or launch protocol.
- [ ] Call `mark_unit_implemented.py --unit <UNIT> --actor implementation_subagent` after edits.

## expected_benchmark_effect
- primary expected gain: lower ISO17 energy/gap error without representation changes.
- expected tradeoff: possible force MAE regression because force loss is already heavily weighted.
- failure signal that would falsify this proposal: energy metrics do not improve, or force degradation reduces Q_total below exact source/control.

## ablation_or_control
- required control or comparison: compare to exact source proposal_008 and SOG+objective proposal_006.
- optional zero-gate / source-fallback / readout-only ablation: not applicable; model architecture is unchanged.

## implementation_notes_for_subagent
This is diagnosis-driven and has no external mechanism claim. Keep it pure: only training constants in `model/train.py`, no changes to model architecture, data, metrics, config, or evaluation code.
