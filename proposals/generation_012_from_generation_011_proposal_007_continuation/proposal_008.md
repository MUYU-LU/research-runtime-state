# Proposal 008: Backward simplify vector residual

- family: simplified_vector_residual
- phase: 1
- jump_type: backward-simplify
- budget_class: small
- expected_capability_gain: Reduce vector residual mixing strength and remove the most aggressive vector-alignment contribution to test whether source energy regression comes from overactive vector coupling.

## one_sentence_hypothesis
Simplifying late vector residual coupling may recover energy stability and gap behavior if generation_011/proposal_007 overfit forces through vector features.

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
- relation_to_source: simplify
- not_a_duplicate_of: This intentionally backs away from generation_011/proposal_007 capacity rather than adding evidence-backed calibration; not a duplicate of calibration proposals.
- lesson_used: Outcome memory says force gains alone are insufficient; a simplify path can reveal whether vector complexity hurt energy Q.

## why_not_duplicate
This intentionally backs away from generation_011/proposal_007 capacity rather than adding evidence-backed calibration; not a duplicate of calibration proposals.

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

## code_insertion_points
- `model/model.py::BalancedInteractionBlock.__init__`: reduce `vector_residual_scale` from source value to a smaller constant such as 0.1.
- `model/model.py::BalancedInteractionBlock.forward`: downweight `vector_alignment` before concatenation or replace it with zeros while preserving input shape.
- `model/train.py::<none>`: no training schedule change.

## minimal_edit_plan
1. Change only `BalancedInteractionBlock` internals, preserving tensor shapes and forward signature.
2. Reduce vector residual contribution and/or alignment term with source-fallback constants, not new dataloader/model contracts.
3. Keep atomref/readout/loss schedule unchanged to isolate simplification.

## implementation_checklist
- [ ] Preserve `E = sum_i E_i` and force-from-energy contract.
- [ ] Preserve benchmark metric field names and runnable entrypoint contract.
- [ ] Modify only the allowed target unit files.
- [ ] Keep tensor shapes compatible with current dataloader and model forward.
- [ ] Add no unbounded cubic neighbor/triplet loops unless explicitly justified by budget.
- [ ] Call `mark_unit_implemented.py --unit <UNIT> --actor implementation_subagent` after edits.

## expected_benchmark_effect
- primary expected gain: recover energy/gap/Q stability if overactive vector coupling caused force-favoring overfit.
- expected tradeoff: likely force MAE regression if vector coupling was genuinely useful.
- failure signal that would falsify this proposal: energy does not improve and force worsens.

## ablation_or_control
- required control or comparison: proposal_010 source-control and proposal_003 energy calibration.
- optional zero-gate / source-fallback / readout-only ablation: set residual scale back to source constant.

## implementation_notes_for_subagent
Implement only inside the materialized target unit, normally limited to `model/model.py` and/or `model/train.py` as listed above. Keep benchmark data, split semantics, evaluation semantics, metric field names, and runnable-unit entrypoint contract fixed. Do not add independent force heads: forces must remain `-autograd(total_energy, positions)`. Use only training-split information for any atomref or bias initialization; never use validation/test energies. If a proposed optional step becomes shape-risky, prefer the smallest source-fallback version rather than broad rewrites.
