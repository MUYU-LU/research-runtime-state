# Proposal 003: Residual vector-readout blend gate

- family: residual_vector_readout_blend
- phase: 2
- jump_type: exploit
- budget_class: small
- expected_capability_gain: Let the model interpolate between scalar-only and full normalized vector readout, reducing the risk of over-using vector norms on ISO17.

## one_sentence_hypothesis
A residual blend gate that adds a learned vector-norm delta to a scalar baseline should preserve source gains only where vector information improves the scalar potential.

## mechanism_refs
- GEN015-M01-gated-invariant-vector-readout-damping

## evidence_refs
- mechanism_cards.json::GEN015-M01-gated-invariant-vector-readout-damping::TorchMD-Net gated vector norm pattern
- patch_blueprints.json::GEN015-M01-gated-invariant-vector-readout-damping::current_code_insertion_point
- context.md::Diff_vs_source::proposal_009 adds normalized vector_norm readout
- context.md::ISO17_history_summary::energy_trend=worsening

## historical_relation
- source_unit: generation_014/proposal_009
- relation_to_source: exploit
- not_a_duplicate_of: proposal_001 because this uses a two-branch residual readout blend rather than gating the vector feature before the same readout.
- why_not_duplicate: The scalar baseline branch gives an explicit fallback path; generation_014/proposal_009 forces all readout predictions through concatenated `[scalar, vector_norm]`.
- lesson_used: Keep the winning normalized vector feature, but isolate it as a trainable correction instead of making it mandatory input to every scalar-energy path.

## benchmark_rationale
- rmd17 energy: Scalar baseline plus vector correction should retain most source energy gains.
- rmd17 force: Vector correction remains differentiable, preserving force-from-energy geometry sensitivity.
- rmd17 gap / Q: Blend gate may protect small RMD17 gap by allowing fallback to scalar branch.
- iso17 energy: Target is less overfit cross-conformer energy behavior by letting the readout suppress vector correction.
- iso17 force: Could slightly regress if correction is suppressed; expected less severe than scalar-only source ancestor.
- iso17 gap / Q: Expected improvement if vector norms caused calibration drift.
- training stability / runtime risk: Low-to-medium; adds a small second readout branch but no neighbor-loop changes.
- control comparison expectation: Should beat source if mandatory concatenation is the ISO17 weakness; otherwise source control will remain stronger.

## files_to_edit
- `model/model.py`
- `model/train.py` if needed, otherwise `none`
- never `config.json` for MLIP-quality changes

## code_insertion_points
- `model/model.py::EvolutionMLIP.__init__`: keep existing `self.readout` for `[scalar_state, vector_norm]` or rename it as vector branch; add `self.scalar_readout = nn.Sequential(nn.Linear(hidden_dim, hidden_dim), nn.SiLU(), nn.Linear(hidden_dim, hidden_dim), nn.SiLU(), nn.Linear(hidden_dim, 1))` and `self.vector_delta_logit = nn.Parameter(torch.tensor(-1.0))`.
- `model/model.py::EvolutionMLIP.forward_energy`: compute `scalar_energy = self.scalar_readout(scalar_state).squeeze(-1)`, `vector_energy = self.readout(torch.cat([scalar_state, vector_norm], dim=-1)).squeeze(-1)`, then `per_atom_energy = scalar_energy + sigmoid(vector_delta_logit) * (vector_energy - scalar_energy)`.
- `model/train.py::train`: none.

## minimal_edit_plan
1. Add a scalar-only readout branch with the same hidden width as the existing readout.
2. Compute scalar and vector-aware per-atom energies from the same final states.
3. Blend from scalar branch toward vector-aware branch using a low-start trainable sigmoid scalar.

## implementation_checklist
- [ ] Preserve `E = sum_i E_i` and force-from-energy contract.
- [ ] Preserve benchmark metric field names and runnable entrypoint contract.
- [ ] Modify only the allowed target unit files.
- [ ] Do not edit `config.json`; change MLIP knobs in `model/model.py` or `model/train.py`.
- [ ] Keep tensor shapes compatible: both branches return `[N]` per-atom energy before summation.
- [ ] Add no unbounded cubic neighbor/triplet loops unless explicitly justified by budget.
- [ ] Keep atomref fitting and autograd force calculation unchanged.
- [ ] Call `mark_unit_implemented.py --unit <UNIT> --actor implementation_subagent` after edits.

## expected_benchmark_effect
- primary expected gain: More robust ISO17 energy/gap with source-like force sensitivity.
- expected tradeoff: Additional branch parameters can overfit or underuse vector information within the fixed 8-epoch budget.
- failure signal that would falsify this proposal: Both energy and force regress relative to source, or ISO17 validation energy remains unstable despite fallback branch.

## ablation_or_control
- required control or comparison: Exact source control; compare to scalar low-start gate and per-channel gate.
- optional zero-gate / source-fallback / readout-only ablation: A zero blend approximates scalar-only readout; source control is full vector branch.

## implementation_notes_for_subagent
Do not change the interaction blocks. The only topology change is localized to per-atom readout after `vector_norm` is computed.
