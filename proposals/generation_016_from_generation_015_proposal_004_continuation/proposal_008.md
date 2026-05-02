# Proposal 008: Radial-type body-order simplification

- family: simplified_body_order_ablation
- phase: 3
- jump_type: backward-simplify
- budget_class: small
- expected_capability_gain: Determine whether a very small invariant radial/type branch is sufficient before paying for full angular body-order complexity.

## one_sentence_hypothesis
A simplified body-order branch using l=0 radial/type invariants plus squared channel products can provide a safer source-adjacent baseline and reveal whether angular l=1/2 terms are truly necessary.

## mechanism_refs
- GEN016-M01-cace-shadow-body-order-representation

## evidence_refs
- paper_artifact:paper_001
- repo_artifact:repo_001
- mechanism_cards.json::GEN016-M01-cace-shadow-body-order-representation A/B basis formulation
- patch_blueprints.json::GEN016-M01-cace-shadow-body-order-representation truncation and ablation guidance
- benchmark_diagnosis.json::source strong RMD17 Q and ISO17 energy bottleneck

## historical_relation
- source_unit: generation_015/proposal_004
- relation_to_source: simplify
- not_a_duplicate_of: This is not an exact control and not a readout/gate simplification; it is a deliberately reduced M01 representation-path ablation.
- lesson_used: Before selecting larger architecture jumps, keep one backward-simplify unit that tests whether the minimal radial/type invariant residual captures most of the benefit with less risk.

## why_not_duplicate
Unlike proposal_003, this removes explicit angular monomials l=1/2 and keeps only l=0 radial/type scatter features plus squared channel products. It is a weaker but safer implementation probe.

## benchmark_rationale
- rmd17 energy: Very likely stable due to smallest branch capacity.
- rmd17 force: Lower gradient-noise risk because no angular polynomial terms.
- rmd17 gap / Q: Expected neutral.
- iso17 energy: May improve if the benefit is mostly element/radial channel reparameterization; likely weaker than full angular body order.
- iso17 force: Expected neutral.
- iso17 gap / Q: Modest possible gain; useful as an ablation even if not top performer.
- training stability / runtime risk: Low.
- control comparison expectation: Should be close to source and safer than full M01 variants.

## files_to_edit
- `model/model.py`
- `model/train.py`: none expected
- never `config.json` for MLIP-quality changes

## code_insertion_points
- `model/model.py::new RadialTypeInvariantBranch`: project existing edge RBF and element-pair embeddings, scatter to receivers, concatenate l=0 sums and squared products.
- `model/model.py::EvolutionMLIP.__init__`: add branch, small readout, and residual scale initialized near -5.
- `model/model.py::EvolutionMLIP.forward_energy`: compute branch after `edge_basis`; add residual to source local energy.
- `model/train.py::none`: no changes.

## minimal_edit_plan
1. Add a small l=0-only branch using existing `edge_basis`, `numbers[i_idx]`, and `numbers[j_idx]`.
2. Build per-atom features by scatter-add and elementwise squared/normalized products; avoid angular terms and descriptor messages.
3. Add a tiny residual atomic energy head with source fallback.

## implementation_checklist
- [ ] Preserve `E = sum_i E_i` and force-from-energy contract.
- [ ] Preserve benchmark metric field names and runnable entrypoint contract.
- [ ] Modify only the allowed target unit files.
- [ ] Do not edit `config.json`; change MLIP knobs in `model/model.py` or `model/train.py`.
- [ ] Keep tensor shapes compatible with current dataloader and model forward.
- [ ] Add no unbounded cubic neighbor/triplet loops.
- [ ] Explicitly document that this is a simplification/ablation of M01, not a full strong body-order implementation.
- [ ] Call `mark_unit_implemented.py --unit <UNIT> --actor implementation_subagent` after edits.

## expected_benchmark_effect
- primary expected gain: Low-risk small ISO17 energy/gap improvement or a clear negative control for full angular body-order features.
- expected tradeoff: May be too weak because it omits explicit angular information.
- failure signal that would falsify this proposal: No gain over source while full angular variants improve, confirming l=0 simplification is insufficient.

## ablation_or_control
- required control or comparison: source control and any selected angular body-order proposal.
- optional zero-gate / source-fallback / readout-only ablation: residual scale fixed to zero.

## implementation_notes_for_subagent
Treat this as a backward-simplify proposal: minimal extra branch, minimal runtime, no message passing, no angular monomials beyond l=0.
