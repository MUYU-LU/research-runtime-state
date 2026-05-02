# Proposal 004: Ultra-narrow late invariant helper jump

- family: late_invariant_diagnostic
- phase: 5
- jump_type: jump
- budget_class: small
- expected_capability_gain: test whether one tiny late invariant statistic can lift ISO17 without reworking the trunk.

## one_sentence_hypothesis
A single ultra-narrow invariant helper injected just before readout can probe the only remaining bounded jump lane while keeping the core directional message path untouched.

## mechanism_refs
- W-BAL-SO3K-002

## evidence_refs
- mechanism_cards.json::W-BAL-SO3K-002
- patch_blueprints.json::W-BAL-SO3K-002
- generation_memory.json
- benchmark_diagnosis.json

## historical_relation
- source_unit: generation_004/proposal_001
- relation_to_source: jump
- not_a_duplicate_of: generation_008/proposal_004 because this proposal is narrower, explicitly gated to zero, and confined to one helper statistic immediately before readout.
- lesson_used: broader late-summary jumps regressed, so only the smallest disable-friendly helper remains defensible.

## benchmark_rationale
Discuss expected effects on all relevant benchmark signals, not force-only:
- rmd17 energy: slight downside risk if the helper disturbs scalar calibration.
- rmd17 force: near-flat if the helper only perturbs invariant readout inputs mildly.
- rmd17 gap / Q: could worsen if the helper injects noisy late information.
- iso17 energy: main target, since a tiny missing invariant summary may matter more there.
- iso17 force: slight positive or neutral.
- iso17 gap / Q: possible gain if the helper captures a missing local summary statistic.
- training stability / runtime risk: moderate but bounded.
- control comparison expectation: this should only survive selection if it clearly earns upside over the source control.

## files_to_edit
- `model/model.py`
- `model/train.py`: none

## code_insertion_points
- `model/model.py::EvolutionMLIP.forward_energy`: add one low-width invariant helper just before readout and gate it so it can collapse to zero.
- `model/train.py::<none>`: none

## minimal_edit_plan
1. Derive one invariant helper feature from existing late scalar/vector state using cheap contractions only.
2. Pass it through a tiny projection and zero-biased gate.
3. Inject it into the readout input as a residual path that can disable itself.

## implementation_checklist
- [ ] Preserve `E = sum_i E_i` and force-from-energy contract.
- [ ] Preserve benchmark metric field names and runnable entrypoint contract.
- [ ] Modify only the allowed target unit files.
- [ ] Keep tensor shapes compatible with current dataloader and model forward.
- [ ] Add no unbounded cubic neighbor/triplet loops unless explicitly justified by budget.
- [ ] Call `mark_unit_implemented.py --unit <UNIT> --actor implementation_subagent` after edits.

## expected_benchmark_effect
- primary expected gain: small ISO17 lift with limited rmd17 damage.
- expected tradeoff: added late helper may still hurt the benchmark balance.
- failure signal that would falsify this proposal: any ISO17 gain is outweighed by a larger rmd17 energy or gap regression.

## ablation_or_control
- required control or comparison: proposal_008 exact source replicate.
- optional zero-gate / source-fallback / readout-only ablation: zero-helper initialization should make fallback behavior easy to test.

## implementation_notes_for_subagent
No new pairwise message-passing stage. Keep the helper width tiny, preferably one narrow projection path, and avoid modifying force computation or the optimizer schedule.
