# Proposal 010: Vector-norm dropout regularized readout

- family: vector_norm_regularized_readout
- phase: 2
- jump_type: wildcard
- budget_class: tiny
- expected_capability_gain: Diagnosis-driven regularization of the successful vector-norm channel to test whether ISO17 energy/gap volatility is caused by brittle vector-feature reliance.

## one_sentence_hypothesis
Applying light dropout only to the normalized vector-norm readout channel during training may improve ISO17 generalization while preserving the source's invariant geometry path at evaluation.

## mechanism_refs
- []

## evidence_refs
- context.md::generation_014/proposal_009::ISO17_energy_trend=worsening and gap_penalty=0.0909369398
- mechanism_cards.json::GEN015-M01-gated-invariant-vector-readout-damping::strong evidence for vector-norm readout path, but not for dropout
- mechanism_cards.json::GEN015-W01-conservative-smoothness-guardrail::weak guardrail against non-conservative/discontinuous mechanisms
- proposal_constraints.json::blocked_mechanisms::implementation rewrite without patch blueprint

## historical_relation
- source_unit: generation_014/proposal_009
- relation_to_source: ablation
- not_a_duplicate_of: proposal_007 because this retains expected vector amplitude at evaluation and uses stochastic training regularization rather than a fixed deterministic damping scale.
- why_not_duplicate: No child of source has tested readout-channel regularization while leaving message passing and evaluation semantics unchanged.
- lesson_used: This has no strong external mechanism card, so it is a conservative wildcard/diagnostic only; strong claims remain with M01 gated damping proposals.

## benchmark_rationale
- rmd17 energy: May improve generalization or slightly regress if dropout underfits within 8 epochs.
- rmd17 force: Risk of slight regression from noisier vector readout training.
- rmd17 gap / Q: Could improve if dropout reduces brittle vector-channel dependence.
- iso17 energy: Primary target; regularization may reduce late validation energy spikes.
- iso17 force: Expected neutral-to-slightly-negative.
- iso17 gap / Q: Target lower gap_penalty and mixed_energy_mae; reject force-only wins with worse gap.
- training stability / runtime risk: Low; one dropout module, active only in training; no benchmark semantic change.
- control comparison expectation: Must beat source control on ISO17 energy/gap or it is just noise.

## files_to_edit
- `model/model.py`
- `model/train.py` if needed, otherwise `none`
- never `config.json` for MLIP-quality changes

## code_insertion_points
- `model/model.py::EvolutionMLIP.__init__`: after `self.vector_norm_layer`, add `self.vector_norm_dropout = nn.Dropout(p=0.05)`.
- `model/model.py::EvolutionMLIP.forward_energy`: after normalized `vector_norm`, apply `regularized_vector_norm = self.vector_norm_dropout(vector_norm)` before readout concatenation.
- `model/train.py::train`: none; existing `model.train()` / `model.eval()` controls dropout behavior.

## minimal_edit_plan
1. Add a small dropout module for the vector_norm channel only.
2. Apply dropout after LayerNorm and before concatenation.
3. Leave all other architecture and training settings unchanged.

## implementation_checklist
- [ ] Preserve `E = sum_i E_i` and force-from-energy contract.
- [ ] Preserve benchmark metric field names and runnable entrypoint contract.
- [ ] Modify only the allowed target unit files.
- [ ] Do not edit `config.json`; change MLIP knobs in `model/model.py` or `model/train.py`.
- [ ] Keep tensor shapes compatible with current dataloader and model forward.
- [ ] Add no unbounded cubic neighbor/triplet loops unless explicitly justified by budget.
- [ ] State in implementation report that dropout is diagnosis-driven and not strong evidence-backed.
- [ ] Call `mark_unit_implemented.py --unit <UNIT> --actor implementation_subagent` after edits.

## expected_benchmark_effect
- primary expected gain: Reduced ISO17 energy/gap overfit from lighter reliance on exact vector-norm channels during training.
- expected tradeoff: Under-training or force regression due to regularization in a short run.
- failure signal that would falsify this proposal: Lower Q_total than source and no reduction in ISO17 energy/gap volatility.

## ablation_or_control
- required control or comparison: Exact source control and fixed damping proposal.
- optional zero-gate / source-fallback / readout-only ablation: If dropout helps, later combine with learned gate only after source variance is understood.

## implementation_notes_for_subagent
This is a weak-evidence wildcard. Keep dropout probability small, localized to vector_norm, and active only through normal PyTorch train/eval modes.
