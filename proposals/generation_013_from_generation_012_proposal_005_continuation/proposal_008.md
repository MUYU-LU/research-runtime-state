# Proposal 008: Direct source control replicate

- family: source_control_replicate
- phase: 2
- jump_type: control
- budget_class: tiny
- expected_capability_gain: No capability gain intended; measure run-to-run variance for generation_012/proposal_005 under unchanged semantics.

## one_sentence_hypothesis
An exact source replicate establishes whether generation_013 gains are real or within benchmark/run variance.

## mechanism_refs
- []

## evidence_refs
- /home/lmy/.openclaw/workspace/research_runtime/ledger/frontier.jsonl::generation_012/proposal_005
- /home/lmy/.openclaw/workspace/research_runtime/generations/generation_012/proposal_005/research_context/implementation_report.json
- /home/lmy/.openclaw/workspace/research_runtime/ledger/generation_reports/generation_012.md

## historical_relation
- source_unit: generation_012/proposal_005
- relation_to_source: control
- not_a_duplicate_of: It is intentionally a duplicate control replica, not an exploit proposal.
- lesson_used: Source has a large positive G_delta=1.2192; a control is needed to interpret small generation_013 changes.

## benchmark_rationale
- rmd17 energy: Expected to reproduce source mixed_energy_mae near 0.0418 within variance.
- rmd17 force: Expected to reproduce source force behavior.
- rmd17 gap / Q: Expected Q_rmd17 near 3.985.
- iso17 energy: Expected to reproduce source mixed_energy_mae near 0.3340 and gap_penalty near 0.0691.
- iso17 force: Expected mixed_force_mae near 0.1853.
- iso17 gap / Q: Expected Q_iso17 near 3.542.
- training stability / runtime risk: Same as source; launch-ready path should be straightforward after required implementation status/smoke.
- control comparison expectation: All non-control proposals should be judged against this replicate as well as generation_012/proposal_005.

## files_to_edit
- `none` (control replicate; no proposal-specific code edits)

## code_insertion_points
- `model/model.py::<none>`: no changes.
- `model/train.py::<none>`: no changes.

## minimal_edit_plan
1. Materialize as a control replica of generation_012/proposal_005.
2. Make no code edits to `model/model.py` or `model/train.py`.
3. Still complete the normal implementation status and remote smoke workflow required for controls.

## implementation_checklist
- [ ] Preserve `E = sum_i E_i` and force-from-energy contract.
- [ ] Preserve benchmark metric field names and runnable entrypoint contract.
- [ ] Modify only the allowed target unit files.
- [ ] Keep tensor shapes compatible with current dataloader and model forward.
- [ ] Add no unbounded cubic neighbor/triplet loops unless explicitly justified by budget.
- [ ] Call `mark_unit_implemented.py --unit <UNIT> --actor implementation_subagent` after edits.
- [ ] Record that no proposal-specific code edits were made because this is a control.

## expected_benchmark_effect
- primary expected gain: None; provides variance baseline.
- expected tradeoff: Consumes one run slot but improves interpretation.
- failure signal that would falsify this proposal: Control deviates strongly from source, indicating variance/runtime effects dominate small proposal deltas.

## ablation_or_control
- required control or comparison: This is the required control.
- optional zero-gate / source-fallback / readout-only ablation: Not applicable.

## implementation_notes_for_subagent
Do not “improve” this unit. It must remain a faithful source control while still passing the standard implementation/smoke gates.
