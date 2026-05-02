# Proposal 007: Fixed-small vector residual simplify

- family: balanced_vector_simplified
- phase: 3
- jump_type: backward-simplify
- budget_class: tiny
- expected_capability_gain: test whether even the source unit's learnable vector residual scale is more flexibility than the benchmark wants.

## one_sentence_hypothesis
Replacing the learned vector residual scale with a fixed smaller constant can reveal whether the remaining generalization gap comes from overactive vector updates rather than scalar structure.

## mechanism_refs
- []

## evidence_refs
- benchmark_diagnosis.json
- current_code_profile.json
- proposal_constraints.json
- evidence_quality.json
- mechanism_cards.json::HYP-B001

## historical_relation
- source_unit: generation_010/proposal_007
- relation_to_source: simplify
- not_a_duplicate_of: generation_010/proposal_007 because the source simplified the scalar path, while this proposal simplifies the vector residual path on top of that source.
- lesson_used: the most successful continuation so far came from removing complexity rather than adding it, so one more narrow simplification is warranted.

## benchmark_rationale
Discuss expected effects on all relevant benchmark signals, not force-only:
- rmd17 energy: likely neutral.
- rmd17 force: slight downside if vector updates become too weak.
- rmd17 gap / Q: could improve if the source still carries unnecessary vector variance.
- iso17 energy: modest upside if simpler vector behavior calibrates better.
- iso17 force: likely neutral to small downside.
- iso17 gap / Q: could improve through stability if not through expressivity.
- training stability / runtime risk: very low.
- control comparison expectation: this is the cleanest next simplify test beyond the source itself.

## files_to_edit
- `model/model.py`
- `model/train.py`: none

## code_insertion_points
- `model/model.py::BalancedInteractionBlock.__init__`: remove or bypass the learned `vector_residual_scale` parameter.
- `model/model.py::BalancedInteractionBlock.forward`: use a fixed conservative residual coefficient for the vector update.
- `model/train.py::<none>`: none

## minimal_edit_plan
1. Replace the learned vector residual scaling parameter with a fixed small constant.
2. Keep the rest of the vector update logic unchanged.
3. Preserve all tensor shapes and output semantics.

## implementation_checklist
- [ ] Preserve `E = sum_i E_i` and force-from-energy contract.
- [ ] Preserve benchmark metric field names and runnable entrypoint contract.
- [ ] Modify only the allowed target unit files.
- [ ] Keep tensor shapes compatible with current dataloader and model forward.
- [ ] Add no unbounded cubic neighbor/triplet loops unless explicitly justified by budget.
- [ ] Call `mark_unit_implemented.py --unit <UNIT> --actor implementation_subagent` after edits.

## expected_benchmark_effect
- primary expected gain: lower-variance behavior and a cleaner attribution of how much vector flexibility is needed.
- expected tradeoff: underpowered vector updates may hurt force accuracy.
- failure signal that would falsify this proposal: both datasets lose force/Q relative to source with no stability benefit.

## ablation_or_control
- required control or comparison: proposal_008 exact source replicate.
- optional zero-gate / source-fallback / readout-only ablation: this proposal is itself the fixed-small vector ablation.

## implementation_notes_for_subagent
Do not remove the vector branch entirely. The goal is only to replace the learned residual amplitude with a fixed smaller amplitude.
