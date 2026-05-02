# Proposal 005: Low-rank vector norm adapter

- family: low_rank_vector_norm_adapter
- phase: 3
- jump_type: jump
- budget_class: small
- expected_capability_gain: Compress normalized vector norms through a small adapter before readout to reduce noisy channel-wise coupling while retaining invariant geometry.

## one_sentence_hypothesis
A bottleneck adapter on `LayerNorm(||vector_state||)` can keep robust invariant vector information and suppress high-variance vector channels that hurt ISO17 transfer.

## mechanism_refs
- GEN015-M01-gated-invariant-vector-readout-damping

## evidence_refs
- mechanism_cards.json::GEN015-M01-gated-invariant-vector-readout-damping::current_vector_norm_shape=[N,H]
- mechanism_cards.json::GEN015-M01-gated-invariant-vector-readout-damping::physical_principle::rotationally_invariant_scalar_energy
- patch_blueprints.json::GEN015-M01-gated-invariant-vector-readout-damping::bounded_edit preserves autograd forces
- context.md::tree_lineage::phase_2 positive mean_G_delta; phase_3 under careful bounded jump

## historical_relation
- source_unit: generation_014/proposal_009
- relation_to_source: jump
- not_a_duplicate_of: proposal_001 because this proposal transforms vector norms through a bottleneck adapter rather than directly learning a multiplicative gate.
- why_not_duplicate: Prior source used all `H` normalized vector channels at full width; this tests low-rank filtering as a mechanism-diverse vector readout.
- lesson_used: Local readout calibration has the best known unit but mixed history; keep the successful invariant channel while reducing channel capacity.

## benchmark_rationale
- rmd17 energy: May remain strong if key vector-norm modes are low-dimensional.
- rmd17 force: Bottleneck could blunt force gains if too narrow; use `H//2` not an extreme compression.
- rmd17 gap / Q: Reduced capacity may improve gap stability.
- iso17 energy: Target is better cross-conformer energy calibration through filtered vector invariants.
- iso17 force: Expected neutral-to-slightly-negative versus source.
- iso17 gap / Q: Lower gap_penalty is the main target.
- training stability / runtime risk: Low; a small MLP and same tensor ranks.
- control comparison expectation: Should beat source only if source vector channel is over-capacity/noisy.

## files_to_edit
- `model/model.py`
- `model/train.py` if needed, otherwise `none`
- never `config.json` for MLIP-quality changes

## code_insertion_points
- `model/model.py::EvolutionMLIP.__init__`: after `self.vector_norm_layer`, add `bottleneck = max(hidden_dim // 2, 16)` and `self.vector_norm_adapter = nn.Sequential(nn.Linear(hidden_dim, bottleneck), nn.SiLU(), nn.Linear(bottleneck, hidden_dim))`.
- `model/model.py::EvolutionMLIP.forward_energy`: after normalized `vector_norm`, compute `adapted_vector_norm = self.vector_norm_adapter(vector_norm)` and concatenate `[scalar_state, adapted_vector_norm]`.
- `model/train.py::train`: none.

## minimal_edit_plan
1. Add a bottleneck vector norm adapter in `__init__`.
2. Replace raw normalized vector_norm in readout input with adapter output.
3. Keep existing readout width `hidden_dim * 2` and all training semantics unchanged.

## implementation_checklist
- [ ] Preserve `E = sum_i E_i` and force-from-energy contract.
- [ ] Preserve benchmark metric field names and runnable entrypoint contract.
- [ ] Modify only the allowed target unit files.
- [ ] Do not edit `config.json`; change MLIP knobs in `model/model.py` or `model/train.py`.
- [ ] Keep tensor shapes compatible: adapter input/output both `[N,H]`.
- [ ] Add no unbounded cubic neighbor/triplet loops unless explicitly justified by budget.
- [ ] Keep vector norm invariant; do not feed orientation-dependent vector components into scalar energy.
- [ ] Call `mark_unit_implemented.py --unit <UNIT> --actor implementation_subagent` after edits.

## expected_benchmark_effect
- primary expected gain: Improved ISO17 gap/Q by filtering vector norm channels.
- expected tradeoff: Possible RMD17 force/Q loss if useful high-frequency vector channels are compressed away.
- failure signal that would falsify this proposal: Lower Q_total than source and no reduction in ISO17 gap_penalty.

## ablation_or_control
- required control or comparison: Compare to source, per-channel gate, and scalar low-start gate.
- optional zero-gate / source-fallback / readout-only ablation: If adapter wins, later compare adapter+gate versus adapter-only.

## implementation_notes_for_subagent
Use a simple adapter only. Avoid dropout, attention, or additional interaction blocks in this proposal.
