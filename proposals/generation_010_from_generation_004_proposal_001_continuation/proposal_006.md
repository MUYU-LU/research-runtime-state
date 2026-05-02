# Proposal 006: Hybrid bounded helper plus narrow mix jump

- family: hybrid_bounded_diagnostic
- phase: 5
- jump_type: jump
- budget_class: medium
- expected_capability_gain: probe whether a tiny late helper only works when paired with a stricter in-block scalar mix.

## one_sentence_hypothesis
A bounded combination of a tiny scalar-mix shrink and a tiny gated late helper may recover source stability while exposing a weak missing invariant summary that neither edit alone captures.

## mechanism_refs
- M-BAL-PAINN-001
- W-BAL-SO3K-002

## evidence_refs
- mechanism_cards.json::M-BAL-PAINN-001
- mechanism_cards.json::W-BAL-SO3K-002
- patch_blueprints.json
- generation_memory.json

## historical_relation
- source_unit: generation_004/proposal_001
- relation_to_source: jump
- not_a_duplicate_of: prior jumps because this proposal keeps both edits ultra-bounded instead of broadening a late helper alone; not_a_duplicate_of proposal_001 because it adds a single diagnostic helper in addition to the mix shrink.
- lesson_used: the evidence suggests the scalar-mix issue is primary, but a tiny helper may still be worth testing if it is paired with stronger source-faithful calibration.

## benchmark_rationale
Discuss expected effects on all relevant benchmark signals, not force-only:
- rmd17 energy: should be safer than helper-only jumps because the scalar path is simultaneously tightened.
- rmd17 force: near-flat.
- rmd17 gap / Q: modest upside if the helper helps without undoing the scalar fix.
- iso17 energy: potential upside from the helper branch.
- iso17 force: neutral to slight positive.
- iso17 gap / Q: could improve if the model was missing one late invariant statistic.
- training stability / runtime risk: medium, since two small edits interact.
- control comparison expectation: this is the highest-variance bounded jump and should be judged against both control and proposal_001.

## files_to_edit
- `model/model.py`
- `model/train.py`: none

## code_insertion_points
- `model/model.py::BalancedInteractionBlock.forward`: apply a stricter narrow scalar-mix gate.
- `model/model.py::EvolutionMLIP.forward_energy`: add one tiny late helper branch gated near zero.
- `model/train.py::<none>`: none

## minimal_edit_plan
1. Reuse the proposal_001-style narrow scalar gate inside the interaction block.
2. Add one ultra-narrow late invariant helper at readout time.
3. Keep both gates small and independently collapsible.

## implementation_checklist
- [ ] Preserve `E = sum_i E_i` and force-from-energy contract.
- [ ] Preserve benchmark metric field names and runnable entrypoint contract.
- [ ] Modify only the allowed target unit files.
- [ ] Keep tensor shapes compatible with current dataloader and model forward.
- [ ] Add no unbounded cubic neighbor/triplet loops unless explicitly justified by budget.
- [ ] Call `mark_unit_implemented.py --unit <UNIT> --actor implementation_subagent` after edits.

## expected_benchmark_effect
- primary expected gain: best bounded upside among jump proposals if the scalar path and late summary both matter a little.
- expected tradeoff: interaction effects could make this less stable than the exploit-only line.
- failure signal that would falsify this proposal: joint edit underperforms both proposal_001 and control, implying the helper is not worth combining.

## ablation_or_control
- required control or comparison: proposal_008 exact source replicate.
- optional zero-gate / source-fallback / readout-only ablation: compare against proposal_001 and proposal_004 to separate combination gain from each component.

## implementation_notes_for_subagent
Keep the helper extremely small. If code complexity grows, prefer simplifying the helper rather than widening the scalar gate. No optimizer or loss changes.
