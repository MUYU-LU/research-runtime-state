# Proposal 002: Scalar low-start vector readout gate

- family: scalar_damped_vector_readout
- phase: 2
- jump_type: exploit
- budget_class: tiny
- expected_capability_gain: Test the minimum-risk damped-vector exploit with a single trainable scalar gate on the normalized vector readout channel.

## one_sentence_hypothesis
A single low-initialized sigmoid scalar multiplying the normalized vector-norm channel can reduce ISO17 energy/gap volatility while preserving the source architecture almost exactly.

## mechanism_refs
- GEN015-M01-gated-invariant-vector-readout-damping

## evidence_refs
- mechanism_cards.json::GEN015-M01-gated-invariant-vector-readout-damping::bounded_generation_015_form::scalar_g=sigmoid(a)
- patch_blueprints.json::GEN015-M01-gated-invariant-vector-readout-damping::bounded_edit
- evidence_provenance.json::repo_artifact:repo_001_supplemental::GatedEquivariantBlock norm-to-scalar trace
- current_context::generation_014/proposal_009::best_known_unit

## historical_relation
- source_unit: generation_014/proposal_009
- relation_to_source: exploit
- not_a_duplicate_of: generation_014/proposal_002 because the source already includes LayerNorm-normalized vector norms and this proposal deliberately uses a negative low-start gate as an ablation-like damping test, not a general unguided gate from the older scalar-only source.
- why_not_duplicate: The edit is a one-parameter multiplier on the current normalized vector path; no prior completed unit tested low-start scalar damping on generation_014/proposal_009.
- lesson_used: Source vector information is valuable, so the safest next exploit is to tune amplitude before changing readout topology.

## benchmark_rationale
- rmd17 energy: Expected near-source, with small risk of reduced geometry-energy coupling early in training.
- rmd17 force: Slight force risk from smaller vector contribution; should remain conservative and differentiable.
- rmd17 gap / Q: Low topology change should protect RMD17 Q unless gate stays too closed.
- iso17 energy: May improve if full-strength vector norm is causing late validation energy spikes.
- iso17 force: Neutral or small regression; the vector channel remains trainable through the scalar gate.
- iso17 gap / Q: Target is lower gap_penalty while maintaining force gains.
- training stability / runtime risk: Very low; one `nn.Parameter` broadcast to `[N,H]`.
- control comparison expectation: Should separate source variance from genuine benefit of vector damping.

## files_to_edit
- `model/model.py`
- `model/train.py` if needed, otherwise `none`
- never `config.json` for MLIP-quality changes

## code_insertion_points
- `model/model.py::EvolutionMLIP.__init__`: after `self.vector_norm_layer`, add `self.vector_readout_logit = nn.Parameter(torch.tensor(-1.5))`.
- `model/model.py::EvolutionMLIP.forward_energy`: after normalized `vector_norm`, compute `gated_vector_norm = torch.sigmoid(self.vector_readout_logit) * vector_norm` and concatenate it with `scalar_state`.
- `model/train.py::train`: none.

## minimal_edit_plan
1. Add one trainable scalar logit initialized around `-1.5`.
2. Multiply `vector_norm` by `sigmoid(logit)` before the existing `torch.cat`.
3. Leave readout dimensions, atomref, training loop, scheduler, and force computation unchanged.

## implementation_checklist
- [ ] Preserve `E = sum_i E_i` and force-from-energy contract.
- [ ] Preserve benchmark metric field names and runnable entrypoint contract.
- [ ] Modify only the allowed target unit files.
- [ ] Do not edit `config.json`; change MLIP knobs in `model/model.py` or `model/train.py`.
- [ ] Keep tensor shapes compatible with current dataloader and model forward.
- [ ] Add no unbounded cubic neighbor/triplet loops unless explicitly justified by budget.
- [ ] Do not replace `LayerNorm(||vector_state||)`; only damp it.
- [ ] Call `mark_unit_implemented.py --unit <UNIT> --actor implementation_subagent` after edits.

## expected_benchmark_effect
- primary expected gain: Cleaner ISO17 energy/gap behavior with negligible implementation risk.
- expected tradeoff: If the source benefits from full vector amplitude, Q_total can fall through weaker force/energy coupling.
- failure signal that would falsify this proposal: Gate stays low and both RMD17/ISO17 force metrics regress without lowering ISO17 mixed_energy_mae or gap_penalty.

## ablation_or_control
- required control or comparison: Compare against exact source control and Proposal 001 per-channel gate.
- optional zero-gate / source-fallback / readout-only ablation: This acts as a near-ablation of vector amplitude; if it wins, later explore per-channel gates.

## implementation_notes_for_subagent
Keep this tiny. Use a scalar `nn.Parameter`; do not add an MLP, dropout, or training-weight changes in this unit.
