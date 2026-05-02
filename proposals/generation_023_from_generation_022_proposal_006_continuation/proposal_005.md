# Proposal 005: Ablation isolates LES all-pair tail by disabling source cutoff charge shell

- family: les_tail_vs_cutoff_shell_ablation
- phase: 5
- jump_type: control
- budget_class: small
- expected_capability_gain: Ablation isolates LES all-pair tail by disabling source cutoff charge shell

## one_sentence_hypothesis
Replacing the existing cutoff shell electrostatic correction with a capped all-pair LES tail should reveal whether proposal_006 gains came from latent electrostatics or from ordinary cutoff residual calibration.

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
- relation_to_source: ablation
- not_a_duplicate_of: Not a duplicate of generation_022/proposal_008 because that ablated pair-vs-residual before the fresh LES evidence; this proposal specifically contrasts CACE LES all-pair real-space tail against the source cutoff shell. Not a duplicate of proposal_001 because it removes/disables the source shell term rather than stacking on top of it.
- lesson_used: The evidence card explicitly asks to distinguish latent-charge physics from local radial-shell noise; this is the direct mechanism isolation run.

## why_not_duplicate
Not a duplicate of generation_022/proposal_008 because that ablated pair-vs-residual before the fresh LES evidence; this proposal specifically contrasts CACE LES all-pair real-space tail against the source cutoff shell. Not a duplicate of proposal_001 because it removes/disables the source shell term rather than stacking on top of it.

## benchmark_rationale
- capacity/scaling hypothesis, if any: none.
- rmd17 energy: may worsen if the cutoff shell was acting as useful local calibration.
- rmd17 force: risk is similar or slightly lower than stacked tails because only one electrostatic branch remains.
- rmd17 gap / Q: if RMD17 Q falls sharply, the source shell was important local calibration rather than transferable LES physics.
- iso17 energy: if all-pair LES improves ISO17 while shell removal hurts little, that supports the mechanism.
- iso17 force: should be monitored because replacing local shell with global tail changes force distribution.
- iso17 gap / Q: the key readout is whether Q_iso17 stays near or above 3.757687 with shell disabled.
- training stability / runtime risk: small/medium; fewer shell parameters but O(N^2) matrix.
- control comparison expectation: interpret alongside exact source and stacked-tail proposals; this is not expected to be the best Q_total, it is a causal ablation.

## files_to_edit
- `model/model.py`
- none (`model/train.py` unchanged)
- never `config.json` for MLIP-quality changes

## code_insertion_points
- `model/model.py::EvolutionMLIP.__init__`: add `les_tail_beta_logit` cap 0.003 sigma 1.2; either set `charge_shell_beta_cap = 0.0` or omit `electrostatic_pair_energy` from the return as the ablation requires.
- `model/model.py::EvolutionMLIP.forward_energy`: keep existing charge neutralization, compute all-pair LES tail, and return energy with LES tail but without the current cutoff shell pair term.
- `model/train.py`: no change.

## minimal_edit_plan
1. Add the LES tail gate and sigma.
2. Disable the existing cutoff shell contribution in the final energy path while leaving charge_head construction intact.
3. Add the capped all-pair LES tail as the only q_i q_j electrostatic residual and document zero-tail behavior.

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
- primary expected gain: causal evidence separating LES all-pair physics from source shell calibration.
- expected tradeoff: Q_total may fall because this is an ablation/control.
- failure signal that would falsify this proposal: LES-only underperforms source on ISO17 and RMD17, indicating all-pair LES does not explain proposal_006 behavior.

## ablation_or_control
- required control or comparison: compare with proposal_001 stacked shell+tail and proposal_006 exact source replicate.
- optional zero-gate / source-fallback / readout-only ablation: beta_tail=0 with shell disabled is a diagnostic negative control, not a viable source fallback.

## implementation_notes_for_subagent
Mechanism detail to preserve in implementation: GEN023-M01-les-realspace-latent-charge-tail maps the LES paper form `q_i = Q_phi(B_i)` and `E = sum_i E_sr(B_i) + E_lr` to the current neutral latent charge head. The benchmark-compatible nonperiodic real-space tail is `E_tail = beta_tail * 0.5 * sum_{i != j} q_i q_j erf(d_ij/(sqrt(2)*sigma))/d_ij`, with diagonal masked to zero. Code trace is fresh repo evidence from BingqingCheng/cace: `cace/modules/les_wrapper.py::LesWrapper.forward` feeds learned latent charges and writes `E_lr`, while `cace/modules/ewald.py::EwaldPotential.compute_potential_realspace` constructs `[N,N,3]` pair displacements, distances, `erf(r/(sigma*sqrt(2)))`, inverse distance, and the pair sum. Insert only in `model/model.py::EvolutionMLIP.__init__` and `model/model.py::EvolutionMLIP.forward_energy`; keep `model/train.py` unchanged unless this proposal says otherwise.

This proposal intentionally sacrifices exact source fallback to isolate the mechanism; keep it labeled control/ablation during selection.
