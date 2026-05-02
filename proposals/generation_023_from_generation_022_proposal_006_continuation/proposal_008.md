# Proposal 008: Bounded learned-sigma LES tail

- family: les_tail_learned_sigma_bounded
- phase: 5
- jump_type: jump
- budget_class: medium
- expected_capability_gain: Bounded learned-sigma LES tail; adapt range separation without changing benchmark semantics

## one_sentence_hypothesis
A bounded learnable sigma for the nonperiodic LES tail may find the appropriate range separation for the current molecules while keeping beta capped and preserving source fallback.

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
- not_a_duplicate_of: Not a duplicate of fixed-sigma proposals_001/003/004 because it learns sigma within a safe interval instead of choosing a fixed range. Not a duplicate of capacity/training proposals because it is a mechanism parameter inside the LES tail only.
- lesson_used: The evidence supports the LES kernel but not a specific sigma for this benchmark; bounded sigma learning tests that uncertainty without importing periodic Ewald or changing data.

## why_not_duplicate
Not a duplicate of fixed-sigma proposals_001/003/004 because it learns sigma within a safe interval instead of choosing a fixed range. Not a duplicate of capacity/training proposals because it is a mechanism parameter inside the LES tail only.

## benchmark_rationale
- capacity/scaling hypothesis, if any: none; this is bounded mechanism calibration.
- rmd17 energy: may improve or remain neutral if sigma learns to suppress harmful near-pair effects.
- rmd17 force: medium risk; bounded sigma in [0.7, 2.5] and beta cap 0.003 limit singular/noisy gradients.
- rmd17 gap / Q: reject if learned sigma/beta drifts to a regime that worsens RMD17 gap without ISO17 gain.
- iso17 energy: target improved mixed_energy_mae and other_energy_mae by adapting range separation.
- iso17 force: should remain conservative; monitor whether sigma learning hurts mixed_force_mae.
- iso17 gap / Q: target source gap_penalty=0.153666 and Q_iso17=3.757687.
- training stability / runtime risk: medium; two scalar learnables plus O(N^2), no train.py change.
- control comparison expectation: if learned sigma beats fixed sigma, it justifies future bounded LES calibration; if not, prefer simpler fixed-sigma tails.

## files_to_edit
- `model/model.py`
- none (`model/train.py` unchanged)
- never `config.json` for MLIP-quality changes

## code_insertion_points
- `model/model.py::EvolutionMLIP.__init__`: add `les_tail_beta_logit=-7.0`, `les_tail_beta_cap=0.003`, and `les_tail_sigma_logit=0.0` mapped to `sigma = 0.7 + 1.8*sigmoid(logit)`.
- `model/model.py::EvolutionMLIP.forward_energy`: compute sigma each forward, build the all-pair nonperiodic LES kernel with that sigma, mask diagonal, and add the beta-capped tail after current charge neutralization.
- `model/train.py`: no change.

## minimal_edit_plan
1. Add beta and sigma logits with safe caps/ranges in `__init__`.
2. Map sigma logit to a bounded positive range in `forward_energy`.
3. Add the all-pair LES tail on top of the source shell term, preserving zero-beta source fallback.

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
- primary expected gain: ISO17 energy/gap improvement by fitting range separation to benchmark molecules.
- expected tradeoff: learned sigma adds a degree of freedom that may overfit or destabilize forces.
- failure signal that would falsify this proposal: learned-sigma variant underperforms fixed-sigma conservative/strong variants or worsens RMD17 force/gap.

## ablation_or_control
- required control or comparison: compare against fixed sigma proposals_001 and _003 plus exact source replicate.
- optional zero-gate / source-fallback / readout-only ablation: beta zero recovers the source regardless of learned sigma.

## implementation_notes_for_subagent
Mechanism detail to preserve in implementation: GEN023-M01-les-realspace-latent-charge-tail maps the LES paper form `q_i = Q_phi(B_i)` and `E = sum_i E_sr(B_i) + E_lr` to the current neutral latent charge head. The benchmark-compatible nonperiodic real-space tail is `E_tail = beta_tail * 0.5 * sum_{i != j} q_i q_j erf(d_ij/(sqrt(2)*sigma))/d_ij`, with diagonal masked to zero. Code trace is fresh repo evidence from BingqingCheng/cace: `cace/modules/les_wrapper.py::LesWrapper.forward` feeds learned latent charges and writes `E_lr`, while `cace/modules/ewald.py::EwaldPotential.compute_potential_realspace` constructs `[N,N,3]` pair displacements, distances, `erf(r/(sigma*sqrt(2)))`, inverse distance, and the pair sum. Insert only in `model/model.py::EvolutionMLIP.__init__` and `model/model.py::EvolutionMLIP.forward_energy`; keep `model/train.py` unchanged unless this proposal says otherwise.

Keep sigma bounded; do not expose it through config.json, and do not use cell/PBC/reciprocal Ewald paths.
