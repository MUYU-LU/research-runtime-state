# Proposal 002: Late stage energy reweight only

- family: loss_rebalance
- phase: 2
- jump_type: exploit
- budget_class: tiny
- expected_capability_gain: Test the evidence-backed stage-two loss rebalance without touching atomref initialization or the model architecture.

## one_sentence_hypothesis
A bounded final-third increase in energy loss weight after force learning stabilizes should recover ISO17 energy while preserving most of the source unit force advantage.

## mechanism_refs
- MATERIALIZED-ENERGY-BASELINE-STAGE2-001

## evidence_refs
- /home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/evidence_run_20260428T083923Z/mechanism_cards.json
- /home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/evidence_run_20260428T083923Z/patch_blueprints.json
- paper_artifact:paper_001
- paper_artifact:paper_002
- repo_artifact:repo_001
- /home/lmy/.openclaw/workspace/research_runtime/ledger/frontier.jsonl

## historical_relation
- source_unit: generation_011/proposal_007
- relation_to_source: exploit
- not_a_duplicate_of: This differs from proposal_001 by leaving atomref random/trainable and from generation_011 proposals by making only a scalar loss-schedule edit.
- lesson_used: The source unit force path is useful, but force-heavy training can hide energy offsets; reweight late rather than from epoch 1.

## why_not_duplicate
This differs from proposal_001 by leaving atomref random/trainable and from generation_011 proposals by making only a scalar loss-schedule edit.

## benchmark_rationale
- rmd17 energy: should remain close to source unless the edit directly changes the energy readout or loss weighting; any gain is secondary to ISO17 recovery.
- rmd17 force: protect the source unit's conservative force path; force-only gains are not sufficient if energy/Q regress.
- rmd17 gap / Q: monitor for gap penalty changes caused by calibration drift; source-like RMD17 Q is acceptable.
- iso17 energy: primary diagnostic for generation_012 because generation_011/proposal_007 improved force but left an energy-transfer bottleneck.
- iso17 force: should stay near source; modest regression is acceptable only if energy/Q improves materially.
- iso17 gap / Q: target lower `mixed_energy_mae` and better `Q_iso17` without worsening split gap semantics.
- training stability / runtime risk: bounded; no benchmark data, split, eval, metric-field, or entrypoint changes are allowed.
- control comparison expectation: compare against proposal_010 source-control and the source unit generation_011/proposal_007.

## files_to_edit
- `model/train.py`

## code_insertion_points
- `model/model.py::EvolutionMLIP`: no change.
- `model/train.py::train`: replace fixed warmup-to-1 energy schedule with a late-stage scalar schedule after about 65% of epochs, e.g. energy weight 1.0 -> 1.35 and force weight 20 -> 17.5.
- `model/train.py::run_epoch`: keep `loss = energy_weight * loss_energy + force_weight * loss_force` and preserve returned keys.

## minimal_edit_plan
1. Locate the epoch loop where `epoch_energy_weight` and `epoch_force_weight` are set.
2. Keep the existing early force-focused warmup, then for epochs >= ceil(0.65 * epochs) smoothly increase energy weight and modestly reduce force weight.
3. Do not change model code, optimizer, metric names, or dataloader semantics.

## implementation_checklist
- [ ] Preserve `E = sum_i E_i` and force-from-energy contract.
- [ ] Preserve benchmark metric field names and runnable entrypoint contract.
- [ ] Modify only the allowed target unit files.
- [ ] Keep tensor shapes compatible with current dataloader and model forward.
- [ ] Add no unbounded cubic neighbor/triplet loops unless explicitly justified by budget.
- [ ] Call `mark_unit_implemented.py --unit <UNIT> --actor implementation_subagent` after edits.

## expected_benchmark_effect
- primary expected gain: ISO17 `mixed_energy_mae` and energy-gap/Q recovery with minimal code risk.
- expected tradeoff: possible small ISO17/RMD17 force degradation if reweighting starts too early or is too large.
- failure signal that would falsify this proposal: force MAE degrades materially and energy MAE stays near source.

## ablation_or_control
- required control or comparison: compare to proposal_001 atomref-only and proposal_010 source-control.
- optional zero-gate / source-fallback / readout-only ablation: set late-stage multiplier to 1.0 to recover exact source training weights.

## implementation_notes_for_subagent
Implement only inside the materialized target unit, normally limited to `model/model.py` and/or `model/train.py` as listed above. Keep benchmark data, split semantics, evaluation semantics, metric field names, and runnable-unit entrypoint contract fixed. Do not add independent force heads: forces must remain `-autograd(total_energy, positions)`. Use only training-split information for any atomref or bias initialization; never use validation/test energies. If a proposed optional step becomes shape-risky, prefer the smallest source-fallback version rather than broad rewrites.
