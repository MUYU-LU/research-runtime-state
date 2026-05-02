# Proposal 003: Freeze atomref after one warmup epoch

- family: delayed_frozen_atomref_offset
- phase: 2
- jump_type: exploit
- budget_class: small
- expected_capability_gain: Let the source perform one epoch of joint residual/offset settling, then lock atomref before late ISO17 energy drift dominates.

## one_sentence_hypothesis
A one-epoch trainable atomref warmup can preserve any useful early residual calibration from proposal_005 while preventing later offset drift under force-heavy training.

## mechanism_refs
- MATERIALIZED-FROZEN-LSTSQ-ATOMREF-OFFSET-001

## evidence_refs
- paper_artifact:paper_002::Forces Are Not Enough energy-stability warning
- repo_artifact:repo_001::src/schnetpack/configs/experiment/md17.yaml
- /home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/evidence_run_20260428T152307Z/mechanism_cards.json
- /home/lmy/.openclaw/workspace/research_runtime/ledger/frontier.jsonl::generation_012/proposal_005

## historical_relation
- source_unit: generation_012/proposal_005
- relation_to_source: exploit
- not_a_duplicate_of: Proposal 001/002 because atomref remains trainable for exactly the first epoch, testing whether immediate freezing is too rigid.
- lesson_used: Source ISO17 validation force improved while energy worsened in later epochs; the edit attacks late drift while retaining early adaptation.

## benchmark_rationale
- rmd17 energy: One warmup epoch may keep the source's strong RMD17 calibration and avoid underfitting from immediate freeze.
- rmd17 force: Residual force path remains unchanged; force should stay near source.
- rmd17 gap / Q: Should preserve high Q_rmd17 if warmup does not destabilize offsets.
- iso17 energy: Expected to improve if drift occurs after the first epoch rather than during initialization.
- iso17 force: Should remain similar because the residual stack trains normally all epochs.
- iso17 gap / Q: Could improve gap if late offset movement was the cause; less strict than immediate freeze.
- training stability / runtime risk: Small edit inside epoch loop; no runtime-heavy architecture change.
- control comparison expectation: If immediate freeze underfits, delayed freeze should beat it; if drift starts immediately, Proposal 001 should beat this.

## files_to_edit
- `model/train.py`
- `model/model.py` none

## code_insertion_points
- `model/model.py::EvolutionMLIP.forward_energy`: no change.
- `model/train.py::train`: store `atomref_fitted`; inside the epoch loop, after epoch 1 optimizer/scheduler step, set `model.atomref.weight.requires_grad_(False)` and rebuild AdamW for non-atomref parameters for remaining epochs.

## minimal_edit_plan
1. Capture `atomref_fitted` from initialization and keep source optimizer for epoch 1.
2. After completing epoch 1, if fitted and more epochs remain, freeze `model.atomref.weight` and rebuild AdamW over non-atomref parameters with the current learning rate.
3. Preserve scheduler semantics as closely as possible by recreating `CosineAnnealingLR` for remaining epochs or, simpler, freeze before epoch 2 and keep optimizer state for other parameters if PyTorch permits.

## implementation_checklist
- [ ] Preserve `E = sum_i E_i` and force-from-energy contract.
- [ ] Preserve benchmark metric field names and runnable entrypoint contract.
- [ ] Modify only the allowed target unit files.
- [ ] Keep tensor shapes compatible with current dataloader and model forward.
- [ ] Add no unbounded cubic neighbor/triplet loops unless explicitly justified by budget.
- [ ] Call `mark_unit_implemented.py --unit <UNIT> --actor implementation_subagent` after edits.
- [ ] Ensure scheduler/history still writes the same field names.

## expected_benchmark_effect
- primary expected gain: ISO17 energy/gap improvement with less risk of fixed-offset underfitting.
- expected tradeoff: More moving parts than Proposal 001; one epoch may already introduce offset drift.
- failure signal that would falsify this proposal: Energy/gap remains close to source or scheduler/optimizer rebuild destabilizes both datasets.

## ablation_or_control
- required control or comparison: Compare against immediate freeze and source control.
- optional zero-gate / source-fallback / readout-only ablation: If optimizer rebuild is risky, use a gradient hook or set atomref grad to None after epoch 1.

## implementation_notes_for_subagent
Keep this bounded. Do not introduce early stopping or validation-dependent behavior; the freeze epoch must be a fixed constant independent of benchmark feedback.
