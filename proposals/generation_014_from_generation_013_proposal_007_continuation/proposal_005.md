# Proposal 005: Additive vector residual energy head

- family: additive_vector_energy_head
- phase: 2
- jump_type: jump
- budget_class: medium
- expected_capability_gain: Increase mechanism diversity by restoring vector geometry as a separate residual energy correction instead of concatenating it into the main scalar readout.

## one_sentence_hypothesis
A zero/small-initialized additive `vector_norm` residual head can reintroduce invariant geometric energy information while preserving the scalar-only readout as a stable baseline.

## mechanism_refs
- GEN014-M01-invariant-vector-readout-repair

## evidence_refs
- mechanism_cards.json::GEN014-M01-invariant-vector-readout-repair::invariant atomic energy contribution
- patch_blueprints.json::GEN014-M01-invariant-vector-readout-repair::gated compact variant
- benchmark_diagnosis.json::proposal_007 scalar-only energy/Q regression

## historical_relation
- source_unit: generation_013/proposal_007
- relation_to_source: jump
- not_a_duplicate_of: Proposal 001 because this keeps the existing scalar readout unchanged and adds a separate residual vector-energy branch.
- why_not_duplicate: Previous generation tested scalar-only versus concatenated-style readouts, not an additive residual vector correction from the scalar-only source.
- lesson_used: Preserve stable scalar path while adding geometry; avoid entangling all readout weights with vector_norm immediately.

## benchmark_rationale
- rmd17 energy: Expected improvement from additive geometry correction.
- rmd17 force: Expected improvement if residual head learns position-sensitive correction.
- rmd17 gap / Q: Bounded residual should reduce risk of gap blow-up.
- iso17 energy: Expected to recover energy lost by scalar-only source.
- iso17 force: Neutral-to-positive.
- iso17 gap / Q: Should improve if residual learns transferable geometry rather than overfitting composition.
- training stability / runtime risk: Medium-low; one small MLP branch, no extra neighbor operations.
- control comparison expectation: Should outperform source if vector-derived residual has useful signal.

## files_to_edit
- `model/model.py`
- `model/train.py` if needed, otherwise `none`

## code_insertion_points
- `model/model.py::EvolutionMLIP.__init__`: keep existing `self.readout` input `hidden_dim`; add `self.vector_readout = nn.Sequential(nn.Linear(hidden_dim, hidden_dim), nn.SiLU(), nn.Linear(hidden_dim, 1))` and optional small scalar gate.
- `model/model.py::EvolutionMLIP.forward_energy`: compute scalar per-atom energy as source does, compute `vector_norm`, add gated `self.vector_readout(vector_norm).squeeze(-1)`.
- `model/train.py::train`: none.

## minimal_edit_plan
1. Add a compact vector_norm residual readout branch.
2. Compute `vector_norm` after interactions.
3. Sum scalar readout energy plus a small/gated vector residual before adding atomref.

## implementation_checklist
- [ ] Preserve `E = sum_i E_i` and force-from-energy contract.
- [ ] Preserve benchmark metric field names and runnable entrypoint contract.
- [ ] Modify only the allowed target unit files.
- [ ] Keep tensor shapes compatible with current dataloader and model forward.
- [ ] Add no unbounded cubic neighbor/triplet loops unless explicitly justified by budget.
- [ ] Call `mark_unit_implemented.py --unit <UNIT> --actor implementation_subagent` after edits.
- [ ] Initialize any residual gate small; do not replace the scalar readout.

## expected_benchmark_effect
- primary expected gain: Energy/Q recovery with lower disruption than concatenation.
- expected tradeoff: Additional branch may undertrain in only 8 epochs or introduce slight overfit.
- failure signal that would falsify this proposal: Residual branch worsens energy/gap without force gain.

## ablation_or_control
- required control or comparison: Compare to proposal_007 and Proposal 001 full concatenation.
- optional zero-gate / source-fallback / readout-only ablation: Zero/small gate should approximate source behavior initially.

## implementation_notes_for_subagent
Do not change interaction blocks. Treat vector_norm as invariant per-atom features of shape `[n_atoms, hidden_dim]`.
