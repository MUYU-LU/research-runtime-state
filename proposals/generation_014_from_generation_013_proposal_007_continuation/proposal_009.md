# Proposal 009: Normalized vector-norm readout repair

- family: normalized_invariant_vector_readout
- phase: 2
- jump_type: wildcard
- budget_class: small
- expected_capability_gain: Test a mechanism-diverse vector repair that normalizes vector_norm before energy readout to reduce scale sensitivity.

## one_sentence_hypothesis
Layer-normalizing `||vector_state||` before concatenated readout restores invariant geometric energy information while reducing the scale mismatch that could harm gap or ISO17 transfer.

## mechanism_refs
- GEN014-M01-invariant-vector-readout-repair

## evidence_refs
- mechanism_cards.json::GEN014-M01-invariant-vector-readout-repair
- patch_blueprints.json::GEN014-M01-invariant-vector-readout-repair
- benchmark_diagnosis.json::proposal_007 gap/energy tradeoff

## historical_relation
- source_unit: generation_013/proposal_007
- relation_to_source: jump
- not_a_duplicate_of: Proposal 001 because this inserts an explicit `LayerNorm(hidden_dim)` on vector_norm before concatenation.
- why_not_duplicate: Prior selected units did not test normalized vector invariant features from scalar-only proposal_007.
- lesson_used: Vector readout is evidence-backed, but raw vector magnitudes may introduce scale variance; normalize the invariant channel.

## benchmark_rationale
- rmd17 energy: Expected improvement from vector channel, potentially smoother than raw concat.
- rmd17 force: Expected modest improvement through normalized geometry dependence.
- rmd17 gap / Q: Normalization may preserve proposal_007's gap benefit better than full raw restoration.
- iso17 energy: Targeted recovery of energy regression with controlled scale.
- iso17 force: Neutral-to-positive.
- iso17 gap / Q: Expected improved Q if normalization improves transfer.
- training stability / runtime risk: Low; one LayerNorm and widened readout.
- control comparison expectation: Should beat control and be less volatile than raw vector restoration.

## files_to_edit
- `model/model.py`
- `model/train.py` if needed, otherwise `none`

## code_insertion_points
- `model/model.py::EvolutionMLIP.__init__`: add `self.vector_norm_layer = nn.LayerNorm(hidden_dim)` and widen readout to `hidden_dim * 2`.
- `model/model.py::EvolutionMLIP.forward_energy`: compute `vector_norm = self.vector_norm_layer(torch.linalg.norm(vector_state, dim=-1))` before concatenation with `scalar_state`.
- `model/train.py::train`: none.

## minimal_edit_plan
1. Add LayerNorm for vector_norm in `__init__`.
2. Widen readout to accept scalar plus normalized vector_norm.
3. Concatenate scalar and normalized vector invariant features for readout.

## implementation_checklist
- [ ] Preserve `E = sum_i E_i` and force-from-energy contract.
- [ ] Preserve benchmark metric field names and runnable entrypoint contract.
- [ ] Modify only the allowed target unit files.
- [ ] Keep tensor shapes compatible with current dataloader and model forward.
- [ ] Add no unbounded cubic neighbor/triplet loops unless explicitly justified by budget.
- [ ] Call `mark_unit_implemented.py --unit <UNIT> --actor implementation_subagent` after edits.
- [ ] Do not add dataset-specific branches or modify loss weights.

## expected_benchmark_effect
- primary expected gain: More robust energy/Q recovery than raw vector concat.
- expected tradeoff: Normalization may erase useful magnitude information and blunt force gains.
- failure signal that would falsify this proposal: No Q improvement over proposal_007 or worse than raw vector restoration.

## ablation_or_control
- required control or comparison: Proposal 008 source control and Proposal 001 raw vector restoration.
- optional zero-gate / source-fallback / readout-only ablation: Later combine normalization with small gate if raw normalized path is too strong.

## implementation_notes_for_subagent
This wildcard is still M01-bounded. Do not alter message passing or introduce attention.
