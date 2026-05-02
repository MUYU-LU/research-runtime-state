# Proposal 003: Vector-conditioned residual multiplier for body-order energy

- family: painn_scalar_multiplier
- phase: 3
- jump_type: exploit
- budget_class: tiny
- expected_capability_gain: Test whether vector context should modulate the amplitude of the body-order residual rather than rewrite its descriptor features.

## one_sentence_hypothesis
A per-atom PaiNN-style invariant multiplier on the existing body-order residual will reduce ISO17 energy drift with less descriptor-capacity risk than adding a full descriptor correction.

## mechanism_refs
- GEN017-M01-painn-style-scalar-vector-mixing-gate

## evidence_refs
- mechanism_cards.json::GEN017-M01 mathematical_form scalar update depends on `||Vv_i||` and `<Uv_i,Vv_i>`
- patch_blueprints.json::GEN017-M01 bounded edit says keep residual damped and source-close
- evidence_provenance.json::paper_artifact:paper_003 and repo_artifact:repo_002 strong-capable support
- benchmark_diagnosis.json::generation_016/proposal_002 source has strong RMD17 Q but ISO17 energy trend worsening

## historical_relation
- source_unit: generation_016/proposal_002
- relation_to_source: exploit
- not_a_duplicate_of: Source uses a global learned `body_order_multiplier`; this proposal keeps the descriptor fixed and replaces/augments only that multiplier with a vector-conditioned per-atom gate.
- lesson_used: generation_016 body-order expansion risked energy instability; amplitude modulation is a smaller intervention than additional descriptor capacity.

## why_not_duplicate
This is not proposal_001's descriptor correction and not proposal_002's norm-only descriptor correction. The body-order descriptor and readout remain unchanged; the only new behavior is a bounded per-atom residual amplitude gate from vector contractions.

## benchmark_rationale
- rmd17 energy: Very likely stable because the body-order readout shape and source interactions are unchanged.
- rmd17 force: Lower risk than descriptor correction; multiplier is smooth and scalar.
- rmd17 gap / Q: Expected neutral.
- iso17 energy: May improve by suppressing harmful body-order residuals for conformers where vector state indicates poor fit.
- iso17 force: Should not degrade much if multiplier scale is near one/no-op initially.
- iso17 gap / Q: Gain depends on reducing gap penalty without lowering force quality.
- training stability / runtime risk: Tiny overhead; low shape risk.
- control comparison expectation: Should be a low-risk exploit that clarifies whether vector context helps via scale rather than content.

## files_to_edit
- `model/model.py`
- `model/train.py`: none expected
- never `config.json` for MLIP-quality changes

## code_insertion_points
- `model/model.py::EvolutionMLIP.__init__`: add `body_residual_u`, `body_residual_v`, and `body_residual_gate = nn.Sequential(nn.Linear(2*hidden_dim, hidden_dim//2), nn.SiLU(), nn.Linear(hidden_dim//2, 1))`; initialize final layer/bias to make gate initially near 1.0 or near a no-op multiplier.
- `model/model.py::EvolutionMLIP.forward_energy`: after `body_order_residual = self.body_order_readout(body_order_descriptor).squeeze(-1)`, compute vector contractions and `per_atom_gate = 1 + small_scale * tanh(gate([norm_v,dot_uv]))`; multiply `body_order_residual` before summing.
- `model/train.py::none`: no training change.

## minimal_edit_plan
1. Add two vector projections and a one-output gate MLP.
2. Compute `norm_v` and `dot_uv` after interactions using only scalar contractions.
3. Multiply the existing `body_order_residual` by a near-no-op per-atom gate, then apply the existing `body_order_multiplier` and sum.

## implementation_checklist
- [ ] Preserve `E = sum_i E_i` and force-from-energy contract.
- [ ] Preserve benchmark metric field names and runnable entrypoint contract.
- [ ] Modify only the allowed target unit files.
- [ ] Do not edit `config.json`; change MLIP knobs in `model/model.py` or `model/train.py`.
- [ ] Keep tensor shapes compatible with current dataloader and model forward.
- [ ] Add no unbounded cubic neighbor/triplet loops unless explicitly justified by budget.
- [ ] Keep the initial residual multiplier source-close.
- [ ] Do not modify `BodyOrderMessageBranch` internals.
- [ ] Call `mark_unit_implemented.py --unit <UNIT> --actor implementation_subagent` after edits.

## expected_benchmark_effect
- primary expected gain: Better ISO17 energy/gap by reducing harmful body-order residual amplitude on difficult conformers.
- expected tradeoff: May be too weak if the descriptor itself needs vector-conditioned features.
- failure signal that would falsify this proposal: Gate saturates or ISO17 energy/gap does not improve against exact control.

## ablation_or_control
- required control or comparison: Exact source control.
- optional zero-gate / source-fallback / readout-only ablation: Fix `per_atom_gate = 1` to recover source.

## implementation_notes_for_subagent
Do not change descriptor dimensions or readout MLP. The only allowed model change is vector-contraction computation and the per-atom multiplier around the existing body-order residual.
