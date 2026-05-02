# Proposal 009: Multiplicative scalar-vector readout cross feature

- family: scalar_vector_cross_readout
- phase: 3
- jump_type: wildcard
- budget_class: small
- expected_capability_gain: Test a mechanism-diverse invariant readout that lets scalar features interact multiplicatively with damped vector norms.

## one_sentence_hypothesis
Adding a bounded `scalar_state * gated_vector_norm` cross feature may capture useful invariant scalar-vector coupling that direct concatenation misses, while damping protects ISO17 energy/gap behavior.

## mechanism_refs
- GEN015-M01-gated-invariant-vector-readout-damping

## evidence_refs
- mechanism_cards.json::GEN015-M01-gated-invariant-vector-readout-damping::rotationally invariant contractions of vector features
- mechanism_cards.json::GEN015-M01-gated-invariant-vector-readout-damping::TorchMD-Net gate/update pattern
- patch_blueprints.json::GEN015-M01-gated-invariant-vector-readout-damping::must_preserve energy-to-force autograd consistency
- context.md::current_source_node::family=normalized_invariant_vector_readout::child_count=0

## historical_relation
- source_unit: generation_014/proposal_009
- relation_to_source: jump
- not_a_duplicate_of: proposals 001-005 because this changes the readout feature basis by adding an elementwise scalar-vector cross term, not only damping or adapting vector norms.
- why_not_duplicate: No prior source child has tested multiplicative invariant cross features after vector_norm LayerNorm.
- lesson_used: Mechanism diversity is needed, but evidence only supports invariant vector contractions and smooth conservative readouts; do not jump to direct-force or discontinuous attention.

## benchmark_rationale
- rmd17 energy: Cross features may improve per-atom energy expressiveness.
- rmd17 force: Because vector norms depend on positions, cross features can improve force sensitivity but may overfit.
- rmd17 gap / Q: Added feature width risks gap overfitting; damping should moderate this.
- iso17 energy: Potential gain if current readout lacks scalar-vector interactions; risk if cross terms amplify validation energy volatility.
- iso17 force: Could improve if cross terms capture transferable geometry; could regress from overfit.
- iso17 gap / Q: Must be judged by Q_total, not force-only; gap penalty is the main watch item.
- training stability / runtime risk: Medium; readout input widens to `3H` but no edge-loop/runtime explosion.
- control comparison expectation: Should beat source control only if cross term adds real signal beyond noise.

## files_to_edit
- `model/model.py`
- `model/train.py` if needed, otherwise `none`
- never `config.json` for MLIP-quality changes

## code_insertion_points
- `model/model.py::EvolutionMLIP.__init__`: add a low-start scalar or per-channel vector gate as in M01, and change the first readout layer from `nn.Linear(hidden_dim * 2, hidden_dim)` to `nn.Linear(hidden_dim * 3, hidden_dim)`.
- `model/model.py::EvolutionMLIP.forward_energy`: compute `gated_vector_norm`, then `cross = scalar_state * gated_vector_norm`, and set `readout_input = torch.cat([scalar_state, gated_vector_norm, cross], dim=-1)`.
- `model/train.py::train`: none.

## minimal_edit_plan
1. Add a low-start gate for normalized vector norms.
2. Widen readout first layer to accept scalar, gated vector norm, and their elementwise product.
3. Compute cross feature after all interactions and before per-atom readout.

## implementation_checklist
- [ ] Preserve `E = sum_i E_i` and force-from-energy contract.
- [ ] Preserve benchmark metric field names and runnable entrypoint contract.
- [ ] Modify only the allowed target unit files.
- [ ] Do not edit `config.json`; change MLIP knobs in `model/model.py` or `model/train.py`.
- [ ] Keep tensor shapes compatible: cross feature is `[N,H]`, concatenated input is `[N,3H]`.
- [ ] Add no unbounded cubic neighbor/triplet loops unless explicitly justified by budget.
- [ ] Keep vector features rotationally invariant by using norms only, not raw vector components.
- [ ] Call `mark_unit_implemented.py --unit <UNIT> --actor implementation_subagent` after edits.

## expected_benchmark_effect
- primary expected gain: Mechanism-diverse Q_total improvement if scalar-vector interactions aid energy calibration.
- expected tradeoff: Higher overfit/ISO17 gap risk than simpler gates.
- failure signal that would falsify this proposal: ISO17 gap_penalty worsens or energy trend remains unstable while force-only metrics improve.

## ablation_or_control
- required control or comparison: Exact source control and per-channel gate proposal.
- optional zero-gate / source-fallback / readout-only ablation: If cross feature wins, later ablate cross term versus gate alone.

## implementation_notes_for_subagent
This is a wildcard. Keep it bounded and invariant; do not add raw vector orientation features, new datasets, or force heads.
