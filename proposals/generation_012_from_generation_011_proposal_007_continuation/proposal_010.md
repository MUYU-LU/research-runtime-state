# Proposal 010: Source continuation control

- family: source_control
- phase: 1
- jump_type: control
- budget_class: tiny
- expected_capability_gain: Materialize the source unit with no proposal-specific model or training changes to measure round-to-round/runtime drift.

## one_sentence_hypothesis
A no-op continuation control establishes whether observed generation_012 changes come from code edits or ordinary stochastic/runtime variation.

## mechanism_refs
- []

## evidence_refs
- /home/lmy/.openclaw/workspace/research_runtime/ledger/frontier.jsonl

## historical_relation
- source_unit: generation_011/proposal_007
- relation_to_source: control
- not_a_duplicate_of: This is required control and intentionally duplicates source behavior only for attribution, not as an innovation proposal.
- lesson_used: Recent improvements/regressions are small enough that a source-control anchor is necessary before attributing calibration changes.

## why_not_duplicate
This is required control and intentionally duplicates source behavior only for attribution, not as an innovation proposal.

## benchmark_rationale
- rmd17 energy: should remain close to source unless the edit directly changes the energy readout or loss weighting; any gain is secondary to ISO17 recovery.
- rmd17 force: protect the source unit's conservative force path; force-only gains are not sufficient if energy/Q regress.
- rmd17 gap / Q: monitor for gap penalty changes caused by calibration drift; source-like RMD17 Q is acceptable.
- iso17 energy: primary diagnostic for generation_012 because generation_011/proposal_007 improved force but left an energy-transfer bottleneck.
- iso17 force: should stay near source; modest regression is acceptable only if energy/Q improves materially.
- iso17 gap / Q: target lower `mixed_energy_mae` and better `Q_iso17` without worsening split gap semantics.
- training stability / runtime risk: negligible for control.
- control comparison expectation: compare against proposal_010 source-control and the source unit generation_011/proposal_007.

## files_to_edit
- `none`

## code_insertion_points
- `model/model.py::<none>`: make no source-code changes after materialization.
- `model/train.py::<none>`: make no source-code changes after materialization.
- Implementation subagent should only mark the unit implemented after verifying materialized files match source and no edit is needed.

## minimal_edit_plan
1. Do not edit `model/model.py` or `model/train.py`.
2. Verify materialized unit preserves source code, benchmark data, split semantics, metric field names, and entrypoint contract.
3. Call the implementation marking script for the materialized control unit.

## implementation_checklist
- [ ] Preserve `E = sum_i E_i` and force-from-energy contract.
- [ ] Preserve benchmark metric field names and runnable entrypoint contract.
- [ ] Modify only the allowed target unit files.
- [ ] Keep tensor shapes compatible with current dataloader and model forward.
- [ ] Add no unbounded cubic neighbor/triplet loops unless explicitly justified by budget.
- [ ] Call `mark_unit_implemented.py --unit <UNIT> --actor implementation_subagent` after edits.

## expected_benchmark_effect
- primary expected gain: no expected gain; measures stochastic/runtime drift around generation_011/proposal_007.
- expected tradeoff: consumes one run slot but protects interpretation of the round.
- failure signal that would falsify this proposal: large control deviation, indicating benchmark variance or materialization drift dominates.

## ablation_or_control
- required control or comparison: all edited proposals should compare against this control.
- optional zero-gate / source-fallback / readout-only ablation: not applicable; this is the source fallback.

## implementation_notes_for_subagent
Implement only inside the materialized target unit, normally limited to `model/model.py` and/or `model/train.py` as listed above. Keep benchmark data, split semantics, evaluation semantics, metric field names, and runnable-unit entrypoint contract fixed. Do not add independent force heads: forces must remain `-autograd(total_energy, positions)`. Use only training-split information for any atomref or bias initialization; never use validation/test energies. If a proposed optional step becomes shape-risky, prefer the smallest source-fallback version rather than broad rewrites.
