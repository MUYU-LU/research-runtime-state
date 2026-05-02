# Proposal 007: Backward simplification to static body-order descriptor

- family: body_order_message_simplify
- phase: 3
- jump_type: backward-simplify
- budget_class: tiny
- expected_capability_gain: Determine whether the source one-step descriptor message is unnecessary or harmful compared with a simpler static invariant body-order residual.

## one_sentence_hypothesis
Removing the descriptor-level edge message from `BodyOrderMessageBranch` may improve ISO17 stability by retaining compact body-order invariants while reducing message-induced force/energy variance.

## mechanism_refs
- []

## evidence_refs
- benchmark_diagnosis.json::generation_016/proposal_002 neutral_variance and ISO17 energy_trend=worsening
- benchmark_diagnosis.json::generation_016/proposal_003 had simpler minimal nu=2 branch with ISO17 Q=3.6327311631507366 but lower RMD17 Q, indicating simplification is worth isolating
- mechanism_cards.json::GEN017-M02 weak_hypothesis cautions against unbounded tensor hierarchy growth and supports keeping Cartesian descriptors small only as weak/background evidence
- proposal_constraints.json::weak_or_hypothesis_mechanisms includes GEN017-M02 but not as strong proposal mechanism

## historical_relation
- source_unit: generation_016/proposal_002
- relation_to_source: simplify
- not_a_duplicate_of: This simplifies the selected source itself by disabling only its descriptor message update; it is not generation_016/proposal_003 because it keeps the source descriptor dimensionality/readout and removes only the message pass.
- lesson_used: generation_016/proposal_001's fuller static body branch was negative, while proposal_003 showed ISO17 component improvement; isolate message-pass contribution without changing descriptor family.

## why_not_duplicate
No prior selected unit exactly tested `generation_016/proposal_002` with `edge_message` removed but the same `BodyOrderMessageBranch` descriptor/readout retained. This backward proposal is a source-specific ablation, not a new external mechanism.

## benchmark_rationale
- rmd17 energy: Could regress if message pass helped source RMD17; should reveal source contribution.
- rmd17 force: May improve or stay stable by removing edge-message gradients.
- rmd17 gap / Q: Expected possibly lower than source but useful as a simplification control.
- iso17 energy: May improve if message aggregation causes energy drift.
- iso17 force: Could improve by reducing residual branch complexity.
- iso17 gap / Q: Tests whether source ISO17 gap penalty came from message pass rather than body-order descriptor itself.
- training stability / runtime risk: Lower runtime and low implementation risk.
- control comparison expectation: Should be interpreted against exact source control and not oversold as evidence-backed architecture gain.

## files_to_edit
- `model/model.py`
- `model/train.py`: none expected
- never `config.json` for MLIP-quality changes

## code_insertion_points
- `model/model.py::BodyOrderMessageBranch.forward`: after `descriptor = self.initial_norm(self._symmetrize(atom_a))`, return `descriptor` directly or combine with a zero-initialized/fixed-zero message scale.
- `model/model.py::BodyOrderMessageBranch.__init__`: optionally keep `edge_gate`, `sender_message`, and `message_norm` unused to minimize diff, or add a fixed zero `message_scale` if cleaner.
- `model/train.py::none`: no training change.

## minimal_edit_plan
1. Preserve `_angular_monomials`, `_symmetrize`, radial/type embeddings, and descriptor dimension exactly.
2. Disable only the edge-message aggregation path in `BodyOrderMessageBranch.forward`.
3. Leave `EvolutionMLIP.forward_energy`, body-order readout, and source training settings unchanged.

## implementation_checklist
- [ ] Preserve `E = sum_i E_i` and force-from-energy contract.
- [ ] Preserve benchmark metric field names and runnable entrypoint contract.
- [ ] Modify only the allowed target unit files.
- [ ] Do not edit `config.json`; change MLIP knobs in `model/model.py` or `model/train.py`.
- [ ] Keep tensor shapes compatible with current dataloader and model forward.
- [ ] Add no unbounded cubic neighbor/triplet loops unless explicitly justified by budget.
- [ ] Do not cite GEN017-M02 as strong evidence; it is weak/background only.
- [ ] Call `mark_unit_implemented.py --unit <UNIT> --actor implementation_subagent` after edits.

## expected_benchmark_effect
- primary expected gain: Lower ISO17 energy/gap instability or clearer diagnosis of the descriptor-message contribution.
- expected tradeoff: Possible loss of source RMD17 Q if the message pass was beneficial.
- failure signal that would falsify this proposal: Worse ISO17 energy/gap and lower RMD17 Q than exact control.

## ablation_or_control
- required control or comparison: Exact generation_016/proposal_002 control.
- optional zero-gate / source-fallback / readout-only ablation: Implement as an explicit zero message scale so source can be restored by setting scale to one in a later repair.

## implementation_notes_for_subagent
This is a backward simplification, not a new mechanism. Do not add vector gates or new contractions here; the value is isolating the existing source message pass.
