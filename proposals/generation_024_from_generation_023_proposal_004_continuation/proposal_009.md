# Proposal 009: Bounded radial-resolution scaling under source architecture

- family: radial_resolution_scaling_source_architecture
- phase: 3
- jump_type: wildcard
- budget_class: small
- expected_capability_gain: Test whether source performance is limited by radial basis resolution rather than the long-range tail mechanism.

## one_sentence_hypothesis
Increasing code-level radial basis resolution modestly while keeping proposal_004's architecture and LES tail intact can reveal whether the current bottleneck is local geometric resolution instead of SOG-style long-range decay.

## mechanism_refs
- []

## evidence_refs
- context.md current capacity/objective knobs: MODEL_NUM_RBF=32, hidden_dim=96, num_interactions=2, cutoff=5.0
- research_skill proposal_format.md: capacity scaling is valid when bounded and code-level
- benchmark_diagnosis.json: source RMD17 is strong but ISO17 transfer still leaves room; no new external mechanism is claimed
- lineage_stats.json: prior `tp_radial_resolution_scaling` was negative, so this must be bounded and not dominate selection
- generation_023_summary.json: source is close to best-known but not clearly superior to global control; capacity bottleneck remains plausible but unproven.

## historical_relation
- source_unit: generation_023/proposal_004
- relation_to_source: ablation
- not_a_duplicate_of: Not a duplicate of SOG proposals because it changes only radial resolution constants; not a duplicate of previous broad radial scaling because it is applied to the current best LES source with no other architecture changes.
- lesson_used: mechanism search should include one bounded capacity control to distinguish local resolution limits from long-range kernel limits.

## why_not_duplicate
This proposal intentionally does not use the SOG mechanism. It preserves current LES tail and tests `num_rbf` as a code-level bottleneck in the current source state, which has not yet been tried for generation_023/proposal_004.

## benchmark_rationale
- capacity/scaling hypothesis, if any: current `num_rbf=32` may under-resolve local radial structure, limiting both force quality and how latent charges are formed.
- rmd17 energy: possible modest gain if local radial resolution improves local energy fit.
- rmd17 force: possible gain but also overfit/runtime risk; keep increase modest, e.g. 32 -> 40 or 48.
- rmd17 gap / Q: should improve only if resolution is a real bottleneck; otherwise may regress like prior radial scaling.
- iso17 energy: possible transfer gain through better local descriptors feeding both readout and charge head.
- iso17 force: possible neutral-to-small gain; not targeted by long-range evidence.
- iso17 gap / Q: improvement would argue that source plateau is not solely LR kernel shape.
- training stability / runtime risk: small-to-medium; more RBF features increase parameter count and memory but no new O(N^3) work.
- control comparison expectation: should be judged against exact source and SOG proposals; avoid selecting if the batch already has too many non-mechanism scalers.

## files_to_edit
- `model/model.py`
- `model/train.py`
- never `config.json` for MLIP-quality changes

## code_insertion_points
- `model/model.py::EvolutionMLIP.__init__` default argument: change `num_rbf` default from `32` to a bounded value such as `40` or `48` if present.
- `model/train.py::MLIP code-level defaults`: change `MODEL_NUM_RBF = 32` to the same bounded value.
- `model/model.py` RBF construction and interaction layers: no semantic edits beyond accepting the new default dimension.
- `model/train.py` training/eval loops: no semantic changes.

## minimal_edit_plan
1. Increase only code-level `num_rbf` from 32 to 40 or 48 in both model and train defaults.
2. Leave hidden_dim, depth, cutoff, body branch, charge heads, LES tail, loss weights, and benchmark code unchanged.
3. Add a comment identifying this as bounded radial-resolution scaling for bottleneck diagnosis.

## implementation_checklist
- [ ] Preserve `E = sum_i E_i` and force-from-energy contract.
- [ ] Preserve benchmark metric field names and runnable entrypoint contract.
- [ ] Modify only the allowed target unit files.
- [ ] Do not edit `config.json`; change MLIP knobs in `model/model.py` or `model/train.py`.
- [ ] Keep tensor shapes compatible with current dataloader and model forward.
- [ ] Add no unbounded cubic neighbor/triplet loops unless explicitly justified by budget.
- [ ] Do not change SOG/LES mechanism code in this scaling probe.
- [ ] Keep scaling bounded; do not simultaneously scale hidden_dim, depth, and num_rbf.
- [ ] Call `mark_unit_implemented.py --unit <UNIT> --actor implementation_subagent` after edits.

## expected_benchmark_effect
- primary expected gain: small force/energy gain if local radial resolution was limiting source descriptors.
- expected tradeoff: modest runtime/memory increase and overfit risk; mechanism coverage not advanced.
- failure signal that would falsify this proposal: no Q improvement or regression relative to exact source/control, especially if SOG proposals improve ISO17 instead.

## ablation_or_control
- required control or comparison: compare with exact source proposal_008 and at least one SOG mechanism proposal.
- optional zero-gate / source-fallback / readout-only ablation: not applicable; source architecture remains otherwise unchanged.

## implementation_notes_for_subagent
This is a wildcard capacity probe, not external-mechanism evidence. Keep the edit minimal and code-level. Do not alter config.json, cutoff, training objective, or long-range tail code.
