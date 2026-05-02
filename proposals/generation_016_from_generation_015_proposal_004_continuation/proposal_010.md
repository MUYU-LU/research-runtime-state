# Proposal 010: Weak conservative-gradient regularized residual

- family: conservative_training_guardrail
- phase: 6
- jump_type: wildcard
- budget_class: small
- expected_capability_gain: Weak, exploratory guardrail to reduce energy/force inconsistency pressure while testing a tiny architecture residual.

## one_sentence_hypothesis
A tiny finite-difference directional derivative regularizer applied to the body-order residual during training may discourage unstable energy-force gradients, but evidence is weak and it should be selected only as a wildcard.

## mechanism_refs
- GEN016-W01-gradient-domain-physics-regularization-guardrail
- GEN016-M01-cace-shadow-body-order-representation

## evidence_refs
- paper_artifact:paper_003
- mechanism_cards.json::GEN016-W01-gradient-domain-physics-regularization-guardrail marked weak_hypothesis and not standalone proposal-ready
- patch_blueprints.json::GEN016-W01-gradient-domain-physics-regularization-guardrail implementation_ready=false guardrail cautions
- paper_artifact:paper_001
- mechanism_cards.json::GEN016-M01-cace-shadow-body-order-representation for the tiny residual branch being regularized
- benchmark_diagnosis.json::source ISO17 force improves while energy trend worsens

## historical_relation
- source_unit: generation_015/proposal_004
- relation_to_source: ablation
- not_a_duplicate_of: No prior proposal in this handoff changes the training-target/physics-regularization path; this is not another local architecture/readout tweak.
- lesson_used: Current code already uses autograd forces, so direct force heads are disallowed; any training regularizer must preserve conservative force-from-energy semantics and be tiny.

## why_not_duplicate
This proposal is explicitly weak and combines a minimal M01 residual with a tiny derivative-consistency regularizer in `model/train.py`; it is distinct from architecture-only body-order proposals and from controls.

## benchmark_rationale
- rmd17 energy: Could remain stable; regularizer may slightly slow fit.
- rmd17 force: May help avoid noisy residual gradients or may hurt if finite-difference noise is high.
- rmd17 gap / Q: Uncertain.
- iso17 energy: Weak possible benefit by discouraging residual energy surfaces that fit force but destabilize energy.
- iso17 force: Expected neutral to mild positive if regularizer is well-scaled.
- iso17 gap / Q: Uncertain; not a strong external-mechanism proposal.
- training stability / runtime risk: Runtime overhead from extra energy evaluations; keep coefficient tiny and apply only during training on one random direction/sample subset.
- control comparison expectation: Should be judged as wildcard/diagnostic, not a primary strong mechanism.

## files_to_edit
- `model/model.py`
- `model/train.py`
- never `config.json` for MLIP-quality changes

## code_insertion_points
- `model/model.py::MinimalNu2Branch / EvolutionMLIP.forward_energy`: add the smallest body-order residual branch from M01 so there is an architecture residual to guard.
- `model/train.py::TRAIN_CONSERVATIVE_FD_WEIGHT constant`: add a tiny code-level default such as 0.001 or lower; do not expose config semantics.
- `model/train.py::run_epoch`: during training only, for at most one sample or one random direction per batch, compare directional finite-difference energy change to `-F·u` and add tiny penalty to `loss`.
- `model/train.py::evaluation path`: leave validation/eval metrics unchanged; no regularizer when `optimizer is None`.

## minimal_edit_plan
1. Add a minimal body-order residual branch with near-zero scale as the architecture component.
2. Add a tiny training-only finite-difference directional consistency penalty using detached random direction and a small epsilon; skip it in validation.
3. Keep all benchmark labels, splits, metrics, and runnable entrypoint unchanged; remove/disable the regularizer if it causes memory/runtime problems.

## implementation_checklist
- [ ] Preserve `E = sum_i E_i` and force-from-energy contract; do not add a direct force head.
- [ ] Preserve benchmark metric field names and runnable entrypoint contract.
- [ ] Modify only the allowed target unit files.
- [ ] Do not edit `config.json`; change MLIP knobs/training constants in `model/model.py` or `model/train.py`.
- [ ] Keep tensor shapes compatible with current dataloader and model forward.
- [ ] Add no unbounded cubic neighbor/triplet loops.
- [ ] Keep regularizer tiny, training-only, and cheap; mark evidence as weak in implementation report if possible.
- [ ] Call `mark_unit_implemented.py --unit <UNIT> --actor implementation_subagent` after edits.

## expected_benchmark_effect
- primary expected gain: Weak/diagnostic; possible ISO17 energy stability improvement if residual gradients are smoother.
- expected tradeoff: Extra training cost and risk of noisy finite-difference penalty hurting optimization.
- failure signal that would falsify this proposal: Slower training plus no energy/gap improvement, or any violation of conservative autograd-force behavior.

## ablation_or_control
- required control or comparison: source control and architecture-only body-order residual proposal.
- optional zero-gate / source-fallback / readout-only ablation: Set `TRAIN_CONSERVATIVE_FD_WEIGHT = 0.0` while retaining the residual branch.

## implementation_notes_for_subagent
This is a weaker wildcard by design. Follow W01 only as a guardrail: no direct force head, no metric changes, no broad expensive regularizer. If implementation budget is tight, prefer making the regularizer disabled-by-default and clearly report that the proposal is diagnostic.
