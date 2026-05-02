# Proposal 004: Two-sigma LES electrostatic tail

- family: les_tail_two_sigma_electrostatic_variant
- phase: 5
- jump_type: jump
- budget_class: medium
- expected_capability_gain: Two-sigma LES electrostatic tail; separate near smoothing from longer-range transfer

## one_sentence_hypothesis
A two-kernel LES tail with separate fixed sigmas can test whether ISO17 transfer needs both softened near-pair electrostatics and longer-range all-pair charge interactions.

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
- not_a_duplicate_of: Not a duplicate of proposal_003 because it uses a bounded two-sigma mixture rather than one sigma=1.5 tail. Not a duplicate of generation_022 multishell charge pair because the shells are all-pair LES kernels, not cutoff near/mid directed-edge kernels.
- lesson_used: The current source uses near/mid cutoff shells; evidence says the unresolved mechanism is all-pair LES domain and erf range separation, so this proposal tests a closer LES analogue while staying bounded.

## why_not_duplicate
Not a duplicate of proposal_003 because it uses a bounded two-sigma mixture rather than one sigma=1.5 tail. Not a duplicate of generation_022 multishell charge pair because the shells are all-pair LES kernels, not cutoff near/mid directed-edge kernels.

## benchmark_rationale
- capacity/scaling hypothesis, if any: none; added parameters are two scalar gates only.
- rmd17 energy: possible neutral/slight gain if two sigmas better match local and nonlocal energy components.
- rmd17 force: medium risk because two kernels can add force components; caps keep total beta <=0.005.
- rmd17 gap / Q: should not worsen beyond source/control noise unless ISO17 gain is substantial.
- iso17 energy: stronger target than single-tail proposals; may reduce within/other energy mismatch by learning range separation.
- iso17 force: monitor for degradation due to extra long-range gradient; no objective changes to compensate.
- iso17 gap / Q: target gap_penalty and Q_iso17 through explicit long-range transfer.
- training stability / runtime risk: medium; O(N^2) plus two kernel evaluations, still acceptable for small molecules.
- control comparison expectation: if two-sigma beats one-sigma, future work can refine sigma/gate; if not, keep simpler proposals.

## files_to_edit
- `model/model.py`
- none (`model/train.py` unchanged)
- never `config.json` for MLIP-quality changes

## code_insertion_points
- `model/model.py::EvolutionMLIP.__init__`: add `les_tail_beta_logits = nn.Parameter(torch.full((2,), -6.5))`, `les_tail_beta_caps = (0.002, 0.003)`, and fixed sigmas `(0.8, 2.0)`.
- `model/model.py::EvolutionMLIP.forward_energy`: compute one `[N,N]` distance matrix and two LES kernels `erf(d/(sqrt(2)*sigma_k))/d`; add `0.5 * sum(q_i*q_j*(beta_0*K_0 + beta_1*K_1))` with diagonal zeroed.
- `model/train.py`: no change.

## minimal_edit_plan
1. Add two beta logits and fixed sigma constants in `__init__`.
2. Build the all-pair nonself matrix once, then form the two LES kernels from the same distances.
3. Add the bounded two-sigma tail to the final energy while preserving the source shell term and zero-beta fallback.

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
- primary expected gain: improved ISO17 energy/gap via range-separated all-pair latent electrostatics.
- expected tradeoff: extra O(N^2) kernel cost and higher force-noise risk than conservative probes.
- failure signal that would falsify this proposal: no ISO17 gain over one-sigma variants or clear RMD17 Q degradation.

## ablation_or_control
- required control or comparison: compare with single-sigma proposal_003 to isolate range-mixture value.
- optional zero-gate / source-fallback / readout-only ablation: zero both gates to recover the source exactly.

## implementation_notes_for_subagent
Mechanism detail to preserve in implementation: GEN023-M01-les-realspace-latent-charge-tail maps the LES paper form `q_i = Q_phi(B_i)` and `E = sum_i E_sr(B_i) + E_lr` to the current neutral latent charge head. The benchmark-compatible nonperiodic real-space tail is `E_tail = beta_tail * 0.5 * sum_{i != j} q_i q_j erf(d_ij/(sqrt(2)*sigma))/d_ij`, with diagonal masked to zero. Code trace is fresh repo evidence from BingqingCheng/cace: `cace/modules/les_wrapper.py::LesWrapper.forward` feeds learned latent charges and writes `E_lr`, while `cace/modules/ewald.py::EwaldPotential.compute_potential_realspace` constructs `[N,N,3]` pair displacements, distances, `erf(r/(sigma*sqrt(2)))`, inverse distance, and the pair sum. Insert only in `model/model.py::EvolutionMLIP.__init__` and `model/model.py::EvolutionMLIP.forward_energy`; keep `model/train.py` unchanged unless this proposal says otherwise.

Keep the two-sigma branch tiny: no vector features, no new readout, no cell or reciprocal path.
