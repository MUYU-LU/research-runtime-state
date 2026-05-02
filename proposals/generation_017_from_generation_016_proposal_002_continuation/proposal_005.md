# Proposal 005: One intraatomic PaiNNMixing block before readout

- family: lightweight_painn_mixing_block
- phase: 4
- jump_type: jump
- budget_class: medium
- expected_capability_gain: Test a bounded PaiNN-like scalar/vector mixing update on the main learned states, not only on the body-order side branch.

## one_sentence_hypothesis
Adding one post-message-passing PaiNNMixing-style scalar/vector state update will improve ISO17 transfer if the current scalar/vector backbone needs intraatomic vector contractions before energy readout.

## mechanism_refs
- GEN017-M01-painn-style-scalar-vector-mixing-gate

## evidence_refs
- mechanism_cards.json::GEN017-M01 repo_code_trace::PaiNNMixing.forward
- evidence_provenance.json::repo_artifact:repo_002 success=true can_support_strong=true
- mechanism_cards.json::GEN017-M01 mathematical_form intraatomic scalar update with `||Vv||` and `<Uv,Vv>`
- patch_blueprints.json::GEN017-M01 notes `BalancedInteractionBlock.forward` already exposes analogous vector invariants
- benchmark_diagnosis.json::source ISO17 best_val_force improves but val energy worsens, suggesting representation/readout coupling issue

## historical_relation
- source_unit: generation_016/proposal_002
- relation_to_source: jump
- not_a_duplicate_of: Prior generation_015/016 proposals used vector-norm readouts, CACE body-order branches, or nonlocal electrostatics; this adds a single PaiNNMixing-like intraatomic update to the existing scalar/vector states after interactions.
- lesson_used: Source body-order branch helped only within neutral variance; a modest phase-4 jump tests direct scalar/vector mixing while keeping all benchmark semantics fixed.

## why_not_duplicate
This is not a full PaiNN port and not proposal_004's body-order-to-scalar adapter. It implements one local intraatomic mixing block on `scalar_state`/`vector_state`, then leaves the body-order branch and readouts structurally intact.

## benchmark_rationale
- rmd17 energy: Some risk because scalar_state changes globally before readout.
- rmd17 force: Conservative forces remain; vector update may alter force curvature.
- rmd17 gap / Q: Must remain near source for success.
- iso17 energy: May improve if scalar energy underuses vector directional context after interaction blocks.
- iso17 force: Could improve vector-gradient smoothness; could regress if mixing too strong.
- iso17 gap / Q: Expected positive only if energy trend improves without force loss.
- training stability / runtime risk: Medium; adds channel-mixing projections and MLPs but no new edge loop.
- control comparison expectation: Should be judged against exact source and lower-risk residual-gate proposals.

## files_to_edit
- `model/model.py`
- `model/train.py`: none expected
- never `config.json` for MLIP-quality changes

## code_insertion_points
- `model/model.py::new IntraatomicPainnMixing`: define a small module with vector channel projections U/V/W, scalar context MLP from `[scalar_state, ||Vv||]`, scalar update including `<Uv,Vv>`, and optional vector update `dmu * Wv`, all with residual scale initialized small.
- `model/model.py::EvolutionMLIP.__init__`: instantiate exactly one `self.post_interaction_mixing` after `self.interactions`.
- `model/model.py::EvolutionMLIP.forward_energy`: after the interaction loop and before `vector_norm_layer`, call `scalar_state, vector_state = self.post_interaction_mixing(scalar_state, vector_state)`.
- `model/train.py::none`: keep objective unchanged.

## minimal_edit_plan
1. Add a compact mixing module modeled on SchNetPack `PaiNNMixing.forward`, using only scalar vector contractions.
2. Initialize final scalar/vector residual projections or scales near zero.
3. Insert exactly once after existing interactions and before readout/body-order residual computation.

## implementation_checklist
- [ ] Preserve `E = sum_i E_i` and force-from-energy contract.
- [ ] Preserve benchmark metric field names and runnable entrypoint contract.
- [ ] Modify only the allowed target unit files.
- [ ] Do not edit `config.json`; change MLIP knobs in `model/model.py` or `model/train.py`.
- [ ] Keep tensor shapes compatible with current dataloader and model forward.
- [ ] Add no unbounded cubic neighbor/triplet loops unless explicitly justified by budget.
- [ ] Use one mixing block only; do not replace the architecture.
- [ ] Keep body-order descriptor dimensions unchanged.
- [ ] Call `mark_unit_implemented.py --unit <UNIT> --actor implementation_subagent` after edits.

## expected_benchmark_effect
- primary expected gain: Better ISO17 energy and Q through stronger scalar/vector coupling in main states.
- expected tradeoff: More architecture risk and runtime than body-order-only gates.
- failure signal that would falsify this proposal: RMD17 force/energy regression or no ISO17 gain relative to simpler M01 variants.

## ablation_or_control
- required control or comparison: Exact source and residual-gate proposals.
- optional zero-gate / source-fallback / readout-only ablation: Set mixing residual scales to zero to recover source.

## implementation_notes_for_subagent
This is a local module, not an external dependency. Follow the M01 formula and repo trace, but do not import SchNetPack or change dataloaders/eval.
