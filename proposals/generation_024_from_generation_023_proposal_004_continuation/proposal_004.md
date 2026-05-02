# Proposal 004: Lightly trainable SOG bandwidths under bounded positive widths

- family: sog_tail_trainable_bandwidths
- phase: 5
- jump_type: jump
- budget_class: medium
- expected_capability_gain: Move beyond fixed LES/SOG widths by learning bounded Gaussian bandwidths while preserving the current all-pair latent-charge contract.

## one_sentence_hypothesis
Learning a few positive bounded SOG bandwidths, initialized from log-spaced widths, will adapt long-range decay length scales to RMD17/ISO17 without importing periodic SOG-Net machinery, while a blend gate preserves exact proposal_004 fallback.

## mechanism_refs
- GEN024-M01-adaptive-sog-realspace-latent-tail

## evidence_refs
- evidence_brief_20260501T222449Z.md
- mechanism_cards.json: SOG-Net Eq. (5) uses trainable Gaussian amplitudes/bandwidths and maps to current all-pair tensors
- patch_blueprints.json: add `sog_tail_log_widths` and capped weights near current `les_tail_sigmas`
- repo_artifact:repo_001: SOGPotential.__init__ stores trainable `wl` and `sl` for SOG channels
- paper_artifact:paper_001: SOG multipliers are motivated by diverse decay rates such as `1/r^p` and `exp(-mu r)/r`
- benchmark_diagnosis.json: proposal_004 is source-near positive but not global-best, so a bounded bandwidth jump is justified.

## historical_relation
- source_unit: generation_023/proposal_004
- relation_to_source: jump
- not_a_duplicate_of: Not a duplicate of proposals_001-003 because those freeze SOG widths or normalize only amplitudes; this learns the distance scales themselves.
- lesson_used: generation_023 fixed-sigma probes were mixed; a controlled trainable-width jump can test whether hand-picked `[0.8,2.0]` is the bottleneck.

## why_not_duplicate
The new degrees of freedom are bounded positive width parameters, initialized at log-spaced values and clamped or transformed into a safe range. Existing LES variants had fixed sigmas; this proposal directly tests bandwidth adaptivity from the SOG evidence.

## benchmark_rationale
- capacity/scaling hypothesis, if any: not global capacity; this is resolution of long-range decay length scales.
- rmd17 energy: may improve if learned widths reduce energy MAE below source mixed_energy_mae=0.028017578125, but over-flexibility risk exists.
- rmd17 force: medium risk because short learned widths can create sharp force gradients; enforce lower bound around 0.5-0.6 and tiny caps.
- rmd17 gap / Q: should remain competitive if widths stay in bounded molecule-relevant range.
- iso17 energy: primary target; learned widths may better match other-split energy decay than fixed LES/SOG widths.
- iso17 force: expected neutral-to-positive if bandwidths avoid too-short channels.
- iso17 gap / Q: expected gain through reduced transfer gap; source gap_penalty=0.1531424820304152 is the target.
- training stability / runtime risk: medium; width gradients can be noisy, but channel count is only M=3 or M=4.
- control comparison expectation: should beat fixed-width SOG proposals only if bandwidth adaptation is a real bottleneck.

## files_to_edit
- `model/model.py`
- none (`model/train.py` unchanged)
- never `config.json` for MLIP-quality changes

## code_insertion_points
- `model/model.py::EvolutionMLIP.__init__`: add `sog_tail_log_width_offsets` or `sog_tail_unconstrained_widths` initialized to log `[0.7,1.4,2.8]`, plus lower/upper buffers and capped amplitude logits.
- `model/model.py::EvolutionMLIP.forward_energy`: transform widths with `softplus`/`sigmoid` into a safe interval such as `[0.5, 3.5]`, compute Gaussian kernels, and mask diagonal.
- `model/model.py` final energy return: keep current `les_tail_energy` and add a bounded `les_tail_energy + blend_gate * (sog_tail_energy - les_tail_energy)` expression initialized to the source-safe side.
- `model/train.py`: no change.

## minimal_edit_plan
1. Add trainable width parameters with explicit comments documenting min/max range and near-log-spaced initialization.
2. Compute bounded widths on each forward pass and use them in the existing all-pair SOG kernel bank.
3. Keep SOG amplitudes tiny/capped and add only a gated scalar delta from source LES toward SOG in the final energy expression.

## implementation_checklist
- [ ] Preserve `E = sum_i E_i` and force-from-energy contract.
- [ ] Preserve benchmark metric field names and runnable entrypoint contract.
- [ ] Modify only the allowed target unit files.
- [ ] Do not edit `config.json`; change MLIP knobs in `model/model.py` or `model/train.py`.
- [ ] Keep tensor shapes compatible with current dataloader and model forward.
- [ ] Add no unbounded cubic neighbor/triplet loops unless explicitly justified by budget.
- [ ] Enforce positive bounded widths; never allow zero/negative/huge width values.
- [ ] Do not add a new charge head, PBC, cells, reciprocal grids, or charge labels.
- [ ] Call `mark_unit_implemented.py --unit <UNIT> --actor implementation_subagent` after edits.

## expected_benchmark_effect
- primary expected gain: improved ISO17 transfer through learned SOG decay scale selection.
- expected tradeoff: higher force-gradient/noise risk than fixed-width proposals.
- failure signal that would falsify this proposal: learned widths collapse to bounds, RMD17 force worsens, or fixed-width SOG performs as well.

## ablation_or_control
- required control or comparison: compare with fixed-width SOG proposal_001/proposal_003 and exact source control.
- optional zero-gate / source-fallback / readout-only ablation: set blend gate to zero to recover proposal_004 exactly; optionally freeze widths at initialization to recover proposal_001-like behavior.

## implementation_notes_for_subagent
This is a controlled jump, not a full SOG-Net port. Only bandwidth adaptivity is added. Keep M small and include a readable comment explaining that the current benchmark has no periodic cell, so the repo's FFT/NUFFT path must not be used.
