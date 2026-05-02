# Proposal 002: Source-biased scalar gate exploit

- family: balanced_scalar_mix_recovery
- phase: 4
- jump_type: exploit
- budget_class: tiny
- expected_capability_gain: improve attribution clarity by using a source-biased learnable gate that can collapse toward the residual path.

## one_sentence_hypothesis
A source-biased gate with stronger shrinkage toward the residual `mixed_scalar` path can test whether the remaining auxiliary context blend is useful at all.

## mechanism_refs
- M-BAL-PAINN-001

## evidence_refs
- mechanism_cards.json::M-BAL-PAINN-001
- patch_blueprints.json::M-BAL-PAINN-001
- benchmark_diagnosis.json
- generation_memory.json

## historical_relation
- source_unit: generation_004/proposal_001
- relation_to_source: exploit
- not_a_duplicate_of: generation_008/proposal_007 because this keeps a nonzero auxiliary blend instead of deleting it entirely, and not_a_duplicate_of generation_008/proposal_001 because the gate is biased harder toward the residual path.
- lesson_used: complete removal looked directionally safer than broader interpolation, so the next exploit should test a very low-cap blend rather than another broad learnable mixer.

## benchmark_rationale
Discuss expected effects on all relevant benchmark signals, not force-only:
- rmd17 energy: expected improvement if overmixing is the main error source.
- rmd17 force: near-flat because message geometry is untouched.
- rmd17 gap / Q: modest positive if energy recovers without force drift.
- iso17 energy: uncertain but should not collapse if a small auxiliary path is still helpful.
- iso17 force: likely neutral.
- iso17 gap / Q: slight downside risk if ISO17 benefits more from extra context than rmd17 does.
- training stability / runtime risk: very low.
- control comparison expectation: should outperform control only if a tiny adaptive blend beats exact source behavior under current variance.

## files_to_edit
- `model/model.py`
- `model/train.py`: none

## code_insertion_points
- `model/model.py::BalancedInteractionBlock.__init__`: define a gate head with bias initialized below the source `0.3` path weight.
- `model/model.py::BalancedInteractionBlock.forward`: clamp `alpha` to roughly `[0.00, 0.12]` and preserve the existing normalization order.
- `model/train.py::<none>`: none

## minimal_edit_plan
1. Reuse existing scalar features as gate input instead of adding new summaries.
2. Produce a low-cap `alpha` with source-biased initialization.
3. Keep the rest of the block mathematically identical.

## implementation_checklist
- [ ] Preserve `E = sum_i E_i` and force-from-energy contract.
- [ ] Preserve benchmark metric field names and runnable entrypoint contract.
- [ ] Modify only the allowed target unit files.
- [ ] Keep tensor shapes compatible with current dataloader and model forward.
- [ ] Add no unbounded cubic neighbor/triplet loops unless explicitly justified by budget.
- [ ] Call `mark_unit_implemented.py --unit <UNIT> --actor implementation_subagent` after edits.

## expected_benchmark_effect
- primary expected gain: recover rmd17 energy while leaving force nearly unchanged.
- expected tradeoff: ISO17 may lose a little if it genuinely needed more context mixing.
- failure signal that would falsify this proposal: the run behaves like proposal_007 or worse, implying the auxiliary path should be removed entirely or left exactly as source.

## ablation_or_control
- required control or comparison: proposal_008 exact source replicate.
- optional zero-gate / source-fallback / readout-only ablation: proposal_007 pure residual simplification serves as the zero-gate comparison.

## implementation_notes_for_subagent
Use only existing `mixed_scalar` and `agg_scalar` features. No new late helper, no extra readout, and no training recipe changes.
