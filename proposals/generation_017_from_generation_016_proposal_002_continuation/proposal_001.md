# Proposal 001: Full PaiNN-style vector-conditioned body-order gate

- family: painn_body_order_gate
- phase: 3
- jump_type: exploit
- budget_class: small
- expected_capability_gain: Improve ISO17 energy/gap by letting the existing body-order residual see post-interaction vector invariants without increasing body-order tensor capacity.

## one_sentence_hypothesis
A near-zero-initialized descriptor correction from PaiNN-style vector norm and vector-dot contractions will stabilize the source body-order residual's ISO17 energy behavior while preserving RMD17 force quality.

## mechanism_refs
- GEN017-M01-painn-style-scalar-vector-mixing-gate

## evidence_refs
- evidence_quality.json::grade=A usable_for_proposal=true usable_for_implementation=true
- evidence_provenance.json::paper_artifact:paper_003 PaiNN PDF strong-capable source
- evidence_provenance.json::repo_artifact:repo_002 SchNetPack strong-capable repo source
- mechanism_cards.json::GEN017-M01-painn-style-scalar-vector-mixing-gate
- patch_blueprints.json::GEN017-M01-painn-style-scalar-vector-mixing-gate
- benchmark_diagnosis.json::generation_016/proposal_002 Q_total=3.9425481167873127, rmd17 Q=4.127178951686343, iso17 Q=3.599662280546256

## historical_relation
- source_unit: generation_016/proposal_002
- relation_to_source: exploit
- not_a_duplicate_of: generation_016/proposal_002 added a body-order descriptor message branch but read it out in isolation; this adds no new body-order hierarchy and only conditions that descriptor on existing learned vector-state contractions.
- lesson_used: generation_016/proposal_002 was neutral-positive overall but ISO17 validation energy worsened late, so the next exploit should couple the residual to directional context rather than increase branch size.

## why_not_duplicate
This is not another CACE/CAMP body-order expansion, not the generation_016 static branch, and not the generation_016 one-step descriptor message itself. It adds a small PaiNNMixing-derived `Uv/Vv -> norm,dot -> descriptor correction` between the existing interaction stack and `body_order_readout`.

## benchmark_rationale
- rmd17 energy: Should stay close to source because the correction starts near zero and the existing atomref/readout path is unchanged.
- rmd17 force: Small risk from extra differentiable curvature; no direct force head or new neighbor loop is introduced.
- rmd17 gap / Q: Expected neutral to slight positive if the correction does not disturb the strong source RMD17 Q.
- iso17 energy: Primary target; vector-conditioned body-order readout may reduce mixed_energy_mae and late validation energy drift.
- iso17 force: Expected mostly preserved; the residual remains damped through scalar energy.
- iso17 gap / Q: Expected improvement if isolated body-order residual was under-conditioned for conformer transfer.
- training stability / runtime risk: Low-medium; adds O(N * hidden_dim * descriptor_dim) MLP work only.
- control comparison expectation: Should beat exact source control only if vector contractions matter beyond run variance.

## files_to_edit
- `model/model.py`
- `model/train.py`: none expected
- never `config.json` for MLIP-quality changes

## code_insertion_points
- `model/model.py::EvolutionMLIP.__init__`: after `body_order_readout` / `body_order_scale`, add `body_vector_u`, `body_vector_v`, a small `body_vector_gate` MLP from `[descriptor, norm_v, dot_uv]` to descriptor_dim, and a near-zero scale/final layer.
- `model/model.py::EvolutionMLIP.forward_energy`: after the interaction loop and before `body_order_residual = self.body_order_readout(body_order_descriptor)`, compute `u = Linear(vector_state.transpose(1,2)).transpose(1,2)`, `v` similarly, `norm_v = sqrt(sum(v*v, dim=-1)+eps)`, `dot_uv = sum(u*v, dim=-1)`, and add a small gated descriptor correction.
- `model/train.py::none`: keep `TRAIN_ENERGY_WEIGHT`, `TRAIN_FORCE_WEIGHT`, optimizer, and warmup unchanged.

## minimal_edit_plan
1. Add two channel-mixing `nn.Linear(hidden_dim, hidden_dim)` modules usable by transposing `vector_state` to `[N,3,H]` and back.
2. Add a descriptor correction MLP with input size `descriptor_dim + 2 * hidden_dim` and output size `descriptor_dim`; initialize its final layer to zero or multiply by a learned scale initialized around `-5`.
3. In `forward_energy`, form invariant `norm_v` and `dot_uv`, correct `body_order_descriptor`, then pass the corrected descriptor through the existing `body_order_readout` and multiplier.

## implementation_checklist
- [ ] Preserve `E = sum_i E_i` and force-from-energy contract.
- [ ] Preserve benchmark metric field names and runnable entrypoint contract.
- [ ] Modify only the allowed target unit files.
- [ ] Do not edit `config.json`; change MLIP knobs in `model/model.py` or `model/train.py`.
- [ ] Keep tensor shapes compatible with current dataloader and model forward.
- [ ] Add no unbounded cubic neighbor/triplet loops unless explicitly justified by budget.
- [ ] Keep cutoff, RBF, atomref, source interactions, and loss weights unchanged.
- [ ] Initialize the new correction as a near no-op so source behavior is recoverable.
- [ ] Call `mark_unit_implemented.py --unit <UNIT> --actor implementation_subagent` after edits.

## expected_benchmark_effect
- primary expected gain: Lower ISO17 mixed_energy_mae/gap without sacrificing the source's RMD17 Q.
- expected tradeoff: Slight runtime and force-curvature risk from the new residual conditioning.
- failure signal that would falsify this proposal: ISO17 energy remains worsening or RMD17 mixed_force_mae regresses while exact control remains stable.

## ablation_or_control
- required control or comparison: Compare against exact generation_016/proposal_002 control.
- optional zero-gate / source-fallback / readout-only ablation: Set correction scale to zero to reproduce source body-order descriptor readout.

## implementation_notes_for_subagent
Use only scalar contractions of vector features (`norm_v`, `dot_uv`) in the energy path. Do not port PaiNN, do not alter `BalancedInteractionBlock`, and do not increase `BodyOrderMessageBranch` descriptor dimension.
