# Proposal 009: Wildcard stochastic atomref smoothing

- family: atomref_smoothing
- phase: 2
- jump_type: wildcard
- budget_class: small
- expected_capability_gain: Apply exponential smoothing between source atomref values and train-split fitted atomrefs to avoid noisy all-in calibration.

## one_sentence_hypothesis
A convex-smoothed atomref initialization can capture stable composition offsets while avoiding overfitting from small train-set least-squares estimates.

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
- relation_to_source: ablation
- not_a_duplicate_of: This wildcard combines atomref evidence with a robustness trick not directly tested by proposal_001/005; it is not a new benchmark or metric.
- lesson_used: Evidence supports E0 baselines but warns small 8-epoch regimes may estimate atomrefs noisily.

## why_not_duplicate
This wildcard combines atomref evidence with a robustness trick not directly tested by proposal_001/005; it is not a new benchmark or metric.

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
- `model/model.py::EvolutionMLIP.__init__`: no required change to atomref shape.
- `model/model.py::EvolutionMLIP.forward_energy`: unchanged.
- `model/train.py::train`: fit count-normalized or ridge atomrefs on train split, then copy `alpha*fitted + (1-alpha)*current` with alpha around 0.5 into observed element rows before optimizer creation.
- `model/train.py::run_epoch`: preserve source or mild late schedule.

## minimal_edit_plan
1. Implement the same training-only atomref estimator as proposal_001 or 005.
2. Blend fitted values with current initialized weights using a fixed alpha such as 0.5; do not read validation/test energies.
3. Keep all downstream training/evaluation contracts unchanged.

## implementation_checklist
- [ ] Preserve `E = sum_i E_i` and force-from-energy contract.
- [ ] Preserve benchmark metric field names and runnable entrypoint contract.
- [ ] Modify only the allowed target unit files.
- [ ] Keep tensor shapes compatible with current dataloader and model forward.
- [ ] Add no unbounded cubic neighbor/triplet loops unless explicitly justified by budget.
- [ ] Call `mark_unit_implemented.py --unit <UNIT> --actor implementation_subagent` after edits.

## expected_benchmark_effect
- primary expected gain: more robust ISO17 energy improvement than raw fitted atomrefs if estimates are noisy.
- expected tradeoff: smaller maximum energy gain than all-in least squares.
- failure signal that would falsify this proposal: neither raw nor smoothed atomrefs improve energy against control.

## ablation_or_control
- required control or comparison: proposal_001 and proposal_005 if selected; otherwise proposal_010.
- optional zero-gate / source-fallback / readout-only ablation: alpha=0 recovers source initialization, alpha=1 recovers fitted atomref.

## implementation_notes_for_subagent
Implement only inside the materialized target unit, normally limited to `model/model.py` and/or `model/train.py` as listed above. Keep benchmark data, split semantics, evaluation semantics, metric field names, and runnable-unit entrypoint contract fixed. Do not add independent force heads: forces must remain `-autograd(total_energy, positions)`. Use only training-split information for any atomref or bias initialization; never use validation/test energies. If a proposed optional step becomes shape-risky, prefer the smallest source-fallback version rather than broad rewrites.
