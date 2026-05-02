# Proposal 001: Narrow per-channel scalar-mix exploit

- family: balanced_scalar_mix_recovery
- phase: 4
- jump_type: exploit
- budget_class: tiny
- expected_capability_gain: recover parent-like rMD17 energy while holding ISO17 near source.

## one_sentence_hypothesis
Replacing the fixed post-update `0.7/0.3` scalar blend with a narrowly clamped per-channel gate should keep the parent directional message path intact while reducing context overmixing that has repeatedly hurt `Q_total`.

## mechanism_refs
- M-BAL-PAINN-001

## evidence_refs
- /home/lmy/.openclaw/workspace/research_runtime/knowledge/briefs/evidence_brief_20260421T013733Z.md
- mechanism_cards.json::M-BAL-PAINN-001
- patch_blueprints.json::M-BAL-PAINN-001
- proposal_constraints.json
- generation_memory.json (generation_008 and generation_009 outcome memory)

## historical_relation
- source_unit: generation_004/proposal_001
- relation_to_source: exploit
- not_a_duplicate_of: generation_008/proposal_001 because this keeps the gate interval much narrower, centered near source behavior, and forbids adding new summary capacity.
- lesson_used: generation_008/proposal_007 and generation_009 outcomes both argue for shrinking or tightly controlling the auxiliary scalar-mix path rather than broadening it.

## benchmark_rationale
Discuss expected effects on all relevant benchmark signals, not force-only:
- rmd17 energy: primary target, because the source already has excellent `mixed_energy_mae 0.5927` and later children mostly regressed.
- rmd17 force: should stay near source because the directional message path and force-from-energy contract are unchanged.
- rmd17 gap / Q: should improve if energy calibration recovers without destabilizing force.
- iso17 energy: slight upside if the bounded gate prevents overshoot from the auxiliary context path.
- iso17 force: expected near-flat to slightly positive.
- iso17 gap / Q: modest upside, but secondary to preserving rmd17.
- training stability / runtime risk: low, since only one tiny in-block gate is added.
- control comparison expectation: should beat the control only if the mix path, not variance, is the true bottleneck.

## files_to_edit
- `model/model.py`
- `model/train.py`: none

## code_insertion_points
- `model/model.py::BalancedInteractionBlock.__init__`: add a tiny gate head that maps `concat(mixed_scalar, agg_scalar)` to per-channel `alpha`.
- `model/model.py::BalancedInteractionBlock.forward`: replace the fixed `0.7/0.3` blend with `alpha` clamped to roughly `[0.05, 0.20]`.
- `model/train.py::<none>`: none

## minimal_edit_plan
1. Add one lightweight gate module and initialize its bias near a small blend weight.
2. Compute per-channel `alpha` from existing scalar features only.
3. Form `new_scalar = layer_norm((1 - alpha) * mixed_scalar + alpha * scalar_mix_norm(scalar_state + agg_scalar))` without changing other paths.

## implementation_checklist
- [ ] Preserve `E = sum_i E_i` and force-from-energy contract.
- [ ] Preserve benchmark metric field names and runnable entrypoint contract.
- [ ] Modify only the allowed target unit files.
- [ ] Keep tensor shapes compatible with current dataloader and model forward.
- [ ] Add no unbounded cubic neighbor/triplet loops unless explicitly justified by budget.
- [ ] Call `mark_unit_implemented.py --unit <UNIT> --actor implementation_subagent` after edits.

## expected_benchmark_effect
- primary expected gain: smaller negative `G_delta` than recent exploit descendants by restoring source-faithful scalar calibration.
- expected tradeoff: may be too conservative to beat variance.
- failure signal that would falsify this proposal: rmd17 `mixed_energy_mae` worsens materially while force stays flat, indicating the scalar-mix path was not the main culprit.

## ablation_or_control
- required control or comparison: proposal_008 exact source replicate.
- optional zero-gate / source-fallback / readout-only ablation: compare against proposal_007 pure residual simplification.

## implementation_notes_for_subagent
Keep the current pairwise directional messaging, `agg_norm`, and `vector_alignment` features. Do not add new message tensors, readout branches, losses, or train-time curriculum changes. This is an in-block scalar-mix refinement only.
