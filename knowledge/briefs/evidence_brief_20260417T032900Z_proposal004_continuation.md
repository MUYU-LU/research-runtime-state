# MLIP Evidence Brief

## question
What is the best bounded next-round continuation from generation_001/proposal_004, the current minimal local equivariant winner, balancing exploit versus jump while preserving the fixed benchmark contract and runnable-unit fit?

## mode
balanced

## local_context
- Source family under review: `generation_001/proposal_004` from `04_jump_minimal_equivariant_local.md`.
- Proposal intent: compact local equivariant interaction with radial edge features, directional edge attributes, and minimal interaction depth.
- Round result summary from `ledger/generation_001_summary.json`:
  - `proposal_004` is the strongest completed unit on both datasets.
  - rMD17 mixed force MAE: `0.2241`
  - ISO17 mixed force MAE: `0.2902`
- Nearby context:
  - `proposal_003` residual scalar pair graph: rMD17 `0.3275`, ISO17 `0.3769`
  - `proposal_005` CACE-style bridge: rMD17 `0.3394`, ISO17 `0.3778`
  - `proposal_006` equivariant triplet hybrid: rMD17 `0.6436`, ISO17 `0.4478`
- Conclusion from local run evidence: the first successful symmetry-aware local jump clearly beat the scalar exploit branch and the more aggressive hybrid jump.

## current_unit_profile
- Representation: atom embeddings plus scalar and vector hidden states.
- Symmetry: local directional updates with vector channels, equivariant in spirit but implemented in a very compact custom way rather than full irreps/e3nn machinery.
- Geometry handling: explicit dense neighbor list from relative displacements inside a cutoff.
- Energy/force pathway: total energy from atomref baseline plus summed atomwise energy head, forces from autograd on positions.
- Training regime: same benchmark-aligned train/eval loop as other generation_001 units, energy weight `1.0`, force weight `20.0`, 8 epochs.
- Known failure modes / limits:
  - only one interaction stage
  - dense `O(N^2)` neighbor construction
  - vector channel is low-rank and only enters through norms in the final scalar pathway
  - no explicit triplets/body-order expansion
  - no long-range decomposition
  - no periodic/cell handling
- Current phase/family: minimal local equivariant winner.
- Current bottleneck: likely underpowered equivariant capacity and limited body-order depth, not absence of symmetry anymore.

## strong_evidence
1. **Direct local benchmark evidence**: `proposal_004` substantially outperforms the closest exploit and bridge baselines, so equivariant local geometry is not speculative here, it is already the strongest validated direction.
2. **Proposal_004 code evidence**: the model wins with a very small recipe, one neighbor pass, scalar filter plus directional vector message, and scalar readout from vector norms. That suggests immediate headroom from exploiting the same family before adding another major branch.
3. **External textual evidence, NequIP** (`arXiv:2101.03164`): SE(3)-equivariant convolutions give more faithful geometric representations and strong data efficiency for interatomic potentials.
4. **External textual evidence, MACE** (`arXiv:2206.07697`): higher-order equivariant messages reduce the need for many layers and improve force-field accuracy, explicitly tying body order to expressivity.
5. **External code evidence**:
   - NequIP README: positions itself as E(3)-equivariant interatomic potentials with compiled training/inference.
   - `nequip/model/nequip_models.py`: uses spherical harmonic edge attrs, Bessel edge length encoding, ConvNetLayer stacks, and force/stress outputs.
   - `nequip/nn/interaction_block.py`: invariant radial MLP conditions tensor-product interactions over equivariant node/edge features.
   - MACE README: explicitly claims higher-order equivariant message passing.
   - `mace/modules/models.py` and `mace/modules/blocks.py`: show irreps-based interaction blocks, radial embeddings, and explicit higher-order equivariant product bases.

## weak_but_relevant
- `proposal_005` suggests that a body-order bridge without a clean equivariant mechanism was not enough in this round, but that does not rule out bounded body-order augmentation inside the winning family.
- `proposal_006` suggests that combining too many hard changes at once, equivariance plus explicit triplets, likely exceeded the round's implementation/training budget.
- Earlier local brief material points to long-range and adaptation branches as real MLIP themes, but they were not the dominant validated gap in this proposal_004-centered review.

