# Proposal 006: Atomref soft-anchor parameter group

- family: soft_anchor_atomref
- phase: 1
- jump_type: jump
- budget_class: small
- expected_capability_gain: Replace hard frozen atomref with a conservative adaptive baseline that can move slowly without destabilizing residual learning.

## one_sentence_hypothesis
Putting fitted atomref in a low-learning-rate optimizer group keeps the M02 energy safeguard adaptive but prevents large baseline drift that could hurt force/energy balance.

## mechanism_refs
- GEN014-M02-atomref-energy-safeguard

## evidence_refs
- mechanism_cards.json::GEN014-M02-atomref-energy-safeguard
- patch_blueprints.json::GEN014-M02-atomref-energy-safeguard::tiny L2/soft alternative
- repo:ACEsuit/mace#99833dea34c0::E0 correction handling
- benchmark_diagnosis.json::proposal_007 frozen atomref energy regression

## historical_relation
- source_unit: generation_013/proposal_007
- relation_to_source: jump
- not_a_duplicate_of: Proposal 003 because this does not fully unfreeze atomref at the main learning rate; it uses a conservative optimizer group.
- why_not_duplicate: No previous selected unit tested a lower-LR trainable atomref from scalar-only proposal_007.
- lesson_used: Hard freeze may be too rigid, but fully trainable offsets can drift; use a bounded middle ground.

## benchmark_rationale
- rmd17 energy: Expected mild improvement by adapting E0 slowly.
- rmd17 force: Mostly neutral; residual rebalancing could slightly affect force.
- rmd17 gap / Q: Should avoid large gap changes.
- iso17 energy: Targeted improvement in within/other energy calibration.
- iso17 force: Neutral to small change.
- iso17 gap / Q: Better Q if energy improves without force loss.
- training stability / runtime risk: Low; optimizer parameter grouping only.
- control comparison expectation: Should be safer than fully trainable atomref if drift is harmful.

## files_to_edit
- `model/train.py`

## code_insertion_points
- `model/train.py::train`: after LSTSQ initialization, do not set `requires_grad_(False)`; build AdamW param groups with atomref weights at `0.1 * learning_rate` and all other params at normal learning rate.
- `model/train.py::run_epoch`: ensure grad clipping covers all optimizer params or leave current `model.parameters()` clipping if all params are trainable.
- `model/model.py::EvolutionMLIP`: none.

## minimal_edit_plan
1. Remove/skip the atomref freeze line.
2. Build two optimizer parameter groups: non-atomref normal LR, atomref low LR.
3. Keep scheduler, loss weights, epochs, and benchmark IO unchanged.

## implementation_checklist
- [ ] Preserve `E = sum_i E_i` and force-from-energy contract.
- [ ] Preserve benchmark metric field names and runnable entrypoint contract.
- [ ] Modify only the allowed target unit files.
- [ ] Keep tensor shapes compatible with current dataloader and model forward.
- [ ] Add no unbounded cubic neighbor/triplet loops unless explicitly justified by budget.
- [ ] Call `mark_unit_implemented.py --unit <UNIT> --actor implementation_subagent` after edits.
- [ ] Verify scheduler handles multiple optimizer groups without changing logs except existing learning_rate field.

## expected_benchmark_effect
- primary expected gain: Energy/Q improvement over frozen source with less risk than full atomref unfreeze.
- expected tradeoff: Smaller gain if atomref needs faster adaptation.
- failure signal that would falsify this proposal: No energy improvement versus source or optimizer/scheduler instability.

## ablation_or_control
- required control or comparison: Compare to proposal_007 and Proposal 003 full trainable atomref.
- optional zero-gate / source-fallback / readout-only ablation: A very small LR approximates the frozen source.

## implementation_notes_for_subagent
Keep this train.py-only. Do not add custom regularization unless needed to implement the parameter group safely.
