# Proposal 001: Direct Atomwise Energy Residual Calibration

- family: atomwise_energy_residual
- phase: 4
- jump_type: exploit
- budget_class: small
- expected_capability_gain: Improve ISO17 energy/gap calibration by adding one bounded direct scalar residual while preserving conservative forces.

## one_sentence_hypothesis
A zero-output atomwise residual head on `[scalar_state, vector_norm]` gives the muted generation_020 PaiNN-style signal a direct energy path, improving energy, gap penalty, Q_iso17, Q_total, and positive G_delta without force collapse.

## mechanism_refs
- GEN021-M01-atomwise-energy-residual-calibration

## evidence_refs
- evidence_brief_20260501T011417Z.md
- mechanism_cards.json::GEN021-M01-atomwise-energy-residual-calibration
- patch_blueprints.json::GEN021-M01-atomwise-energy-residual-calibration
- generation_summaries/generation_020.json::generation_020/proposal_003 neutral_variance Q_total=4.047840586729483
- repo_artifact:repo_001 SchNetPack Atomwise.forward and Forces.forward traces
- paper_artifact:paper_001 Forces Are Not Enough
- paper_artifact:paper_002 SchNet continuous-filter energy/force training

## historical_relation
- source_unit: generation_020/proposal_003
- relation_to_source: exploit
- not_a_duplicate_of: generation_020/proposal_001/002/003 added hidden-state PaiNN-style mixers; this proposal places the new pathway directly on atomwise energy instead of relying on another tiny representation residual.
- why_not_duplicate: the source's final mixer has effective scalar/vector scales near 1e-4/2e-5 and was neutral; this proposal removes that attenuation stage for the new correction while retaining zero-output source fallback.
- lesson_used: generation_020 best child improved Q_total by only +0.02181, below margin; target energy/gap/Q rather than force-only or more muted vector feedback.

## benchmark_rationale
Discuss expected effects on all relevant benchmark signals, not force-only:
- capacity/scaling hypothesis, if any: no global capacity scaling; add one small per-atom residual MLP so attribution stays mechanism-centric.
- rmd17 energy: expected neutral-to-slightly-better mixed_energy_mae because beta is capped at 0.02 and initialized as an exact zero-output fallback.
- rmd17 force: slight risk because force is the gradient of the residual energy; smooth SiLU/LayerNorm and small beta should preserve mixed_force_mae.
- rmd17 gap / Q: should not worsen gap_penalty from 0.00828; Q_rmd17 should remain within neutral variance or improve modestly.
- iso17 energy: primary target is lower mixed_energy_mae and validation energy transfer error.
- iso17 force: expected neutral to small regression; reject if force regression cancels energy gains.
- iso17 gap / Q: primary target is reducing ISO17 gap_penalty 0.14068 and raising Q_iso17 above 3.76869.
- training stability / runtime risk: low runtime cost, no new neighbor/triplet loops; risk is beta too large causing energy-force tradeoff.
- control comparison expectation: should beat unchanged source/control by Q_total G_delta > +0.03 or at least improve Q_iso17 without Q_rmd17 collapse.

- validation terms: energy, force, gap penalty, Q_rmd17, Q_iso17, Q_total, and G_delta are the selection-facing signals.

## files_to_edit
- `model/model.py`
- `model/train.py` if needed, otherwise `none`
- never `config.json` for MLIP-quality changes

## code_insertion_points
- `model/model.py::EvolutionMLIP.__init__`: add `energy_residual_head` using LayerNorm(hidden_dim*2), Linear(hidden_dim*2, hidden_dim//2), SiLU, Linear(hidden_dim//2, 1), plus capped `energy_residual_scale_logit`.
- `model/model.py::EvolutionMLIP.forward_energy`: after `vector_norm`, `scalar_vector_input`, `readout_norm`, and before returning summed energy, compute `residual_input=torch.cat([scalar_state, vector_norm], dim=-1)` and add `beta * energy_residual.sum()`.
- `model/train.py::train/run_epoch`: none; keep current objective so this is model-only.
- code-level MLIP knobs may include `EvolutionMLIP.__init__` defaults, `MODEL_*` constants, or `TRAIN_*` constants when present

## minimal_edit_plan
1. Add the residual head and zero-initialize its final Linear weight/bias.
2. Set `beta = 0.02 * sigmoid(logit)` with logit initialized around 0 or use a small positive bounded parameter; do not reproduce the generation_020 1e-4 effective attenuation.
3. Add the residual to the scalar energy sum using invariant inputs only; leave force autograd unchanged.

## implementation_checklist
- [ ] Preserve `E = sum_i E_i` and force-from-energy contract.
- [ ] Preserve benchmark metric field names and runnable entrypoint contract.
- [ ] Modify only the allowed target unit files.
- [ ] Do not edit `config.json`; change MLIP knobs in `model/model.py` or `model/train.py`.
- [ ] Keep tensor shapes compatible with current dataloader and model forward.
- [ ] Add no unbounded cubic neighbor/triplet loops unless explicitly justified by budget.
- [ ] Call `mark_unit_implemented.py --unit generation_021/proposal_001 --actor implementation_subagent` after edits.

## expected_benchmark_effect
- primary expected gain: ISO17 mixed_energy_mae/gap_penalty improvement leading to higher Q_iso17, Q_total, and G_delta.
- expected tradeoff: tiny RMD17/ISO17 force regression is possible through energy-gradient coupling.
- failure signal that would falsify this proposal: Q_total stays within ±0.03 of source or ISO17 gap improves only by sacrificing Q_rmd17 force/energy.

## ablation_or_control
- required control or comparison: compare to unchanged generation_020/proposal_003 and generation_020/proposal_008 control replicate.
- optional zero-gate / source-fallback / readout-only ablation: set beta to zero to confirm exact source fallback; compare proposal_002 scalar-only residual.

## implementation_notes_for_subagent
Keep the existing final TPInvariantPaiNNMixing in place; this proposal tests whether a direct energy residual can expose useful scalar/vector-norm information under the fixed 8-epoch benchmark.
