# Proposal 006: Frozen offset with residual readout weight decay split

- family: frozen_offset_readout_regularized
- phase: 3
- jump_type: jump
- budget_class: small
- expected_capability_gain: Keep the fitted atomref fixed and reduce residual readout over-drift by applying slightly stronger weight decay to readout parameters only.

## one_sentence_hypothesis
If ISO17 energy drift comes from residual readout overfitting after the composition offset is fitted, freezing atomref plus readout-specific regularization should lower gap_penalty without reducing the message-passing force path too much.

## mechanism_refs
- MATERIALIZED-FROZEN-LSTSQ-ATOMREF-OFFSET-001

## evidence_refs
- repo_artifact:repo_001::src/schnetpack/atomistic/atomwise.py::Atomwise.forward
- repo_artifact:repo_001::src/schnetpack/transform/atomistic.py::AddOffsets.forward
- /home/lmy/.openclaw/workspace/research_runtime/ledger/frontier.jsonl::generation_012/proposal_005
- /home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/evidence_run_20260428T152307Z/current_code_profile.json

## historical_relation
- source_unit: generation_012/proposal_005
- relation_to_source: jump
- not_a_duplicate_of: Proposal 005 because this leaves loss schedule unchanged and regularizes only residual readout parameters.
- lesson_used: The source's residual stack already gives strong force; the risky component for energy/gap may be readout calibration rather than neighbor geometry.

## benchmark_rationale
- rmd17 energy: Moderate readout regularization may preserve excellent RMD17 energy by avoiding late overfit.
- rmd17 force: Force can regress if readout underfits; keep decay modest.
- rmd17 gap / Q: Should remain high if regularization is not excessive.
- iso17 energy: Target improved generalization to ISO17 other split energy.
- iso17 force: Expected mostly neutral; interactions unchanged, readout gradients remain differentiable.
- iso17 gap / Q: Lower other/within energy mismatch should improve gap_penalty and Q_iso17.
- training stability / runtime risk: Small optimizer parameter-group edit; no runtime overhead.
- control comparison expectation: Should beat pure freeze only if residual readout overfit contributes beyond atomref drift.

## files_to_edit
- `model/train.py`
- `model/model.py` none

## code_insertion_points
- `model/model.py::EvolutionMLIP.forward_energy`: no change.
- `model/train.py::train`: freeze fitted atomref; build AdamW parameter groups with default weight decay for most non-atomref parameters and a slightly larger decay for names starting with `readout.`.

## minimal_edit_plan
1. Capture `atomref_fitted` and freeze/exclude atomref after successful initialization.
2. Split `model.named_parameters()` into `readout` and `other` non-atomref trainable parameter groups.
3. Use source AdamW settings, setting readout weight_decay to e.g. `2 * CONFIG.get("weight_decay", 1e-5)` while preserving betas/lr.

## implementation_checklist
- [ ] Preserve `E = sum_i E_i` and force-from-energy contract.
- [ ] Preserve benchmark metric field names and runnable entrypoint contract.
- [ ] Modify only the allowed target unit files.
- [ ] Keep tensor shapes compatible with current dataloader and model forward.
- [ ] Add no unbounded cubic neighbor/triplet loops unless explicitly justified by budget.
- [ ] Call `mark_unit_implemented.py --unit <UNIT> --actor implementation_subagent` after edits.
- [ ] Ensure all trainable non-atomref parameters appear in exactly one optimizer group.

## expected_benchmark_effect
- primary expected gain: Improved ISO17 energy/gap generalization after offset freeze.
- expected tradeoff: Possible underfitting of readout and mild force regression.
- failure signal that would falsify this proposal: Both energy and force worsen relative to pure freeze, indicating regularization is unnecessary.

## ablation_or_control
- required control or comparison: Compare to Proposal 001 and source control.
- optional zero-gate / source-fallback / readout-only ablation: Set readout decay multiplier to 1.0 to recover pure optimizer-exclusion behavior.

## implementation_notes_for_subagent
Keep parameter grouping simple and auditable. Do not change model dimensions, interaction count, batch size, epoch count, or benchmark config schema.
