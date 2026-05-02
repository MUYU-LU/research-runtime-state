# Proposal 005: Explicit scalar-vector tensor-product interaction sibling

- family: low_rank_tensor_product_interaction
- phase: 4
- jump_type: jump
- budget_class: medium
- expected_capability_gain: add NequIP-inspired l=0/l=1 radial-weighted tensor-product message terms as a new geometric information-flow axis.

## one_sentence_hypothesis
An additive low-rank tensor-product branch using scalar state, vector state, edge unit vectors, and radial weights should improve geometry-sensitive energy/force coupling beyond the current hand-coded dot/unit updates.

## mechanism_refs
- G018-MECH-003

## evidence_refs
- paper_artifact:paper_003
- repo_artifact:repo_003
- mechanism_cards.json:G018-MECH-003.repo_code_trace
- patch_blueprints.json:G018-MECH-003
- generation_017 outcome report: PaiNN-like gate changes did not beat the parent; this implements explicit tensor-product couplings instead of more norm/dot gating.

## historical_relation
- source_unit: generation_016/proposal_002
- relation_to_source: jump
- not_a_duplicate_of: generation_017/proposal_003/proposal_004/proposal_005 because those were PaiNN-style scalar multipliers/mixing; this adds radial-weighted tensor-product terms with separate scalar and vector deltas.
- lesson_used: use explicit structured l=0/l=1 couplings and small residual scale to avoid repeating local gate tradeoffs.

## benchmark_rationale
- rmd17 energy: explicit scalar-vector tensor products may refine local geometry energy, especially angular response.
- rmd17 force: branch directly updates vector state and is differentiable through unit vectors already used by the parent; preserve clamps/normalization.
- rmd17 gap / Q: potential moderate positive if structured coupling generalizes better than unconstrained gates.
- iso17 energy: better geometric information flow may reduce conformer energy errors without needing dataset-specific changes.
- iso17 force: may improve force consistency if vector updates carry radial-conditioned geometric terms; risk is over-amplifying vector messages.
- iso17 gap / Q: expected gain only if energy improves without destabilizing forces.
- training stability / runtime risk: O(E*H) extra operations comparable to current interaction block; initialize branch scale near zero.
- control comparison expectation: should outperform control if both energy and force improve, not merely one dataset component.

## files_to_edit
- `model/model.py`
- `model/train.py` none
- never `config.json` for MLIP-quality changes

## code_insertion_points
- `model/model.py::TPInteractionBranch`: add a branch class near `BalancedInteractionBlock` with radial MLP weights for scalar->scalar, vector-dot->scalar, scalar*unit->vector, vector_parallel, and vector_self terms.
- `model/model.py::EvolutionMLIP.__init__`: add `self.tp_branches = nn.ModuleList([...])` parallel to `self.interactions`, with residual scale logits near -5.
- `model/model.py::EvolutionMLIP.forward_energy`: in the existing interaction loop, call both the current interaction and TP branch, then residual-add `delta_scalar` and `delta_vector`.
- `model/model.py::BalancedInteractionBlock.forward`: leave existing block mostly unchanged unless helper reuse is needed.
- `model/train.py`: no change; forces remain autograd from energy.

## minimal_edit_plan
1. Implement `TPInteractionBranch.forward(scalar_state, vector_state, edge_src, edge_dst, edge_unit, edge_basis)` producing `[N,H]` and `[N,H,3]` deltas via scatter-add.
2. Use radial MLP outputs shaped `[E,5,H]` for the five bounded l=0/l=1 couplings described by G018-MECH-003.
3. Normalize scatter outputs by neighbor count as the current interaction does; apply LayerNorm/gate and near-zero residual scale.
4. Keep hidden_dim, num_interactions, cutoff, RBF, readout, losses, and benchmark entrypoints unchanged.

## implementation_checklist
- [ ] Preserve `E = sum_i E_i` and force-from-energy contract.
- [ ] Preserve benchmark metric field names and runnable entrypoint contract.
- [ ] Modify only the allowed target unit files.
- [ ] Do not edit `config.json`; change MLIP knobs in `model/model.py` or `model/train.py`.
- [ ] Keep tensor shapes compatible with current dataloader and model forward.
- [ ] Add no unbounded cubic neighbor/triplet loops unless explicitly justified by budget.
- [ ] Do not add e3nn/NequIP dependencies; implement l=0/l=1 PyTorch terms only.
- [ ] Call `mark_unit_implemented.py --unit <UNIT> --actor implementation_subagent` after edits.

## expected_benchmark_effect
- primary expected gain: local geometric coupling improves energy and force together, especially RMD17 force and ISO17 energy/force balance.
- expected tradeoff: extra vector updates can destabilize force gradients if residual scale is too large.
- failure signal that would falsify this proposal: force MAE worsens on both datasets or Q gains are absent despite higher runtime.

## ablation_or_control
- required control or comparison: source replicate and generation_017 PaiNN-mixing tradeoff units.
- optional zero-gate / source-fallback / readout-only ablation: disable vector-vector term while keeping scalar*unit; zero TP residual scale should recover source.

## implementation_notes_for_subagent
Make this branch visibly different from a gate tweak: compute radial-weighted tensor-product terms and scatter them. Keep it additive and bounded; do not rewrite the full interaction stack.
