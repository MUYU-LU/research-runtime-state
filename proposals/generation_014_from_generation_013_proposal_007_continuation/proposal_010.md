# Proposal 010: Soft atomref deviation penalty

- family: atomref_deviation_regularized
- phase: 1
- jump_type: wildcard
- budget_class: small
- expected_capability_gain: Mechanism-diverse atomref safeguard that allows E0 adaptation but penalizes large movement from the LSTSQ fitted baseline.

## one_sentence_hypothesis
Adding a tiny penalty on atomref deviation from its fitted LSTSQ values should recover energy calibration while preventing the baseline drift risk of fully trainable atomref.

## mechanism_refs
- GEN014-M02-atomref-energy-safeguard

## evidence_refs
- mechanism_cards.json::GEN014-M02-atomref-energy-safeguard
- patch_blueprints.json::GEN014-M02-atomref-energy-safeguard::tiny L2 regularization alternative
- repo:ACEsuit/mace#99833dea34c0::baseline atomic energy correction
- benchmark_diagnosis.json::proposal_007 energy/Q regression

## historical_relation
- source_unit: generation_013/proposal_007
- relation_to_source: jump
- not_a_duplicate_of: Proposal 006 because this uses an explicit deviation penalty rather than only a lower atomref learning rate.
- why_not_duplicate: Generation_013 did not test soft regularization of trainable fitted atomref from the scalar-only source.
- lesson_used: Hard-freeze may be brittle; fully free atomref may drift. A soft anchor tests the middle mechanism directly.

## benchmark_rationale
- rmd17 energy: Expected improvement if small E0 corrections are needed.
- rmd17 force: Mostly neutral; penalty affects energy baseline not force directly.
- rmd17 gap / Q: Should protect Q by limiting energy drift.
- iso17 energy: Primary target for improved within/other energy calibration.
- iso17 force: Expected neutral.
- iso17 gap / Q: Should improve if atomref adjustment reduces energy gap without force penalty.
- training stability / runtime risk: Low-to-medium; requires storing fitted atomref snapshot and adding scalar loss term.
- control comparison expectation: Should beat frozen source if hard freeze caused energy regression.

## files_to_edit
- `model/train.py`

## code_insertion_points
- `model/train.py::train`: after `initialize_atomref_lstsq`, clone `atomref_anchor = model.atomref.weight.detach().clone()` and keep atomref trainable.
- `model/train.py::run_epoch`: accept optional `atomref_anchor`/`atomref_penalty_weight` and add a tiny mean-squared deviation penalty to `batch_loss` during training only, preserving reported MAE fields.
- `model/model.py::EvolutionMLIP`: none.

## minimal_edit_plan
1. Store a detached copy of fitted atomref weights after LSTSQ initialization.
2. Do not freeze atomref.
3. Add a small training-only penalty such as `1e-4 * mean((atomref.weight - anchor)^2)` without changing evaluation metrics or output schema.

## implementation_checklist
- [ ] Preserve `E = sum_i E_i` and force-from-energy contract.
- [ ] Preserve benchmark metric field names and runnable entrypoint contract.
- [ ] Modify only the allowed target unit files.
- [ ] Keep tensor shapes compatible with current dataloader and model forward.
- [ ] Add no unbounded cubic neighbor/triplet loops unless explicitly justified by budget.
- [ ] Call `mark_unit_implemented.py --unit <UNIT> --actor implementation_subagent` after edits.
- [ ] Do not log new benchmark metric fields or alter eval semantics.

## expected_benchmark_effect
- primary expected gain: Better energy/Q than frozen proposal_007 with lower drift than full trainable atomref.
- expected tradeoff: Penalty may be too weak/strong; could add code complexity in `run_epoch`.
- failure signal that would falsify this proposal: Energy/Q do not improve or penalty changes training loss without benchmark gain.

## ablation_or_control
- required control or comparison: Proposal 008 exact control, Proposal 003 full trainable atomref, Proposal 006 low-LR atomref.
- optional zero-gate / source-fallback / readout-only ablation: Penalty weight near infinity approximates freeze; zero approximates full unfreeze.

## implementation_notes_for_subagent
Keep the penalty internal to training loss only. Do not change `benchmark_metrics.json` fields, data splits, eval code, or entrypoint behavior.
