# Proposal 005: Hardness-stabilized charge residual

- family: latent_charge_hardness_residual
- phase: 4
- jump_type: exploit
- budget_class: medium
- expected_capability_gain: Stabilize the electrostatic residual with element-conditioned hardness so ISO17 energy can improve without charge blow-up.

## one_sentence_hypothesis
Adding a positive element-conditioned hardness penalty to the neutral latent charge residual will make the nonlocal energy-decomposition path better conditioned than an unconstrained q-head.

## mechanism_refs
- GEN016-M02-bounded-electrostatic-energy-decomposition

## evidence_refs
- paper_artifact:paper_002
- repo_artifact:repo_001
- mechanism_cards.json::GEN016-M02-bounded-electrostatic-energy-decomposition ChargeEq/Ewald code trace
- patch_blueprints.json::GEN016-M02-bounded-electrostatic-energy-decomposition bounded direct residual guidance
- proposal_constraints.json::allowed_mechanisms includes GEN016-M02-bounded-electrostatic-energy-decomposition
- benchmark_diagnosis.json::source ISO17 energy instability

## historical_relation
- source_unit: generation_015/proposal_004
- relation_to_source: exploit
- not_a_duplicate_of: This is not the plain M02 direct residual; it adds a bounded hardness/self-energy term to constrain latent charges while avoiding the full linear solve.
- lesson_used: Because unlabelled latent charges are medium-high risk, the first exploit should include physical damping and a source fallback.

## why_not_duplicate
Compared with proposal_004, this proposal changes the residual formula to `E_nonlocal = beta * E_pair + gamma * sum_i softplus(J_Z_i) q_i^2`, using element-conditioned hardness to regularize charge magnitudes.

## benchmark_rationale
- rmd17 energy: Hardness penalty should reduce residual overfitting and preserve source energy.
- rmd17 force: Smoother/smaller q reduces force-regression risk.
- rmd17 gap / Q: Expected neutral.
- iso17 energy: May improve less aggressively than proposal_004 but with better stability.
- iso17 force: Expected safer than unconstrained electrostatic residual.
- iso17 gap / Q: Modest positive if energy calibration improves without force cost.
- training stability / runtime risk: Medium O(N^2); added hardness is cheap and stabilizing.
- control comparison expectation: Should be more stable than plain q residual if both are selected.

## files_to_edit
- `model/model.py`
- `model/train.py`: none expected
- never `config.json` for MLIP-quality changes

## code_insertion_points
- `model/model.py::EvolutionMLIP.__init__`: add q head, element hardness embedding/parameter constrained by softplus, `electrostatic_log_scale`, and `hardness_log_scale` initialized small.
- `model/model.py::new _charge_energy_residual`: compute neutral normalized q, damped pair term, and positive hardness self-energy.
- `model/model.py::EvolutionMLIP.forward_energy`: add residual after local source per-atom energy.
- `model/train.py::none`: retain source training weights.

## minimal_edit_plan
1. Implement the neutral q-head and all-pair damped residual as in M02, but with `q=tanh(q_raw)` and `q -= mean(q)`.
2. Add `hardness = softplus(self.charge_hardness(numbers)).squeeze(-1) + eps` and a small positive `sum(hardness * q^2)` term.
3. Return local source energy plus damped pair/self residual under tiny learnable scales.

## implementation_checklist
- [ ] Preserve `E = sum_i E_i` plus differentiable scalar nonlocal/self residual and force-from-energy contract.
- [ ] Preserve benchmark metric field names and runnable entrypoint contract.
- [ ] Modify only the allowed target unit files.
- [ ] Do not edit `config.json`; change MLIP knobs in `model/model.py` or `model/train.py`.
- [ ] Keep tensor shapes compatible with current dataloader and model forward.
- [ ] Add no unbounded cubic neighbor/triplet loops.
- [ ] Ensure hardness is positive and residual scale starts near no-op.
- [ ] Call `mark_unit_implemented.py --unit <UNIT> --actor implementation_subagent` after edits.

## expected_benchmark_effect
- primary expected gain: Safer ISO17 energy/gap improvement than an unconstrained charge residual.
- expected tradeoff: Regularization may suppress useful nonlocal signal.
- failure signal that would falsify this proposal: q collapses to zero with no ISO17 improvement or force/energy both regress.

## ablation_or_control
- required control or comparison: source control and beta/gamma zero source fallback.
- optional zero-gate / source-fallback / readout-only ablation: disable hardness term to compare with proposal_004 if both exist.

## implementation_notes_for_subagent
This is a bounded charge-stabilization exploit, not a full charge-equilibration solve. Keep all additions inside `model/model.py` and preserve source train/eval semantics.
