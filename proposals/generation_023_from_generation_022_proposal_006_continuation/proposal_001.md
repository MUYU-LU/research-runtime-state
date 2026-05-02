# Proposal 001: Near-zero capped LES tail

- family: les_tail_conservative_source_fallback
- phase: 5
- jump_type: exploit
- budget_class: small
- expected_capability_gain: Near-zero capped LES tail; ISO17 energy/gap lift while zero beta recovers generation_022/proposal_006

## one_sentence_hypothesis
Adding an all-nonself-pair LES real-space tail with a very small positive gate should test long-range latent-charge physics beyond the 5A cutoff while preserving the current source as an explicit zero-tail fallback.

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
- relation_to_source: exploit
- not_a_duplicate_of: Not a duplicate of generation_022/proposal_006 because proposal_006 only uses directed cutoff edges and shell kernels; this proposal adds an all-pair nonperiodic erf(1/r) LES tail. Not a duplicate of generation_022/proposal_001/002/003/004/005 because those did not use the CACE LES real-space all-pair code trace.
- lesson_used: Proposal_006 improved ISO17 Q over its parent but lost to the control replicate in Q_total; therefore beta_tail must be capped near zero and source fallback must be exact.

## why_not_duplicate
Not a duplicate of generation_022/proposal_006 because proposal_006 only uses directed cutoff edges and shell kernels; this proposal adds an all-pair nonperiodic erf(1/r) LES tail. Not a duplicate of generation_022/proposal_001/002/003/004/005 because those did not use the CACE LES real-space all-pair code trace.

## benchmark_rationale
- capacity/scaling hypothesis, if any: none; this is a mechanism-domain test, not capacity scaling.
- rmd17 energy: should remain close to source mixed_energy_mae=0.0289746 because beta_tail is capped at <=0.002 and initialized nearly zero.
- rmd17 force: risk is added long-range force noise; tiny cap and smooth erf kernel should limit mixed_force_mae regression from 0.0604828.
- rmd17 gap / Q: reject if rmd17 gap_penalty worsens materially beyond source 0.010653 without ISO17 compensation.
- iso17 energy: primary target is ISO17 mixed_energy_mae=0.262740 and worsening val-energy trend; all-pair latent electrostatics may reduce other-molecule energy error.
- iso17 force: should be neutral/slightly improved if learned charges encode transferable electrostatics, but cap avoids force domination.
- iso17 gap / Q: target gap_penalty=0.153666 and Q_iso17=3.757687; a small gain here is the main reason to select this exploit.
- training stability / runtime risk: O(N^2) pair matrix per molecule but current molecules are small; no train.py change.
- control comparison expectation: beta_tail=0 should reproduce generation_022/proposal_006; compare also with best control generation_022/proposal_007 Q_total=4.052381.

## files_to_edit
- `model/model.py`
- none (`model/train.py` unchanged)
- never `config.json` for MLIP-quality changes

## code_insertion_points
- `model/model.py::EvolutionMLIP.__init__`: reuse `charge_head`; add `les_tail_beta_logit = nn.Parameter(torch.tensor(-8.0))`, `les_tail_beta_cap = 0.002`, and fixed `les_tail_sigma = 1.0` as a simple float/buffer.
- `model/model.py::EvolutionMLIP.forward_energy`: after `charge = charge_raw - charge_raw.mean()`, build `all_rij = positions[:,None,:] - positions[None,:,:]`, `all_dij`, mask diagonal, compute `erf(all_dij/(sqrt(2)*sigma))/all_dij`, and add the capped tail to the existing return energy.
- `model/train.py`: no change.

## minimal_edit_plan
1. Add the tail gate and sigma constants in `__init__`, initialized so beta is near zero.
2. Compute the nonperiodic all-pair LES kernel in `forward_energy` using `torch.erf`, with diagonal masked to zero and distances clamped.
3. Add `les_tail_beta * 0.5 * sum(q_i*q_j*kernel)` alongside the existing cutoff shell electrostatic pair energy; do not remove the source shell term.

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
- primary expected gain: small ISO17 energy/gap/Q improvement from beyond-cutoff latent electrostatics.
- expected tradeoff: minor runtime cost and possible tiny RMD17 force noise.
- failure signal that would falsify this proposal: Q_total remains below the source/control variance band or RMD17 mixed_force_mae/gap worsens without ISO17 Q gain.

## ablation_or_control
- required control or comparison: zero-beta fallback must be algebraically equivalent to generation_022/proposal_006, and full result must be compared against generation_022/proposal_007 control replicate.
- optional zero-gate / source-fallback / readout-only ablation: set beta cap/logit to produce exactly zero tail for a local sanity run before benchmark launch.

## implementation_notes_for_subagent
Mechanism detail to preserve in implementation: GEN023-M01-les-realspace-latent-charge-tail maps the LES paper form `q_i = Q_phi(B_i)` and `E = sum_i E_sr(B_i) + E_lr` to the current neutral latent charge head. The benchmark-compatible nonperiodic real-space tail is `E_tail = beta_tail * 0.5 * sum_{i != j} q_i q_j erf(d_ij/(sqrt(2)*sigma))/d_ij`, with diagonal masked to zero. Code trace is fresh repo evidence from BingqingCheng/cace: `cace/modules/les_wrapper.py::LesWrapper.forward` feeds learned latent charges and writes `E_lr`, while `cace/modules/ewald.py::EwaldPotential.compute_potential_realspace` constructs `[N,N,3]` pair displacements, distances, `erf(r/(sigma*sqrt(2)))`, inverse distance, and the pair sum. Insert only in `model/model.py::EvolutionMLIP.__init__` and `model/model.py::EvolutionMLIP.forward_energy`; keep `model/train.py` unchanged unless this proposal says otherwise.

Use no PBC or cell inputs; this is direct real-space LES only. Keep the current charge neutralization and shell pair term unchanged.
