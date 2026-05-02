# Proposal 005: Charge-pair energy with ISO17 energy-balanced warmup

- family: spookynet_charge_objective_balance
- phase: 4
- jump_type: jump
- budget_class: medium
- expected_capability_gain: Improve ISO17 energy/gap while controlling force tradeoff by pairing electrostatic energy with a slightly less force-heavy code-level warmup.

## one_sentence_hypothesis
The charge-pair mechanism may need a small early energy signal to learn useful q values, so a bounded code-level warmup adjustment should improve ISO17 energy without redefining benchmark metrics.

## mechanism_refs
- `GEN022-M01-neutral-charge-electrostatic-energy-head`
  - formula: SpookyNet Eq. (23) E_ele = k_e sum_i sum_{j>i} q_i q_j [f_switch(r_ij)/sqrt(r_ij^2+1) + (1-f_switch(r_ij))/r_ij]; Eq. (24) q_i = w_q^T f_i + q_Zi + (1/N)(Q - sum_j(w_q^T f_j + q_Zj)). Current bounded neutral variant: q_raw_i = q_scale*tanh(charge_head([scalar_state_i, vector_norm_i])); q_i = q_raw_i - mean_j q_raw_j; E_charge = beta*0.5*sum_directed q_i q_j * cutoff_weight_ij / sqrt(d_ij^2+1).
  - repo_code_trace: repo_artifact:repo_001 -> OUnke/SpookyNet@d57b1fc02c4f1304a9445b2b9aa55a906818dd1b:spookynet/modules/electrostatic_energy.py::ElectrostaticEnergy._coulomb lines 180-202 compute ke/2*q[idx_i]*q[idx_j], damped vs 1/r switch, and scatter-add pair electrostatic contributions; ElectrostaticEnergy.forward uses this nonperiodic Coulomb path unless Ewald is enabled; electronic_embedding.py::ElectronicEmbedding.forward shows learned electronic scalars modulating atom features.
  - current_insertion_point: current insertion point: model/model.py::EvolutionMLIP.__init__ add zero/near-zero initialized charge/electronic head and scale parameter; model/model.py::EvolutionMLIP.forward_energy after vector_norm/readout_norm/residual_input are available and before final return, reuse existing i_idx, j_idx, dij, cutoff_weight from _build_neighbor_list; model/train.py keeps benchmark loss/objective semantics unless explicitly listed.

## evidence_refs
- active evidence brief: `/home/lmy/.openclaw/workspace/research_runtime/knowledge/briefs/evidence_brief_20260501T091811Z.md`
- active evidence package: `/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/evidence_run_20260501T091811Z`
- `mechanism_cards.json` strong card `GEN022-M01-neutral-charge-electrostatic-energy-head` with formula derivation, tensor shapes, repo code trace, and current insertion point
- `patch_blueprints.json` blueprint `GEN022-M01-neutral-charge-electrostatic-energy-head` marked implementation_ready=true
- `proposal_constraints.json` allows `GEN022-M01-neutral-charge-electrostatic-energy-head` as strong evidence; blocked mechanisms include unproven model-family labels and ordinary force-only proposals
- `evidence_provenance.json`: `paper_artifact:paper_001` and `repo_artifact:repo_001` are fresh strong-capable sources; audit_report issues=[]
- source metrics: generation_021/proposal_001 Q_total=4.047536521538605, Q_rmd17=4.210072139663386, Q_iso17=3.7456846593068707; ISO17 mixed_energy_mae=0.26671175340941544 and gap_penalty=0.1417151905668173 worsened versus generation_020/proposal_003

## historical_relation
- source_unit: generation_021/proposal_001
- relation_to_source: jump
- not_a_duplicate_of: Not a duplicate of generation_021 training_objective attempts because the architectural mechanism is still explicit SpookyNet q_i q_j pair energy; objective change only supports charge learning.
- lesson_used: Training-only families show negative mean G_delta, so objective changes should not stand alone; pair them with evidence-backed electrostatics and keep the schedule bounded.

## why_not_duplicate
Not a duplicate of generation_021 training_objective attempts because the architectural mechanism is still explicit SpookyNet q_i q_j pair energy; objective change only supports charge learning.

## benchmark_rationale
Discuss expected effects on all relevant benchmark signals, not force-only:
- capacity/scaling hypothesis, if any: Electrostatic proposal with a training support knob; does not turn the mechanism into ordinary residual calibration.
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
- `model/train.py`
- never `config.json` for MLIP-quality changes

## code_insertion_points
- `model/model.py::EvolutionMLIP.__init__/forward_energy`: implement neutral charge pair energy as in proposal_001 with beta cap 0.01.
- `model/train.py::train_model`: change only code-level warmup constants so epochs 1-2 use energy factor floor 0.8 instead of 0.6 and force factor ceiling 1.05 instead of 1.1; keep final weights 1/20 and metric semantics.
- `model/train.py` constants remain config-independent.

## minimal_edit_plan
1. Add neutral charge head and damped pair energy with zero-init fallback.
2. Adjust only the early warmup multipliers in train.py to slightly expose energy/gap signal to the charge head.
3. Keep final loss weights and benchmark evaluation unchanged; document that this is not a config edit.

## implementation_checklist
- [ ] Preserve `E = sum_i E_i` plus documented scalar correction terms and keep forces as `-grad(total_energy, positions)`.
- [ ] Preserve benchmark metric field names, split semantics, and runnable entrypoint contract.
- [ ] Modify only the allowed target unit files listed above.
- [ ] Do not edit `config.json`; change MLIP knobs in `model/model.py` or `model/train.py` only.
- [ ] Keep tensor shapes compatible with current single-molecule dataloader and model forward.
- [ ] Add no unbounded cubic neighbor/triplet loops and no Ewald/cell dependency.
- [ ] Reuse existing `i_idx`, `j_idx`, `dij`, and `cutoff_weight`; do not build a new all-pairs path.
- [ ] Call `mark_unit_implemented.py --unit generation_022/proposal_005 --actor implementation_subagent` after edits.

## expected_benchmark_effect
- primary expected gain: Improve ISO17 energy/gap while controlling force tradeoff by pairing electrostatic energy with a slightly less force-heavy code-level warmup.
- expected tradeoff: possible small RMD17/force regression if new scalar terms create noisy gradients; bounded scales and zero-init should limit this.
- failure signal that would falsify this proposal: Q_total <= source/control after variance, ISO17 gap not improved, or force MAE regression dominates any energy gain.

## ablation_or_control
- required control or comparison: compare against proposal_007 exact source replicate and against proposal_010 non-electrostatic calibration comparator where relevant.
- optional zero-gate / source-fallback / readout-only ablation: implementation may set beta/gate scale to zero to verify source fallback before smoke; do not change benchmark semantics.

## implementation_notes_for_subagent
Use the materialized source unit only. Preserve the current `EvolutionMLIP.forward` energy-to-force contract. For electrostatic proposals, implement the cited SpookyNet mechanism as a scalar pair-energy term using existing directed neighbor tensors (`i_idx`, `j_idx`, `dij`, `cutoff_weight`) and neutralized learned charges; do not replace it with an ordinary atomwise energy residual. Do not edit `config.json`, dataloader, eval metrics, or runnable entrypoint.
