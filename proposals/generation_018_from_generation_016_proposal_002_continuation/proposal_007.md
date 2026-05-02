# Proposal 007: Latent charge-like conditioned readout with zero-mean auxiliary regularizer

- family: latent_charge_conditioned_readout
- phase: 4
- jump_type: wildcard
- budget_class: small
- expected_capability_gain: introduce a label-free environment-conditioned scalar head to stabilize energy decomposition and reduce ISO17 gap.

## one_sentence_hypothesis
A zero-mean latent charge-like scalar and graph context feeding a damped conditioned readout should improve per-atom energy decomposition while preserving force-from-energy and dataset schema.

## mechanism_refs
- G018-MECH-004

## evidence_refs
- paper_artifact:paper_004
- repo_artifact:repo_004
- mechanism_cards.json:G018-MECH-004.repo_code_trace
- patch_blueprints.json:G018-MECH-004
- generation_016/proposal_002 runtime summary: ISO17 validation energy worsens while force improves, motivating readout/energy-decomposition conditioning.

## historical_relation
- source_unit: generation_016/proposal_002
- relation_to_source: jump / wildcard
- not_a_duplicate_of: generation_016/proposal_004/proposal_005 latent electrostatic/hardness residuals because this uses the fresh CHGNet-style site-wise head as a label-free conditioned readout with explicit zero-mean regularization, not a previous latent residual family.
- lesson_used: generation_017 training-only stability probe regressed; make the auxiliary loss tiny and tied to a real readout mechanism rather than changing benchmark weights.

## benchmark_rationale
- rmd17 energy: conditioned readout may improve decomposition; damped residual should avoid harming source energy.
- rmd17 force: forces still derive from energy; auxiliary regularizer does not introduce force labels or detachments.
- rmd17 gap / Q: expected neutral-to-small positive if latent scalar captures transferable atom roles.
- iso17 energy: primary target; source has high mixed_energy_mae and worsening validation energy trend despite force improvement.
- iso17 force: should remain close if lambda_aux is small and conditioned head is residual.
- iso17 gap / Q: zero-mean q and graph context target energy gap/generalization without altering evaluator semantics.
- training stability / runtime risk: negligible O(NH) cost; risk is latent q drift or too-large auxiliary penalty.
- control comparison expectation: should improve ISO17 energy/gap more than controls and not regress RMD17 force.

## files_to_edit
- `model/model.py`
- `model/train.py`
- never `config.json` for MLIP-quality changes

## code_insertion_points
- `model/model.py::EvolutionMLIP.__init__`: add `latent_q_head`, `global_gate`, `conditioned_readout`, `conditioned_scale`, and an auxiliary-loss holder.
- `model/model.py::EvolutionMLIP.forward_energy`: after `readout_norm`, compute `q = q_head(z)`, zero-center it per molecule, compute attention/mean graph context `g`, and add a damped conditioned energy residual.
- `model/model.py::EvolutionMLIP.forward`: expose/store `self.last_aux_loss` without detaching the energy path.
- `model/train.py::run_epoch`: add `aux_weight * model.last_aux_loss` to training loss if present; keep energy/force losses and metric fields unchanged.

## minimal_edit_plan
1. Implement latent q and global context from final scalar features; enforce `q = q - q.mean()` for the current single-graph batch semantics.
2. Feed `[z, q, g]` through a small conditioned residual head and add it to old per-atom energy with near-zero scale.
3. Store `last_aux_loss = (q.pow(2).mean())` or neutrality penalty; in train.py add a tiny code-level constant `AUX_WEIGHT = 1e-4`.
4. Do not require external charge/magnetic labels and do not change dataloader/eval schemas.

## implementation_checklist
- [ ] Preserve `E = sum_i E_i` and force-from-energy contract.
- [ ] Preserve benchmark metric field names and runnable entrypoint contract.
- [ ] Modify only the allowed target unit files.
- [ ] Do not edit `config.json`; change MLIP knobs in `model/model.py` or `model/train.py`.
- [ ] Keep tensor shapes compatible with current dataloader and model forward.
- [ ] Add no unbounded cubic neighbor/triplet loops unless explicitly justified by budget.
- [ ] Keep auxiliary regularization label-free and small; no dataset schema changes.
- [ ] Call `mark_unit_implemented.py --unit <UNIT> --actor implementation_subagent` after edits.

## expected_benchmark_effect
- primary expected gain: ISO17 mixed_energy_mae/gap and Q_total via better energy decomposition.
- expected tradeoff: auxiliary term can suppress useful latent variation if too strong.
- failure signal that would falsify this proposal: q regularization reduces train loss but worsens other_energy/gap or force MAE versus control.

## ablation_or_control
- required control or comparison: source control and a lambda_aux=0 conditioned-head-only variant if materialized separately in future.
- optional zero-gate / source-fallback / readout-only ablation: conditioned residual scale zero recovers source; set `AUX_WEIGHT=0` to isolate readout conditioning.

## implementation_notes_for_subagent
Keep this label-free. Do not add charge labels, material-specific assumptions, or benchmark schema changes. The auxiliary term is a small code-level training knob in `model/train.py`, not a `config.json` setting.
