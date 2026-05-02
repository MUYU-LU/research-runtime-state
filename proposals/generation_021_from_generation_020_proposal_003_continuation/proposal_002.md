# Proposal 002: Scalar-Only Atomwise Residual Ablation

- family: atomwise_energy_residual
- phase: 4
- jump_type: backward-simplify
- budget_class: tiny
- expected_capability_gain: Isolate whether a direct scalar readout residual alone improves energy/gap/Q without vector-norm coupling.

## one_sentence_hypothesis
A scalar_state-only zero-output atomwise residual provides a cleaner SchNet-style energy correction than the muted PaiNN mixer and should improve energy/gap terms if vector_norm is unnecessary noise.

## mechanism_refs
- GEN021-M01-atomwise-energy-residual-calibration

## evidence_refs
- evidence_brief_20260501T011417Z.md
- mechanism_cards.json::GEN021-M01-atomwise-energy-residual-calibration ablation input scalar_state only vs scalar_state+vector_norm
- patch_blueprints.json::GEN021-M01-atomwise-energy-residual-calibration
- generation_summaries/generation_020.json::proposal_002 scalar-only hidden feedback was neutral_variance not a direct energy residual
- repo_artifact:repo_001 SchNetPack Atomwise.forward per-atom scalar aggregation

## historical_relation
- source_unit: generation_020/proposal_003
- relation_to_source: ablation
- not_a_duplicate_of: generation_020/proposal_002 used scalar-only representation feedback before readout; this proposal uses scalar-only direct energy residual after readout normalization.
- why_not_duplicate: tests direct energy calibration, not hidden-state mixing; removes vector_norm from residual input to bound force-gradient complexity.
- lesson_used: generation_020 hidden mixer family was too muted under 8 epochs; direct atomwise energy pooling is better aligned with benchmark energy/gap/Q.

## benchmark_rationale
Discuss expected effects on all relevant benchmark signals, not force-only:
- capacity/scaling hypothesis, if any: no broad capacity scale; one small scalar residual head.
- rmd17 energy: should reduce or preserve mixed_energy_mae if source scalar_state contains enough energy information.
- rmd17 force: lower force risk than vector_norm residual because no explicit vector norm path enters the residual.
- rmd17 gap / Q: expected neutral gap_penalty and stable Q_rmd17; any degradation means even scalar residual is overfitting.
- iso17 energy: direct target; lower mixed_energy_mae would show energy calibration bottleneck.
- iso17 force: expected neutral because residual is smooth and capped at 0.01-0.02.
- iso17 gap / Q: should reduce gap_penalty enough to raise Q_iso17 if vector_norm was noisy.
- training stability / runtime risk: tiny cost and low implementation risk.
- control comparison expectation: compared to proposal_001, if scalar-only wins Q_total/G_delta, vector_norm coupling is unnecessary; if it loses, vector_norm carries useful muted PaiNN information.

- validation terms: energy, force, gap penalty, Q_rmd17, Q_iso17, Q_total, and G_delta are the selection-facing signals.

## files_to_edit
- `model/model.py`
- `model/train.py` if needed, otherwise `none`
- never `config.json` for MLIP-quality changes

## code_insertion_points
- `model/model.py::EvolutionMLIP.__init__`: add `scalar_energy_residual_head` with LayerNorm(hidden_dim), Linear(hidden_dim, hidden_dim//2), SiLU, Linear(hidden_dim//2,1), zero final layer, and beta cap <=0.02.
- `model/model.py::EvolutionMLIP.forward_energy`: after `scalar_state = self.readout_norm(...)` and before `per_atom_energy.sum()`, compute residual from `scalar_state` only and add to energy.
- `model/train.py::train/run_epoch`: none.
- code-level MLIP knobs may include `EvolutionMLIP.__init__` defaults, `MODEL_*` constants, or `TRAIN_*` constants when present

## minimal_edit_plan
1. Add scalar-only residual head after existing readout normalization.
2. Zero-initialize final residual projection; set capped beta to 0.01 or 0.02.
3. Return `atomref + per_atom_energy.sum() + body_order_multiplier * body_order_residual.sum() + beta * residual.sum()`.

## implementation_checklist
- [ ] Preserve `E = sum_i E_i` and force-from-energy contract.
- [ ] Preserve benchmark metric field names and runnable entrypoint contract.
- [ ] Modify only the allowed target unit files.
- [ ] Do not edit `config.json`; change MLIP knobs in `model/model.py` or `model/train.py`.
- [ ] Keep tensor shapes compatible with current dataloader and model forward.
- [ ] Add no unbounded cubic neighbor/triplet loops unless explicitly justified by budget.
- [ ] Call `mark_unit_implemented.py --unit generation_021/proposal_002 --actor implementation_subagent` after edits.

## expected_benchmark_effect
- primary expected gain: safer ISO17 energy/gap and Q_iso17 improvement with minimal force disturbance.
- expected tradeoff: smaller gain than proposal_001 if vector_norm contains useful geometry.
- failure signal that would falsify this proposal: no positive Q_total G_delta and no ISO17 gap_penalty reduction.

## ablation_or_control
- required control or comparison: compare to proposal_001 scalar+vector_norm residual and unchanged control.
- optional zero-gate / source-fallback / readout-only ablation: beta=0 should exactly recover the source energy path.

## implementation_notes_for_subagent
Do not change final TPInvariantPaiNNMixing or training weights; this must remain a one-factor scalar-only direct residual ablation.
