# Proposal 010: RoPE global context feeding latent conditioned readout

- family: rope_conditioned_latent_readout_hybrid
- phase: 5
- jump_type: wildcard
- budget_class: medium
- expected_capability_gain: combine nonlocal geometric context with a constrained latent scalar readout to attack ISO17 energy/gap from two evidence-backed axes.

## one_sentence_hypothesis
Feeding a low-cost Euclidean RoPE global context into a zero-mean latent conditioned readout should improve global conformer energy generalization more than either a purely local gate or an unconstrained readout MLP.

## mechanism_refs
- G018-MECH-001
- G018-MECH-004

## evidence_refs
- paper_artifact:paper_001
- repo_artifact:repo_001
- paper_artifact:paper_004
- repo_artifact:repo_004
- patch_blueprints.json:G018-MECH-001
- patch_blueprints.json:G018-MECH-004
- generation_017 outcome report: local repair axes failed to beat parent, motivating a broader wildcard branch-diversification proposal.

## historical_relation
- source_unit: generation_016/proposal_002
- relation_to_source: jump
- not_a_duplicate_of: proposal_001/proposal_002 because RoPE context is used only as readout conditioning, not as per-layer or plain readout residual; not a duplicate of proposal_007 because q/global context receives geometry-aware RoPE features.
- lesson_used: source is best known but ISO17 energy/gap remains weak; combine two bounded global/readout mechanisms rather than further local PaiNN/body-order repairs.

## benchmark_rationale
- rmd17 energy: hybrid readout may alter energy decomposition; keep both residuals damped to protect source performance.
- rmd17 force: RoPE context is position-dependent, but only near readout; low frequency and zero q-regularization should limit force noise.
- rmd17 gap / Q: expected neutral if global latent context is not needed; any drop flags over-combination.
- iso17 energy: primary target because geometry-aware global context plus latent q should help other-conformer energy transfer.
- iso17 force: local force backbone remains unchanged; watch for readout-position gradient noise.
- iso17 gap / Q: expected reduction in gap_penalty by conditioning per-atom energy on molecule-level shape and constrained latent roles.
- training stability / runtime risk: combines two modules, so keep dimensions small and auxiliary weight tiny; medium budget but no all-pairs or external dependencies.
- control comparison expectation: should beat source control by a clear ISO17 energy/gap improvement; otherwise simpler single-axis proposals are preferred.

## files_to_edit
- `model/model.py`
- `model/train.py`
- never `config.json` for MLIP-quality changes

## code_insertion_points
- `model/model.py::GlobalRoPEAttentionSideChannel`: add/readout-only small context module from G018-MECH-001.
- `model/model.py::EvolutionMLIP.__init__`: add `readout_global_context`, `latent_q_head`, `global_gate`, `conditioned_readout`, residual scales, and aux-loss holder.
- `model/model.py::EvolutionMLIP.forward_energy`: after `readout_norm`, compute RoPE context, concatenate/merge it into q/global context computation, and add a damped conditioned per-atom energy residual.
- `model/model.py::EvolutionMLIP.forward`: store `last_aux_loss` without altering force autograd.
- `model/train.py::run_epoch`: add tiny auxiliary q penalty if present, preserving energy/force metric fields.

## minimal_edit_plan
1. Implement one readout-only RoPE global context with M<=6 or M<=8 and low frequencies.
2. Compute latent q from `[scalar_state, rope_context]`, zero-center q, compute global pooled context, and feed a small conditioned residual energy head.
3. Add `AUX_WEIGHT = 1e-4` in train.py for q magnitude/neutrality only; do not alter energy_weight or force_weight.
4. Keep all residual scales near zero and leave interaction/body-order branches untouched.

## implementation_checklist
- [ ] Preserve `E = sum_i E_i` and force-from-energy contract.
- [ ] Preserve benchmark metric field names and runnable entrypoint contract.
- [ ] Modify only the allowed target unit files.
- [ ] Do not edit `config.json`; change MLIP knobs in `model/model.py` or `model/train.py`.
- [ ] Keep tensor shapes compatible with current dataloader and model forward.
- [ ] Add no unbounded cubic neighbor/triplet loops unless explicitly justified by budget.
- [ ] Keep both mechanisms bounded; no per-layer global attention in this wildcard.
- [ ] Call `mark_unit_implemented.py --unit <UNIT> --actor implementation_subagent` after edits.

## expected_benchmark_effect
- primary expected gain: ISO17 mixed_energy_mae/gap and Q_total through global geometry-conditioned energy decomposition.
- expected tradeoff: medium implementation complexity and risk of compounding two weak residuals into force noise.
- failure signal that would falsify this proposal: simpler proposal_002 or proposal_007 matches/exceeds it, or hybrid improves train energy while worsening ISO17 gap.

## ablation_or_control
- required control or comparison: exact source control plus single-axis proposals 002 and 007 if selected.
- optional zero-gate / source-fallback / readout-only ablation: zero RoPE scale leaves latent q readout; zero conditioned scale leaves source; AUX_WEIGHT=0 isolates regularizer impact.

## implementation_notes_for_subagent
Implement the smallest hybrid, not two full proposals glued together. Use readout-only RoPE context and label-free q conditioning; do not touch interaction blocks, body-order branch, dataloader, evaluator, or `config.json`.
