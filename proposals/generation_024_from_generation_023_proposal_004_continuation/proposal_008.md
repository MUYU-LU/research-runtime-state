# Proposal 008: Exact source replicate control

- family: control_replicate
- phase: 0
- jump_type: control
- budget_class: tiny
- expected_capability_gain: Measure run-to-run variance for generation_023/proposal_004 before interpreting small SOG or objective deltas.

## one_sentence_hypothesis
An exact copy of generation_023/proposal_004 provides the required control baseline for deciding whether generation_024 mechanism deltas exceed benchmark noise.

## mechanism_refs
- []

## evidence_refs
- current source unit: generation_023/proposal_004
- round policy control requirement from research_skill evolution loop
- generation_023_summary.json: source Q_total=4.049140532359024 and exact/control-like outcomes in generation_023 varied substantially
- benchmark_diagnosis.json: source terminal_success with remote_smoke_passed=true and no repair attempts

## historical_relation
- source_unit: generation_023/proposal_004
- relation_to_source: control
- not_a_duplicate_of: It is intentionally an exact duplicate as a control replicate, not a new mechanism proposal.
- lesson_used: generation_023 control replicates and siblings show enough variance/tradeoff that small Q differences need a fresh same-source comparison.

## why_not_duplicate
This is deliberately a duplicate at the code level and should be marked/treated as a control replicate. It is not meant to claim a new mechanism or external-evidence contribution.

## benchmark_rationale
- capacity/scaling hypothesis, if any: none.
- rmd17 energy: expected near source mixed_energy_mae=0.028017578125 within run noise.
- rmd17 force: expected near source mixed_force_mae=0.0603061974274693 within run noise.
- rmd17 gap / Q: expected near source gap_penalty=0.009423666275278415 and Q_rmd17=4.206413224218935.
- iso17 energy: expected near source mixed_energy_mae=0.2679998259591584, subject to seed/training variance.
- iso17 force: expected near source mixed_force_mae=0.14805813421552996.
- iso17 gap / Q: expected near source gap_penalty=0.1531424820304152 and Q_iso17=3.7570626760477586.
- training stability / runtime risk: same as source; no additional risk.
- control comparison expectation: use this to decide whether SOG proposals improve beyond noise and whether source remains competitive with best_known_unit generation_022/proposal_007.

## files_to_edit
- none
- never `config.json` for MLIP-quality changes

## code_insertion_points
- none

## minimal_edit_plan
1. Exact copy of source unit.
2. Do not modify `model/model.py`.
3. Do not modify `model/train.py`.

## implementation_checklist
- [ ] Do not change `model/model.py`.
- [ ] Do not change `model/train.py`.
- [ ] Preserve `E = sum_i E_i` and force-from-energy contract by leaving source code untouched.
- [ ] Preserve benchmark metric field names and runnable entrypoint contract.
- [ ] Do not edit `config.json`.
- [ ] Mark implemented as control replicate if required by workflow.
- [ ] Call `mark_unit_implemented.py --unit <UNIT> --actor implementation_subagent` after materialization/implementation handling.

## expected_benchmark_effect
- primary expected gain: no mechanism gain; provides variance estimate and source baseline.
- expected tradeoff: consumes one run slot but prevents over-interpreting small deltas.
- failure signal that would falsify this proposal: implementation differs from source or fails smoke/launch despite being a copy.

## ablation_or_control
- required control or comparison: this proposal is the required exact source control.
- optional zero-gate / source-fallback / readout-only ablation: not applicable; source code already includes its learned zero-gatable LES tail.

## implementation_notes_for_subagent
If selected/materialized, do not edit either allowed code file. The implementation handoff should mark it as a control replicate and leave proposal_004 code exactly unchanged.
