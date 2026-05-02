# Proposal 009: Near-disabled helper wildcard

- family: late_helper_presence_diagnostic
- phase: 4
- jump_type: wildcard
- budget_class: small
- expected_capability_gain: distinguish whether helper presence alone is harmful, versus active helper use.

## one_sentence_hypothesis
A helper branch that is structurally present but initialized almost fully off can separate architectural-presence effects from helper-activation effects.

## mechanism_refs
- []

## evidence_refs
- benchmark_diagnosis.json
- current_code_profile.json
- proposal_constraints.json
- evidence_quality.json
- mechanism_cards.json::HYP-B002

## historical_relation
- source_unit: generation_010/proposal_007
- relation_to_source: jump
- not_a_duplicate_of: proposal_004 because this wildcard is explicitly diagnostic and keeps the helper far closer to zero.
- lesson_used: earlier helper expansions regressed, so the safest remaining question is whether helper presence itself is already too much.

## benchmark_rationale
Discuss expected effects on all relevant benchmark signals, not force-only:
- rmd17 energy: should stay near source if helper presence is benign.
- rmd17 force: near-neutral.
- rmd17 gap / Q: useful diagnostic only.
- iso17 energy: little upside expected, but any improvement would be informative.
- iso17 force: likely neutral.
- iso17 gap / Q: mostly diagnostic.
- training stability / runtime risk: low.
- control comparison expectation: if this matches control while proposal_004 regresses, helper activation rather than helper presence is the problem.

## files_to_edit
- `model/model.py`
- `model/train.py`: none

## code_insertion_points
- `model/model.py::EvolutionMLIP.__init__`: add the smallest helper branch with an even more negative gate bias than proposal_004.
- `model/model.py::EvolutionMLIP.forward_energy`: thread the helper through readout while keeping the effective coefficient near zero.
- `model/train.py::<none>`: none

## minimal_edit_plan
1. Add a tiny helper branch that matches proposal_004 structurally.
2. Initialize and clamp its gate much closer to zero than proposal_004.
3. Preserve the source path as the overwhelmingly dominant path.

## implementation_checklist
- [ ] Preserve `E = sum_i E_i` and force-from-energy contract.
- [ ] Preserve benchmark metric field names and runnable entrypoint contract.
- [ ] Modify only the allowed target unit files.
- [ ] Keep tensor shapes compatible with current dataloader and model forward.
- [ ] Add no unbounded cubic neighbor/triplet loops unless explicitly justified by budget.
- [ ] Call `mark_unit_implemented.py --unit <UNIT> --actor implementation_subagent` after edits.

## expected_benchmark_effect
- primary expected gain: diagnostic clarity about helper-presence cost.
- expected tradeoff: probably little or no upside.
- failure signal that would falsify this proposal: it still regresses meaningfully against control, implying helper presence alone is harmful.

## ablation_or_control
- required control or comparison: proposal_008 exact source replicate.
- optional zero-gate / source-fallback / readout-only ablation: compare directly against proposal_004.

## implementation_notes_for_subagent
This should be smaller and more off-biased than proposal_004 in both width and initialization. The point is diagnosis, not performance chasing.
