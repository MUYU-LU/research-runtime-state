# Proposal 009: Agg-norm-only wildcard exploit

- family: scalar_path_diagnostic_wildcard
- phase: 4
- jump_type: wildcard
- budget_class: tiny
- expected_capability_gain: isolate whether the safer invariant summary is `agg_norm` alone rather than the full existing auxiliary scalar blend.

## one_sentence_hypothesis
Using only the already-computed `agg_norm` statistic to gate the auxiliary scalar mix could preserve directional-to-invariant contraction benefits while stripping away noisier context interactions.

## mechanism_refs
- M-BAL-PAINN-001

## evidence_refs
- mechanism_cards.json::M-BAL-PAINN-001
- evidence_provenance.json
- benchmark_diagnosis.json
- generation_memory.json

## historical_relation
- source_unit: generation_004/proposal_001
- relation_to_source: jump
- not_a_duplicate_of: proposals_001-003 because this wildcard changes which existing invariant summary is allowed to influence the blend, rather than only changing blend strength.
- lesson_used: the evidence favors invariant contractions over unrestricted context mixing, so a narrower contraction-only wildcard is justified.

## benchmark_rationale
Discuss expected effects on all relevant benchmark signals, not force-only:
- rmd17 energy: could improve if `agg_norm` is the useful invariant and the rest of the auxiliary context is noise.
- rmd17 force: should remain stable.
- rmd17 gap / Q: possible modest gain if calibration improves.
- iso17 energy: uncertain, because some removed context may have helped.
- iso17 force: neutral.
- iso17 gap / Q: medium uncertainty, which is why this is a wildcard.
- training stability / runtime risk: low.
- control comparison expectation: the value is diagnostic, not necessarily top-line upside.

## files_to_edit
- `model/model.py`
- `model/train.py`: none

## code_insertion_points
- `model/model.py::BalancedInteractionBlock.forward`: restrict the auxiliary mix gate input to the safest existing invariant summary, preferably `agg_norm` with optional residual scalar context.
- `model/model.py::BalancedInteractionBlock.__init__`: adjust the gate head input width accordingly.
- `model/train.py::<none>`: none

## minimal_edit_plan
1. Remove noisier gate inputs while keeping current tensor routes intact.
2. Compute the mix coefficient from `agg_norm`-centric features only.
3. Keep the blend bounded and source-fallback friendly.

## implementation_checklist
- [ ] Preserve `E = sum_i E_i` and force-from-energy contract.
- [ ] Preserve benchmark metric field names and runnable entrypoint contract.
- [ ] Modify only the allowed target unit files.
- [ ] Keep tensor shapes compatible with current dataloader and model forward.
- [ ] Add no unbounded cubic neighbor/triplet loops unless explicitly justified by budget.
- [ ] Call `mark_unit_implemented.py --unit <UNIT> --actor implementation_subagent` after edits.

## expected_benchmark_effect
- primary expected gain: cleaner invariant contraction path with less scalar noise.
- expected tradeoff: may discard genuinely useful context cues.
- failure signal that would falsify this proposal: both datasets regress similarly, implying the removed context carried necessary information.

## ablation_or_control
- required control or comparison: proposal_008 exact source replicate.
- optional zero-gate / source-fallback / readout-only ablation: compare against proposal_002 to isolate whether input restriction beats simple shrinkage.

## implementation_notes_for_subagent
Do not invent new invariant features. Reuse already-computed features and only narrow the gate input.
