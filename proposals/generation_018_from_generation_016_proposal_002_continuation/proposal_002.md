# Proposal 002: Late readout-only Euclidean RoPE context residual

- family: readout_rope_global_context
- phase: 4
- jump_type: exploit
- budget_class: small
- expected_capability_gain: test the same G018-MECH-001 nonlocal geometry signal at the lowest-risk readout insertion point.

## one_sentence_hypothesis
Adding a single late Euclidean RoPE global context residual immediately before per-atom energy readout should capture molecule-level conformer context with less force-path disruption than per-layer global attention.

## mechanism_refs
- G018-MECH-001

## evidence_refs
- paper_artifact:paper_001
- repo_artifact:repo_001
- mechanism_cards.json:G018-MECH-001.current_code_insertion_point
- patch_blueprints.json:G018-MECH-001.bounded_edit
- generation_016/proposal_002 runtime summary: strong local RMD17 and weaker ISO17 energy/gap indicate a readout-context exploit target.

## historical_relation
- source_unit: generation_016/proposal_002
- relation_to_source: exploit
- not_a_duplicate_of: proposal_001 because this does not inject global context inside every interaction block; it only conditions the final readout.
- lesson_used: generation_017 local PaiNN/body-order changes frequently hurt Q_total; a late residual limits interference with trained local message dynamics.

## benchmark_rationale
- rmd17 energy: late context can alter per-atom energy decomposition but should be damped enough to preserve source mixed_energy_mae.
- rmd17 force: fewer position-dependent operations than per-layer insertion should reduce force-gradient noise.
- rmd17 gap / Q: expected neutral to slight gain; the zero-gate fallback should remain close to source/control.
- iso17 energy: global context before readout targets within/other conformer energy differences and the source's worsening ISO17 validation energy trend.
- iso17 force: local interaction force basis remains unchanged, so force MAE should not be the primary tradeoff.
- iso17 gap / Q: expected gap_penalty improvement if global RoPE encodes molecule shape information not available in cutoff features.
- training stability / runtime risk: small O(N*M*Dq*Dv) extra cost once per forward; lower risk than proposal_001.
- control comparison expectation: should separate from generation_017 controls by improving ISO17 energy/gap while staying inside neutral variance on RMD17 force.

## files_to_edit
- `model/model.py`
- `model/train.py` none
- never `config.json` for MLIP-quality changes

## code_insertion_points
- `model/model.py::GlobalRoPEAttentionSideChannel`: same bounded module as G018-MECH-001 but instantiated once.
- `model/model.py::EvolutionMLIP.__init__`: add `self.readout_global_context`, `self.readout_context_norm`, and `self.readout_context_scale`.
- `model/model.py::EvolutionMLIP.forward_energy`: after `scalar_state = self.readout_norm(scalar_state)` and before `self.readout(scalar_state)`, add a damped `scalar_state = scalar_state + scale * context`.
- `model/train.py`: no changes; keep losses and metric names fixed.

## minimal_edit_plan
1. Add one global RoPE context module using centered positions, fixed direction buffer, low frequencies, and q/k/v projections.
2. Apply it only after the final interaction stack and readout normalization; residual-add the projected context to `scalar_state` with sigmoid/logit scale initialized near zero.
3. Leave all interaction blocks, body-order branch, atomref, optimizer, and train losses unchanged.
4. Include comments that this is the readout-only exploit variant of G018-MECH-001, not the per-layer proposal.

## implementation_checklist
- [ ] Preserve `E = sum_i E_i` and force-from-energy contract.
- [ ] Preserve benchmark metric field names and runnable entrypoint contract.
- [ ] Modify only the allowed target unit files.
- [ ] Do not edit `config.json`; change MLIP knobs in `model/model.py` or `model/train.py`.
- [ ] Keep tensor shapes compatible with current dataloader and model forward.
- [ ] Add no unbounded cubic neighbor/triplet loops unless explicitly justified by budget.
- [ ] Ensure the residual scale can be set to zero to recover source behavior.
- [ ] Call `mark_unit_implemented.py --unit <UNIT> --actor implementation_subagent` after edits.

## expected_benchmark_effect
- primary expected gain: ISO17 mixed_energy_mae and gap_penalty improvement with minimal local-force disruption.
- expected tradeoff: may underperform proposal_001 if nonlocal information must influence message passing earlier.
- failure signal that would falsify this proposal: readout context changes RMD17 forces materially while ISO17 energy/gap remains near control.

## ablation_or_control
- required control or comparison: source replicate and proposal_001 per-layer RoPE variant if both are selected.
- optional zero-gate / source-fallback / readout-only ablation: fixed zero residual should reproduce source; M=6 default can be compared to M=10 if runtime allows.

## implementation_notes_for_subagent
Prefer the smallest safe implementation: one module, one call site, one residual scale. Do not alter `BalancedInteractionBlock`, neighbor list, body-order branch, training schedule, or any benchmark/runtime config.
