# Proposal 003: Stronger LES tail with sigma=1.5 and beta cap 0.004

- family: les_tail_stronger_sigma15
- phase: 5
- jump_type: jump
- budget_class: small
- expected_capability_gain: Stronger LES tail with sigma=1.5 and beta cap 0.004; target ISO17 gap transfer

## one_sentence_hypothesis
A moderately stronger LES tail with a smoother sigma should extend latent-charge interactions across all molecular pairs and may improve ISO17 other-molecule energy/gap more than the near-zero probes.

## mechanism_refs
- GEN023-M01-les-realspace-latent-charge-tail

## evidence_refs
- evidence_brief_20260501T153754Z.md
- mechanism_cards.json: GEN023-M01-les-realspace-latent-charge-tail
- patch_blueprints.json: blueprint GEN023-M01-les-realspace-latent-charge-tail
- proposal_constraints.json: allowed_mechanisms=[GEN023-M01-les-realspace-latent-charge-tail]
- paper_artifact:paper_001: LES Eq. (1) latent charges q_i = Q_phi(B_i), learned from energy/forces
- repo_artifact:repo_001: BingqingCheng/cace, cace/modules/les_wrapper.py::LesWrapper.forward, cace/modules/ewald.py::EwaldPotential.compute_potential_realspace
- current_unit_profile: generation_022/proposal_006 already has neutral charge_head over residual_input=[scalar_state, ||vector_state||]

## historical_relation
- source_unit: generation_022/proposal_006
- relation_to_source: jump
- not_a_duplicate_of: Not a duplicate of proposal_001/002 because cap and sigma are materially larger and the proposal tests a stronger electrostatic regime. Not a duplicate of generation_022/proposal_004 because that was still a cutoff electronic pair gate, not CACE LES all-pair real-space.
- lesson_used: Generation_022/proposal_006 was the best non-control charge-shell child but still below control; a stronger LES variant is justified only as a bounded jump with explicit failure criteria.

## why_not_duplicate
Not a duplicate of proposal_001/002 because cap and sigma are materially larger and the proposal tests a stronger electrostatic regime. Not a duplicate of generation_022/proposal_004 because that was still a cutoff electronic pair gate, not CACE LES all-pair real-space.

## benchmark_rationale
- capacity/scaling hypothesis, if any: none.
- rmd17 energy: may slightly improve due to smoother long-range energy but risks overfitting global pair energy.
- rmd17 force: moderate risk of long-range force components; sigma=1.5 smooths short distances to avoid singular force spikes.
- rmd17 gap / Q: tolerate only small gap movement; reject if RMD17 Q falls toward generation_022/proposal_002/008 levels.
- iso17 energy: primary target; stronger tail should attack other_energy_mae=0.283071 and mixed_energy_mae=0.262740.
- iso17 force: may remain stable because forces are conservative and kernel is smooth, but monitor mixed_force_mae=0.148905.
- iso17 gap / Q: target gap_penalty=0.153666 and Q_iso17=3.757687; a real win should beat source by more than noise.
- training stability / runtime risk: medium due to stronger beta; still only O(N^2), no dataloader or launch changes.
- control comparison expectation: must beat control Q_total=4.052381 or produce a clear ISO17 improvement large enough to justify later refinement.

## files_to_edit
- `model/model.py`
- none (`model/train.py` unchanged)
- never `config.json` for MLIP-quality changes

## code_insertion_points
- `model/model.py::EvolutionMLIP.__init__`: add `les_tail_beta_logit = nn.Parameter(torch.tensor(-6.0))`, `les_tail_beta_cap = 0.004`, and fixed `les_tail_sigma = 1.5`.
- `model/model.py::EvolutionMLIP.forward_energy`: after neutral charge construction, compute all-pair nonperiodic LES `erf(d/(sqrt(2)*1.5))/d` and add it in addition to the source shell energy.
- `model/train.py`: no change.

## minimal_edit_plan
1. Add stronger beta gate and sigma constants.
2. Implement all-pair `[N,N]` distance/kernel with diagonal zeroed and `0.5` pair-energy factor.
3. Add the tail to the final energy return while preserving current cutoff shell, body-order residual, energy residual, and readout terms.

## implementation_checklist
- [ ] Preserve `E = sum_i E_i` plus additive scalar residual terms and force-from-energy autograd contract.
- [ ] Preserve benchmark metric field names, split semantics, dataset semantics, and runnable entrypoint contract.
- [ ] Modify only the allowed target unit files.
- [ ] Do not edit `config.json`; change MLIP knobs in `model/model.py` or `model/train.py` only if explicitly listed.
- [ ] Keep tensor shapes compatible with current dataloader and model forward: numbers `[N]`, positions `[N,3]`, charge `[N]`, LES pair matrix `[N,N]`.
- [ ] Add no unbounded cubic neighbor/triplet loops; the only all-pair operation may be the explicit O(N^2) nonperiodic LES tail justified for current small molecules.
- [ ] Do not add PBC, reciprocal Ewald, cell inputs, charge labels, or a charge-equilibration solve.
- [ ] Call `mark_unit_implemented.py --unit <UNIT> --actor implementation_subagent` after edits.

## expected_benchmark_effect
- primary expected gain: larger ISO17 energy/gap improvement than conservative probes.
- expected tradeoff: greater risk to RMD17 force/gap and runtime.
- failure signal that would falsify this proposal: stronger cap improves neither ISO17 energy nor Q_total, or causes RMD17 gap/force regression.

## ablation_or_control
- required control or comparison: compare to proposal_001/002 for beta-strength response and to source/control replicate for variance.
- optional zero-gate / source-fallback / readout-only ablation: zero beta should recover proposal_006; sigma only matters when beta is nonzero.

## implementation_notes_for_subagent
Mechanism detail to preserve in implementation: GEN023-M01-les-realspace-latent-charge-tail maps the LES paper form `q_i = Q_phi(B_i)` and `E = sum_i E_sr(B_i) + E_lr` to the current neutral latent charge head. The benchmark-compatible nonperiodic real-space tail is `E_tail = beta_tail * 0.5 * sum_{i != j} q_i q_j erf(d_ij/(sqrt(2)*sigma))/d_ij`, with diagonal masked to zero. Code trace is fresh repo evidence from BingqingCheng/cace: `cace/modules/les_wrapper.py::LesWrapper.forward` feeds learned latent charges and writes `E_lr`, while `cace/modules/ewald.py::EwaldPotential.compute_potential_realspace` constructs `[N,N,3]` pair displacements, distances, `erf(r/(sigma*sqrt(2)))`, inverse distance, and the pair sum. Insert only in `model/model.py::EvolutionMLIP.__init__` and `model/model.py::EvolutionMLIP.forward_energy`; keep `model/train.py` unchanged unless this proposal says otherwise.

Do not implement periodic Ewald despite the repo filename; use only `compute_potential_realspace` pattern for nonperiodic molecules.
