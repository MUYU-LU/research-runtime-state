# Proposal 008: Exact source replicate control for generation_018

- family: source_control_replicate
- phase: 3
- jump_type: control
- budget_class: tiny
- expected_capability_gain: measure generation_018 runtime/control variance for generation_016/proposal_002 before interpreting branch-diversification proposals.

## one_sentence_hypothesis
An exact no-edit replicate of generation_016/proposal_002 is needed to distinguish real G018 mechanism gains from run-to-run variance and generation_017 neutral-control behavior.

## mechanism_refs
- G018-MECH-001
- G018-MECH-002
- G018-MECH-003
- G018-MECH-004

## evidence_refs
- generation_016/proposal_002 runtime summary: parent Q_total 3.9425481167873127 and current best-known unit.
- generation_017 outcome report: controls reached Q_total 3.8868060502667934 and 3.912585595964674 while no child beat parent.
- evidence_quality.json: proposal package is usable, but control is intentionally no-mechanism implementation to calibrate the four mechanism axes.
- proposal_constraints.json: allowed mechanisms G018-MECH-001 through G018-MECH-004 define the branches this control will compare against.

## historical_relation
- source_unit: generation_016/proposal_002
- relation_to_source: control
- not_a_duplicate_of: generation_017/proposal_007/proposal_008 because those were previous-generation controls; this calibrates the current generation_018 batch, evidence package, and remote runtime conditions.
- lesson_used: generation_017 best child was neutral variance and controls were close; selection needs a fresh control before attributing small deltas to new mechanisms.

## benchmark_rationale
- rmd17 energy: should reproduce source-level RMD17 energy within normal run variance.
- rmd17 force: should reproduce source-level RMD17 mixed_force_mae around 0.06364 within variance.
- rmd17 gap / Q: establishes current-batch variance for source Q_rmd17 4.12718.
- iso17 energy: establishes whether source ISO17 energy/gap variability alone can explain proposed gains.
- iso17 force: controls for launch/GPU/training variation in mixed_force_mae.
- iso17 gap / Q: critical because generation_017 controls varied and no child beat parent; compare all candidate gains to this control.
- training stability / runtime risk: no code change; standard implementation status and smoke are still required.
- control comparison expectation: all selected mechanism branches should beat this unit by more than variance/margin before being treated as useful.

## files_to_edit
- `none` (control replicate; no `model/model.py` or `model/train.py` edits)
- never `config.json` for MLIP-quality changes

## code_insertion_points
- `model/model.py`: none; copy source unchanged during materialization.
- `model/train.py`: none; copy source unchanged during materialization.
- implementation status: control may skip proposal-specific code edits but must still be marked implemented, synced, remote-smoked, and made launch_ready by workflow scripts.

## minimal_edit_plan
1. Do not modify any runnable-unit code after materialization.
2. Verify materialized files match source generation_016/proposal_002 for tracked model/train files.
3. Mark the control implemented using the normal workflow and require remote smoke before launch.
4. Use its metrics only as variance/control context, not as a mechanism claim.

## implementation_checklist
- [ ] Preserve `E = sum_i E_i` and force-from-energy contract by making no code change.
- [ ] Preserve benchmark metric field names and runnable entrypoint contract.
- [ ] Modify only the allowed target unit files; for this control, modify none.
- [ ] Do not edit `config.json`; change no MLIP knobs.
- [ ] Keep tensor shapes compatible with current dataloader and model forward by preserving source code.
- [ ] Add no unbounded cubic neighbor/triplet loops unless explicitly justified by budget.
- [ ] Confirm no accidental model/train diff before marking implemented.
- [ ] Call `mark_unit_implemented.py --unit <UNIT> --actor implementation_subagent` after confirming no edits.

## expected_benchmark_effect
- primary expected gain: none; expected to estimate variance around the source parent.
- expected tradeoff: consumes one launch slot but improves interpretability of all selected branches.
- failure signal that would falsify this proposal: control cannot smoke/launch, or metrics differ wildly due to environment issues rather than normal variance.

## ablation_or_control
- required control or comparison: this is the required control; compare every selected proposal's Q_total and component metrics against it.
- optional zero-gate / source-fallback / readout-only ablation: not applicable; the source itself is the fallback.

## implementation_notes_for_subagent
If selected/materialized, do not edit code. The implementation subagent should only inspect, confirm no diff, and mark implemented as a control according to workflow rules.
