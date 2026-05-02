# Proposal 009: Smooth outer-domain LES tail beyond the source cutoff

- family: les_tail_outer_cutoff_taper
- phase: 5
- jump_type: exploit
- budget_class: small
- expected_capability_gain: Test LES long-range physics only outside the existing 5A cutoff shell to avoid double-counting local charge calibration

## one_sentence_hypothesis
Adding a smooth, capped LES real-space tail that is effectively active only beyond the current cutoff should isolate the missing long-range latent-charge signal while leaving the source cutoff shell to handle local calibration.

## mechanism_refs
- GEN023-M01-les-realspace-latent-charge-tail

## evidence_refs
- evidence_brief_20260501T153754Z.md
- mechanism_cards.json: GEN023-M01-les-realspace-latent-charge-tail
- patch_blueprints.json: blueprint GEN023-M01-les-realspace-latent-charge-tail
- proposal_constraints.json: allowed_mechanisms=[GEN023-M01-les-realspace-latent-charge-tail]
- paper_artifact:paper_001: LES Eq. (1) latent charges `q_i = Q_phi(B_i)` and range split `E = sum_i E_sr(B_i) + E_lr`
- repo_artifact:repo_001: BingqingCheng/cace `cace/modules/les_wrapper.py::LesWrapper.forward`, `cace/modules/ewald.py::EwaldPotential.forward`, and `cace/modules/ewald.py::EwaldPotential.compute_potential_realspace`
- current_unit_profile: generation_022/proposal_006 computes neutral latent charges from `residual_input=[scalar_state, ||vector_state||]` and uses only directed cutoff edges for its existing q_i q_j shell term
- benchmark_diagnosis.json: source Q_total=4.042395946355124, RMD17 gap_penalty=0.010653186008917345, ISO17 gap_penalty=0.1536659406879372, ISO17 val-energy trend worsening

## historical_relation
- source_unit: generation_022/proposal_006
- relation_to_source: exploit
- not_a_duplicate_of: Not a duplicate of proposals_001/002/003/004/007/008 because those apply the LES kernel to all nonself pairs without explicitly suppressing the inside-cutoff contribution. Not a duplicate of proposal_005 because it keeps the source cutoff shell instead of replacing it. Not a duplicate of proposal_006 because it adds a nonperiodic all-pair distance matrix and smooth outer-domain LES tail.
- lesson_used: The source already contains a useful local multishell charge correction but underperformed a control replicate; the evidence asks whether the missing mechanism is the LES real-space long-range domain rather than another local radial-shell perturbation.

## why_not_duplicate
This proposal uniquely gates the LES tail by a smooth outer-cutoff taper `S(d)` so the new mechanism tests beyond-cutoff latent electrostatics while preserving the source's local cutoff shell. Existing generation_023 proposals vary beta, sigma, charge normalization, learned sigma, or shell replacement; none isolate only the outside-cutoff LES domain.

## benchmark_rationale
- capacity/scaling hypothesis, if any: none; this is a domain/taper mechanism test with only one scalar beta gate and one fixed taper width.
- rmd17 energy: should stay close to source mixed_energy_mae=0.0289746 because local within-cutoff energy calibration remains handled by the existing shell term.
- rmd17 force: lower force-noise risk than full all-pair stacked tails because near-pair gradients from the new branch are suppressed by the smooth taper.
- rmd17 gap / Q: should protect source Q_rmd17=4.1957007 better than stronger all-pair tails; reject if gap_penalty rises without ISO17 benefit.
- iso17 energy: primary target is other/mixed energy transfer; beyond-cutoff charge interactions may reduce ISO17 mixed_energy_mae=0.2627397 and the worsening validation energy trend.
- iso17 force: expected neutral to mildly improved if the longer-distance conservative gradient is useful; taper should avoid near-distance force spikes.
- iso17 gap / Q: target a reduction in ISO17 gap_penalty=0.1536659 without sacrificing RMD17.
- training stability / runtime risk: O(N^2) pair matrix, but only scalar operations and smooth bounded gates; no train.py change.
- control comparison expectation: should be compared to proposal_001 full all-pair conservative tail and proposal_006 exact source replicate to decide whether inside-cutoff LES contributions are helpful or harmful.

## files_to_edit
- `model/model.py`
- none (`model/train.py` unchanged)
- never `config.json` for MLIP-quality changes

