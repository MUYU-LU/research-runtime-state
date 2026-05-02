# Proposal 005: Signed SOG amplitudes with zero-sum regularized kernel budget

- family: sog_tail_signed_kernel_contrast
- phase: 5
- jump_type: jump
- budget_class: medium
- expected_capability_gain: Allow a small contrastive Gaussian mixture to represent non-monotone residual decay while keeping total long-range scale bounded.

## one_sentence_hypothesis
A tiny signed SOG amplitude bank, constrained by a total absolute-value cap and added as a zero-gated residual to the source LES tail, can model residual long-range decay shapes that a positive-only LES/SOG tail cannot, potentially improving ISO17 gap without large architecture changes.

## mechanism_refs
- GEN024-M01-adaptive-sog-realspace-latent-tail

## evidence_refs
- evidence_brief_20260501T222449Z.md
- mechanism_cards.json: SOG-Net Eq. (5) trainable amplitudes over Gaussian bandwidths
- repo_artifact:repo_001: SOGPotential.compute_potential_SOG_realspace multiplies `wl_l exp(-d^2/s_l^2)` and sums channels
- patch_blueprints.json: permits a small capped trainable Gaussian bank and warns to keep total LR scale no larger than current LES caps
- benchmark_diagnosis.json: source has high RMD17 Q but ISO17 mixed_energy_mae=0.2679998259591584 and gap_penalty=0.1531424820304152
- lineage_stats.json: LES family has one positive current source but other LES variants were negative, suggesting shape not simple amplitude may matter.

## historical_relation
- source_unit: generation_023/proposal_004
- relation_to_source: jump
- not_a_duplicate_of: Not a duplicate of positive/softmax SOG proposals because amplitudes may be signed under an absolute budget; not a duplicate of LES variants because Gaussian channels can subtract one range while adding another.
- lesson_used: generation_023 proposal_002 improved ISO17 but lost RMD17; a contrastive kernel may tune transfer energy without simply increasing all long-range force components.

## why_not_duplicate
This proposal changes the amplitude parameterization, not just kernel family. It uses `a = cap * tanh(raw) / sum(abs(tanh(raw)))` or an equivalent absolute-budget normalization so channels can form small positive/negative contrasts across widths, then adds the signed SOG energy through a near-zero residual gate.

## benchmark_rationale
- capacity/scaling hypothesis, if any: none; mechanism expressivity in the long-range kernel shape only.
- rmd17 energy: possible improvement if contrastive channels cancel harmful short-range energy bias; risk if signs create oscillatory forces.
- rmd17 force: medium risk; bounded absolute scale and width floor are mandatory.
- rmd17 gap / Q: should not lose more than source/control noise if total absolute cap is <= current LES cap.
- iso17 energy: target improvement by fitting residual decay shapes that positive mixtures cannot express.
- iso17 force: uncertain; sign contrasts may help transfer but can increase force oscillation.
- iso17 gap / Q: primary success signal is improved Q_iso17 beyond source and proposal_002.
- training stability / runtime risk: medium; same O(N^2*M) runtime, but signed amplitudes may be less stable.
- control comparison expectation: should be selected only if the batch can tolerate a higher-risk jump with clear mechanism evidence.

## files_to_edit
- `model/model.py`
- none (`model/train.py` unchanged)
- never `config.json` for MLIP-quality changes

## code_insertion_points
- `model/model.py::EvolutionMLIP.__init__`: add fixed SOG width buffer and raw signed amplitude parameters initialized near zero; add a scalar absolute cap such as `0.0015` or below current LES total cap.
- `model/model.py::EvolutionMLIP.forward_energy`: compute `raw = tanh(logits)`, normalize by `raw.abs().sum().clamp_min(eps)`, multiply by total cap and optional near-zero gate, then form SOG kernel sum.
- `model/model.py` final return: add a near-zero gated signed SOG residual beside the existing `les_tail_energy`; do not replace the source tail in this high-risk variant.
- `model/train.py`: no change.

## minimal_edit_plan
1. Add signed amplitude parameters and fixed widths with comments noting the absolute budget.
2. Build the masked Gaussian bank and combine channels with absolute-normalized signed weights.
3. Add the scalar residual energy with an independent near-zero gate beside `les_tail_energy`; keep all other source branches unchanged.

## implementation_checklist
- [ ] Preserve `E = sum_i E_i` and force-from-energy contract.
- [ ] Preserve benchmark metric field names and runnable entrypoint contract.
- [ ] Modify only the allowed target unit files.
- [ ] Do not edit `config.json`; change MLIP knobs in `model/model.py` or `model/train.py`.
- [ ] Keep tensor shapes compatible with current dataloader and model forward.
- [ ] Add no unbounded cubic neighbor/triplet loops unless explicitly justified by budget.
- [ ] Clamp/normalize signed amplitudes to a strict absolute scale cap.
- [ ] Keep diagonal zero and safe distance clamps from source all-pair block.
- [ ] Call `mark_unit_implemented.py --unit <UNIT> --actor implementation_subagent` after edits.

## expected_benchmark_effect
- primary expected gain: ISO17 gap/energy gain from contrastive adaptive decay.
- expected tradeoff: greater force-noise and training-instability risk than positive-only SOG.
- failure signal that would falsify this proposal: RMD17 force or gap regresses materially, or signed channels collapse to near-zero without ISO17 gain.

## ablation_or_control
- required control or comparison: compare with positive normalized SOG proposal_003 and exact source control.
- optional zero-gate / source-fallback / readout-only ablation: zero the signed SOG residual gate to recover proposal_004 exactly; force all weights positive to recover a proposal_003-like variant.

## implementation_notes_for_subagent
This proposal is intentionally a higher-risk jump. Do not combine it with trainable widths or training-objective changes; the signed amplitude budget is the only new idea. Keep caps small enough that a sign mistake cannot dominate the existing learned local and LES energies.
