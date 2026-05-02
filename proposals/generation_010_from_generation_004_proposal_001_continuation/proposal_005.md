# Proposal 005: Gated readout-side helper jump

- family: late_invariant_diagnostic
- phase: 5
- jump_type: jump
- budget_class: small
- expected_capability_gain: distinguish whether the late-helper idea helps only when attached at readout rather than earlier in the trunk.

## one_sentence_hypothesis
Attaching a tiny gated invariant helper directly to the readout input, with stricter disable behavior than prior jump attempts, can test a narrow late-summary hypothesis without contaminating trunk updates.

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
- not_a_duplicate_of: proposal_004 because this variant keeps the helper strictly readout-side instead of blending it back into an earlier scalar state.
- lesson_used: prior late-summary probes were too easy to let bleed into energy calibration; a cleaner readout-side isolation is the safer diagnostic.

## benchmark_rationale
Discuss expected effects on all relevant benchmark signals, not force-only:
- rmd17 energy: mild downside risk, but smaller than earlier helper placements.
- rmd17 force: expected nearly unchanged.
- rmd17 gap / Q: neutral to slightly negative unless the helper is genuinely useful.
- iso17 energy: possible moderate upside if readout lacks one compact invariant feature.
- iso17 force: neutral.
- iso17 gap / Q: could improve if the helper adds stable summary information.
- training stability / runtime risk: moderate but bounded by tiny width and gate.
- control comparison expectation: should only beat control on aggregate `Q_total`, not isolated force movement.

## files_to_edit
- `model/model.py`
- `model/train.py`: none

## code_insertion_points
- `model/model.py::EvolutionMLIP.forward_energy`: compute one helper branch immediately before the atom-wise readout and fuse it through a zero-biased gate.
- `model/train.py::<none>`: none

## minimal_edit_plan
1. Create one tiny helper feature from existing late hidden state only.
2. Apply a narrow gate initialized near off.
3. Concatenate or residually add it to the readout input with shape-preserving projection.

## implementation_checklist
- [ ] Preserve `E = sum_i E_i` and force-from-energy contract.
- [ ] Preserve benchmark metric field names and runnable entrypoint contract.
- [ ] Modify only the allowed target unit files.
- [ ] Keep tensor shapes compatible with current dataloader and model forward.
- [ ] Add no unbounded cubic neighbor/triplet loops unless explicitly justified by budget.
- [ ] Call `mark_unit_implemented.py --unit <UNIT> --actor implementation_subagent` after edits.

## expected_benchmark_effect
- primary expected gain: cleaner test of the late-summary hypothesis with lower trunk disruption.
- expected tradeoff: helper may be too weak to matter.
- failure signal that would falsify this proposal: no measurable ISO17 improvement and any rmd17 regression beyond control variance.

## ablation_or_control
- required control or comparison: proposal_008 exact source replicate.
- optional zero-gate / source-fallback / readout-only ablation: compare against proposal_004 to isolate placement effects.

## implementation_notes_for_subagent
Prefer residual-add with projection over broad concatenation if shapes allow. The helper must remain optional and cheap.