## background_context
The generation_001 results indicate a phase change: moving from scalar local models to even a minimal symmetry-aware local model gave the largest quality gain. The question for the next round is therefore not whether to keep equivariant locality at all, but whether to exploit it cleanly or jump again toward richer body order or heavier framework structure.

## mathematical_forms
- Current proposal_004 effectively uses:
  - neighbor edges \( (i,j) \) for \(\|r_{ij}\| < r_c\)
  - radial basis \(\phi(d_{ij})\)
  - scalar message \(m^{(s)}_{ij} = f_s(h_i, h_j, \phi(d_{ij})) \odot g_s(\phi(d_{ij}))\)
  - directional vector message \(m^{(v)}_{ij} = g_v(\phi(d_{ij})) \, \hat r_{ij}\)
  - aggregated updates by sum over neighbors
  - scalar readout from concatenated scalar state and vector norms
- Missing higher-order form relative to MACE-style evidence:
  - no explicit product basis or triplet/body-order contraction
  - no irreps-preserving tensor products across multiple \(l\) channels
- External evidence supports two next mathematical moves:
  1. deepen equivariant interaction composition while keeping the same local edge basis
  2. add bounded higher-body structure, for example triplet-aware or product-basis summaries, without changing benchmark I/O

## physical_principles
- Locality is already supported and validated under current cutoffs.
- Rotation-aware directional structure matters for forces and local environment discrimination; proposal_004 validates this empirically.
- Force consistency is preserved through autograd-from-energy and should remain unchanged in any continuation.
- Conservation/symmetry risks appear if future edits inject directional features in ad hoc ways without preserving the energy-first path.
- Efficiency matters: the current dense neighbor construction is acceptable for bounded experiments but is a scaling liability relative to graph-based implementations.

## chemical_regime
- rMD17 and ISO17 are short-range molecular force benchmarks where local geometry and angular chemistry matter strongly.
- The winning result is consistent with chemistry that needs directional bonding information, not merely pair distances.
- The evidence does **not** yet force a long-range electrostatics branch as the next default move for this benchmark pair.
- A bounded body-order increase is chemically plausible because local conformational force errors often depend on angular environment and correlated neighbor structure.

## textual_evidence
- NequIP abstract (`arXiv:2101.03164`): equivariant convolutions for geometric tensors provide a more information-rich and faithful representation of atomic environments, with strong data efficiency.
- MACE abstract (`arXiv:2206.07697`): higher-order equivariant messages improve expressivity and allow strong accuracy with only a small number of message-passing iterations.
- Local proposal text for `04_jump_minimal_equivariant_local.md`: this branch was intended as a clean test of whether the frontier needed a real representation jump. The completed run answered yes.

## code_evidence
- `proposal_004/model/model.py`
  - explicit `_build_neighbor_list()` from pairwise displacements and cutoff
  - separate scalar and vector message paths
  - vector information only enters the scalar state through `torch.linalg.norm`
  - exactly one aggregation/update stage
- `proposal_004/model/train.py`
  - no special equivariant training machinery, just Adam and energy-plus-force L1 loss
  - this is important because the gain came from representation change, not exotic training recipe
- NequIP code pattern
  - `nequip/model/nequip_models.py` imports spherical harmonic edge attrs, Bessel edge encodings, ConvNetLayer, and force outputs
  - `nequip/nn/interaction_block.py` shows invariant radial networks controlling equivariant tensor interactions
- MACE code pattern
  - `mace/modules/models.py` centers model construction on interaction blocks plus equivariant product-basis/readout blocks
  - `mace/modules/blocks.py` makes the implementation cost visible: irreps bookkeeping, tensor products, and specialized radial/cutoff modules

## relevant_papers
- **SE(3)-Equivariant Graph Neural Networks for Data-Efficient and Accurate Interatomic Potentials** (`arXiv:2101.03164`)
  - Matters because it directly supports continuing the equivariant-local family after a strong first win.
- **Higher Order Equivariant Message Passing Neural Networks for Fast and Accurate Force Fields** (`arXiv:2206.07697`)
  - Matters because it explains why adding higher body order on top of equivariance can outperform shallow two-body message passing without requiring many layers.

## relevant_repos
- **NequIP** (`mir-group/nequip`)
  - Matters as the cleanest reference for local equivariant interaction stacks and force-from-energy outputs.
