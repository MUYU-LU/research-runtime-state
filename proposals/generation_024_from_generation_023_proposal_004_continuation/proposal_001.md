# Proposal 001: Replace LES tail with three-width real-space SOG bank

- family: sog_tail_replace_three_width
- phase: 5
- jump_type: exploit
- budget_class: medium
- expected_capability_gain: Replace rigid two-sigma LES tail with a bounded three-width Gaussian mixture to improve ISO17 transfer energy/gap without disturbing RMD17 force quality.

## one_sentence_hypothesis
Blending proposal_004's fixed `erf(d/sigma)/d` all-pair tail toward a tiny capped three-bandwidth SOG `q_i q_j exp(-d^2/s_l^2)` bank will better fit the long-range decay family that controls ISO17 energy/gap while preserving conservative force autograd and exact source fallback.

## mechanism_refs
- GEN024-M01-adaptive-sog-realspace-latent-tail

## evidence_refs
- evidence_brief_20260501T222449Z.md
- evidence_quality.json: grade A, fresh local PDF and repo verified, strong mechanism card available
- mechanism_cards.json: GEN024-M01-adaptive-sog-realspace-latent-tail
- patch_blueprints.json: blueprint GEN024-M01-adaptive-sog-realspace-latent-tail
- proposal_constraints.json: allowed_mechanisms=[GEN024-M01-adaptive-sog-realspace-latent-tail]
- paper_artifact:paper_001: SOG-Net Eq. (5) Gaussian multiplier mixture for adaptive long-range decay
- repo_artifact:repo_001: CACE-SOG/cace/modules/sog.py::SOGPotential.compute_potential_SOG_realspace
- benchmark_diagnosis.json: source Q_total=4.049140532359024, RMD17 Q=4.206413224218935, ISO17 Q=3.7570626760477586

## historical_relation
- source_unit: generation_023/proposal_004
- relation_to_source: exploit
- not_a_duplicate_of: Not a duplicate of generation_023/proposal_004 because it replaces the two LES kernels rather than adding or retuning them; not a duplicate of generation_023/proposal_002 because the kernel family changes from erf/d to Gaussian SOG.
- lesson_used: generation_023 showed the two-sigma LES variant was the only positive child of generation_022/proposal_006, but its ISO17 Q still lagged and no child beat the global best; use evidence-backed adaptive decay rather than another LES amplitude tweak.

## why_not_duplicate
This proposal changes the long-range multiplier family at the current all-pair insertion point by computing both the existing `les_kernels = erf(...)/d` and a bounded SOG bank `sum_l a_l exp(-d^2/s_l^2)`, then using a tiny capped blend/delta gate. It keeps the same neutral latent charge and source architecture, so the comparison isolates the SOG decay family while retaining exact source fallback when the blend gate is zero.

## benchmark_rationale
- capacity/scaling hypothesis, if any: none; this is mechanism-family replacement, not width/depth scaling.
- rmd17 energy: should remain near source because the total SOG amplitude is capped no larger than current LES caps and initialized near zero.
- rmd17 force: mild risk from Gaussian gradients at short distances; use widths that include a short but not singular channel and no uncapped amplitudes.
- rmd17 gap / Q: expected to stay within source/control noise unless the Gaussian bank overfits; diagonal masking and tiny caps should avoid catastrophic gap shifts.
- iso17 energy: primary target; SOG evidence says Gaussian mixtures can adapt to diverse long-range decay rates, addressing source mixed_energy_mae=0.2679998259591584.
- iso17 force: expected neutral-to-slight gain if the tail improves conformation transfer; monitor for force degradation above proposal_004 mixed_force_mae=0.14805813421552996.
- iso17 gap / Q: expected gain by reducing gap_penalty=0.1531424820304152 through a more flexible all-pair transfer kernel.
- training stability / runtime risk: medium; O(N^2*M) with M=3 is bounded for current molecule sizes, no PBC/FFT/NUFFT.
- control comparison expectation: should beat exact-source control if the LES plateau came from kernel rigidity rather than run noise.

## files_to_edit
- `model/model.py`
- none (`model/train.py` unchanged)
- never `config.json` for MLIP-quality changes

## code_insertion_points
- `model/model.py::EvolutionMLIP.__init__`: keep `les_tail_beta_logits`, `les_tail_beta_caps`, and `les_tail_sigmas`; add `sog_tail_weight_logits`, a small total cap, fixed log-spaced SOG widths such as `[0.7, 1.4, 2.8]`, and a near-zero blend/delta gate.
- `model/model.py::EvolutionMLIP.forward_energy`: reuse lines 583-594 all-pair `all_rij`, `all_dij`, `nonself`, and neutral `charge`; compute the existing LES energy and a SOG candidate energy from `torch.exp(-(safe_all_dij/sigma_l)**2)`.
- `model.py` final energy return: add `les_tail_energy + blend_gate * (sog_tail_energy - les_tail_energy)` or an equivalent source-fallback delta at the current `les_tail_energy` location.
- `model/train.py`: no change.

## minimal_edit_plan
1. Keep the source LES computation intact and add three fixed SOG widths plus capped trainable amplitude logits initialized near zero.
2. Compute `[3,N,N]` SOG kernels from the existing all-pair distances, multiply by the nonself mask, and form a scalar `0.5 * sum(q_i*q_j*K_ij)`.
3. Blend from source LES toward SOG with a near-zero capped gate, preserving the directed cutoff shell electrostatic term and all other source branches.

## implementation_checklist
- [ ] Preserve `E = sum_i E_i` and force-from-energy contract.
- [ ] Preserve benchmark metric field names and runnable entrypoint contract.
- [ ] Modify only the allowed target unit files.
- [ ] Do not edit `config.json`; change MLIP knobs in `model/model.py` or `model/train.py`.
- [ ] Keep tensor shapes compatible with current dataloader and model forward.
- [ ] Add no unbounded cubic neighbor/triplet loops; the only new work is O(N^2*3).
- [ ] Do not add cell, periodic PBC, reciprocal grids, NUFFT, TensorFlow, charge labels, or dataloader fields.
- [ ] Keep a zero-gate fallback so the tail exactly recovers proposal_004 when the SOG blend/delta gate is zero.
- [ ] Call `mark_unit_implemented.py --unit <UNIT> --actor implementation_subagent` after edits.

## expected_benchmark_effect
- primary expected gain: improved ISO17 mixed_energy_mae and Q_iso17 from adaptive long-range decay.
- expected tradeoff: small RMD17 force-noise risk and slightly higher O(N^2*M) runtime.
- failure signal that would falsify this proposal: ISO17 Q does not exceed proposal_004 or force/gap penalties worsen despite near-zero caps.

## ablation_or_control
- required control or comparison: compare against proposal_004 source/control and generation_023 proposal_002/004 LES variants.
- optional zero-gate / source-fallback / readout-only ablation: set the SOG blend/delta gate to zero to recover proposal_004 exactly; set it near one to test full SOG replacement.

## implementation_notes_for_subagent
Use only the benchmark-compatible real-space branch from SOG-Net. The intended formula is `E_sog = 0.5 * sum_{i != j} q_i q_j * sum_l a_l exp(-d_ij^2 / s_l^2)`, with `q` equal to the existing neutral latent charge in proposal_004. Do not port periodic SOG, reciprocal-space code, volume/cell inputs, or large bandwidth banks. Keep total amplitude tiny and capped near the existing LES total scale.
