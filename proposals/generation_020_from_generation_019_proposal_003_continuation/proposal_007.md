# Proposal 007: TP-only source simplification without body-order branch

- family: tp_body_order_simplification
- phase: 3
- jump_type: backward-simplify
- budget_class: tiny
- expected_capability_gain: Determine whether the source's body-order side branch is diluting the successful TP signal and ISO17 transfer.

## one_sentence_hypothesis
Disabling or zeroing the BodyOrderMessageBranch while preserving the calibrated TP path may improve interpretability and possibly Q_total if body-order residuals add variance rather than useful signal.

## mechanism_refs
- []

## evidence_refs
- current_code_profile.json source has TPInteractionBranch and BodyOrderMessageBranch
- benchmark_diagnosis.json generation_019/proposal_003 Q_total=4.026030, G_delta=-0.023958
- generation_019 selection/outcome memory: no child beat parent; body/rank variants did not clearly improve the frontier
- proposal_constraints.json permits diagnosis-driven simplification when not claiming external mechanism evidence

## historical_relation
- source_unit: generation_019/proposal_003
- relation_to_source: simplify
- not_a_duplicate_of: This is not a GEN020-M01 mechanism proposal and not the exact control; it removes or freezes a side branch to test source complexity.
- lesson_used: Recent broader architectural additions were neutral, so backward simplification is needed to locate whether complexity is hurting Q_total.

## why_not_duplicate
The source keeps a BodyOrderMessageBranch and calibrated TP residuals. This proposal intentionally keeps TP scale calibration and removes/zeros only the body-order contribution, making it a diagnostic simplification rather than another new mixer.

## benchmark_rationale
- capacity/scaling hypothesis, if any: Negative capacity change; tests whether simpler TP-only model generalizes better.
- rmd17 energy: May slightly worsen mixed_energy_mae=0.031769 if body-order helped local energy; acceptable only if Q_total or ISO17 improves.
- rmd17 force: Must protect mixed_force_mae=0.060948 because TP branch is the likely force carrier.
- rmd17 gap / Q: Q_rmd17=4.166948 may drop modestly; large drop falsifies simplification.
- iso17 energy: If body-order residual overfits local chemistry, disabling it could improve mixed_energy_mae=0.252341 or other_energy_mae=0.279956.
- iso17 force: Expected neutral/slight negative; monitor mixed_force_mae=0.149767.
- iso17 gap / Q: Success would lower gap_penalty=0.144950 or raise Q_iso17 despite less capacity.
- training stability / runtime risk: Lower runtime and lower complexity; no external mechanism claim.
- control comparison expectation: Compare to exact source control proposal_008; if simplification beats control, future M01 variants should consider body-order pruning.

## files_to_edit
- `model/model.py`
- `model/train.py` none
- never `config.json` for MLIP-quality changes

## code_insertion_points
- `model/model.py::EvolutionMLIP.forward_energy`: set the body-order residual contribution to zero or skip the branch while preserving all TP/BalancedInteractionBlock state updates.
- `model/model.py::EvolutionMLIP.__init__`: optionally keep BodyOrderMessageBranch instantiated for checkpoint compatibility, but gate its contribution to zero.
- `model/train.py`: no change.

## minimal_edit_plan
1. Preserve source TPInteractionBranch, residual scale calibration, readout, atomref, and force-from-energy behavior.
2. Disable the body-order energy/residual contribution with a fixed zero gate or no-op path.
3. Do not add GEN020-M01 mixer or any new mechanism in this simplification.
4. Keep shape compatibility and source fallback by making only the side contribution zero.

## implementation_checklist
- [ ] Preserve `E = sum_i E_i` and force-from-energy contract.
- [ ] Preserve benchmark metric field names and runnable entrypoint contract.
- [ ] Modify only the allowed target unit files.
- [ ] Do not edit `config.json`; change MLIP knobs in `model/model.py` or `model/train.py`.
- [ ] Keep tensor shapes compatible with current dataloader and model forward.
- [ ] Add no new mechanisms, edge loops, training objectives, or direct force heads.
- [ ] Keep simplification reversible and localized.
- [ ] Call `mark_unit_implemented.py --unit <UNIT> --actor implementation_subagent` after edits.

## expected_benchmark_effect
- primary expected gain: Diagnostic clarity; possible ISO17 gap/Q improvement if body-order residual dilutes TP signal.
- expected tradeoff: Reduced capacity may hurt RMD17 or energy precision.
- failure signal that would falsify this proposal: Q_total clearly below source/control with no compensating interpretability lesson.

## ablation_or_control
- required control or comparison: Compare to exact source replicate proposal_008 and all M01 additions.
- optional zero-gate / source-fallback / readout-only ablation: Zero body gate is the ablation; no further control needed.

## implementation_notes_for_subagent
This is diagnosis-driven with `mechanism_refs: []`. Do not cite it as strong external evidence and do not combine it with the PaiNN mixer.
