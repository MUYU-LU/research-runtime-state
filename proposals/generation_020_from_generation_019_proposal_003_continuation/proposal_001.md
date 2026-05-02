# Proposal 001: Full bounded intra-layer PaiNN TP mixer

- family: painn_tp_intralayer_mixing
- phase: 5
- jump_type: exploit
- budget_class: small
- expected_capability_gain: Let TP vector geometry influence later scalar messages while remaining source-recoverable.

## one_sentence_hypothesis
Adding a zero-initialized PaiNN-style norm/dot mixer after every existing TP residual merge will lower ISO17 energy/gap error without sacrificing the source unit's RMD17 force quality.

## mechanism_refs
- GEN020-M01-painn-intra-layer-vector-norm-mixing

## evidence_refs
- paper_artifact:paper_001 equations 9-10 PaiNN scalar/vector mixing derivation
- repo_artifact:repo_001 `src/schnetpack/representation/painn.py::PaiNNMixing.forward`
- evidence_quality.json grade A, strong_card_target_met=true
- patch_blueprints.json blueprint GEN020-M01-painn-intra-layer-vector-norm-mixing
- benchmark_diagnosis.json source metrics Q_total=4.026030, Q_rmd17=4.166948, Q_iso17=3.764325

## historical_relation
- source_unit: generation_019/proposal_003
- relation_to_source: exploit
- not_a_duplicate_of: generation_019/proposal_003 only calibrated TP residual scale logits; this changes the information path by feeding vector norms and vector-vector dots back into scalar_state before later message passes.
- lesson_used: generation_019 produced neutral variance rather than a parent-beating child, so the new path must be source-recoverable and bounded rather than a broad rewrite.

## why_not_duplicate
This is not another rank-2 TP, CACE, body-order, or residual-scale proposal. It keeps BalancedInteractionBlock, TPInteractionBranch, BodyOrderMessageBranch, readout, neighbor lists, and force-from-energy semantics unchanged, and adds only the evidence-backed atomwise PaiNNMixing block at the specified insertion point.

## benchmark_rationale
- capacity/scaling hypothesis, if any: No width/depth scaling; test mechanism before capacity.
- rmd17 energy: Preserve mixed_energy_mae=0.031769 and gap_penalty=0.010551 by zero-initializing final mixer outputs or residual logits <= -6.
- rmd17 force: Preserve mixed_force_mae=0.060948; any regression without Q_total gain falsifies the exploit.
- rmd17 gap / Q: Q_rmd17=4.166948 should remain within the control/source envelope because scalar outputs use invariant contractions only.
- iso17 energy: Primary target is mixed_energy_mae=0.252341 and within/other split 0.210919/0.279956; vector information enters scalar messages earlier than the current late readout.
- iso17 force: Expected neutral-to-slightly-positive effect through a smoother energy surface; force-only improvement with worse energy/gap is not success.
- iso17 gap / Q: Primary target is gap_penalty=0.144950 and Q_iso17=3.764325; useful result should lift Q_iso17 and Q_total beyond source/control variance.
- training stability / runtime risk: O(N*H^2)+O(N*H) per layer, no new edge/triplet loops; main risk is optimization from scalar feedback, bounded by alpha_s/alpha_v <= 0.05 and zero init.
- control comparison expectation: Compare to generation_019/proposal_003 Q_total=4.026030, generation_019/proposal_008 control Q_total=4.023487, and parent generation_018/proposal_005 Q_total=4.049988.

## files_to_edit
- `model/model.py`
- `model/train.py` none
- never `config.json` for MLIP-quality changes

## code_insertion_points
- `model/model.py::new class TPInvariantPaiNNMixing`: implement bias-free channel projections for `mu_V` and `mu_W`, norm `[N,H]`, dot `[N,H]`, scalar delta, dot-gated scalar delta, and scalar-gated vector delta.
- `model/model.py::EvolutionMLIP.__init__`: add `self.tp_invariant_mixers = nn.ModuleList([... for _ in range(num_interactions)])` with zero-initialized final layers or logits <= -6.
- `model/model.py::EvolutionMLIP.forward_energy`: after `scalar_state = next_scalar_state + scalar_scale * delta_scalar` and `vector_state = next_vector_state + vector_scale * delta_vector`, call the matching mixer.
- `model/train.py`: no change.

## minimal_edit_plan
1. Add `TPInvariantPaiNNMixing(hidden_dim)` using the current `[N,H,3]` vector layout and dim=-1 spatial contractions.
2. Generate `mu_V`, `mu_W`, `vector_norm`, and `vector_dot`; feed `cat([scalar_state, vector_norm], dim=-1)` to an MLP producing bounded scalar, dot, and vector gates.
3. Add scalar and vector residuals with caps <=0.05, initialized to exact or near-exact source behavior.
4. Insert one mixer after each TP residual merge and leave all benchmark/eval/data semantics unchanged.

## implementation_checklist
- [ ] Preserve `E = sum_i E_i` and force-from-energy contract.
- [ ] Preserve benchmark metric field names and runnable entrypoint contract.
- [ ] Modify only the allowed target unit files.
- [ ] Do not edit `config.json`; change MLIP knobs in `model/model.py` or `model/train.py`.
- [ ] Keep tensor shapes compatible with scalar_state `[N,H]`, vector_state `[N,H,3]`, and current dataloader.
- [ ] Add no unbounded cubic neighbor/triplet loops.
- [ ] Initialize new residual path so source behavior is recoverable.
- [ ] Call `mark_unit_implemented.py --unit <UNIT> --actor implementation_subagent` after edits.

## expected_benchmark_effect
- primary expected gain: Lower ISO17 mixed_energy_mae/gap_penalty and raise Q_iso17/Q_total by letting TP vector geometry condition scalar updates before later layers.
- expected tradeoff: Small runtime and optimization risk; RMD17 gains are not expected, preservation is the key.
- failure signal that would falsify this proposal: Q_total below source/control envelope, RMD17 mixed_force_mae or mixed_energy_mae regression, ISO17 gap worsening, or any loss of conservative forces.

## ablation_or_control
- required control or comparison: Very-negative residual logits or zero final mixer weights must reproduce generation_019/proposal_003.
- optional zero-gate / source-fallback / readout-only ablation: Logically separable scalar-only and vector-delta-disabled variants are covered by proposals 002 and 003.

## implementation_notes_for_subagent
Implement only the evidence-backed atomwise mixer. Do not port PaiNNInteraction, do not add new neighbor geometry, do not change config/evaluator/metrics, and do not stack unrelated rank-2/body-order changes into this exploit.
