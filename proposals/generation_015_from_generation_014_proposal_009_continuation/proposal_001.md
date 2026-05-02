# Proposal 001: Per-channel damped vector-norm gate

- family: gated_invariant_vector_readout_damping
- phase: 2
- jump_type: exploit
- budget_class: small
- expected_capability_gain: Preserve the generation_014/proposal_009 vector-norm frontier gain while reducing ISO17 energy/gap over-reliance on the normalized vector channel.

## one_sentence_hypothesis
A learned per-channel sigmoid gate on `LayerNorm(||vector_state||)` lets the current scalar readout keep useful invariant geometry while damping vector channels that destabilize ISO17 energy calibration.

## mechanism_refs
- GEN015-M01-gated-invariant-vector-readout-damping

## evidence_refs
- evidence_quality.json::grade=A::usable_for_implementation=true
- mechanism_cards.json::GEN015-M01-gated-invariant-vector-readout-damping::strong
- patch_blueprints.json::GEN015-M01-gated-invariant-vector-readout-damping::implementation_ready=true
- proposal_constraints.json::allowed_mechanisms=GEN015-M01-gated-invariant-vector-readout-damping
- current_context::generation_014/proposal_009::Q_total=3.8988711909426823::ISO17_energy_trend=worsening

## historical_relation
- source_unit: generation_014/proposal_009
- relation_to_source: exploit
- not_a_duplicate_of: generation_014/proposal_002 because this starts from the already successful normalized vector-norm readout source and uses per-channel damping rather than only the older scalar gate variant.
- why_not_duplicate: generation_014/proposal_009 has no learned vector readout damping; it concatenates full-strength normalized vector norms directly into the readout.
- lesson_used: The source is the best known unit, but ISO17 validation energy worsens late and ISO17 gap_penalty remains high, so exploit should protect the vector path without making it stronger by default.

## benchmark_rationale
- rmd17 energy: Should remain close to source because scalar state and normalized vector norms are still available to the readout.
- rmd17 force: Moderate risk of force regression if the gate suppresses useful vector sensitivity; per-channel learning should preserve channels with useful gradients.
- rmd17 gap / Q: Small RMD17 gap should be protected by avoiding new neighbor or force semantics.
- iso17 energy: Primary target; damped vector contribution may reduce late validation energy spikes and mixed_energy_mae.
- iso17 force: Expected neutral-to-slightly-negative relative to source if damping reduces geometry sensitivity, but still better than scalar-only ancestors if gates open where useful.
- iso17 gap / Q: Target is lower gap_penalty than 0.0909369 with Q_iso17 non-regression or small gain.
- training stability / runtime risk: Low; one small gate MLP/linear and no new loops.
- control comparison expectation: Must beat exact generation_014/proposal_009 control or at least show better ISO17 energy/gap without unacceptable RMD17 loss.

## files_to_edit
- `model/model.py`
- `model/train.py` if needed, otherwise `none`
- never `config.json` for MLIP-quality changes

## code_insertion_points
- `model/model.py::EvolutionMLIP.__init__`: after `self.vector_norm_layer`, add `self.vector_readout_gate = nn.Sequential(nn.Linear(hidden_dim * 2, hidden_dim), nn.SiLU(), nn.Linear(hidden_dim, hidden_dim))` and initialize the final bias negative if practical.
- `model/model.py::EvolutionMLIP.forward_energy`: after `vector_norm = self.vector_norm_layer(...)`, compute `gate = torch.sigmoid(self.vector_readout_gate(torch.cat([scalar_state, vector_norm], dim=-1)))` and concatenate `scalar_state` with `gate * vector_norm`.
- `model/train.py::train`: none; preserve the current loss, scheduler, atomref initialization, and force-from-energy training path.

## minimal_edit_plan
1. Add the per-channel gate module in `EvolutionMLIP.__init__` without changing hidden_dim, cutoff, num_rbf, dataloaders, or readout output semantics.
2. In `forward_energy`, construct gate input `[scalar_state, vector_norm]`, multiply `vector_norm` by `sigmoid(gate_logits)`, and feed `[scalar_state, gated_vector_norm]` to the existing readout width.
3. Optionally set the final gate bias to about `-1.5` so the vector channel starts damped but trainable.

## implementation_checklist
- [ ] Preserve `E = sum_i E_i` and force-from-energy contract.
- [ ] Preserve benchmark metric field names and runnable entrypoint contract.
- [ ] Modify only the allowed target unit files.
- [ ] Do not edit `config.json`; change MLIP knobs in `model/model.py` or `model/train.py`.
- [ ] Keep tensor shapes compatible with current dataloader and model forward: gate and vector_norm both `[N, H]`.
- [ ] Add no unbounded cubic neighbor/triplet loops unless explicitly justified by budget.
- [ ] Keep `_build_neighbor_list`, `_cutoff_weight`, and autograd force computation unchanged.
- [ ] Call `mark_unit_implemented.py --unit <UNIT> --actor implementation_subagent` after edits.

## expected_benchmark_effect
- primary expected gain: Small Q_total improvement through better ISO17 mixed_energy_mae/gap balance while keeping most source RMD17 gains.
- expected tradeoff: Dampening can reduce vector-derived force gains if gates remain too closed.
- failure signal that would falsify this proposal: Q_total below source with no ISO17 energy/gap improvement, or RMD17 force regression large enough to erase source advantage.

## ablation_or_control
- required control or comparison: Exact source control replicate and source metrics Q_rmd17=4.054452, Q_iso17=3.609935, Q_total=3.898871.
- optional zero-gate / source-fallback / readout-only ablation: Compare learned gate values qualitatively against a fixed low gate proposal and the source full-strength normalized vector readout.

## implementation_notes_for_subagent
This is the strongest evidence-backed exploit. Keep it as a localized readout edit; do not change message passing, atomref fitting, loss weights, benchmark files, or `main.py`.
