# Proposal 010: Body-Order-Conditioned Energy Residual Wildcard

- family: body_order_energy_residual
- phase: 4
- jump_type: wildcard
- budget_class: medium
- expected_capability_gain: Use existing body-order descriptors as additional invariant inputs to a direct energy residual for a more expressive but still bounded calibration jump.

## one_sentence_hypothesis
Adding `body_order_descriptor` to the GEN021-M01 atomwise residual input should improve ISO17 energy/gap/Q if current scalar/vector features miss transferable local body-order calibration.

## mechanism_refs
- GEN021-M01-atomwise-energy-residual-calibration

## evidence_refs
- evidence_brief_20260501T011417Z.md
- mechanism_cards.json::GEN021-M01-atomwise-energy-residual-calibration optional input b_i / body_order_descriptor
- patch_blueprints.json::GEN021-M01-atomwise-energy-residual-calibration
- current source model.py::BodyOrderMessageBranch and body_order_readout
- generation_summaries/generation_020.json::proposal_003 ISO17 gap_penalty=0.14068, Q_total=4.04784
- repo_artifact:repo_001 Atomwise.forward/Forces.forward direct energy pooling pattern

## historical_relation
- source_unit: generation_020/proposal_003
- relation_to_source: jump
- not_a_duplicate_of: proposal_001 uses scalar_state+vector_norm only; this wildcard includes existing body_order_descriptor in the direct residual input.
- why_not_duplicate: it is evidence-supported by GEN021-M01's optional `b_i` term and reuses already-computed descriptors, avoiding new O(N^3) body-order loops.
- lesson_used: previous body-order branch exists but ISO17 gap remains high; a direct calibrated residual may expose body-order information more effectively.

## benchmark_rationale
Discuss expected effects on all relevant benchmark signals, not force-only:
- capacity/scaling hypothesis, if any: moderate readout/input scaling using existing descriptor_dim; no new neighbor complexity.
- rmd17 energy: may improve if body-order descriptor calibrates local energy; overfitting risk is higher than proposal_001.
- rmd17 force: residual gradients include body-order descriptor path, so force MAE risk is moderate but conservative.
- rmd17 gap / Q: require Q_rmd17 not to collapse; a meaningful result should preserve RMD17 gap_penalty.
- iso17 energy: primary target is transfer energy calibration from richer invariant descriptors.
- iso17 force: monitor for descriptor-induced force noise.
- iso17 gap / Q: target substantial gap_penalty reduction and Q_iso17 lift.
- training stability / runtime risk: medium runtime/parameter risk from descriptor projection but no new graph loops.
- control comparison expectation: as wildcard/jump, it must produce clear Q_total G_delta > +0.03; neutral result should defer to simpler residual proposals.

- validation terms: energy, force, gap penalty, Q_rmd17, Q_iso17, Q_total, and G_delta are the selection-facing signals.

## files_to_edit
- `model/model.py`
- `model/train.py` if needed, otherwise `none`
- never `config.json` for MLIP-quality changes

## code_insertion_points
- `model/model.py::EvolutionMLIP.__init__`: add body-order-conditioned residual head with input dimension `hidden_dim*2 + self.body_order_branch.descriptor_dim`, LayerNorm, Linear to hidden_dim//2, SiLU, Linear to 1, zero final projection, beta cap <=0.02.
- `model/model.py::EvolutionMLIP.forward_energy`: concatenate `scalar_state`, `vector_norm`, and `body_order_descriptor` after readout normalization, compute residual, and add `beta * residual.sum()` to energy.
- `model/train.py::train/run_epoch`: none.
- code-level MLIP knobs may include `EvolutionMLIP.__init__` defaults, `MODEL_*` constants, or `TRAIN_*` constants when present

## minimal_edit_plan
1. Reuse existing `body_order_descriptor`; do not recompute descriptors or alter BodyOrderMessageBranch.
2. Add the bounded direct residual head with input `[scalar_state, vector_norm, body_order_descriptor]` and zero final output.
3. Keep beta<=0.02 and preserve all training settings for clean wildcard attribution.

## implementation_checklist
- [ ] Preserve `E = sum_i E_i` and force-from-energy contract.
- [ ] Preserve benchmark metric field names and runnable entrypoint contract.
- [ ] Modify only the allowed target unit files.
- [ ] Do not edit `config.json`; change MLIP knobs in `model/model.py` or `model/train.py`.
- [ ] Keep tensor shapes compatible with current dataloader and model forward.
- [ ] Add no unbounded cubic neighbor/triplet loops unless explicitly justified by budget.
- [ ] Call `mark_unit_implemented.py --unit generation_021/proposal_010 --actor implementation_subagent` after edits.

## expected_benchmark_effect
- primary expected gain: larger ISO17 energy/gap/Q_iso17 improvement than simple residual, raising Q_total and G_delta.
- expected tradeoff: higher overfit/force risk and slightly higher runtime than proposal_001.
- failure signal that would falsify this proposal: no Q_total gain beyond simple residual or force/gap regressions that show descriptor conditioning is too noisy.

## ablation_or_control
- required control or comparison: compare to proposal_001 scalar+vector_norm residual and exact source control.
- optional zero-gate / source-fallback / readout-only ablation: zero beta confirms source fallback; future ablation can remove body_order_descriptor while keeping head width.

## implementation_notes_for_subagent
This is the only wildcard/jump in the set. Keep it bounded and evidence-supported: reuse existing descriptors, preserve invariance, and do not introduce new triplet/body-order enumeration.
