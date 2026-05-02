# Proposal 007: Residual-only scalar-path simplification

- family: balanced_scalar_mix_simplified
- phase: 3
- jump_type: backward-simplify
- budget_class: tiny
- expected_capability_gain: test whether removing the auxiliary scalar-mix path entirely is cleaner than any learnable shrink.

## one_sentence_hypothesis
Collapsing the post-update scalar blend to the pure residual `mixed_scalar` path can determine whether the safest recovery move is full simplification rather than bounded gating.

## mechanism_refs
- M-BAL-PAINN-001

## evidence_refs
- mechanism_cards.json::M-BAL-PAINN-001
- generation_memory.json
- benchmark_diagnosis.json

## historical_relation
- source_unit: generation_004/proposal_001
- relation_to_source: simplify
- not_a_duplicate_of: generation_008/proposal_007 because this round needs a fresh, fully specified simplification anchor relative to the new evidence package and exploit set.
- lesson_used: prior evidence says shrinking the scalar-mix path is safer than enlarging it, so the cleanest simplify baseline remains important.

## benchmark_rationale
Discuss expected effects on all relevant benchmark signals, not force-only:
- rmd17 energy: could improve if the auxiliary path is the main source of calibration drift.
- rmd17 force: likely neutral.
- rmd17 gap / Q: may improve via lower variance, but could lose any genuine benefit from the auxiliary branch.
- iso17 energy: downside risk if ISO17 relied on the extra context path.
- iso17 force: neutral.
- iso17 gap / Q: possible modest drop if simplification is too aggressive.
- training stability / runtime risk: very low.
- control comparison expectation: useful as the cleanest attribution check against all gated exploit variants.

## files_to_edit
- `model/model.py`
- `model/train.py`: none

## code_insertion_points
- `model/model.py::BalancedInteractionBlock.forward`: replace the final mixed/context interpolation with pure `mixed_scalar` residual output.
- `model/model.py::BalancedInteractionBlock.__init__`: remove or bypass now-unused scalar-mix-specific gate plumbing only if necessary.
- `model/train.py::<none>`: none

## minimal_edit_plan
1. Bypass the auxiliary `scalar_mix_norm(scalar_state + agg_scalar)` blend path.
2. Return the residual `mixed_scalar` path directly after the existing update.
3. Clean up any dead references without changing other behavior.

## implementation_checklist
- [ ] Preserve `E = sum_i E_i` and force-from-energy contract.
- [ ] Preserve benchmark metric field names and runnable entrypoint contract.
- [ ] Modify only the allowed target unit files.
- [ ] Keep tensor shapes compatible with current dataloader and model forward.
- [ ] Add no unbounded cubic neighbor/triplet loops unless explicitly justified by budget.
- [ ] Call `mark_unit_implemented.py --unit <UNIT> --actor implementation_subagent` after edits.

## expected_benchmark_effect
- primary expected gain: strongest interpretability and lowest-variance read on whether the auxiliary scalar path should exist.
- expected tradeoff: may underfit if the removed path was genuinely helpful.
- failure signal that would falsify this proposal: both datasets lose `Q_dataset` despite stable training, implying the auxiliary path still carries useful signal.

## ablation_or_control
- required control or comparison: proposal_008 exact source replicate.
- optional zero-gate / source-fallback / readout-only ablation: this proposal is itself the zero-gate ablation for proposals_001-003.

## implementation_notes_for_subagent
Do not re-architect the block after removing the blend. Simplicity is the point.
