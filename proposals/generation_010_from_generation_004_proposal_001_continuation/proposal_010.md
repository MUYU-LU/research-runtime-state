# Proposal 010: Helper-disabled wildcard diagnostic

- family: late_invariant_diagnostic
- phase: 5
- jump_type: wildcard
- budget_class: small
- expected_capability_gain: determine whether a compile-time-present but near-disabled helper is safer than a fully active late helper jump.

## one_sentence_hypothesis
A structurally present but strongly off-biased late helper can test whether helper parameterization itself is harmless, separating architecture-presence effects from active-helper effects.

## mechanism_refs
- W-BAL-SO3K-002

## evidence_refs
- mechanism_cards.json::W-BAL-SO3K-002
- patch_blueprints.json::W-BAL-SO3K-002
- generation_memory.json
- evidence_quality.json

## historical_relation
- source_unit: generation_004/proposal_001
- relation_to_source: jump
- not_a_duplicate_of: proposal_004 and proposal_005 because this wildcard keeps the helper initialized much closer to off, acting as a diagnostic between pure control and active late-helper jumps.
- lesson_used: recent helper-style moves regressed, so the safest remaining question is whether the helper should be almost entirely dormant.

## benchmark_rationale
Discuss expected effects on all relevant benchmark signals, not force-only:
- rmd17 energy: should stay close to control if the off-biased helper is truly harmless.
- rmd17 force: neutral.
- rmd17 gap / Q: near-control unless tiny helper effects matter.
- iso17 energy: small upside at best.
- iso17 force: neutral.
- iso17 gap / Q: likely near-control, but useful if it outperforms active helper variants.
- training stability / runtime risk: low-medium.
- control comparison expectation: if this matches control and active helper variants regress, the round learns that helper presence is acceptable but activation is not.

## files_to_edit
- `model/model.py`
- `model/train.py`: none

## code_insertion_points
- `model/model.py::EvolutionMLIP.forward_energy`: add one tiny late helper branch with an initialization and clamp that keeps its gate strongly near zero.
- `model/train.py::<none>`: none

## minimal_edit_plan
1. Add the smallest helper branch needed for the late-summary diagnostic.
2. Initialize and clamp its gate close to zero so the helper is nearly disabled.
3. Preserve a clean path to compare against the active helper variants.

## implementation_checklist
- [ ] Preserve `E = sum_i E_i` and force-from-energy contract.
- [ ] Preserve benchmark metric field names and runnable entrypoint contract.
- [ ] Modify only the allowed target unit files.
- [ ] Keep tensor shapes compatible with current dataloader and model forward.
- [ ] Add no unbounded cubic neighbor/triplet loops unless explicitly justified by budget.
- [ ] Call `mark_unit_implemented.py --unit <UNIT> --actor implementation_subagent` after edits.

## expected_benchmark_effect
- primary expected gain: diagnostic clarity about helper activation risk.
- expected tradeoff: probably little or no upside.
- failure signal that would falsify this proposal: it still regresses meaningfully versus control, implying helper presence alone is harmful.

## ablation_or_control
- required control or comparison: proposal_008 exact source replicate.
- optional zero-gate / source-fallback / readout-only ablation: compare against proposal_005 to isolate active-helper versus near-disabled-helper behavior.

## implementation_notes_for_subagent
Keep this helper even smaller and more strongly off-biased than proposals_004 and_005. The point is diagnostic separation, not chasing maximum upside.
