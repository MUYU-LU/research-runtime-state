# Proposal 003: Atomref init plus gentle late rebalance

- family: energy_baseline_stage2
- phase: 2
- jump_type: exploit
- budget_class: small
- expected_capability_gain: Combine the two evidence-backed low-risk interventions: training-only atomref initialization plus a gentler final-quarter energy rebalance.

## one_sentence_hypothesis
Initializing per-element E0 and then mildly increasing late energy weight should attack ISO17 energy offset from both parameter and objective sides while keeping conservative forces.

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
- not_a_duplicate_of: This is the direct materialization of the mechanism card; it is not a duplicate of proposal_001 or 002 because it tests the interaction of both evidence-backed edits.
- lesson_used: Prior outcomes show isolated representation jumps did not reliably improve Q; the current evidence supports calibration before added capacity.

## why_not_duplicate
This is the direct materialization of the mechanism card; it is not a duplicate of proposal_001 or 002 because it tests the interaction of both evidence-backed edits.

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
- `model/model.py`
- `model/train.py`

## code_insertion_points
- `model/model.py::EvolutionMLIP.__init__`: keep atomref trainable and compatible with source state dict.
- `model/model.py::EvolutionMLIP.forward_energy`: preserve atomref + readout energy decomposition.
- `model/train.py::train`: initialize atomref from training split before optimizer construction.
- `model/train.py::train`: add final-quarter energy rebalance, e.g. energy 1.0 -> 1.2 and force 20 -> 18.5.
- `model/train.py::run_epoch`: preserve separate `loss_energy`/`loss_force` metric fields.

## minimal_edit_plan
1. Implement the training-only atomref initialization helper from proposal_001.
2. Add a conservative final-quarter stage-two scalar schedule smaller than proposal_002.
3. Keep all model interactions, neighbor construction, batch semantics, and eval metric names fixed.

## implementation_checklist
- [ ] Preserve `E = sum_i E_i` and force-from-energy contract.
- [ ] Preserve benchmark metric field names and runnable entrypoint contract.
- [ ] Modify only the allowed target unit files.
- [ ] Keep tensor shapes compatible with current dataloader and model forward.
- [ ] Add no unbounded cubic neighbor/triplet loops unless explicitly justified by budget.
- [ ] Call `mark_unit_implemented.py --unit <UNIT> --actor implementation_subagent` after edits.

## expected_benchmark_effect
- primary expected gain: best chance among exploits to lower ISO17 energy and improve total Q while preserving source force.
- expected tradeoff: combined calibration may overfit small train-set composition if atomref estimates are crude.
- failure signal that would falsify this proposal: both ISO17 energy and force regress, indicating calibration noise dominates.

## ablation_or_control
- required control or comparison: compare against proposal_001 and proposal_002 to attribute atomref vs schedule.
- optional zero-gate / source-fallback / readout-only ablation: disable either atomref init or stage-two schedule independently.

## implementation_notes_for_subagent
Implement only inside the materialized target unit, normally limited to `model/model.py` and/or `model/train.py` as listed above. Keep benchmark data, split semantics, evaluation semantics, metric field names, and runnable-unit entrypoint contract fixed. Do not add independent force heads: forces must remain `-autograd(total_energy, positions)`. Use only training-split information for any atomref or bias initialization; never use validation/test energies. If a proposed optional step becomes shape-risky, prefer the smallest source-fallback version rather than broad rewrites.
