# Proposal 004: Neutral latent electrostatic residual

- family: latent_electrostatic_residual
- phase: 4
- jump_type: jump
- budget_class: small
- expected_capability_gain: Add a bounded nonlocal energy-decomposition term to target ISO17 conformer energy/gap failures.

## one_sentence_hypothesis
A neutralized latent charge head with a damped all-pair Coulomb-like residual will improve ISO17 energy calibration by separating nonlocal pair energy from the source local atomic readout.

## mechanism_refs
- GEN016-M02-bounded-electrostatic-energy-decomposition

## evidence_refs
- paper_artifact:paper_002
- repo_artifact:repo_001
- mechanism_cards.json::GEN016-M02-bounded-electrostatic-energy-decomposition
- patch_blueprints.json::GEN016-M02-bounded-electrostatic-energy-decomposition
- benchmark_diagnosis.json::generation_015/proposal_004 ISO17 val energy worsening and gap_penalty=0.09986681269946639
- current_code_profile.json::EvolutionMLIP.forward_energy scalar_state insertion point

## historical_relation
- source_unit: generation_015/proposal_004
- relation_to_source: jump
- not_a_duplicate_of: Prior source descendants are cutoff-local learned energies; this adds a separate all-pair nonlocal energy term and latent charge decomposition.
- lesson_used: Good source forces but weak ISO17 energy/gap suggest the next jump should target energy decomposition/nonlocal information, not another local gate.

## why_not_duplicate
The proposed q-head and pair-energy sum operate after the local scalar state is formed and use all atom pairs, so it changes energy decomposition and nonlocal information paths rather than the existing local message block/readout mechanics.

## benchmark_rationale
- rmd17 energy: Should remain stable with beta initialized near zero.
- rmd17 force: Smooth damped pair residual may help or mildly hurt; force regression is the key risk.
- rmd17 gap / Q: Expected neutral if residual is damped.
- iso17 energy: Primary target; latent nonlocal term may reduce conformer mixed_energy_mae.
- iso17 force: Could improve long-ish intramolecular gradients; risk if charges overfit.
- iso17 gap / Q: Expected improvement through lower gap_penalty and better other-conformer energy.
- training stability / runtime risk: O(N^2) all-pairs acceptable for current small molecules; charge magnitude needs damping/clamping.
- control comparison expectation: beta=0 should reproduce source; selected run should beat source on ISO17 energy/gap.

## files_to_edit
- `model/model.py`
- `model/train.py`: none expected; optionally keep `TRAIN_ENERGY_WEIGHT`/`TRAIN_FORCE_WEIGHT` unchanged
- never `config.json` for MLIP-quality changes

## code_insertion_points
- `model/model.py::EvolutionMLIP.__init__`: after readout modules, add `self.charge_head = nn.Linear(hidden_dim, 1)`, `self.electrostatic_log_scale = nn.Parameter(torch.tensor(-5.0))`, and sigma/eps constants or buffers.
- `model/model.py::new _electrostatic_residual`: compute all i<j distances, `q = tanh(q_raw).sub(mean).div(sqrt(N))`, damped `erf(r/(sqrt(2)*sigma))/(r+eps)` pair energy.
- `model/model.py::EvolutionMLIP.forward_energy`: after final `scalar_state` and `per_atom_energy`, compute local energy and return `local_energy + sigmoid(log_scale) * E_elec`.
- `model/train.py::none`: no benchmark semantic changes.

## minimal_edit_plan
1. Add charge head over final scalar states and neutralize charges per sample.
2. Add differentiable damped all-pair energy with stable eps, optional smooth cutoff, and tiny beta initialization.
3. Add the residual to the scalar energy return so forces remain autograd-derived.

## implementation_checklist
- [ ] Preserve `E = sum_i E_i` local energy plus scalar residual and force-from-energy contract.
- [ ] Preserve benchmark metric field names and runnable entrypoint contract.
- [ ] Modify only the allowed target unit files.
- [ ] Do not edit `config.json`; change MLIP knobs in `model/model.py` or `model/train.py`.
- [ ] Keep tensor shapes compatible with current dataloader and model forward.
- [ ] Add no unbounded cubic neighbor/triplet loops; all-pairs O(N^2) only.
- [ ] Clamp or normalize q to prevent charge blow-up.
- [ ] Call `mark_unit_implemented.py --unit <UNIT> --actor implementation_subagent` after edits.

## expected_benchmark_effect
- primary expected gain: ISO17 mixed_energy_mae and gap_penalty improvement.
- expected tradeoff: Latent charges are unlabelled and may not identify in 8 epochs; force MAE may regress if beta grows too fast.
- failure signal that would falsify this proposal: Charge magnitudes explode, ISO17 energy remains unstable, or RMD17 force degrades.

## ablation_or_control
- required control or comparison: beta=0/source control and generation_015/proposal_004.
- optional zero-gate / source-fallback / readout-only ablation: run with `electrostatic_log_scale` fixed near -inf to verify no-op equivalence.

## implementation_notes_for_subagent
Implement the direct neutral q-head residual only. Do not port full charge equilibration, spin/charge inputs, Ewald periodicity, or any dataset/metric changes.
