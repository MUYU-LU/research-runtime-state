# Proposal 004: Shared recurrent PaiNN mixer across layers

- family: shared_painn_feedback
- phase: 5
- jump_type: jump
- budget_class: small
- expected_capability_gain: Test whether a single shared invariant mixer provides stable cross-layer vector-to-scalar feedback with fewer free parameters.

## one_sentence_hypothesis
A shared GEN020-M01 mixer reused after each TP merge can make vector-conditioned scalar feedback more data-efficient than independent per-layer mixers, improving ISO17 Q without overfitting RMD17.

## mechanism_refs
- GEN020-M01-painn-intra-layer-vector-norm-mixing

## evidence_refs
- mechanism_cards.json GEN020-M01 mathematical_form and source-recoverability requirement
- patch_blueprints.json target insertion points after each TP merge
- current_code_profile.json H=96, vector_state `[N,H,3]`, TP branch already present
- benchmark_diagnosis.json Q_total=4.026030, parent Q_total=4.049988

## historical_relation
- source_unit: generation_019/proposal_003
- relation_to_source: jump
- not_a_duplicate_of: This is broader than exploit proposals because the same mixer is recurrently applied across layers, imposing shared invariant feedback rather than independent layer-specific corrections.
- lesson_used: Source is neutral versus parent; a shared low-parameter jump tests mechanism form while limiting capacity and variance.

## why_not_duplicate
It is not proposal_001's independent per-layer module. Parameter sharing changes the inductive bias: the same norm/dot contraction rule must work at all message-passing depths.

## benchmark_rationale
- capacity/scaling hypothesis, if any: Reduces parameters relative to full independent mixers; tests inductive bias, not raw capacity.
- rmd17 energy: Shared zero-start mixer should protect mixed_energy_mae=0.031769.
- rmd17 force: Preserve mixed_force_mae=0.060948; shared weights may reduce force noise versus many independent gates.
- rmd17 gap / Q: Avoid gap_penalty >0.010551 and keep Q_rmd17 near 4.166948.
- iso17 energy: Targets mixed_energy_mae=0.252341 by consistently injecting vector invariants into scalar channels before each later pass.
- iso17 force: Expected neutral/slight gain; if force improves but energy/gap worsens, mechanism is miscalibrated.
- iso17 gap / Q: Seek Q_iso17 >3.764325 and lower gap_penalty=0.144950.
- training stability / runtime risk: Same compute as a mixer call per layer but fewer parameters; recurrent application can amplify residuals, so cap <=0.03-0.05 is mandatory.
- control comparison expectation: Improvement must exceed source/control variance and be interpreted against full per-layer proposal_001.

## files_to_edit
- `model/model.py`
- `model/train.py` none
- never `config.json` for MLIP-quality changes

## code_insertion_points
- `model/model.py::TPInvariantPaiNNMixing`: implement the bounded mixer primitive.
- `model/model.py::EvolutionMLIP.__init__`: create one `self.shared_tp_invariant_mixer` instead of one module per interaction.
- `model/model.py::EvolutionMLIP.forward_energy`: call the same mixer after every TP residual merge.
- `model/train.py`: no change.

## minimal_edit_plan
1. Implement the M01 mixer with zero-start residuals and alpha caps.
2. Instantiate exactly one shared mixer module.
3. Apply it after each TP merge with no per-layer extra parameters except optional scalar/vector alpha logits shared across all calls.
4. Leave all data/eval/config semantics unchanged.

## implementation_checklist
- [ ] Preserve `E = sum_i E_i` and force-from-energy contract.
- [ ] Preserve benchmark metric field names and runnable entrypoint contract.
- [ ] Modify only the allowed target unit files.
- [ ] Do not edit `config.json`; change MLIP knobs in `model/model.py` or `model/train.py`.
- [ ] Keep tensor shapes compatible with current dataloader and model forward.
- [ ] Add no unbounded neighbor/triplet loops.
- [ ] Ensure repeated application cannot exceed bounded residual caps.
- [ ] Call `mark_unit_implemented.py --unit <UNIT> --actor implementation_subagent` after edits.

## expected_benchmark_effect
- primary expected gain: ISO17 energy/gap lift with less parameter variance than independent mixers.
- expected tradeoff: Shared rule may be too restrictive for early vs late layers; recurrent use can still destabilize if caps are too high.
- failure signal that would falsify this proposal: Worse Q_total than proposal_001/003 or RMD17 regression, indicating sharing is the wrong bias.

## ablation_or_control
- required control or comparison: Zero shared gate recovers source.
- optional zero-gate / source-fallback / readout-only ablation: Compare full independent proposal_001 to shared proposal_004 for parameterization effect.

## implementation_notes_for_subagent
Do not accidentally instantiate per-layer mixers. The point is a shared recurrent atomwise mixer, not larger capacity.
