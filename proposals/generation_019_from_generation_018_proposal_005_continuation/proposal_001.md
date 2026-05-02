# Proposal 001: Near-zero rank-2 Cartesian TP sibling

- family: rank2_cartesian_tp_sibling
- phase: 4
- jump_type: exploit
- budget_class: small
- expected_capability_gain: Add bounded symmetric-traceless angular anisotropy while preserving the generation_018/proposal_005 scalar-vector TP win.

## one_sentence_hypothesis
A near-zero gated S(u)=u⊗u-I/3 branch inside TPInteractionBranch should reduce ISO17 energy/gap aliasing without giving up the RMD17 force/energy gains from the existing l=0/l=1 tensor-product path.

## mechanism_refs
- GEN019-M01-rank2-cartesian-tp-sibling

## evidence_refs
- evidence_brief_20260430T111940Z.md
- mechanism_cards.json::GEN019-M01-rank2-cartesian-tp-sibling
- patch_blueprints.json::GEN019-M01-rank2-cartesian-tp-sibling
- paper_artifact:paper_001 HotPP/TensorNet Cartesian contraction evidence
- repo_artifact:repo_001 torchmd-net TensorNet I/A/S radial message code trace
- benchmark_diagnosis.json for source metrics

## historical_relation
- source_unit: generation_018/proposal_005
- relation_to_source: exploit
- not_a_duplicate_of: Not a duplicate of generation_018/proposal_005 because it keeps its five l=0/l=1 radial TP weights unchanged and adds only a separately gated rank-2 S-channel; not generation_018/proposal_006 because this is full-stack and source-preserving rather than first-layer-only.
- lesson_used: The winning signal was explicit scalar-vector TP; first-layer-only TP regressed energy, so the new path must be all-layer, damped, and ablatable instead of replacing the source branch.

## why_not_duplicate
Not a duplicate of generation_018/proposal_005 because it keeps its five l=0/l=1 radial TP weights unchanged and adds only a separately gated rank-2 S-channel; not generation_018/proposal_006 because this is full-stack and source-preserving rather than first-layer-only. The source unit is already a frontier win, so this proposal is deliberately scoped around preserving its explicit scalar-vector tensor-product signal unless the proposal is the exact control or backward-simplification branch.

## benchmark_rationale
Current source generation_018/proposal_005 is the best-known unit: Q_total=4.049988, Q_rmd17=4.199739, Q_iso17=3.771881, G_delta=+0.107440 over generation_016/proposal_002. RMD17 is already strong (mixed_energy_mae=0.029077, mixed_force_mae=0.060116, gap_penalty=0.007114). ISO17 remains the main headroom (mixed_energy_mae=0.244736, mixed_force_mae=0.149781, gap_penalty=0.145198). Generation_018/proposal_003 showed a nearby product-basis branch can approach the frontier (Q_total=4.025879) mostly through ISO17 force/geometry, while first-layer-only TP and RoPE variants regressed Q_total. The control from generation_018/proposal_008 reached Q_total=3.931143, so small gains must clear source variance rather than only beat the old parent.
- capacity/scaling hypothesis, if any: No broad capacity increase; adds O(E*H*5) rank-2 basis/projection only.
- rmd17 energy: Source mixed_energy_mae is 0.029077 with improving train/val energy; proposal should not regress this beyond neutral variance.
- rmd17 force: Source mixed_force_mae is 0.060116 and is the strongest part of the branch; any force regression must be treated as a failure unless Q_total improves clearly and gap is controlled.
- rmd17 gap / Q: Source gap_penalty is 0.007114 and Q_dataset/Q_rmd17 is 4.199739; preserve this as the benchmark anchor.
- iso17 energy: Source mixed_energy_mae is 0.244736 with within/other energy split 0.212976/0.265909; this is the main improvement target.
- iso17 force: Source mixed_force_mae is 0.149781; keep neutral-to-positive force behavior and avoid force-only gains that worsen energy.
- iso17 gap / Q: Source gap_penalty is 0.145198 and Q_dataset/Q_iso17 is 3.771881; useful proposals should lower gap or raise Q_iso17 without harming Q_rmd17.
- training stability / runtime risk: Primary target is ISO17 mixed_energy_mae and gap_penalty; RMD17 metrics should remain within neutral variance because residual_logit starts near -5 and scalar/vector TP scales are preserved.
- control comparison expectation: Compare against proposal_008 exact source replicate and the source metrics above; Q_total must be interpreted relative to control variance, not force-only ranking.