- **MACE** (`ACEsuit/mace`)
  - Matters as the clearest reference for bounded higher-order equivariant extensions and the real implementation cost of irreps-heavy designs.

## capability_gap
- Current unit can do:
  - local cutoff graph construction
  - scalar and directional vector messages
  - energy-first force prediction
  - atomref baseline
- External methods expect for the next tier:
  - repeated equivariant interactions or richer body-order contraction
  - more principled channel mixing than vector-norm injection alone
  - better graph efficiency than dense all-pairs masking
- Gap judgments:
  - **Exploit deeper minimal equivariant local**: low to medium gap
  - **Add bounded body-order inside current family**: medium gap
  - **Adopt full NequIP/MACE-style irreps stack**: medium to high gap
  - **Add long-range/electrostatics branch now**: medium method gap, low benchmark priority

## implementable_design_moves
1. **Exploit move: two-stage minimal equivariant local stack**
   - Principle: keep the winning inductive bias and increase interaction depth modestly.
   - Math form: repeat the current local scalar/vector aggregation once more with residual state carry.
   - Code pattern: bounded edits inside `model.py`, reusing current neighbor list, RBF, scalar/vector states, and readout contract.
   - Expected effect: better local environment mixing and force refinement on both datasets.
   - Control: compare directly against frozen proposal_004 hyperparameters and epoch budget.
2. **Exploit-to-bridge move: bounded body-order augmentation inside proposal_004**
   - Principle: add directional/body-order signal without jumping to full irreps framework.
   - Math form: simple triplet-aware or pair-product summary per center, merged into the scalar state before readout.
   - Code pattern: local helper around neighbor edge features; avoid e3nn and keep scalar total energy output.
   - Expected effect: capture angular chemistry missed by the one-pass vector-norm pathway.
   - Control: same training loop and parameter budget, plus ablation removing the body-order path.
3. **Jump move: disciplined NequIP-like refactor, not full hybrid**
   - Principle: if the round wants one genuine jump, upgrade representation quality, not branch count.
   - Math form: spherical-harmonic edge attrs and cleaner equivariant interaction composition.
   - Code pattern: borrow structural ideas from NequIP while keeping benchmark I/O identical.
   - Expected effect: higher ceiling than proposal_004, but only if implementation is kept narrow.
   - Control: no extra triplet branch in the same unit.

## exploit_angles
- **Best exploit**: deepen proposal_004 into a two-stage residual minimal equivariant local model.
- **Second exploit**: improve the scalar readout pathway so vector information influences atom energies through richer coupling than norms alone.
- **Third exploit**: replace dense all-pairs masking with a cleaner neighbor-edge pipeline only if needed for stability or speed, not as the main scientific change.

## jump_angles
- **Best bounded jump**: add a small body-order augmentation within the proposal_004 family, not a separate heavy hybrid.
- **Secondary jump**: a clean NequIP-like interaction refactor with irreps-style structure, only if the round can tolerate medium-high implementation risk.
- **Deprioritized jump**: repeat `proposal_006`-style hybrid equivariant-plus-triplet complexity in one shot.

## risks_or_mismatches
- The current winner may still be benefiting from a lucky simplicity/stability point; a heavier rewrite can easily erase that gain.
- `proposal_006` is a warning that combining multiple major inductive-bias jumps at once can hurt both fit and diagnosability.
- `proposal_005` is a warning that body-order ideas without a clean, well-coupled interaction design may underperform.
- Full NequIP/MACE implementations imply nontrivial irreps/dependency complexity that exceeds the bounded-fit profile of the current unit family.
- Dense neighbor construction is a practical but not benchmark-semantic issue; do not confuse engineering cleanup with the next scientific hypothesis.

## followup_queries
- Does proposal_004 keep its lead under a second seed or slightly longer training, confirming the family rather than a single-run win?
- Is the next measurable gain better explained by interaction depth or by explicit body-order features?
- Can vector features be coupled into the energy head more directly without importing full irreps infrastructure?

## confidence
**medium-high**

Explanation: confidence is high that the continuation should stay centered on the proposal_004 family, because local benchmark evidence is decisive. Confidence is medium on the exact next mechanism, depth versus bounded body order, because external literature supports both and local generation_001 only tested coarse versions of each.