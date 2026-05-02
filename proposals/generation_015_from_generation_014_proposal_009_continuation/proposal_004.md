# Proposal 004: TorchMD-style gated scalar update before readout

- family: gated_equivariant_scalar_update_readout
- phase: 3
- jump_type: jump
- budget_class: medium
- expected_capability_gain: Move from raw vector-norm concatenation to a small TorchMD-style gated scalar update that consumes vector norms before scalar energy prediction.

## one_sentence_hypothesis
A localized gated scalar update `scalar_state <- LayerNorm(scalar_state + gate * f([scalar_state, ||v||]))` should use invariant vector information more smoothly than direct readout concatenation.

## mechanism_refs
- GEN015-M01-gated-invariant-vector-readout-damping

## evidence_refs
- mechanism_cards.json::GEN015-M01-gated-invariant-vector-readout-damping::repo_code_trace::GatedEquivariantBlock.forward
- evidence_provenance.json::repo_artifact:repo_001_supplemental::torchmdnet/models/utils.py::GatedEquivariantBlock
- patch_blueprints.json::GEN015-M01-gated-invariant-vector-readout-damping::target_insertion_points
- proposal_constraints.json::blocked_mechanisms excludes rewrites without patch blueprint; this is localized to readout/update

## historical_relation
- source_unit: generation_014/proposal_009
- relation_to_source: jump
- not_a_duplicate_of: generation_014/proposal_009 because source concatenates normalized vector norms directly to the final readout, while this proposal first folds vector norms into scalar state through a gated residual update and then uses a scalar readout.
- why_not_duplicate: It tests the repo-traced GatedEquivariantBlock idea more directly than a simple vector-feature multiplier.
- lesson_used: Phase-2 normalized vector readout won; a cautious phase-3 jump should keep invariant vector norms but change where they enter the scalar potential.

## benchmark_rationale
- rmd17 energy: Expected to stay competitive by retaining vector-derived invariant information.
- rmd17 force: Vector norms still depend on positions through message passing, so force sensitivity remains available.
- rmd17 gap / Q: Added normalization/gating can protect gap; extra parameters may slightly destabilize small data.
- iso17 energy: Primary possible gain from smoother vector-to-scalar integration before final readout.
- iso17 force: Expected neutral; if update is too damped, force gains may fall.
- iso17 gap / Q: Target lower gap_penalty and better Q_iso17 through gated scalar calibration.
- training stability / runtime risk: Medium; adds one residual update MLP and LayerNorm but no new edge loops.
- control comparison expectation: Should beat source only if direct concatenation is the bottleneck, not if source simply needs amplitude damping.

## files_to_edit
- `model/model.py`
- `model/train.py` if needed, otherwise `none`
- never `config.json` for MLIP-quality changes

## code_insertion_points
- `model/model.py::EvolutionMLIP.__init__`: after `self.vector_norm_layer`, add `self.readout_scalar_update = nn.Sequential(nn.Linear(hidden_dim * 2, hidden_dim), nn.SiLU(), nn.Linear(hidden_dim, hidden_dim))`, `self.readout_scalar_gate = nn.Sequential(nn.Linear(hidden_dim * 2, hidden_dim), nn.SiLU(), nn.Linear(hidden_dim, hidden_dim))`, and `self.readout_norm = nn.LayerNorm(hidden_dim)`; change final `self.readout` first layer to `nn.Linear(hidden_dim, hidden_dim)`.
- `model/model.py::EvolutionMLIP.forward_energy`: after `vector_norm`, compute update/gate from `[scalar_state, vector_norm]`, set `scalar_state = self.readout_norm(scalar_state + sigmoid(gate) * update)`, then call scalar-only `self.readout(scalar_state)`.
- `model/train.py::train`: none.

## minimal_edit_plan
1. Add a readout-local gated scalar update module and LayerNorm.
2. Change readout input width from `2H` to `H` because vector information is folded into scalar_state first.
3. Apply update after all interaction blocks and before per-atom energy summation.

## implementation_checklist
- [ ] Preserve `E = sum_i E_i` and force-from-energy contract.
- [ ] Preserve benchmark metric field names and runnable entrypoint contract.
- [ ] Modify only the allowed target unit files.
- [ ] Do not edit `config.json`; change MLIP knobs in `model/model.py` or `model/train.py`.
- [ ] Keep tensor shapes compatible: update/gate/scalar_state are `[N,H]` and per_atom_energy is `[N]`.
- [ ] Add no unbounded cubic neighbor/triplet loops unless explicitly justified by budget.
- [ ] Do not add a direct-force head or discontinuous top-k neighbor logic.
- [ ] Call `mark_unit_implemented.py --unit <UNIT> --actor implementation_subagent` after edits.

## expected_benchmark_effect
- primary expected gain: Better ISO17 energy/gap calibration from a smoother gated vector-to-scalar path.
- expected tradeoff: More parameters than direct damping; may overfit or underperform in fixed 8 epochs.
- failure signal that would falsify this proposal: Runtime smoke shape failure, source-level RMD17 force lost, or ISO17 energy trend still worsens.

## ablation_or_control
- required control or comparison: Compare to proposals 001/002 to distinguish topology benefit from simple vector damping.
- optional zero-gate / source-fallback / readout-only ablation: Initialize final gate bias negative so it starts near scalar-only fallback.

## implementation_notes_for_subagent
This is a small jump, not a full TorchMD-Net rewrite. Do not alter neighbor construction, edge basis, interaction blocks, or the runnable entrypoint.
