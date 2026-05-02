# Proposal 003: Late-layer PaiNN mixer only

- family: painn_late_layer_mixing
- phase: 4
- jump_type: exploit
- budget_class: tiny
- expected_capability_gain: Add vector-norm scalar feedback only where it can affect final energy with minimal disruption to early message passing.

## one_sentence_hypothesis
Applying GEN020-M01 only after the final interaction block should improve ISO17 scalar energy calibration while preserving the source unit's learned early TP dynamics.

## mechanism_refs
- GEN020-M01-painn-intra-layer-vector-norm-mixing

## evidence_refs
- mechanism_cards.json GEN020-M01 data_flow and ablation/control guidance
- repo_artifact:repo_001 `PaiNNMixing.forward` norm/dot contractions
- current_code_profile.json source insertion point after TP residual merge
- benchmark_diagnosis.json RMD17 mixed_force_mae=0.060948 and ISO17 gap_penalty=0.144950

## historical_relation
- source_unit: generation_019/proposal_003
- relation_to_source: exploit
- not_a_duplicate_of: Unlike proposal_001, this does not place a mixer after every layer; unlike proposal_002, it may include both scalar and vector residuals but only in the last layer.
- lesson_used: When recent generations added broader body-order/rank-2 changes, gains were neutral; a late-only source-recoverable probe tests whether placement, not mechanism size, is the bottleneck.

## why_not_duplicate
This is a placement ablation of the strong mechanism. It answers whether the current model only needs a final invariant correction, not a recurrent per-layer feedback path.

## benchmark_rationale
- capacity/scaling hypothesis, if any: No scaling; fewer parameters than proposal_001.
- rmd17 energy: Should preserve mixed_energy_mae=0.031769 because early message passing is untouched and final residual is zero-start.
- rmd17 force: Should preserve mixed_force_mae=0.060948 better than full-stack mixing.
- rmd17 gap / Q: Q_rmd17=4.166948 should remain stable; late residual must not inflate gap_penalty=0.010551.
- iso17 energy: Targets mixed_energy_mae=0.252341 through final scalar correction informed by vector norms/dots.
- iso17 force: Expected neutral-to-slightly-positive if final scalar surface smooths; no direct force head.
- iso17 gap / Q: A useful result lowers gap_penalty=0.144950 or improves Q_iso17=3.764325 without RMD17 loss.
- training stability / runtime risk: Lowest M01 runtime/optimization risk; if this fails while proposal_001 succeeds, recurrent feedback is needed.
- control comparison expectation: Source/control Q_total around 4.026/4.023 is the neutral baseline; parent Q_total=4.049988 remains the aspirational threshold.

## files_to_edit
- `model/model.py`
- `model/train.py` none
- never `config.json` for MLIP-quality changes

## code_insertion_points
- `model/model.py::TPInvariantPaiNNMixing`: same bounded mixer primitive as GEN020-M01.
- `model/model.py::EvolutionMLIP.__init__`: instantiate one mixer or a ModuleList with identity/no-op entries except the last layer.
- `model/model.py::EvolutionMLIP.forward_energy`: call the mixer only when `layer_idx == num_interactions - 1` after the TP merge.
- `model/train.py`: no change.

## minimal_edit_plan
1. Add the bounded mixer class with source-fallback initialization.
2. Wire it only to the final interaction-layer merge.
3. Keep alpha caps <=0.05; optionally set vector alpha lower than scalar alpha.
4. Do not alter earlier interaction blocks, BodyOrderMessageBranch, or readout.

## implementation_checklist
- [ ] Preserve `E = sum_i E_i` and force-from-energy contract.
- [ ] Preserve benchmark metric field names and runnable entrypoint contract.
- [ ] Modify only the allowed target unit files.
- [ ] Do not edit `config.json`; change MLIP knobs in `model/model.py` or `model/train.py`.
- [ ] Keep tensor shapes compatible with current dataloader and model forward.
- [ ] Add no new edge/triplet loops and no direct force head.
- [ ] Ensure non-final layers are exact source behavior.
- [ ] Call `mark_unit_implemented.py --unit <UNIT> --actor implementation_subagent` after edits.

## expected_benchmark_effect
- primary expected gain: Smaller but cleaner ISO17 energy/gap lift with almost no RMD17 regression.
- expected tradeoff: May underperform full per-layer mixing if later message passes must consume vector-conditioned scalar features.
- failure signal that would falsify this proposal: No Q_iso17/Q_total gain or any RMD17 degradation, implying the final correction is insufficient or harmful.

## ablation_or_control
- required control or comparison: Zero final mixer recovers source.
- optional zero-gate / source-fallback / readout-only ablation: Interpret beside proposal_001 to separate placement from mechanism.

## implementation_notes_for_subagent
Prefer the simplest possible last-layer-only wiring. Avoid hidden changes to all layers via loops unless explicitly guarded by layer index.
