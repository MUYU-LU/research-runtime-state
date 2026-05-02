# Proposal 002: Scalar-only PaiNN norm/dot feedback

- family: painn_scalar_feedback_ablation
- phase: 4
- jump_type: exploit
- budget_class: tiny
- expected_capability_gain: Isolate whether invariant vector contractions improve scalar energy channels without vector-state feedback risk.

## one_sentence_hypothesis
A scalar-only PaiNN mixer using vector norms and vector-vector dots should target ISO17 energy/gap while avoiding the optimization risk of modifying vector_state.

## mechanism_refs
- GEN020-M01-painn-intra-layer-vector-norm-mixing

## evidence_refs
- repo_artifact:repo_001 `PaiNNMixing.forward` scalar update path `dq_intra + dqmu_intra * <mu_V,mu_W>`
- paper_artifact:paper_001 invariant scalar update from vector norms/products
- mechanism_cards.json ablation note: disable vector_delta to test whether energy gains require vector-state feedback
- benchmark_diagnosis.json ISO17 mixed_energy_mae=0.252341, gap_penalty=0.144950

## historical_relation
- source_unit: generation_019/proposal_003
- relation_to_source: exploit
- not_a_duplicate_of: Unlike proposal_001, this deliberately sets `alpha_v=0` and changes only scalar_state; unlike source proposal_003, it adds norm/dot information rather than only recalibrating existing TP scales.
- lesson_used: RMD17 force is already strong, so the first low-risk exploit should protect vector dynamics and test scalar energy transfer directly.

## why_not_duplicate
This is the scalar-path ablation requested by the evidence card, not a separate mechanism family. It shares the GEN020-M01 contraction code but forbids vector residual updates so selection can interpret gains or failures cleanly.

## benchmark_rationale
- capacity/scaling hypothesis, if any: No capacity scaling beyond a small scalar MLP on `[scalar_state, vector_norm]`.
- rmd17 energy: Mixed_energy_mae=0.031769 should remain stable because vector_state and message geometry are unchanged.
- rmd17 force: Mixed_force_mae=0.060948 should have lower regression risk than full mixer because `vector_state` is untouched.
- rmd17 gap / Q: Preserve gap_penalty=0.010551 and Q_rmd17=4.166948; any RMD17 drop suggests scalar feedback is destabilizing.
- iso17 energy: Main target is mixed_energy_mae=0.252341 and other_energy_mae=0.279956 by adding invariant vector geometry to scalar channels.
- iso17 force: Expected neutral; force-only gains are secondary unless energy/gap also improve.
- iso17 gap / Q: Target Q_iso17=3.764325 and gap_penalty=0.144950; success requires gap-neutral or gap-positive behavior.
- training stability / runtime risk: Tiny overhead; lower risk than full mixer because vector residual branch is disabled.
- control comparison expectation: Compare against proposal_001 to decide whether vector-state feedback is needed and against source/control Q_total around 4.026/4.023.

## files_to_edit
- `model/model.py`
- `model/train.py` none
- never `config.json` for MLIP-quality changes

## code_insertion_points
- `model/model.py::TPInvariantPaiNNMixing`: implement only scalar outputs from norm and dot; keep vector output gate fixed at zero or omit vector_delta.
- `model/model.py::EvolutionMLIP.__init__`: add per-layer scalar-only mixers initialized to source fallback.
- `model/model.py::EvolutionMLIP.forward_energy`: update `scalar_state` after TP merge; pass `vector_state` through unchanged.
- `model/train.py`: no change.

## minimal_edit_plan
1. Reuse the GEN020-M01 vector projections and invariant contractions.
2. Produce `scalar_delta = alpha_s * (a_ss + a_sv * vector_dot)` with `alpha_s <= 0.05` and zero-initialized final outputs.
3. Return `(scalar_state + scalar_delta, vector_state)` exactly.
4. Add assertions or comments documenting `alpha_v=0` source-recoverable ablation behavior.

## implementation_checklist
- [ ] Preserve `E = sum_i E_i` and force-from-energy contract.
- [ ] Preserve benchmark metric field names and runnable entrypoint contract.
- [ ] Modify only the allowed target unit files.
- [ ] Do not edit `config.json`; change MLIP knobs in `model/model.py` or `model/train.py`.
- [ ] Keep tensor shapes compatible with current dataloader and model forward.
- [ ] Add no new edge, triplet, direct-force, or vector-state residual path.
- [ ] Keep `vector_state` bitwise-equivalent aside from existing source computations when scalar gate is zero.
- [ ] Call `mark_unit_implemented.py --unit <UNIT> --actor implementation_subagent` after edits.

## expected_benchmark_effect
- primary expected gain: ISO17 energy/gap improvement with minimal RMD17 force risk.
- expected tradeoff: Smaller upside than full mixer because vector feedback cannot improve later vector messages.
- failure signal that would falsify this proposal: No ISO17 energy/gap improvement versus source, or any significant RMD17 force/energy regression despite the scalar-only scope.

## ablation_or_control
- required control or comparison: Zero scalar gate must exactly recover source.
- optional zero-gate / source-fallback / readout-only ablation: Compare to full mixer proposal_001 and late-layer-only proposal_003.

## implementation_notes_for_subagent
Keep this as a clean ablation. Do not add vector_delta, training objective changes, readout changes, or capacity scaling.
