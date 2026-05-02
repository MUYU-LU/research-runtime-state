# Proposal 005: Directional alignment feedback jump

- family: directional_alignment_feedback
- phase: 4
- jump_type: jump
- budget_class: small
- expected_capability_gain: add a bounded directional feedback signal inside the interaction block without introducing explicit triplet enumeration.

## one_sentence_hypothesis
Feeding a small extra directional-alignment summary back into the scalar update may improve chemically directional cases while staying cheaper and safer than explicit angular message passing.

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
- not_a_duplicate_of: explicit angular or triplet proposals from earlier generations because this remains pair-based and bounded, using only already available vectors and directions.
- lesson_used: the evidence package flags missing angular capability, but proposal constraints forbid pretending we have strong angular evidence, so this should be a cautious proxy rather than a full angular rewrite.

## benchmark_rationale
Discuss expected effects on all relevant benchmark signals, not force-only:
- rmd17 energy: slight downside risk from extra interaction complexity.
- rmd17 force: possible upside if directional feedback helps local geometry.
- rmd17 gap / Q: should improve only if the current source misses bounded directional cues.
- iso17 energy: modest upside possible.
- iso17 force: plausible upside on direction-sensitive environments.
- iso17 gap / Q: potential transfer gain if the proxy captures some angular structure cheaply.
- training stability / runtime risk: medium-low.
- control comparison expectation: should outperform exploit proposals only if directional information is the real missing capability.

## files_to_edit
- `model/model.py`
- `model/train.py`: none

## code_insertion_points
- `model/model.py::BalancedInteractionBlock.__init__`: add one narrow projection or gate for directional feedback.
- `model/model.py::BalancedInteractionBlock.forward`: compute a bounded directional summary from existing vector and unit tensors, then append it to the scalar update path.
- `model/train.py::<none>`: none

## minimal_edit_plan
1. Build one extra scalar feature from existing directional quantities already available in `forward`.
2. Feed that feature into the scalar update path with a small learned gate.
3. Keep all operations pairwise and shape-compatible.

## implementation_checklist
- [ ] Preserve `E = sum_i E_i` and force-from-energy contract.
- [ ] Preserve benchmark metric field names and runnable entrypoint contract.
- [ ] Modify only the allowed target unit files.
- [ ] Keep tensor shapes compatible with current dataloader and model forward.
- [ ] Add no unbounded cubic neighbor/triplet loops unless explicitly justified by budget.
- [ ] Call `mark_unit_implemented.py --unit <UNIT> --actor implementation_subagent` after edits.

## expected_benchmark_effect
- primary expected gain: better force/Q on direction-sensitive local environments.
- expected tradeoff: complexity may hurt the very stable source behavior.
- failure signal that would falsify this proposal: no force improvement on either dataset while energy worsens.

## ablation_or_control
- required control or comparison: proposal_008 exact source replicate.
- optional zero-gate / source-fallback / readout-only ablation: initialize the added directional gate conservatively so the source path remains available.

## implementation_notes_for_subagent
Do not add explicit triplet loops or neighbor-of-neighbor passes. Use only existing pairwise tensors already present in `BalancedInteractionBlock.forward`.
