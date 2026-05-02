# Proposal 010: Readout-only invariant norm/dot adapter

- family: invariant_readout_adapter_wildcard
- phase: 4
- jump_type: wildcard
- budget_class: tiny
- expected_capability_gain: Test whether the useful part of PaiNN-style vector contractions can be expressed as a final energy adapter without recurrent state feedback.

## one_sentence_hypothesis
A zero-start final readout adapter using invariant vector norms/dots may improve ISO17 energy/gap with less disruption than inserting mixers into every message-passing layer.

## mechanism_refs
- []

## evidence_refs
- current_code_profile.json source has vector_state `[N,H,3]` and late readout vector-norm information but no pre-readout feedback
- mechanism_cards.json GEN020-M01 explains why recurrent feedback is stronger; this proposal is a diagnosis-only readout ablation, not a strong-mechanism claim
- benchmark_diagnosis.json ISO17 mixed_energy_mae=0.252341, gap_penalty=0.144950
- proposal_constraints.json blocked mechanism rule: this proposal does not claim external strong evidence without the full patch blueprint

## historical_relation
- source_unit: generation_019/proposal_003
- relation_to_source: ablation
- not_a_duplicate_of: Unlike proposals 001-004, it does not feed vector contractions back into scalar_state before subsequent messages; unlike control, it adds a final zero-start scalar energy adapter.
- lesson_used: Evidence says the current late vector norm does not feed into later messages; this wildcard tests whether readout-only contraction is enough before committing to recurrent mixing.

## why_not_duplicate
This is deliberately a weaker, diagnosis-driven wildcard. It should not be selected as the main M01 implementation if strong mechanism coverage is limited, but it can isolate whether final invariant correction alone explains the expected benefit.

## benchmark_rationale
- capacity/scaling hypothesis, if any: Tiny final adapter only; no message-passing capacity increase.
- rmd17 energy: Zero-start adapter should preserve mixed_energy_mae=0.031769 unless final energy correction overfits.
- rmd17 force: Forces still come from energy; monitor mixed_force_mae=0.060948 because final adapter changes the energy surface.
- rmd17 gap / Q: Preserve Q_rmd17=4.166948 and gap_penalty=0.010551.
- iso17 energy: Target mixed_energy_mae=0.252341 by adding final invariant vector contraction features to per-atom energy.
- iso17 force: Expected neutral; no vector-state feedback means limited force upside.
- iso17 gap / Q: Useful if gap_penalty=0.144950 falls or Q_iso17=3.764325 rises without RMD17 loss.
- training stability / runtime risk: Very low runtime; weaker mechanism support because it omits the evidence-backed intra-layer feedback.
- control comparison expectation: If this matches M01 proposals, recurrent feedback may be unnecessary; if it fails, full intra-layer mixing is justified.

## files_to_edit
- `model/model.py`
- `model/train.py` none
- never `config.json` for MLIP-quality changes

## code_insertion_points
- `model/model.py::EvolutionMLIP.__init__`: add a small final invariant readout adapter MLP with zero-initialized output.
- `model/model.py::EvolutionMLIP.forward_energy`: after message passing and before/alongside per-atom energy readout, compute vector norms/dots from final `vector_state` and add a bounded scalar per-atom residual.
- `model/train.py`: no change.

## minimal_edit_plan
1. Keep all interaction blocks and TP residual calibration unchanged.
2. Compute final invariant features such as `sqrt(sum(vector_state**2, dim=-1)+eps)` and optionally a learned bias-free dot projection.
3. Feed final scalar_state plus invariant features into a tiny adapter capped <=0.03-0.05 and zero-initialized.
4. Add its scalar output to per-atom energy only; do not alter vector_state or force computation.

## implementation_checklist
- [ ] Preserve `E = sum_i E_i` and force-from-energy contract.
- [ ] Preserve benchmark metric field names and runnable entrypoint contract.
- [ ] Modify only the allowed target unit files.
- [ ] Do not edit `config.json`; change MLIP knobs in `model/model.py` or `model/train.py`.
- [ ] Keep tensor shapes compatible with current dataloader and model forward.
- [ ] Add no new message-passing, edge loops, triplets, or direct force heads.
- [ ] Make the adapter zero-start and removable to recover source.
- [ ] Call `mark_unit_implemented.py --unit <UNIT> --actor implementation_subagent` after edits.

## expected_benchmark_effect
- primary expected gain: Low-risk ISO17 energy/gap improvement if final invariant correction is sufficient.
- expected tradeoff: Weaker than GEN020-M01 because vector information does not affect later scalar messages; may be too late to improve forces.
- failure signal that would falsify this proposal: No Q_iso17/Q_total gain versus control, or RMD17 degradation from final energy overfit.

## ablation_or_control
- required control or comparison: Exact control proposal_008 and intra-layer M01 proposals 001-004.
- optional zero-gate / source-fallback / readout-only ablation: Zero adapter recovers source; this proposal itself is the readout-only ablation.

## implementation_notes_for_subagent
Do not cite this as strong external evidence. It is a wildcard to probe whether M01's invariant contraction idea helps only at readout, while preserving benchmark semantics.
