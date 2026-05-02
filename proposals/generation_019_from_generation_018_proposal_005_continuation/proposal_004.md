# Proposal 004: Rank-2 TP plus CACE ν=2 consistency hybrid

- family: rank2_tp_cace_hybrid
- phase: 4
- jump_type: jump
- budget_class: medium
- expected_capability_gain: Combine the two strong evidence cards: TP S-channel angular messages and CACE-consistent invariant body-order energy residual.

## one_sentence_hypothesis
A source-preserving rank-2 TP sibling plus a tightened CACE ν=2 body-order descriptor should address both force-direction/angular aliasing and ISO17 energy-gap transfer better than either side path alone.

## mechanism_refs
- GEN019-M01-rank2-cartesian-tp-sibling
- GEN019-M02-cace-nu2-ab-consistency

## evidence_refs
- mechanism_cards.json::GEN019-M01-rank2-cartesian-tp-sibling
- mechanism_cards.json::GEN019-M02-cace-nu2-ab-consistency
- patch_blueprints.json both implementation-ready blueprints
- repo_artifact:repo_001 TensorNet I/A/S
- repo_artifact:repo_002 CACE AngularTensorProduct/Symmetrizer
- repo_artifact:repo_003 MACE symmetric contraction

## historical_relation
- source_unit: generation_018/proposal_005
- relation_to_source: jump
- not_a_duplicate_of: Not proposal_001 or proposal_005 alone because it deliberately tests interaction between the rank-2 TP angular channel and CACE invariant body-order branch; not generation_018/proposal_003 because it preserves the proven TP branch from proposal_005 as the main path.
- lesson_used: generation_018/proposal_003 was close to the frontier and proposal_005 was the frontier; a bounded combination tests whether their positive signals are complementary rather than mutually exclusive.

## why_not_duplicate
Not proposal_001 or proposal_005 alone because it deliberately tests interaction between the rank-2 TP angular channel and CACE invariant body-order branch; not generation_018/proposal_003 because it preserves the proven TP branch from proposal_005 as the main path. The source unit is already a frontier win, so this proposal is deliberately scoped around preserving its explicit scalar-vector tensor-product signal unless the proposal is the exact control or backward-simplification branch.

## benchmark_rationale
Current source generation_018/proposal_005 is the best-known unit: Q_total=4.049988, Q_rmd17=4.199739, Q_iso17=3.771881, G_delta=+0.107440 over generation_016/proposal_002. RMD17 is already strong (mixed_energy_mae=0.029077, mixed_force_mae=0.060116, gap_penalty=0.007114). ISO17 remains the main headroom (mixed_energy_mae=0.244736, mixed_force_mae=0.149781, gap_penalty=0.145198). Generation_018/proposal_003 showed a nearby product-basis branch can approach the frontier (Q_total=4.025879) mostly through ISO17 force/geometry, while first-layer-only TP and RoPE variants regressed Q_total. The control from generation_018/proposal_008 reached Q_total=3.931143, so small gains must clear source variance rather than only beat the old parent.
- capacity/scaling hypothesis, if any: Medium branch-combination budget; no hidden_dim/depth increase, but adds both O(E*H*5) and small descriptor product work.
- rmd17 energy: Source mixed_energy_mae is 0.029077 with improving train/val energy; proposal should not regress this beyond neutral variance.
- rmd17 force: Source mixed_force_mae is 0.060116 and is the strongest part of the branch; any force regression must be treated as a failure unless Q_total improves clearly and gap is controlled.
- rmd17 gap / Q: Source gap_penalty is 0.007114 and Q_dataset/Q_rmd17 is 4.199739; preserve this as the benchmark anchor.
- iso17 energy: Source mixed_energy_mae is 0.244736 with within/other energy split 0.212976/0.265909; this is the main improvement target.
- iso17 force: Source mixed_force_mae is 0.149781; keep neutral-to-positive force behavior and avoid force-only gains that worsen energy.
- iso17 gap / Q: Source gap_penalty is 0.145198 and Q_dataset/Q_iso17 is 3.771881; useful proposals should lower gap or raise Q_iso17 without harming Q_rmd17.
- training stability / runtime risk: Expected to target ISO17 mixed_energy_mae/gap while retaining RMD17 force; runtime/memory risk is higher than single-card exploits and must be monitored.
- control comparison expectation: Compare against proposal_008 exact source replicate and the source metrics above; Q_total must be interpreted relative to control variance, not force-only ranking.

## files_to_edit
- `model/model.py`
- `model/train.py` only if minor auxiliary safeguards are needed; otherwise `none`
- never `config.json` for MLIP-quality changes

## code_insertion_points
- `model/model.py::TPInteractionBranch`: implement proposal_001 rank-2 S-channel as a near-zero residual.
- `model/model.py::BodyOrderMessageBranch._angular_monomials/_symmetrize`: audit monomial ordering and add bounded CACE ν=2 contraction/projection back to descriptor_dim.
- `model/model.py::EvolutionMLIP.forward_energy`: preserve scalar-vector TP combine order and keep body_order_multiplier small.
- `model/train.py`: preserve fixed evaluation semantics and metric logging; no ISO17-only hacks.

## minimal_edit_plan
1. Implement the rank-2 S-channel first with a zero-recoverable gate.
2. Tighten BodyOrderMessageBranch to CACE ν=2 consistency with a projection initialized near source behavior.
3. Keep both added residuals independently gated so either can be ablated by setting its logit very negative.
4. Do not increase num_interactions, hidden_dim, cutoff, or num_rbf in this hybrid.

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
- primary expected gain: If complementarity is real, Q_total should exceed 4.049988 through Q_iso17 while Q_rmd17 remains near source. Expected tradeoff is moderate runtime and overfitting risk. Falsified by RMD17 regression, OOM/smoke failure, or gains only in one metric with worse gap penalty.
- expected tradeoff: Runtime, memory, or optimization risk must be judged against Q_dataset/Q_rmd17/Q_iso17/Q_total, not a single force metric. For tiny/control proposals the tradeoff should be interpretability rather than capacity.
- failure signal that would falsify this proposal: Q_total below the source/control envelope, RMD17 force or energy regression beyond neutral variance, ISO17 gap_penalty worse without compensating Q gain, smoke/runtime failure, or loss of force-from-energy behavior.

## ablation_or_control
- required control or comparison: Required comparisons: exact source, proposal_001-style rank2-only, proposal_005-style CACE-only; optional disable each residual gate independently.
- optional zero-gate / source-fallback / readout-only ablation: Keep every new residual source-recoverable by a zero/very-negative gate when the proposal includes a branch; for control, no ablation beyond exact copy is needed.

## implementation_notes_for_subagent
This is the broadest mechanism jump in the set; keep each sub-branch small and independently source-recoverable. Implement only inside the materialized target unit. Do not edit global round state, proposal files, selection files, benchmark data, evaluator code, or `config.json` for MLIP quality. Preserve the generation_018/proposal_005 tensor shapes: scalar_state `[N,H]`, vector_state `[N,H,3]`, edge basis `[E,num_rbf]`, energy scalar, forces `[N,3]` by autograd.
