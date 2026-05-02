# Proposal 003: Normalized SOG mixture with frozen log-spaced widths

- family: sog_tail_normalized_width_mixture
- phase: 5
- jump_type: exploit
- budget_class: small
- expected_capability_gain: Let the model redistribute a fixed long-range tail budget across Gaussian widths instead of learning unconstrained amplitudes.

## one_sentence_hypothesis
A normalized softmax SOG mixture with frozen log-spaced widths and a single capped blend scale will test whether proposal_004 needs adaptive decay shape while keeping the total long-range force budget stable and retaining exact source fallback.

## mechanism_refs
- GEN024-M01-adaptive-sog-realspace-latent-tail

## evidence_refs
- evidence_brief_20260501T222449Z.md
- mechanism_cards.json: SOG-Net Eq. (5) maps to a bounded molecule-compatible Gaussian bank
- patch_blueprints.json: small M=3 or 4 bank and cap no larger than current LES total scale
- repo_artifact:repo_001: nonperiodic real-space SOG computes weighted sums over `exp(-d_ij^2/s_l^2)`
- benchmark_diagnosis.json: source strong RMD17 but ISO17 energy/gap still leave room for transfer improvement
- generation_023_summary.json: proposal_004 best Q_total, proposal_002 achieved better ISO17 but weaker RMD17, suggesting range-budget allocation matters.

## historical_relation
- source_unit: generation_023/proposal_004
- relation_to_source: exploit
- not_a_duplicate_of: Not a duplicate of proposal_001 because it normalizes amplitudes under one total scale rather than learning independent signed caps; not a duplicate of proposal_002 because it can replace LES or be the sole long-range all-pair tail.
- lesson_used: previous LES variants varied sigma and cap separately; this proposal controls total tail strength to isolate decay-shape adaptation.

## why_not_duplicate
Proposal_004's two LES caps can both grow independently. This proposal computes a SOG candidate with `softmax(width_logits)` times one small positive total cap, then blends from the source LES tail toward that candidate with a near-zero gate, so it tests distribution across SOG widths under a stable force budget rather than increasing total long-range amplitude.

## benchmark_rationale
- capacity/scaling hypothesis, if any: none.
- rmd17 energy: expected neutral because total all-pair scale is bounded and initialized near the current LES scale or smaller.
- rmd17 force: lower risk than independent amplitudes because normalized weights prevent a large sum of channels.
- rmd17 gap / Q: expected stable; if it drops, Gaussian shape alone may be harmful for local-force-dominated RMD17.
- iso17 energy: primary target, especially other-split energy where source other_energy_mae=0.294130859375.
- iso17 force: possible slight gain if width allocation captures conformation-level interactions; no force-only tuning.
- iso17 gap / Q: expected to improve if the source's fixed `[0.8,2.0]` sigmas are under-resolved.
- training stability / runtime risk: small; three or four widths, one total cap, no training-loop change.
- control comparison expectation: should outperform exact source or at least match it with better ISO17 gap if adaptive shape is useful.

## files_to_edit
- `model/model.py`
- none (`model/train.py` unchanged)
- never `config.json` for MLIP-quality changes

## code_insertion_points
- `model/model.py::EvolutionMLIP.__init__`: add `sog_tail_mix_logits`, `sog_tail_total_logit`, `sog_tail_total_cap`, and fixed width buffer `[0.6, 1.2, 2.4, 3.6]` or `[0.7, 1.4, 2.8]`.
- `model/model.py::EvolutionMLIP.forward_energy`: compute `weights = softmax(sog_tail_mix_logits)`, `total = cap * sigmoid(sog_tail_total_logit)`, and `kernel = total * sum_l weights_l * exp(-d^2/s_l^2)`.
- `model/model.py` final energy return: use `les_tail_energy + blend_gate * (normalized_sog_tail_energy - les_tail_energy)` or an equivalent gated successor so blend zero exactly recovers source.
- `model/train.py`: no change.

## minimal_edit_plan
1. Add fixed SOG width buffer and normalized mixture parameters with near-zero total scale.
2. Reuse the all-pair distance tensor and neutral charge to compute `sog_tail_energy` with a softmax-normalized width mixture.
3. Add a blend/delta expression from `les_tail_energy` toward the normalized SOG tail, with zero gate equal to exact source behavior.

## implementation_checklist
- [ ] Preserve `E = sum_i E_i` and force-from-energy contract.
- [ ] Preserve benchmark metric field names and runnable entrypoint contract.
- [ ] Modify only the allowed target unit files.
- [ ] Do not edit `config.json`; change MLIP knobs in `model/model.py` or `model/train.py`.
- [ ] Keep tensor shapes compatible with current dataloader and model forward.
- [ ] Add no unbounded cubic neighbor/triplet loops; this is O(N^2*M) only.
- [ ] Use positive bounded widths and a finite diagonal-safe distance exactly as in source all-pair block.
- [ ] Keep total scale capped at or below the current combined LES cap unless a comment documents a smaller safer cap.
- [ ] Call `mark_unit_implemented.py --unit <UNIT> --actor implementation_subagent` after edits.

## expected_benchmark_effect
- primary expected gain: ISO17 energy/gap improvement from learned width allocation under a stable long-range budget.
- expected tradeoff: less expressivity than independently signed/uncapped SOG amplitudes.
- failure signal that would falsify this proposal: no ISO17 improvement over exact source, or RMD17 Q falls despite fixed total scale.

## ablation_or_control
- required control or comparison: compare with proposal_001 independent-amplitude replacement and proposal_002 additive residual.
- optional zero-gate / source-fallback / readout-only ablation: set blend gate to zero to recover exact source; freeze softmax weights at initialization to test a fixed-shape candidate.

## implementation_notes_for_subagent
Use this when the selection wants a conservative mechanism-isolation exploit. The key is normalized width weights, not maximum flexibility. Do not introduce new charge channels, loss changes, or capacity scaling here.
