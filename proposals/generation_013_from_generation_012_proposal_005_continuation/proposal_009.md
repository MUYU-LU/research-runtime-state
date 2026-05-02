# Proposal 009: Wildcard atomref drift penalty

- family: atomref_drift_penalized_offset
- phase: 2
- jump_type: wildcard
- budget_class: small
- expected_capability_gain: Penalize movement away from the fitted atomref instead of freezing it, allowing small calibration adjustments while discouraging ISO17-damaging drift.

## one_sentence_hypothesis
A quadratic penalty to keep `atomref.weight` near its least-squares initialization may retain useful adaptation while preventing the baseline from wandering under energy-only gradients.

## mechanism_refs
- MATERIALIZED-FROZEN-LSTSQ-ATOMREF-OFFSET-001

## evidence_refs
- repo_artifact:repo_001::src/schnetpack/transform/atomistic.py::AddOffsets.forward
- paper_artifact:paper_001::SchNet energy/force loss
- paper_artifact:paper_002::force-only insufficiency warning
- /home/lmy/.openclaw/workspace/research_runtime/ledger/frontier.jsonl::generation_012/proposal_005

## historical_relation
- source_unit: generation_012/proposal_005
- relation_to_source: ablation
- not_a_duplicate_of: Freeze proposals because atomref remains trainable but softly tethered to the fitted value.
- lesson_used: If immediate freezing underfits, soft tethering tests whether limited atomref adaptation can improve energy without late drift.

## benchmark_rationale
- rmd17 energy: Should remain close to source by starting from the same fitted baseline and permitting small corrections.
- rmd17 force: Atomref penalty has no direct force derivative through positions, so force path remains residual.
- rmd17 gap / Q: Expected stable if penalty is modest.
- iso17 energy: Target lower energy drift than source while less rigid than freeze.
- iso17 force: Expected neutral to slight improvement if residual training benefits from small offset adaptation.
- iso17 gap / Q: Potential gap improvement if atomref drift magnitude was the culprit.
- training stability / runtime risk: Adds tiny scalar regularization each batch; no data/split changes.
- control comparison expectation: Should fall between source and hard-freeze behavior; best if hard freeze underfits.

## files_to_edit
- `model/train.py`
- `model/model.py` none

## code_insertion_points
- `model/model.py::EvolutionMLIP.forward_energy`: no change.
- `model/train.py::train`: after successful atomref fitting, clone `atomref_anchor = model.atomref.weight.detach().clone()`; pass it into `run_epoch` or add optional args so training loss includes `atomref_drift_weight * mean((model.atomref.weight - atomref_anchor)^2)`.
- `model/train.py::run_epoch`: add optional `atomref_anchor=None` and `atomref_drift_weight=0.0`; add penalty only when training and anchor is not None.

## minimal_edit_plan
1. Extend `run_epoch` signature with optional atomref drift penalty arguments defaulting to no-op.
2. In `train`, clone the fitted atomref anchor after successful least-squares initialization.
3. During training only, add a small penalty such as `CONFIG.get("atomref_drift_weight", 0.01) * torch.mean((model.atomref.weight - anchor) ** 2)` to `batch_loss`.

## implementation_checklist
- [ ] Preserve `E = sum_i E_i` and force-from-energy contract.
- [ ] Preserve benchmark metric field names and runnable entrypoint contract.
- [ ] Modify only the allowed target unit files.
- [ ] Keep tensor shapes compatible with current dataloader and model forward.
- [ ] Add no unbounded cubic neighbor/triplet loops unless explicitly justified by budget.
- [ ] Call `mark_unit_implemented.py --unit <UNIT> --actor implementation_subagent` after edits.
- [ ] Ensure validation/eval loss does not include training-only penalty in reported metrics.

## expected_benchmark_effect
- primary expected gain: Improved ISO17 energy/gap with less underfit risk than hard freeze.
- expected tradeoff: Extra hyperparameter may be too weak or too strong; less clean mechanistic test than freeze.
- failure signal that would falsify this proposal: Atomref still drifts and ISO17 energy remains source-like, or penalty harms both energy and force.

## ablation_or_control
- required control or comparison: Compare to hard-freeze, delayed-freeze, and source control.
- optional zero-gate / source-fallback / readout-only ablation: `atomref_drift_weight=0.0` recovers source behavior; very large weight approximates freeze.

## implementation_notes_for_subagent
Keep the penalty deterministic and train-only. Do not add new metrics or alter evaluation outputs; the penalty is internal to optimization only.