## files_to_edit
- `model/model.py`
- `model/train.py` only to preserve constants/metrics if touched; otherwise `none`
- never `config.json` for MLIP-quality changes

## code_insertion_points
- `model/model.py::TPInteractionBranch.__init__`: add `rank2_edge_mlp` or extend the existing edge MLP to produce `w_S`; add `rank2_norm`, `rank2_out`, `rank2_gate`, and `rank2_residual_logit` initialized near -5.
- `model/model.py::TPInteractionBranch.forward`: after `w_ss,w_vs,w_sv,w_vp,w_vself`, compute `S=[ux^2-1/3, ux*uy, ux*uz, uy^2-1/3, uy*uz]`, form `[E,H,5]`, scatter to `[N,H,5]`, normalize by neighbor count, project to `delta_rank2_scalar`.
- `model/model.py::EvolutionMLIP.forward_energy`: add `rank2_delta_scalar` to the scalar residual combine after each TP branch while preserving existing `delta_scalar`/`delta_vector` scales.
- `model/train.py`: no training semantic change; preserve `TRAIN_ENERGY_WEIGHT=1.0`, `TRAIN_FORCE_WEIGHT=20.0`, grad clipping, and metric logging.

## minimal_edit_plan
1. Do not remove or reinitialize the existing TPInteractionBranch l=0/l=1 paths.
2. Add a pure-torch symmetric-traceless basis helper in TPInteractionBranch.forward and scatter-add it with current `i_idx`/`j_idx`.
3. Project the rank-2 aggregate to `[N,H]` through a tiny initialized output layer and multiply by `0.1*sigmoid(rank2_residual_logit)`.
4. Return/include the rank-2 scalar delta in the per-interaction update; keep vector_state update unchanged.

## implementation_checklist
- [ ] Preserve `E = sum_i E_i` and force-from-energy contract.
- [ ] Preserve benchmark metric field names and runnable entrypoint contract.
- [ ] Modify only the allowed target unit files.
- [ ] Do not edit `config.json`; change MLIP knobs in `model/model.py` or `model/train.py`.
- [ ] Keep tensor shapes compatible with current dataloader and model forward.
- [ ] Add no unbounded cubic neighbor/triplet loops unless explicitly justified by budget.
- [ ] Preserve the existing scalar-vector `TPInteractionBranch` path unless this proposal is the explicit control/simplification case.
- [ ] Call `mark_unit_implemented.py --unit <UNIT> --actor implementation_subagent` after edits.

## expected_benchmark_effect
- primary expected gain: Expected to lift Q_iso17 through lower mixed_energy_mae and gap_penalty; Q_rmd17 should stay close to 4.199739 with at most tiny runtime increase. Falsified if RMD17 mixed_force_mae or mixed_energy_mae regresses beyond neutral variance or Q_total falls below the source/control envelope.
- expected tradeoff: Runtime, memory, or optimization risk must be judged against Q_dataset/Q_rmd17/Q_iso17/Q_total, not a single force metric. For tiny/control proposals the tradeoff should be interpretability rather than capacity.
- failure signal that would falsify this proposal: Q_total below the source/control envelope, RMD17 force or energy regression beyond neutral variance, ISO17 gap_penalty worse without compensating Q gain, smoke/runtime failure, or loss of force-from-energy behavior.

## ablation_or_control
- required control or comparison: Compare against exact source control and a zero-gate rank2_residual_logit ablation; any gain should disappear when rank2 is frozen near zero.
- optional zero-gate / source-fallback / readout-only ablation: Keep every new residual source-recoverable by a zero/very-negative gate when the proposal includes a branch; for control, no ablation beyond exact copy is needed.

## implementation_notes_for_subagent
Use only PyTorch tensor ops; no Warp/e3nn dependency. Keep hidden_dim=96, num_rbf=32, cutoff=5.0, num_interactions=2. Implement only inside the materialized target unit. Do not edit global round state, proposal files, selection files, benchmark data, evaluator code, or `config.json` for MLIP quality. Preserve the generation_018/proposal_005 tensor shapes: scalar_state `[N,H]`, vector_state `[N,H,3]`, edge basis `[E,num_rbf]`, energy scalar, forces `[N,3]` by autograd.
