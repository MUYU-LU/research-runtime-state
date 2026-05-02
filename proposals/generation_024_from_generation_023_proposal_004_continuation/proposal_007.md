# Proposal 007: Single long Gaussian SOG simplification of two-sigma LES

- family: sog_tail_single_width_simplify
- phase: 4
- jump_type: backward-simplify
- budget_class: tiny
- expected_capability_gain: Determine whether proposal_004's gain comes from any all-pair latent-charge tail or specifically from two-sigma LES complexity.

## one_sentence_hypothesis
Blending the two-sigma LES tail toward one tiny long-range Gaussian SOG channel will simplify the branch while testing whether a single smooth all-pair decay is enough for ISO17 transfer and preserving exact source fallback.

## mechanism_refs
- GEN024-M01-adaptive-sog-realspace-latent-tail

## evidence_refs
- evidence_brief_20260501T222449Z.md
- mechanism_cards.json: SOG mechanism maps to current all-pair distance block and permits small M rather than full SOG-Net
- patch_blueprints.json: bounded edit allows M=3 or 4; this proposal deliberately uses M=1 as a backward-simplify ablation
- generation_023_summary.json: two-sigma proposal_004 was best, while several LES variants underperformed, so complexity should be tested
- lineage_stats.json: `les_tail_two_sigma_electrostatic_variant` had positive G_delta, but `les_tail_stronger_sigma15` and `les_tail_outer_cutoff_taper` were negative.

## historical_relation
- source_unit: generation_023/proposal_004
- relation_to_source: simplify
- not_a_duplicate_of: Not a duplicate of generation_023/proposal_003 because it uses a Gaussian SOG channel rather than one LES `erf/d` sigma; not a duplicate of proposal_001 because it uses one width only.
- lesson_used: a simpler branch can reveal whether the source improvement is robust all-pair latent electrostatics or a fragile two-kernel fit.

## why_not_duplicate
This proposal intentionally removes mixture complexity. It is a backward-simplify/control-like ablation of the new SOG mechanism, not another attempt to maximize expressive power.

## benchmark_rationale
- capacity/scaling hypothesis, if any: none; lower mechanism capacity than source tail.
- rmd17 energy: may stay close to source if the long tail mainly shifts energy smoothly.
- rmd17 force: lower risk than multi-channel SOG due to one smooth width and tiny cap.
- rmd17 gap / Q: expected stable if proposal_004's two-sigma separation was not essential.
- iso17 energy: may improve if the long Gaussian isolates the transfer component without short-range force noise.
- iso17 force: expected neutral or slight gain; simplified branch has less chance to overfit forces.
- iso17 gap / Q: success means a one-width smooth all-pair latent charge tail captures most transfer value.
- training stability / runtime risk: tiny-to-small; O(N^2) one channel, no training change.
- control comparison expectation: should beat exact source only if simplification improves generalization; otherwise it is informative as a negative control.

## files_to_edit
- `model/model.py`
- none (`model/train.py` unchanged)
- never `config.json` for MLIP-quality changes

## code_insertion_points
- `model/model.py::EvolutionMLIP.__init__`: keep two LES buffers active and add one `sog_tail_beta_logit`, `sog_tail_beta_cap`, fixed width such as `2.0` or `2.4`, and a near-zero blend gate.
- `model/model.py::EvolutionMLIP.forward_energy`: reuse current all-pair `safe_all_dij` and `nonself` tensors; compute one `exp(-d^2/s^2)` candidate kernel.
- `model/model.py` final return: use a gated simplification expression such as `les_tail_energy + blend_gate * (single_sog_tail_energy - les_tail_energy)`.
- `model/train.py`: no change.

## minimal_edit_plan
1. Keep the two-sigma LES source computation and add one fixed-width SOG scalar candidate plus blend gate.
2. Compute one masked Gaussian all-pair kernel and its neutral-charge candidate energy.
3. Blend from source LES toward this simplified tail, preserving all local, body-order, residual, and cutoff-shell terms.

## implementation_checklist
- [ ] Preserve `E = sum_i E_i` and force-from-energy contract.
- [ ] Preserve benchmark metric field names and runnable entrypoint contract.
- [ ] Modify only the allowed target unit files.
- [ ] Do not edit `config.json`; change MLIP knobs in `model/model.py` or `model/train.py`.
- [ ] Keep tensor shapes compatible with current dataloader and model forward.
- [ ] Add no unbounded cubic neighbor/triplet loops; this is O(N^2) only.
- [ ] Keep the branch exactly zero-gatable.
- [ ] Do not change training objective or model capacity in this simplification proposal.
- [ ] Call `mark_unit_implemented.py --unit <UNIT> --actor implementation_subagent` after edits.

## expected_benchmark_effect
- primary expected gain: cleaner ISO17 generalization if two-sigma LES was over-parameterized.
- expected tradeoff: lower maximum expressivity than multi-width SOG proposals.
- failure signal that would falsify this proposal: Q_total drops below source/control or ISO17 gap worsens, showing mixture complexity is needed.

## ablation_or_control
- required control or comparison: compare against source proposal_004, exact copy proposal_008, and multi-width SOG proposal_001.
- optional zero-gate / source-fallback / readout-only ablation: zero the blend gate to recover proposal_004 exactly; set blend high to test the single-SOG simplification.

## implementation_notes_for_subagent
Keep this intentionally simple. One width, one cap, one scalar energy. Use the SOG formula from evidence but do not add normalized mixtures, signed weights, trainable widths, objective changes, or capacity changes.
