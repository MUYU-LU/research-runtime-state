# Proposal 002: Ultra-conservative LES beta probe

- family: les_tail_ultra_conservative_beta_probe
- phase: 5
- jump_type: exploit
- budget_class: tiny
- expected_capability_gain: Ultra-conservative LES beta probe; measure whether any all-pair tail signal survives variance

## one_sentence_hypothesis
A beta cap of only 0.001 with stronger negative initialization should provide a near-source exploit that can reveal whether the LES tail has a beneficial gradient without overwhelming the stable local model.

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
- not_a_duplicate_of: Not a duplicate of proposal_001 because this is intentionally more conservative: smaller beta cap, more negative logit, and explicit source-near probe behavior. Not a duplicate of generation_022 charge-shell variants because it uses all-pair nonperiodic LES rather than cutoff shells.
- lesson_used: Control replicate variance currently exceeds the source improvement; this proposal treats LES as a cautious exploit rather than a broad jump.

## why_not_duplicate
Not a duplicate of proposal_001 because this is intentionally more conservative: smaller beta cap, more negative logit, and explicit source-near probe behavior. Not a duplicate of generation_022 charge-shell variants because it uses all-pair nonperiodic LES rather than cutoff shells.

## benchmark_rationale
- capacity/scaling hypothesis, if any: none.
- rmd17 energy: expected almost unchanged versus source because beta_tail <=0.001 and starts around zero.
- rmd17 force: should preserve force behavior better than stronger electrostatic variants; reject if force MAE worsens beyond noise.
- rmd17 gap / Q: should not increase gap_penalty beyond 0.010653 by more than variance.
- iso17 energy: may slightly improve mixed_energy_mae if tail gradient encourages transferable charges; improvement may be too small to rise above noise.
- iso17 force: low-risk; should not meaningfully alter mixed_force_mae=0.148905.
- iso17 gap / Q: target a small reduction in 0.153666 gap_penalty without sacrificing RMD17 Q.
- training stability / runtime risk: O(N^2) cost only; numerical risk low due to tiny cap and diagonal mask.
- control comparison expectation: selected only if it beats source and control variance; otherwise it functions as a safe negative result.

## files_to_edit
- `model/model.py`
- none (`model/train.py` unchanged)
- never `config.json` for MLIP-quality changes

## code_insertion_points
- `model/model.py::EvolutionMLIP.__init__`: add `les_tail_beta_logit` initialized to `-10.0`, `les_tail_beta_cap = 0.001`, and `les_tail_sigma = 1.0`; keep `charge_shell_beta_logits` untouched.
- `model/model.py::EvolutionMLIP.forward_energy`: compute all-pair nonself LES kernel after neutral charge construction and add only the tiny gated scalar tail.
- `model/train.py`: no change.

## minimal_edit_plan
1. Add one scalar beta gate with cap 0.001 and sigma 1.0.
2. Reuse existing neutral `charge` exactly; no new charge head, labels, or objective.
3. Add the LES tail term after `electrostatic_pair_energy` and keep all other model/train behavior identical.

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
- primary expected gain: low-variance signal of whether all-pair LES tail improves ISO17 gap/energy.
- expected tradeoff: improvement may be too small; runtime still increases O(N^2).
- failure signal that would falsify this proposal: metrics indistinguishable from source/control or any measurable RMD17 force degradation.

## ablation_or_control
- required control or comparison: compare against proposal_001 and exact source/control replicate to determine beta sensitivity.
- optional zero-gate / source-fallback / readout-only ablation: force `les_tail_beta=0` should exactly recover source outputs except floating no-op code path.

## implementation_notes_for_subagent
Mechanism detail to preserve in implementation: GEN023-M01-les-realspace-latent-charge-tail maps the LES paper form `q_i = Q_phi(B_i)` and `E = sum_i E_sr(B_i) + E_lr` to the current neutral latent charge head. The benchmark-compatible nonperiodic real-space tail is `E_tail = beta_tail * 0.5 * sum_{i != j} q_i q_j erf(d_ij/(sqrt(2)*sigma))/d_ij`, with diagonal masked to zero. Code trace is fresh repo evidence from BingqingCheng/cace: `cace/modules/les_wrapper.py::LesWrapper.forward` feeds learned latent charges and writes `E_lr`, while `cace/modules/ewald.py::EwaldPotential.compute_potential_realspace` constructs `[N,N,3]` pair displacements, distances, `erf(r/(sigma*sqrt(2)))`, inverse distance, and the pair sum. Insert only in `model/model.py::EvolutionMLIP.__init__` and `model/model.py::EvolutionMLIP.forward_energy`; keep `model/train.py` unchanged unless this proposal says otherwise.

This is one of the conservative exploit proposals required for the set; prioritize exact source fallback over ambition.
