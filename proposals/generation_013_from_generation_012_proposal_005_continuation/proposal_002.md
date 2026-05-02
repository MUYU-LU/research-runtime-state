# Proposal 002: Exclude atomref from optimizer with explicit residual parameters

- family: optimizer_excluded_atomref_offset
- phase: 2
- jump_type: exploit
- budget_class: tiny
- expected_capability_gain: Same fixed-offset mechanism as Proposal 001, but implemented by explicit optimizer parameter groups to avoid accidental atomref updates.

## one_sentence_hypothesis
Building AdamW only over non-atomref parameters makes the least-squares composition baseline a fixed offset while keeping the residual interaction/readout trainable.

## mechanism_refs
- MATERIALIZED-FROZEN-LSTSQ-ATOMREF-OFFSET-001

## evidence_refs
- repo_artifact:repo_001::src/schnetpack/transform/atomistic.py::RemoveOffsets
- repo_artifact:repo_001::src/schnetpack/transform/atomistic.py::AddOffsets.forward
- /home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/evidence_run_20260428T152307Z/patch_blueprints.json
- /home/lmy/.openclaw/workspace/research_runtime/ledger/generation_reports/generation_012.md

## historical_relation
- source_unit: generation_012/proposal_005
- relation_to_source: exploit
- not_a_duplicate_of: Proposal 001 because this tests optimizer exclusion rather than `requires_grad_(False)`, making the handoff robust if later code toggles trainability.
- lesson_used: Offset gradients receive no force signal; excluding them from AdamW directly targets the source's late ISO17 energy drift without changing interactions.

## benchmark_rationale
- rmd17 energy: Should retain proposal_005's excellent RMD17 energy because the same fitted baseline is used.
- rmd17 force: Force contract is unchanged; atomref exclusion has zero direct force effect.
- rmd17 gap / Q: Q_rmd17 should remain close to 3.985 if residual training dynamics are unchanged.
- iso17 energy: Expected to reduce calibration drift by preventing AdamW updates to `atomref.weight`.
- iso17 force: Expected neutral; any degradation implies optimizer grouping affected unintended parameters.
- iso17 gap / Q: Expected modest Q_iso17 gain through lower mixed_energy_mae/gap_penalty.
- training stability / runtime risk: Tiny; fewer optimizer states and no new operations.
- control comparison expectation: Should match Proposal 001 if both implement the same mechanism; divergence flags implementation sensitivity.

## files_to_edit
- `model/train.py`
- `model/model.py` none

## code_insertion_points
- `model/model.py::EvolutionMLIP.forward_energy`: no change; keep additive atomref term.
- `model/train.py::train`: after `initialize_atomref_lstsq`, build `trainable_params = [p for n, p in model.named_parameters() if not n.startswith("atomref.")]` and pass that list to AdamW when fitting succeeded.

## minimal_edit_plan
1. Store `atomref_fitted = initialize_atomref_lstsq(...)`.
2. If fitted, build AdamW from named parameters excluding `atomref.`; otherwise use `model.parameters()`.
3. Keep scheduler, weights, epochs, dataloaders, and metric logging identical to source.

## implementation_checklist
- [ ] Preserve `E = sum_i E_i` and force-from-energy contract.
- [ ] Preserve benchmark metric field names and runnable entrypoint contract.
- [ ] Modify only the allowed target unit files.
- [ ] Keep tensor shapes compatible with current dataloader and model forward.
- [ ] Add no unbounded cubic neighbor/triplet loops unless explicitly justified by budget.
- [ ] Call `mark_unit_implemented.py --unit <UNIT> --actor implementation_subagent` after edits.
- [ ] Verify no non-atomref parameter is accidentally excluded.

## expected_benchmark_effect
- primary expected gain: Lower ISO17 mixed_energy_mae/gap_penalty via fixed composition offset.
- expected tradeoff: Same scientific risk as Proposal 001: fixed atomref may underfit if adaptation was beneficial.
- failure signal that would falsify this proposal: Results materially differ from Proposal 001 without a clear implementation reason, or optimizer construction fails.

## ablation_or_control
- required control or comparison: Compare to Proposal 001 and generation_012/proposal_005.
- optional zero-gate / source-fallback / readout-only ablation: Fallback to full `model.parameters()` if fitting fails.

## implementation_notes_for_subagent
Use explicit parameter filtering only in `model/train.py`. Do not alter `initialize_atomref_lstsq` math or the model energy formula.
