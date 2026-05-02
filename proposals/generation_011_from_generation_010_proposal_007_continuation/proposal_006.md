# Proposal 006: Extra interaction depth jump

- family: deeper_local_message_passing
- phase: 4
- jump_type: jump
- budget_class: medium
- expected_capability_gain: test whether the source is underpowered in depth rather than in feature design.

## one_sentence_hypothesis
Adding one more interaction block with conservative residual scaling may improve cross-dataset representation power enough to raise Q, at acceptable runtime cost, if the simplified source is now too shallow.

## mechanism_refs
- []

## evidence_refs
- benchmark_diagnosis.json
- current_code_profile.json
- proposal_constraints.json
- evidence_quality.json
- mechanism_cards.json::HYP-B003

## historical_relation
- source_unit: generation_010/proposal_007
- relation_to_source: jump
- not_a_duplicate_of: prior late-helper jumps because this changes depth instead of readout structure.
- lesson_used: the source is stable and compact, so one principled way to probe capacity is a bounded depth increase rather than reviving large helper branches.

## benchmark_rationale
Discuss expected effects on all relevant benchmark signals, not force-only:
- rmd17 energy: could improve if more passes help local refinement, but runtime risk exists.
- rmd17 force: possible modest upside.
- rmd17 gap / Q: improvement only if current depth is the main bottleneck.
- iso17 energy: plausible upside from richer neighborhood propagation.
- iso17 force: mild upside possible.
- iso17 gap / Q: could improve if source underfits transfer structure.
- training stability / runtime risk: medium, because deeper stacks can destabilize or slow training.
- control comparison expectation: should be selected only if the loop wants one medium-budget capacity probe.

## files_to_edit
- `model/model.py`
- `model/train.py`: none

## code_insertion_points
- `model/model.py::EvolutionMLIP.__init__`: increase the number of interaction blocks or explicitly append one additional block.
- `model/model.py::EvolutionMLIP.forward_energy`: keep the same loop structure while running the extra block.
- `model/train.py::<none>`: none

## minimal_edit_plan
1. Add one additional `BalancedInteractionBlock` to the interaction stack.
2. Keep hidden size and all interfaces unchanged.
3. Preserve the source readout and force contract while accepting moderate extra runtime.

## implementation_checklist
- [ ] Preserve `E = sum_i E_i` and force-from-energy contract.
- [ ] Preserve benchmark metric field names and runnable entrypoint contract.
- [ ] Modify only the allowed target unit files.
- [ ] Keep tensor shapes compatible with current dataloader and model forward.
- [ ] Add no unbounded cubic neighbor/triplet loops unless explicitly justified by budget.
- [ ] Call `mark_unit_implemented.py --unit <UNIT> --actor implementation_subagent` after edits.

## expected_benchmark_effect
- primary expected gain: improved capacity and cross-dataset Q.
- expected tradeoff: higher runtime and possible over-smoothing or harder optimization.
- failure signal that would falsify this proposal: runtime increases with flat or worse metrics, implying depth is not the right next lever.

## ablation_or_control
- required control or comparison: proposal_008 exact source replicate.
- optional zero-gate / source-fallback / readout-only ablation: none.

## implementation_notes_for_subagent
Keep this as a pure depth change. Do not combine it with helper branches, angular approximations, or train-schedule changes.
