# Proposal 008: Exact source control replicate

- family: source_control_replicate
- phase: 3
- jump_type: control
- budget_class: tiny
- expected_capability_gain: Provide a variance anchor for generation_017 against generation_016/proposal_002's terminal-success metrics.

## one_sentence_hypothesis
An exact copy of generation_016/proposal_002 is required to separate real M01 gains from run variance in a source whose G_delta was only +0.024853 within the neutral margin.

## mechanism_refs
- []

## evidence_refs
- current source unit: generation_016/proposal_002
- benchmark_diagnosis.json::unit_Q_total=3.9425481167873127 and unit_G_delta=0.02485300089811604
- research_skill round policy control requirement
- proposal_format.md::Control proposal skeleton

## historical_relation
- source_unit: generation_016/proposal_002
- relation_to_source: control
- not_a_duplicate_of: This intentionally duplicates the source as a control replicate; it is not an attempted capability proposal.
- lesson_used: Generation_016/proposal_002 was neutral-variance, so a control is necessary before interpreting small ISO17/gap changes.

## why_not_duplicate
This is a deliberate exact control. It should not be selected as novelty; it anchors variance for the M01 exploit/jump proposals.

## benchmark_rationale
- rmd17 energy: Expected to match source within run variance.
- rmd17 force: Expected to match source within run variance.
- rmd17 gap / Q: Expected Q_rmd17 around 4.127 subject to stochastic training variance.
- iso17 energy: Expected to reproduce source mixed_energy_mae around 0.305858, with possible variance.
- iso17 force: Expected to reproduce source mixed_force_mae around 0.175689.
- iso17 gap / Q: Expected Q_iso17 around 3.59966.
- training stability / runtime risk: Same as source.
- control comparison expectation: Candidate proposals should beat this by more than neutral/variance margin to be credible.

## files_to_edit
- none

## code_insertion_points
- none

## minimal_edit_plan
1. Exact copy of source unit.

## implementation_checklist
- [ ] Do not change `model/model.py`.
- [ ] Do not change `model/train.py`.
- [ ] Preserve benchmark metric field names and runnable entrypoint contract.
- [ ] Do not edit `config.json`.
- [ ] Mark implemented as control replicate if required by workflow.
- [ ] Call `mark_unit_implemented.py --unit <UNIT> --actor implementation_subagent` after materialization/status handling.

## expected_benchmark_effect
- primary expected gain: None; variance measurement only.
- expected tradeoff: Consumes one run budget slot.
- failure signal that would falsify this proposal: Any code diff from generation_016/proposal_002 or failure to smoke/launch under the inherited entrypoint.

## ablation_or_control
- required control or comparison: This is the control.
- optional zero-gate / source-fallback / readout-only ablation: Not applicable.

## implementation_notes_for_subagent
Do not edit code. If the workflow requires an implementation status file, mark the unit as a control replicate through the normal bundled script; do not hand-edit global state.
