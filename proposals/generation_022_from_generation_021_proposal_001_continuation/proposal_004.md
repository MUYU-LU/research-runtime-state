# Proposal 004: Aggressive charge-electronic gated pair interaction

- family: spookynet_electronic_pair_gate
- phase: 5
- jump_type: jump
- budget_class: medium
- expected_capability_gain: Larger ISO17 energy/gap improvement by letting electronic charge scalars gate pair messages as well as pair energy.

## one_sentence_hypothesis
A bounded electronic scalar gate inspired by SpookyNet ElectronicEmbedding can couple learned neutral charges back into the last scalar state and improve transfer more than a readout-only pair energy.

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
- not_a_duplicate_of: Not a duplicate of conservative charge-head proposals because it adds an electronic interaction path: neutral q features gate the final scalar update before readout while still adding q_i q_j energy.
- lesson_used: Low-rank TP and PaiNN late mixing were the strongest historical mechanism branches; this jump combines that source state with a fresh electronic interaction mechanism instead of another atomwise residual.

## why_not_duplicate
Not a duplicate of conservative charge-head proposals because it adds an electronic interaction path: neutral q features gate the final scalar update before readout while still adding q_i q_j energy.

## benchmark_rationale
Discuss expected effects on all relevant benchmark signals, not force-only:
- capacity/scaling hypothesis, if any: Required aggressive charge/electronic interaction variant; still uses charge-neutral pair energy and cites SpookyNet repo electronic_embedding trace.
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
- `model/model.py::EvolutionMLIP.__init__`: add charge head, beta logit, and `electronic_gate = Linear(2 -> hidden_dim)` or `Linear(hidden_dim*2 + 2 -> hidden_dim)` with zero-init output.
- `model/model.py::EvolutionMLIP.forward_energy`: compute neutral q; compute per-atom electronic features `[q_i, abs(q_i)]`; add `0.05*tanh(electronic_gate(...))` to scalar_state before final readout, then add q_i q_j pair energy.
- `model/train.py`: no change.

## minimal_edit_plan
1. Implement zero-init neutral charge head and pair energy with beta cap 0.015.
2. Build a tiny electronic gate from invariant residual_input plus q features; zero-init so source behavior is recovered.
3. Apply the gate only after existing TP/PaiNN mixing and before `per_atom_energy`; add pair energy to total return.

## implementation_checklist
- [ ] Preserve `E = sum_i E_i` plus documented scalar correction terms and keep forces as `-grad(total_energy, positions)`.
- [ ] Preserve benchmark metric field names, split semantics, and runnable entrypoint contract.
- [ ] Modify only the allowed target unit files listed above.
- [ ] Do not edit `config.json`; change MLIP knobs in `model/model.py` or `model/train.py` only.
- [ ] Keep tensor shapes compatible with current single-molecule dataloader and model forward.
- [ ] Add no unbounded cubic neighbor/triplet loops and no Ewald/cell dependency.
- [ ] Reuse existing `i_idx`, `j_idx`, `dij`, and `cutoff_weight`; do not build a new all-pairs path.
- [ ] Call `mark_unit_implemented.py --unit generation_022/proposal_004 --actor implementation_subagent` after edits.

## expected_benchmark_effect
- primary expected gain: Larger ISO17 energy/gap improvement by letting electronic charge scalars gate pair messages as well as pair energy.
- expected tradeoff: possible small RMD17/force regression if new scalar terms create noisy gradients; bounded scales and zero-init should limit this.
- failure signal that would falsify this proposal: Q_total <= source/control after variance, ISO17 gap not improved, or force MAE regression dominates any energy gain.

## ablation_or_control
- required control or comparison: compare against proposal_007 exact source replicate and against proposal_010 non-electrostatic calibration comparator where relevant.
- optional zero-gate / source-fallback / readout-only ablation: implementation may set beta/gate scale to zero to verify source fallback before smoke; do not change benchmark semantics.

## implementation_notes_for_subagent
Use the materialized source unit only. Preserve the current `EvolutionMLIP.forward` energy-to-force contract. For electrostatic proposals, implement the cited SpookyNet mechanism as a scalar pair-energy term using existing directed neighbor tensors (`i_idx`, `j_idx`, `dij`, `cutoff_weight`) and neutralized learned charges; do not replace it with an ordinary atomwise energy residual. Do not edit `config.json`, dataloader, eval metrics, or runnable entrypoint.
