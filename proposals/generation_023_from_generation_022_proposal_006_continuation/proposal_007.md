# Proposal 007: RMS-normalized latent charges before LES tail

- family: les_tail_charge_variance_control
- phase: 5
- jump_type: exploit
- budget_class: small
- expected_capability_gain: RMS-normalized latent charges before LES tail; reduce charge-scale variance risk

## one_sentence_hypothesis
Normalizing neutral latent charges to a tiny bounded RMS before the LES tail should test the real-space electrostatic kernel while preventing random charge-scale drift from dominating force and gap metrics.

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
- not_a_duplicate_of: Not a duplicate of proposal_001 because it adds a variance-control normalization around q before the LES tail. Not a duplicate of exact source control because it changes the mechanism branch while keeping source fallback through beta zero.
- lesson_used: Prior latent charge/electrostatic families mostly underperformed; controlling charge variance is a conservative way to test whether failures came from scale instability rather than the LES kernel itself.

## why_not_duplicate
Not a duplicate of proposal_001 because it adds a variance-control normalization around q before the LES tail. Not a duplicate of exact source control because it changes the mechanism branch while keeping source fallback through beta zero.

## benchmark_rationale
- capacity/scaling hypothesis, if any: none; normalization is a variance-control wrapper.
- rmd17 energy: expected close to source; q RMS clamp should prevent large electrostatic energy shifts.
- rmd17 force: lower risk than stronger variants because q_i magnitudes entering all-pair gradients are normalized/clamped.
- rmd17 gap / Q: should protect gap_penalty from worsening beyond source 0.010653.
- iso17 energy: may improve if transferable relative charge pattern matters more than raw charge scale.
- iso17 force: should be stable unless normalization introduces discontinuity; use smooth RMS with epsilon.
- iso17 gap / Q: target source Q_iso17=3.757687 and gap_penalty=0.153666 through stable all-pair signal.
- training stability / runtime risk: small/medium; O(N^2), plus smooth RMS normalization.
- control comparison expectation: if normalized-tail beats unnormalized conservative tail, future LES work should keep q scale control.

## files_to_edit
- `model/model.py`
- none (`model/train.py` unchanged)
- never `config.json` for MLIP-quality changes

## code_insertion_points
- `model/model.py::EvolutionMLIP.__init__`: add `les_tail_beta_logit=-7.0`, `les_tail_beta_cap=0.0025`, `les_tail_sigma=1.0`, and `les_charge_rms_target=0.05` as constants/buffers.
- `model/model.py::EvolutionMLIP.forward_energy`: after `charge = charge_raw - charge_raw.mean()`, compute `q_tail = charge * (target_rms / sqrt(mean(charge^2)+eps)).clamp(max=1.0)` or an equivalent smooth cap, then use `q_tail` only in the LES tail while leaving source shell energy on raw neutral charge.
- `model/train.py`: no change.

## minimal_edit_plan
1. Add beta/sigma constants and charge RMS target.
2. Build a smooth RMS-normalized `q_tail` for the LES branch only; keep original `charge` for existing shell term.
3. Add all-pair LES tail using `q_tail_i*q_tail_j` and capped beta.

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
- primary expected gain: stable ISO17 gap/energy improvement with less force risk than stronger raw-charge tails.
- expected tradeoff: RMS normalization may suppress useful learned charge magnitude information.
- failure signal that would falsify this proposal: no ISO17 benefit over proposal_001 or unexpected instability from the normalization.

## ablation_or_control
- required control or comparison: compare to proposal_001 unnormalized conservative LES and exact source replicate.
- optional zero-gate / source-fallback / readout-only ablation: beta zero recovers source; normalization exists only inside the tail branch.

## implementation_notes_for_subagent
Mechanism detail to preserve in implementation: GEN023-M01-les-realspace-latent-charge-tail maps the LES paper form `q_i = Q_phi(B_i)` and `E = sum_i E_sr(B_i) + E_lr` to the current neutral latent charge head. The benchmark-compatible nonperiodic real-space tail is `E_tail = beta_tail * 0.5 * sum_{i != j} q_i q_j erf(d_ij/(sqrt(2)*sigma))/d_ij`, with diagonal masked to zero. Code trace is fresh repo evidence from BingqingCheng/cace: `cace/modules/les_wrapper.py::LesWrapper.forward` feeds learned latent charges and writes `E_lr`, while `cace/modules/ewald.py::EwaldPotential.compute_potential_realspace` constructs `[N,N,3]` pair displacements, distances, `erf(r/(sigma*sqrt(2)))`, inverse distance, and the pair sum. Insert only in `model/model.py::EvolutionMLIP.__init__` and `model/model.py::EvolutionMLIP.forward_energy`; keep `model/train.py` unchanged unless this proposal says otherwise.

Use smooth differentiable normalization; do not detach charges unless necessary for numerical safety, because forces should remain energy-conservative through the full energy graph.
