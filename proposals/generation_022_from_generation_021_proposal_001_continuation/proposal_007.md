# Proposal 007: Exact source replicate variance control

- family: control_replicate
- phase: 0
- jump_type: control
- budget_class: tiny
- expected_capability_gain: Measure generation_022 run variance around generation_021/proposal_001 before attributing small Q_total changes to new mechanisms.

## one_sentence_hypothesis
An exact source replicate establishes whether observed electrostatic gains exceed normal RMD17/ISO17 variance.

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
- not_a_duplicate_of: Not a duplicate in scientific role: this is the required generation control replicate, not a mechanism candidate or residual calibration.
- lesson_used: Control replicates have shown Q_total variance comparable to small G_delta values, including generation_021/proposal_007 slightly exceeding the source.

## why_not_duplicate
Not a duplicate in scientific role: this is the required generation control replicate, not a mechanism candidate or residual calibration.

## benchmark_rationale
Discuss expected effects on all relevant benchmark signals, not force-only:
- capacity/scaling hypothesis, if any: No SpookyNet mechanism is implemented here; it anchors interpretation of all charge-pair proposals.
- rmd17 energy: should remain close to source mixed_energy_mae=0.030508691406250003; reject if RMD17 energy drift erases Q_rmd17 strength.
- rmd17 force: source mixed_force_mae=0.05835015199595364 is strong; any added scalar term must keep conservative force gradients bounded.
- rmd17 gap / Q: tolerate only neutral variance around Q_rmd17=4.210072139663386 unless ISO17 gain is clearly larger.
- iso17 energy: primary diagnostic because source mixed_energy_mae=0.26671175340941544 and validation energy trend worsened.
- iso17 force: source mixed_force_mae=0.15079258253733485; expected to remain within small tradeoff unless energy/gap gains dominate Q_total.
- iso17 gap / Q: primary target is reducing gap_penalty=0.1417151905668173 and lifting Q_iso17=3.7456846593068707.
- training stability / runtime risk: no benchmark/config changes; O(E) edge operations only for electrostatic proposals, no Ewald, no all-pairs, no cubic loops.
- control comparison expectation: compare against exact source control proposal_007 and source Q_total=4.047536521538605; require positive G_delta beyond observed control variance.

## files_to_edit
- none
- never `config.json` for MLIP-quality changes

## code_insertion_points
- none

## minimal_edit_plan
1. Exact copy of generation_021/proposal_001.
2. Do not change model/model.py or model/train.py.
3. Mark implemented as a control replicate if materialized.

## implementation_checklist
- [ ] Do not change `model/model.py`.
- [ ] Do not change `model/train.py`.
- [ ] Preserve benchmark metric field names and runnable entrypoint contract.
- [ ] Mark implemented as control replicate if required by workflow.
- [ ] Call `mark_unit_implemented.py --unit generation_022/proposal_007 --actor implementation_subagent` after control status is prepared.

## expected_benchmark_effect
- primary expected gain: Measure generation_022 run variance around generation_021/proposal_001 before attributing small Q_total changes to new mechanisms.
- expected tradeoff: possible small RMD17/force regression if new scalar terms create noisy gradients; bounded scales and zero-init should limit this.
- failure signal that would falsify this proposal: Q_total <= source/control after variance, ISO17 gap not improved, or force MAE regression dominates any energy gain.

## ablation_or_control
- required control or comparison: compare against proposal_007 exact source replicate and against proposal_010 non-electrostatic calibration comparator where relevant.
- optional zero-gate / source-fallback / readout-only ablation: implementation may set beta/gate scale to zero to verify source fallback before smoke; do not change benchmark semantics.

## implementation_notes_for_subagent
Use the materialized source unit only. Preserve the current `EvolutionMLIP.forward` energy-to-force contract. For electrostatic proposals, implement the cited SpookyNet mechanism as a scalar pair-energy term using existing directed neighbor tensors (`i_idx`, `j_idx`, `dij`, `cutoff_weight`) and neutralized learned charges; do not replace it with an ordinary atomwise energy residual. Do not edit `config.json`, dataloader, eval metrics, or runnable entrypoint.