## code_insertion_points
- `model/model.py::EvolutionMLIP.__init__`: add `les_outer_beta_logit = nn.Parameter(torch.tensor(-7.5))`, `les_outer_beta_cap = 0.0025`, fixed `les_outer_sigma = 1.2`, fixed `les_outer_cutoff = self.cutoff` or `5.0`, and fixed `les_outer_taper_width = 0.5` as simple attributes/buffers.
- `model/model.py::EvolutionMLIP.forward_energy`: after `charge = charge_raw - charge_raw.mean()`, build the nonperiodic pair displacement matrix `all_rij = positions[:, None, :] - positions[None, :, :]`, distances `all_dij`, diagonal mask, LES kernel `erf(all_dij/(sqrt(2)*sigma))/all_dij`, and a smooth outer taper `S(d)=sigmoid((d-les_outer_cutoff)/les_outer_taper_width)` with diagonal zeroed.
- `model/model.py::EvolutionMLIP.forward_energy`: add `E_outer = beta_outer * 0.5 * sum_{i != j} q_i q_j S(d_ij) erf(d_ij/(sqrt(2)*sigma))/d_ij` to the final scalar energy while leaving the existing cutoff shell term unchanged.
- `model/train.py`: no change.

## minimal_edit_plan
1. Add one capped beta gate and fixed sigma/cutoff/taper constants in `EvolutionMLIP.__init__`, initialized near zero for source fallback.
2. Reuse the existing neutralized latent `charge`; do not add charge labels, charge equilibration, PBC, cell, or reciprocal Ewald inputs.
3. Compute the all-pair direct real-space LES kernel and multiply by a smooth outer-cutoff taper before summing `0.5 * q_i*q_j*K_ij`.
4. Add the tapered LES outer-domain scalar to the current energy return without removing the source shell, body-order residual, atomref/readout, or force-from-energy path.

## implementation_checklist
- [ ] Preserve `E = sum_i E_i` plus additive scalar residual terms and force-from-energy autograd contract.
- [ ] Preserve benchmark metric field names, split semantics, dataset semantics, and runnable entrypoint contract.
- [ ] Modify only the allowed target unit files.
- [ ] Do not edit `config.json`; keep MLIP knobs in `model/model.py`/`model/train.py` only.
- [ ] Keep tensor shapes compatible with current dataloader and model forward: numbers `[N]`, positions `[N,3]`, charge `[N]`, LES pair matrix `[N,N]`.
- [ ] Add no unbounded cubic neighbor/triplet loops; the only all-pair operation may be the explicit O(N^2) nonperiodic LES tail justified for current small molecules.
- [ ] Do not add PBC, reciprocal Ewald, cell inputs, system-charge labels, or a charge-equilibration solve.
- [ ] Keep the taper smooth/differentiable and diagonal-masked so autograd forces remain finite.
- [ ] Call `mark_unit_implemented.py --unit <UNIT> --actor implementation_subagent` after edits.

## expected_benchmark_effect
- primary expected gain: ISO17 energy/gap improvement from beyond-cutoff latent electrostatics with less RMD17 force/gap regression than ungated all-pair tails.
- expected tradeoff: if most useful LES signal lies inside the cutoff, this outer-only variant may be weaker than proposal_001/003.
- failure signal that would falsify this proposal: no ISO17 Q gain over source/control or worse RMD17 force/gap despite suppressing near-pair tail contributions.

## ablation_or_control
- required control or comparison: compare against proposal_001 near-zero full all-pair tail, proposal_005 shell-disabled LES ablation, and proposal_006 exact source replicate.
- optional zero-gate / source-fallback / readout-only ablation: setting `beta_outer=0` must algebraically recover generation_022/proposal_006, because the source shell remains unchanged.

## implementation_notes_for_subagent
Mechanism detail to preserve: GEN023-M01 maps LES latent charges `q_i = Q_phi(B_i)` and range-separated energy `E = sum_i E_sr(B_i) + E_lr` onto the current neutral latent charge head. The current source already has `q_raw_i = 0.1*tanh(charge_head([scalar_state_i, ||vector_state_i||]))`, `q_i = q_raw_i - mean(q_raw)`, and a cutoff-shell `E_shell = 0.5*sum_{directed cutoff edges} q_i q_j cutoff_weight_ij*(beta_near/sqrt(d_ij^2+1)+beta_mid/d_ij)`. This proposal adds only the outer-domain LES tail:

`E_outer = beta_outer * 0.5 * sum_{i != j} q_i q_j * sigmoid((d_ij-r_cut)/tau) * erf(d_ij/(sqrt(2)*sigma)) / d_ij`,

with diagonal masked to zero, `r_cut=5.0`, `tau=0.5`, `sigma=1.2`, and a near-zero capped `beta_outer`. The fresh repo trace is CACE `LesWrapper.forward` writing latent charges/E_lr and `EwaldPotential.compute_potential_realspace` constructing `[N,N,3]` displacements, `[N,N]` distances, `erf(r/(sigma*sqrt(2)))`, inverse distance, and pair sums. Use only the nonperiodic real-space pattern; do not import cell/PBC/reciprocal Ewald behavior.
