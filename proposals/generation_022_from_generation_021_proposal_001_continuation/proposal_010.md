# Proposal 010: Source TP/PaiNN body-order reweight without electrostatics

- family: painn_body_order_rebalance
- phase: 4
- jump_type: wildcard
- budget_class: small
- expected_capability_gain: Recover ISO17 force/energy balance by reducing body-order/residual interference while preserving the successful TP/PaiNN source mechanism.

## one_sentence_hypothesis
A non-electrostatic wildcard that slightly rebalances existing body-order and residual scales can test whether source ISO17 loss is from over-calibration rather than missing charge physics.

## mechanism_refs
- []

## evidence_refs
- current source unit: `generation_021/proposal_001`
- proposal context: `/home/lmy/.openclaw/workspace/research_runtime/proposals/generation_022_from_generation_021_proposal_001_continuation/context.md`
- control/comparator policy from research_skill generation loop
- source metrics: generation_021/proposal_001 Q_total=4.047536521538605, Q_rmd17=4.210072139663386, Q_iso17=3.7456846593068707
- SpookyNet evidence package remains the active package for this round, but this proposal intentionally does not claim external mechanism evidence

## historical_relation
- source_unit: generation_021/proposal_001
- relation_to_source: control
- not_a_duplicate_of: Not a duplicate of electrostatic proposals because it deliberately uses no SpookyNet mechanism_refs and provides a non-charge comparator; not a config or benchmark change.
- lesson_used: If this comparator matches charge proposals, improvements may be calibration/variance rather than electrostatic mechanism; if it lags, the SpookyNet pair-energy evidence is strengthened.

## why_not_duplicate
Not a duplicate of electrostatic proposals because it deliberately uses no SpookyNet mechanism_refs and provides a non-charge comparator; not a config or benchmark change.

## benchmark_rationale
Discuss expected effects on all relevant benchmark signals, not force-only:
- capacity/scaling hypothesis, if any: Comparator for selection diversity; diagnosis-driven, not external-mechanism-driven.
- rmd17 energy: should remain close to source mixed_energy_mae=0.030508691406250003; reject if RMD17 energy drift erases Q_rmd17 strength.
- rmd17 force: source mixed_force_mae=0.05835015199595364 is strong; any added scalar term must keep conservative force gradients bounded.
- rmd17 gap / Q: tolerate only neutral variance around Q_rmd17=4.210072139663386 unless ISO17 gain is clearly larger.
- iso17 energy: primary diagnostic because source mixed_energy_mae=0.26671175340941544 and validation energy trend worsened.
- iso17 force: source mixed_force_mae=0.15079258253733485; expected to remain within small tradeoff unless energy/gap gains dominate Q_total.
- iso17 gap / Q: primary target is reducing gap_penalty=0.1417151905668173 and lifting Q_iso17=3.7456846593068707.
- training stability / runtime risk: no benchmark/config changes; O(E) edge operations only for electrostatic proposals, no Ewald, no all-pairs, no cubic loops.
- control comparison expectation: compare against exact source control proposal_007 and source Q_total=4.047536521538605; require positive G_delta beyond observed control variance.

## files_to_edit
- `model/model.py`
- `model/train.py`: none
- never `config.json` for MLIP-quality changes

## code_insertion_points
- `model/model.py::EvolutionMLIP.__init__`: initialize `body_order_scale` from -4.0 to -4.6 and `energy_residual_scale_logit` from 0.0 to -0.75, or cap residual multiplier from 0.02 to 0.012.
- `model/model.py::EvolutionMLIP.forward_energy`: preserve current return structure; no new mechanism path.
- `model/train.py`: no change.

## minimal_edit_plan
1. Reduce only the code-level default scale of body-order and/or atomwise residual terms.
2. Do not add charge heads, kernels, objective changes, or config edits.
3. Use as a calibration comparator against electrostatic pair-energy proposals.

## implementation_checklist
- [ ] Preserve `E = sum_i E_i` plus documented scalar correction terms and keep forces as `-grad(total_energy, positions)`.
- [ ] Preserve benchmark metric field names, split semantics, and runnable entrypoint contract.
- [ ] Modify only the allowed target unit files listed above.
- [ ] Do not edit `config.json`; change MLIP knobs in `model/model.py` or `model/train.py` only.
- [ ] Keep tensor shapes compatible with current single-molecule dataloader and model forward.
- [ ] Add no unbounded cubic neighbor/triplet loops and no Ewald/cell dependency.
- [ ] Reuse existing `i_idx`, `j_idx`, `dij`, and `cutoff_weight`; do not build a new all-pairs path.
- [ ] Call `mark_unit_implemented.py --unit generation_022/proposal_010 --actor implementation_subagent` after edits.

## expected_benchmark_effect
- primary expected gain: Recover ISO17 force/energy balance by reducing body-order/residual interference while preserving the successful TP/PaiNN source mechanism.
- expected tradeoff: possible small RMD17/force regression if new scalar terms create noisy gradients; bounded scales and zero-init should limit this.
- failure signal that would falsify this proposal: Q_total <= source/control after variance, ISO17 gap not improved, or force MAE regression dominates any energy gain.

## ablation_or_control
- required control or comparison: compare against proposal_007 exact source replicate and against proposal_010 non-electrostatic calibration comparator where relevant.
- optional zero-gate / source-fallback / readout-only ablation: implementation may set beta/gate scale to zero to verify source fallback before smoke; do not change benchmark semantics.

## implementation_notes_for_subagent
Use the materialized source unit only. Preserve the current `EvolutionMLIP.forward` energy-to-force contract. For electrostatic proposals, implement the cited SpookyNet mechanism as a scalar pair-energy term using existing directed neighbor tensors (`i_idx`, `j_idx`, `dij`, `cutoff_weight`) and neutralized learned charges; do not replace it with an ordinary atomwise energy residual. Do not edit `config.json`, dataloader, eval metrics, or runnable entrypoint.
