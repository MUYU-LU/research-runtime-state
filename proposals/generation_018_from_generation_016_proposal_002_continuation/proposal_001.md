# Proposal 001: Damped Euclidean RoPE global context between local interaction blocks

- family: euclidean_rope_global_sidechannel
- phase: 4
- jump_type: jump
- budget_class: medium
- expected_capability_gain: add bounded nonlocal atom context to reduce ISO17 energy/gap error without replacing the successful generation_016 local message backbone.

## one_sentence_hypothesis
A small-M Euclidean rotary global-attention side-channel, zero/damped initialized and inserted between current local interaction blocks, should improve conformer/global energy transfer while preserving the existing local force fit and force-from-energy contract.

## mechanism_refs
- G018-MECH-001

## evidence_refs
- paper_artifact:paper_001
- repo_artifact:repo_001
- patch_blueprints.json:G018-MECH-001
- proposal_constraints.json:allowed_mechanisms.G018-MECH-001
- generation_017 outcome report: no child beat parent; PaiNN/local repairs were tradeoffs, so this branch changes the mechanism axis.

## historical_relation
- source_unit: generation_016/proposal_002
- relation_to_source: jump
- not_a_duplicate_of: generation_017/proposal_001/proposal_002/proposal_003/proposal_004/proposal_005 because those stayed in PaiNN/body-order/norm-dot local mixing; this adds an all-atom RoPE context path from G018-MECH-001.
- lesson_used: generation_017 benchmark tradeoffs suggest not adding another local scalar/vector gate; use zero/damped global residual so parent behavior is recoverable at initialization.

## benchmark_rationale
- rmd17 energy: source already has strong RMD17 mixed_energy_mae 0.03278; keep the global residual small so local energy quality does not regress.
- rmd17 force: new path is differentiable in centered positions; cap frequencies and residual scale to avoid noisy high-frequency force gradients.
- rmd17 gap / Q: expected small positive or neutral; RMD17 is not the main target, but Q should not drop if the residual stays bounded.
- iso17 energy: source ISO17 energy worsened during training and mixed_energy_mae is 0.30586; nonlocal context targets conformer/global state missing from cutoff-only interactions.
- iso17 force: force MAE is competitive but not enough to offset energy/gap; preserve the current local branch as the dominant force path.
- iso17 gap / Q: should reduce gap_penalty 0.11347 by giving each atom a molecule-level context before readout.
- training stability / runtime risk: O(N*M*Dq*Dv) overhead with M<=10, Dq/Dv<=H/2; initialize residual logit near -5 and avoid pairwise O(N^2) attention tables.
- control comparison expectation: should beat a control replicate only if ISO17 mixed_energy_mae/gap improve without RMD17 force regression.

## files_to_edit
- `model/model.py`
- `model/train.py` none
- never `config.json` for MLIP-quality changes

## code_insertion_points
- `model/model.py::GlobalRoPEAttentionSideChannel`: add a PyTorch-only module after `BalancedInteractionBlock` or immediately before `EvolutionMLIP`.
- `model/model.py::EvolutionMLIP.__init__`: add `self.global_contexts = nn.ModuleList([...])` parallel to `self.interactions`, fixed normalized direction/frequency buffers, and a trainable residual scale initialized to a small value.
- `model/model.py::EvolutionMLIP.forward_energy`: after each `interaction(...)` call in the lines 323-332 loop, compute `delta = global_context(scalar_state, positions)` using centered positions and add `sigmoid(scale) * delta` to `scalar_state`.
- `model/train.py`: no loss, optimizer, dataloader, metric, or entrypoint change.

## minimal_edit_plan
1. Implement `GlobalRoPEAttentionSideChannel` with fixed directions, low frequencies, q/k/v projections, rotary pair rotation, graph-wide `kv = einsum('nmd,nh->mdh', ...)`, and output projection back to `[N,H]`.
2. Center positions as `positions - positions.mean(dim=0, keepdim=True)` inside the module; never detach positions.
3. Wire one side-channel per interaction block with `M<=10`, even `Dq`, `Dv<=hidden_dim//2`, dropout off by default, and residual scale near zero.
4. Keep existing neighbor graph, RBF, body_order_branch, readout, and train/eval contracts unchanged.

## implementation_checklist
- [ ] Preserve `E = sum_i E_i` and force-from-energy contract.
- [ ] Preserve benchmark metric field names and runnable entrypoint contract.
- [ ] Modify only the allowed target unit files.
- [ ] Do not edit `config.json`; change MLIP knobs in `model/model.py` or `model/train.py`.
- [ ] Keep tensor shapes compatible with current dataloader and model forward.
- [ ] Add no unbounded cubic neighbor/triplet loops unless explicitly justified by budget.
- [ ] Keep attention cost bounded by small fixed direction count; no all-pairs attention matrix.
- [ ] Call `mark_unit_implemented.py --unit <UNIT> --actor implementation_subagent` after edits.

## expected_benchmark_effect
- primary expected gain: ISO17 energy/gap and total Q via nonlocal geometry-aware context.
- expected tradeoff: moderate runtime increase and possible small RMD17 force regression if frequencies are too high.
- failure signal that would falsify this proposal: ISO17 energy/gap does not improve over source/control or RMD17 mixed_force_mae worsens enough to lower Q_total.

## ablation_or_control
- required control or comparison: exact generation_016/proposal_002 control replicate and generation_017 control outcomes.
- optional zero-gate / source-fallback / readout-only ablation: residual scale fixed at zero should reproduce source behavior; optional M=6 vs M=10 direction comparison.

## implementation_notes_for_subagent
Use only native PyTorch. The side-channel must be a residual supplement, not a rewrite. If implementation time is tight, implement the single-graph version assumed by current dataloaders and document that it uses the batch semantics already present in `forward_energy`.
