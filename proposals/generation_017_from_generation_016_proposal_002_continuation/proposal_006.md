# Proposal 006: Dual-gated descriptor and scalar residual coupling

- family: painn_dual_body_scalar_gate
- phase: 4
- jump_type: jump
- budget_class: medium
- expected_capability_gain: Combine vector-conditioned body-order descriptor correction with a small scalar-readout gate to test whether coordinated coupling beats isolated residual edits.

## one_sentence_hypothesis
A coupled but damped pair of M01 gates—one correcting the body-order descriptor and one modulating final scalar readout—will improve ISO17 energy/gap if source stagnation comes from mismatch between body-order side energy and main scalar energy.

## mechanism_refs
- GEN017-M01-painn-style-scalar-vector-mixing-gate

## evidence_refs
- mechanism_cards.json::GEN017-M01 supports coupling body-order residual to vector contractions
- mechanism_cards.json::GEN017-M01 risk_or_mismatch warns against merely increasing body-order capacity
- patch_blueprints.json::GEN017-M01 bounded edit and target insertion points
- benchmark_diagnosis.json::generation_016/proposal_002 neutral_variance with ISO17 energy trend worsening
- evidence_provenance.json::paper_artifact:paper_003 and repo_artifact:repo_002 strong evidence rule satisfied

## historical_relation
- source_unit: generation_016/proposal_002
- relation_to_source: jump
- not_a_duplicate_of: Source has a standalone body-order residual; this proposal tests coordinated vector-conditioned gates across the side residual and final scalar update, without adding new tensor contractions.
- lesson_used: Separate body-order capacity can harm energy; coordinated damping may make the side path useful only when scalar/vector state supports it.

## why_not_duplicate
This is not a full body-order hierarchy, not a nonlocal charge residual, and not the single-gate exploit. It is a controlled phase-4 jump with two near-zero gates sharing the same vector contractions.

## benchmark_rationale
- rmd17 energy: Moderate risk due touching scalar readout; mitigated by zero-start scales.
- rmd17 force: Conservative but extra gates may alter gradients.
- rmd17 gap / Q: Success requires not losing the source RMD17 advantage.
- iso17 energy: Expected improvement if mismatched side/main readouts caused energy drift.
- iso17 force: Should remain acceptable if gates stay small and smooth.
- iso17 gap / Q: Target lower energy gap penalty with retained force MAE.
- training stability / runtime risk: Medium; two small MLPs no new edges.
- control comparison expectation: Should be selected only if a higher-risk coordinated coupling axis is desired.

## files_to_edit
- `model/model.py`
- `model/train.py`: none expected
- never `config.json` for MLIP-quality changes

## code_insertion_points
- `model/model.py::EvolutionMLIP.__init__`: add shared vector U/V projections, `body_descriptor_gate`, and `scalar_readout_gate` modules, each with near-zero final scale.
- `model/model.py::EvolutionMLIP.forward_energy`: after interactions compute `norm_v` and `dot_uv`; use them once to correct `body_order_descriptor` and once to add a tiny gate to `scalar_update` or `scalar_state` before final readout.
- `model/train.py::none`: no loss or schedule change.

## minimal_edit_plan
1. Add shared vector contraction projections and helper code to compute M01 invariants.
2. Apply a small descriptor correction before `body_order_readout`.
3. Apply a separate small scalar gate before final `readout`, both initialized as no-ops.

## implementation_checklist
- [ ] Preserve `E = sum_i E_i` and force-from-energy contract.
- [ ] Preserve benchmark metric field names and runnable entrypoint contract.
- [ ] Modify only the allowed target unit files.
- [ ] Do not edit `config.json`; change MLIP knobs in `model/model.py` or `model/train.py`.
- [ ] Keep tensor shapes compatible with current dataloader and model forward.
- [ ] Add no unbounded cubic neighbor/triplet loops unless explicitly justified by budget.
- [ ] Share vector contractions rather than duplicating heavy modules.
- [ ] Keep both gates near no-op at initialization.
- [ ] Call `mark_unit_implemented.py --unit <UNIT> --actor implementation_subagent` after edits.

## expected_benchmark_effect
- primary expected gain: Better ISO17 mixed_energy_mae/gap than single-gate variants if side/main readout mismatch is real.
- expected tradeoff: Higher overfitting and RMD17 regression risk.
- failure signal that would falsify this proposal: Worse RMD17 Q or unstable ISO17 energy trend relative to simpler M01 exploits.

## ablation_or_control
- required control or comparison: Exact source plus at least one single-gate proposal.
- optional zero-gate / source-fallback / readout-only ablation: Zero either gate independently to identify descriptor-vs-scalar contribution.

## implementation_notes_for_subagent
Keep the edit bounded: no new body-order monomials, no new edge message pass, no external dependency, and no training change.
