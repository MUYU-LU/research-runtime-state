# Proposal 002: Add tiny SOG residual beside existing LES tail

- family: sog_tail_additive_residual
- phase: 5
- jump_type: exploit
- budget_class: small
- expected_capability_gain: Test SOG decay flexibility as a source-near residual while retaining proposal_004's positive two-sigma LES tail.

## one_sentence_hypothesis
Adding a separately capped near-zero SOG residual on top of the current two-sigma LES tail will expose adaptive Gaussian long-range decay benefits with less regression risk than replacing the proven proposal_004 tail.

## mechanism_refs
- GEN024-M01-adaptive-sog-realspace-latent-tail

## evidence_refs
- evidence_brief_20260501T222449Z.md
- mechanism_cards.json: GEN024-M01-adaptive-sog-realspace-latent-tail, especially bounded edit permitting adding SOG behind a separate tiny cap
- patch_blueprints.json: current insertion point in `EvolutionMLIP.__init__` and `forward_energy` after neutral charge
- repo_artifact:repo_001: SOGPotential.forward adds a separate scalar SOG potential to the short-range energy
- paper_artifact:paper_001: SOG-Net SR/LR decomposition with learned long-range Gaussian channels
- generation_023_summary.json: proposal_004 Q_total=4.049140532359024 was best in generation_023; proposal_002 had slightly better ISO17 but lower RMD17.

## historical_relation
- source_unit: generation_023/proposal_004
- relation_to_source: exploit
- not_a_duplicate_of: Not a duplicate of proposal_001 because this preserves the existing LES tail and only adds a low-amplitude SOG residual; not a duplicate of generation_023/proposal_004 because it introduces a new Gaussian kernel family.
- lesson_used: source is already a small positive step over its parent, so a conservative additive probe is safer than replacing the winning branch when RMD17 Q is strong.

## why_not_duplicate
The current source has only two `erf/d` LES kernels. This proposal keeps them untouched and adds an independent SOG branch with its own total cap, so any gain can be attributed to residual adaptive decay rather than LES retuning or source-copy noise.

## benchmark_rationale
- capacity/scaling hypothesis, if any: none; only a few scalar SOG amplitudes/width buffers are added.
- rmd17 energy: expected mostly unchanged because source LES branch remains and SOG residual starts near zero.
- rmd17 force: lower risk than replacement because the residual cap can be set below the current combined LES cap, e.g. <=0.001.
- rmd17 gap / Q: should remain near source Q_rmd17=4.206413224218935 if the SOG residual stays small.
- iso17 energy: target modest gain over source mixed_energy_mae=0.2679998259591584 by adding missing decay components without disturbing the LES baseline.
- iso17 force: small possible gain; watch for degradation relative to source mixed_force_mae=0.14805813421552996.
- iso17 gap / Q: expected mild improvement if source plateau is kernel under-flexibility rather than amplitude.
- training stability / runtime risk: small-to-medium; additional O(N^2*3) kernel evaluations but no new data fields or loss changes.
- control comparison expectation: should clear exact source/control by more than run noise; if not, the SOG residual is likely too weak or unnecessary.

## files_to_edit
- `model/model.py`
- none (`model/train.py` unchanged)
- never `config.json` for MLIP-quality changes

## code_insertion_points
- `model/model.py::EvolutionMLIP.__init__`: keep existing `les_tail_beta_logits`, `les_tail_beta_caps`, and `les_tail_sigmas`; add `sog_tail_weight_logits`, `sog_tail_cap`, and fixed log-spaced widths `[0.7, 1.4, 2.8]`.
- `model/model.py::EvolutionMLIP.forward_energy`: after `les_tail_energy` is computed, reuse `safe_all_dij`, `nonself`, and `charge` to compute an additive SOG residual energy.
- `model/model.py` final return: add `+ sog_tail_energy` beside `+ les_tail_energy`.
- `model/train.py`: no change.

## minimal_edit_plan
1. Add three SOG amplitude logits initialized around `-8.0` and a total cap no larger than `0.001`.
2. Compute a masked three-width Gaussian bank from existing all-pair distances and combine it with capped amplitudes.
3. Add the resulting scalar residual to the final energy without changing the source LES and cutoff-shell terms.

## implementation_checklist
- [ ] Preserve `E = sum_i E_i` and force-from-energy contract.
- [ ] Preserve benchmark metric field names and runnable entrypoint contract.
- [ ] Modify only the allowed target unit files.
- [ ] Do not edit `config.json`; change MLIP knobs in `model/model.py` or `model/train.py`.
- [ ] Keep tensor shapes compatible with current dataloader and model forward.
- [ ] Add no unbounded cubic neighbor/triplet loops unless explicitly justified by budget.
- [ ] Keep the SOG residual independently zero-gatable so proposal_004 behavior is exactly recoverable.
- [ ] Do not alter energy/force loss weights or training schedule in this mechanism-isolation proposal.
- [ ] Call `mark_unit_implemented.py --unit <UNIT> --actor implementation_subagent` after edits.

## expected_benchmark_effect
- primary expected gain: modest ISO17 Q increase with minimal RMD17 regression.
- expected tradeoff: smaller upside than replacing LES, plus slight runtime increase.
- failure signal that would falsify this proposal: benchmark indistinguishable from source/control or RMD17 force worsens despite tiny residual cap.

## ablation_or_control
- required control or comparison: compare to exact source replicate and proposal_001 replacement; this distinguishes residual-vs-replacement value.
- optional zero-gate / source-fallback / readout-only ablation: set the SOG residual cap/logits to zero; source behavior should be exactly recovered.

## implementation_notes_for_subagent
This is the safest SOG exploitation path. Do not remove current LES code. Add the new residual only after the existing all-pair distance block so tensors are reused. Use the SOG-Net real-space formula and code trace as evidence, but limit the implementation to three Gaussian channels and a tiny total cap.
