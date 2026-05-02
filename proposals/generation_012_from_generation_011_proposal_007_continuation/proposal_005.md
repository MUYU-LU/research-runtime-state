# Proposal 005: Composition-normalized atomref least squares

- family: composition_lstsq
- phase: 3
- jump_type: jump
- budget_class: small
- expected_capability_gain: Use a small regularized least-squares solve over training molecular compositions to estimate atomref values, a stronger baseline jump than count-normalized offsets.

## one_sentence_hypothesis
A regularized train-split composition least-squares E0 estimate should improve cross-molecule ISO17 energy calibration more reliably than naive count normalization.

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
- relation_to_source: jump
- not_a_duplicate_of: This jumps from simple heuristic initialization to a closed-form composition fit; it is not a duplicate of proposal_001, which uses count-normalized offsets only.
- lesson_used: The MACE E0 evidence supports atomwise baselines, and ISO17 composition diversity makes a composition-level solve plausible.

## why_not_duplicate
This jumps from simple heuristic initialization to a closed-form composition fit; it is not a duplicate of proposal_001, which uses count-normalized offsets only.

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
- `model/model.py::EvolutionMLIP.__init__`: keep existing atomref embedding.
- `model/model.py::EvolutionMLIP.forward_energy`: unchanged atomref + readout decomposition.
- `model/train.py::train`: build a train-only composition matrix over observed atomic numbers and solve ridge least squares for per-element E0 before optimizer creation.
- `model/train.py::run_epoch`: optionally keep source weights or pair with very mild late schedule only if implementation remains small.

## minimal_edit_plan
1. Collect per-sample composition counts and scalar energies from training loader only.
2. Solve `(X^T X + lambda I) e0 = X^T y` on CPU or model device with a small ridge, then copy fitted observed element values into `model.atomref.weight`.
3. Fallback to source/random atomref if the solve is singular or no energies are found; preserve all metrics and contracts.

## implementation_checklist
- [ ] Preserve `E = sum_i E_i` and force-from-energy contract.
- [ ] Preserve benchmark metric field names and runnable entrypoint contract.
- [ ] Modify only the allowed target unit files.
- [ ] Keep tensor shapes compatible with current dataloader and model forward.
- [ ] Add no unbounded cubic neighbor/triplet loops unless explicitly justified by budget.
- [ ] Call `mark_unit_implemented.py --unit <UNIT> --actor implementation_subagent` after edits.

## expected_benchmark_effect
- primary expected gain: stronger ISO17 energy transfer through better per-element baseline estimates.
- expected tradeoff: slightly more implementation complexity and risk of overfitting tiny train composition matrix.
- failure signal that would falsify this proposal: ISO17 energy gap grows or force worsens without energy gain.

## ablation_or_control
- required control or comparison: proposal_001 count-normalized atomref and proposal_010 source-control.
- optional zero-gate / source-fallback / readout-only ablation: set ridge solve output to zeros/source init.

## implementation_notes_for_subagent
Implement only inside the materialized target unit, normally limited to `model/model.py` and/or `model/train.py` as listed above. Keep benchmark data, split semantics, evaluation semantics, metric field names, and runnable-unit entrypoint contract fixed. Do not add independent force heads: forces must remain `-autograd(total_energy, positions)`. Use only training-split information for any atomref or bias initialization; never use validation/test energies. If a proposed optional step becomes shape-risky, prefer the smallest source-fallback version rather than broad rewrites.
