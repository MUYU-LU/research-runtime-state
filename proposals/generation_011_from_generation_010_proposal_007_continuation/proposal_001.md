# Proposal 001: Tiny scalar context re-entry gate

- family: balanced_scalar_reentry
- phase: 3
- jump_type: exploit
- budget_class: tiny
- expected_capability_gain: recover some iso17 energy calibration without undoing the source unit's simplification win.

## one_sentence_hypothesis
A very small gated re-entry of normalized aggregate scalar context after the source unit's pure residual update can improve iso17 energy calibration while keeping the strong low-risk behavior of generation_010/proposal_007.

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
- relation_to_source: exploit
- not_a_duplicate_of: generation_010/proposal_002 because that earlier scalar-mix gate was sourced from generation_004/proposal_001 and regressed badly; this proposal starts from the already simplified source and only allows a much smaller post-update re-entry path.
- lesson_used: generation_010/proposal_007 showed that full scalar-path simplification is safer than active blend variants, so any exploit should stay source-tight and off-biased.

## benchmark_rationale
Discuss expected effects on all relevant benchmark signals, not force-only:
- rmd17 energy: should stay close to source if the new gate remains small.
- rmd17 force: should remain near source because the interaction core stays unchanged.
- rmd17 gap / Q: low risk, slight upside only if the source underuses neighborhood context.
- iso17 energy: primary upside, since iso17 still shows larger mixed energy error than rmd17.
- iso17 force: expected near-neutral.
- iso17 gap / Q: modest upside if the small context return helps transfer without reopening instability.
- training stability / runtime risk: low.
- control comparison expectation: should beat proposal_008 only modestly if the re-entry is genuinely helpful.

## files_to_edit
- `model/model.py`
- `model/train.py`: none

## code_insertion_points
- `model/model.py::BalancedInteractionBlock.__init__`: add a narrow scalar re-entry gate and a conservative off-biased initialization.
- `model/model.py::BalancedInteractionBlock.forward`: compute a normalized aggregate-context tensor and re-inject it with a tiny bounded gate after `mixed_scalar`.
- `model/train.py::<none>`: none

## minimal_edit_plan
1. Add one tiny gate module for scalar context re-entry.
2. Form a normalized aggregate-context candidate from `scalar_state + agg_scalar`.
3. Blend it back into `mixed_scalar` with a strongly limited coefficient before layer norm.

## implementation_checklist
- [ ] Preserve `E = sum_i E_i` and force-from-energy contract.
- [ ] Preserve benchmark metric field names and runnable entrypoint contract.
- [ ] Modify only the allowed target unit files.
- [ ] Keep tensor shapes compatible with current dataloader and model forward.
- [ ] Add no unbounded cubic neighbor/triplet loops unless explicitly justified by budget.
- [ ] Call `mark_unit_implemented.py --unit <UNIT> --actor implementation_subagent` after edits.

## expected_benchmark_effect
- primary expected gain: slight iso17 energy and Q recovery over the source.
- expected tradeoff: even a tiny gate may reopen the energy drift seen in earlier mix-heavy variants.
- failure signal that would falsify this proposal: rmd17 energy or force regresses materially versus the source despite stable training.

## ablation_or_control
- required control or comparison: proposal_008 exact source replicate.
- optional zero-gate / source-fallback / readout-only ablation: compare against source by initializing the new gate strongly off.

## implementation_notes_for_subagent
Keep the gate smaller and more strongly off-biased than any generation_010 scalar-mix proposal. The point is a tiny post-source correction, not a return to active scalar blending.
