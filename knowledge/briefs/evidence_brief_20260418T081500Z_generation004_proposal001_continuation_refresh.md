# MLIP Evidence Brief

## question
What single bounded, benchmark-centric continuation should guide `generation_005` from source unit `generation_004/proposal_001`, after a fresh evidence refresh that adds new local literature beyond the prior continuation brief and keeps balanced evidence mode?

## mode
balanced

## local_context
- Continuation source under review: `research_runtime/generations/generation_004/proposal_001`
- Frontier status from prior round decision context: highest completed non-control `Q_total` in `generation_004`, with `Q_rmd17 = 3.0291`, `Q_iso17 = 3.3267`, `Q_total = 3.1333`.
- Lineage intent from `research_runtime/proposals/generation_003_proposal_004_continuation/proposal_001.md`: preserve the local equivariant energy-first family, improve calibration and residual behavior, and rebalance rMD17 without sacrificing cross-dataset upside.
- This refresh is evidence-only. No runnable code edits, no selection file, no materialization, no runs.
- Fresh-refresh requirement for this brief: explicitly separate **newly added evidence** from **reused prior evidence**.

## current_unit_profile
- Model family: compact custom local equivariant MLIP, NequIP-style in spirit, not a full irreps framework transplant.
- Phase: exploit continuation, staying inside the validated local equivariant family.
- Present capabilities in `research_runtime/generations/generation_004/proposal_001/model/model.py`:
  - atom embedding plus atomref baseline
  - local cutoff graph from positions
  - scalar and vector channels
  - two repeated `BalancedInteractionBlock`s
  - Gaussian RBF plus cosine cutoff envelope
  - energy-first prediction with forces from autograd
  - scalar update already uses `agg_norm` and `vector_alignment`
- Missing capabilities:
  - no explicit triplet/body-order contraction
  - no irreps tensor products
  - no explicit nonlocal branch or electronic-state inputs
  - dense all-pairs neighbor build before masking
- Likely bottlenecks:
  - final energy readout still compresses vector content to norms only
  - angular/body-order capacity remains bounded despite improved in-block coupling
  - optimization is clean overall, so the next gap is more likely representational than optimizer-only
- Likely implementation surface:
  - `model/model.py` for readout or bounded body-order augmentation
  - `model/train.py` only for secondary schedule polish

## benchmark_dossier
### Dataset metrics
| dataset | split metrics | mixed force | mixed energy | gap penalty | Q_dataset |
|---|---|---:|---:|---:|---:|
| rMD17 | mild OOD F/E `0.10458 / 0.59297`, hard OOD F/E `0.10503 / 0.59259` | 0.10485 | 0.59274 | 0.00429 | 3.02911 |
| ISO17 | within F/E `0.18116 / 0.75503`, other F/E `0.19033 / 0.79636` | 0.18666 | 0.77982 | 0.04911 | 3.32669 |

### Cross-dataset view
- `Q_total = 3.13326`, best completed non-control result in the round context used for continuation.
- Source is balanced, not force-only: both datasets are strong, energy is dramatically improved over parent lineage, and split gaps remain controlled.
- Relative to parent `generation_003/proposal_004`, the biggest gain is energy calibration, especially rMD17 energy.

### Training dynamics
- rMD17:
  - validation force improves from `0.2955` to `0.1046`
  - validation energy improves from `86.41` to `0.5930`
  - temporary energy spike at epoch 4 (`28.00`) but full recovery by the end
- ISO17:
  - validation force improves from `0.1975` to `0.1599`
  - validation energy improves from `45.92` to `1.04`
  - stronger volatility, including epoch-4 energy spike (`69.97`), then recovery
- Best practical reading: end-state is strong and reliable, but ISO17 still shows capacity-sensitive optimization turbulence.

### Runtime / reliability
- terminal success, one launch, zero retries, zero repairs
- smoke passed and synced in prior frontier context
- runtime evidence supports the unit as a real frontier source, not a rescue artifact

### Control comparison
- No same-generation direct control replicate is attached to `generation_004/proposal_001`.
- Reused lineage control reference remains `generation_003/proposal_008`, which is far worse on benchmark-complete metrics.
- Therefore large gains are real, but small future gains should still be interpreted cautiously without a source-matched replicate.

## mathematical_evidence
### Newly added evidence
1. **ACE completeness / efficiency / stability** (`/mnt/c/Users/1/Desktop/文献/MLIP/MLIP理论基础 - ACE完备性效率与稳定性.pdf`, locally extracted)
   - ACE frames invariant polynomial bases as systematically extensible many-body expansions with guarantees around completeness and efficient recursive evaluation.
   - Important implication here: body-order enrichment does not have to mean a full framework rewrite if a compact invariant basis summary can be injected into the existing local model.
2. **ELoRA** (`/mnt/c/Users/1/Desktop/文献/MLIP/MLIP参数高效微调 - ELoRA等变低秩适配.pdf`, locally extracted)
   - ELoRA argues that naive low-rank adaptation can break equivariance, and proposes path-dependent low-rank updates that preserve equivariance.
   - Relevant mathematical lesson: if the next move introduces low-rank channel adaptation or extra coupling blocks, symmetry-preserving structure matters more than generic PEFT-style rank reduction.
3. **SO3KRATES / Euclidean Transformer** (`/mnt/c/Users/1/Desktop/文献/MLIP/MLIP分子力场 - 欧氏Transformer快速稳定力场.pdf`, locally extracted)
   - Separates invariant and equivariant information while avoiding expensive tensor products.
   - Strongly relevant to the present code because the current block already distinguishes scalar and vector streams; the paper supports further separation-and-recombination without full irreps machinery.

### Reused prior evidence
- NequIP and MACE remain the prior reference points for disciplined equivariance and higher-order message passing.
- Prior brief already established that a full irreps-heavy transplant would be higher friction than a bounded family continuation.

## physical_evidence
### Newly added evidence
1. **Forces Are Not Enough** (`/mnt/c/Users/1/Desktop/文献/MLIP/MLIP力场基准 - Forces Are Not Enough分子模拟评测.pdf`, locally extracted)
   - Direct warning that low test force error does not guarantee good simulation behavior and that stability is a distinct objective.
   - This reinforces the workflow rule to keep energy, gap, and training stability visible, not just force MAE.
2. **SpookyNet** (`/mnt/c/Users/1/Desktop/文献/MLIP/MLIP分子力场 - SpookyNet含电子自由度非局域力场.pdf`, locally extracted)
   - Highlights failure modes of strict locality when charge, spin, or nonlocal effects matter.
   - For current benchmarks, this is more caution than immediate action: nothing in the present benchmark dossier shows a nonlocal branch is the most urgent bottleneck.
3. **SO3KRATES** (same local PDF as above)
   - Connects stability and extrapolation robustness to richer equivariant representations, but also emphasizes computational efficiency.
   - This supports a bounded representational upgrade over a heavy rewrite.

### Reused prior evidence
- Existing source preserves force-from-energy consistency, locality, and rotationally safe energy construction.
- Current benchmark behavior shows locality is adequate for rMD17 and ISO17 in this frontier setting.

## chemical_evidence
### Newly added evidence
- **SpookyNet** is molecule-centric and explicitly addresses chemistry regimes where electronic state and nonlocality matter. That broadens the chemistry map, but also sharpens the mismatch call: the present benchmark pair does not yet justify adding charge/spin/nonlocal machinery as the next bounded step.
- **Forces Are Not Enough** reinforces that chemically meaningful simulation behavior can diverge from force-only ranking, matching the need to keep benchmark-complete selection criteria.
- **ACE** supports many-body/angular sensitivity as a chemically meaningful way to improve local descriptors without abandoning local molecular modeling.

### Reused prior evidence
- rMD17 and ISO17 both reward local angular discrimination and stable energy surfaces.
- Atomref and energy-first prediction remain chemistry-safe parts of the current design.

## textual_evidence
### Newly added evidence
- **Forces Are Not Enough**: direct claim that force-only evaluation is misaligned with practical MD objectives and that stability should be treated as a key metric.
- **ELoRA**: direct claim that preserving equivariance during low-rank adaptation materially improves data efficiency and accuracy.
- **SO3KRATES**: direct claim that separating invariant/equivariant information can improve the balance of accuracy, stability, and speed without expensive tensor products.
- **SpookyNet**: direct claim that purely local models can miss nonlocal electronic effects, but those effects are especially relevant when electronic states vary.

### Reused prior evidence
- Proposal intent remains an exploit, not a new architecture family jump.
- Prior NequIP/MACE evidence still supports staying geometric and local, with bounded body-order expansion as the natural next-capacity direction.

## code_evidence
### Local code evidence
- `BalancedInteractionBlock` already performs a meaningful mid-block scalar/vector recombination through `agg_norm` and `vector_alignment`.
- The strongest remaining bottleneck is that the final `readout` sees `torch.cat([scalar_state, vector_norm], dim=-1)`, so terminal directional content is reduced to norms.
- This means the code already validated one level of scalar-vector fusion internally, but the energy head still lacks a richer invariant summary of directional structure.
- Dense pair construction is still present, but benchmark evidence does not say this is the main science bottleneck for the next bounded step.

### External code-pattern evidence
- No fresh repository deep-read was completed in this refresh because web fetch was unavailable.
- Prior reused repo evidence for NequIP and MACE remains valid background only.
- Fresh literature still adds actionable code-pattern implications:
  - ACE suggests compact invariant many-body summaries rather than a full new framework.
  - ELoRA warns against generic low-rank edits that would silently break symmetry assumptions.
  - SO3KRATES supports explicit invariant/equivariant stream separation with cheaper coupling than tensor-product-heavy designs.

## relevant_papers
### Newly added evidence
1. **Forces are not Enough: Benchmark and Critical Evaluation for Machine Learning Force Fields with Molecular Simulations**
2. **SpookyNet: Learning force fields with electronic degrees of freedom and nonlocal effects**
3. **ELoRA: Low-Rank Adaptation for Equivariant GNNs**
4. **A Euclidean transformer for fast and stable machine learned force fields**
5. **Atomic Cluster Expansion: Completeness, Efficiency and Stability**

### Reused prior evidence
6. **SE(3)-Equivariant Graph Neural Networks for Data-Efficient and Accurate Interatomic Potentials**
7. **Higher Order Equivariant Message Passing Neural Networks for Fast and Accurate Force Fields**

## local_literature
### Newly added evidence, all locally verified by extraction
- `/mnt/c/Users/1/Desktop/文献/MLIP/MLIP力场基准 - Forces Are Not Enough分子模拟评测.pdf`
- `/mnt/c/Users/1/Desktop/文献/MLIP/MLIP分子力场 - SpookyNet含电子自由度非局域力场.pdf`
- `/mnt/c/Users/1/Desktop/文献/MLIP/MLIP参数高效微调 - ELoRA等变低秩适配.pdf`
- `/mnt/c/Users/1/Desktop/文献/MLIP/MLIP分子力场 - 欧氏Transformer快速稳定力场.pdf`
- `/mnt/c/Users/1/Desktop/文献/MLIP/MLIP理论基础 - ACE完备性效率与稳定性.pdf`

### Reused prior evidence
- prior brief grounded NequIP and MACE as the main family-level references

## relevant_repos
### Reused prior evidence
- `mir-group/nequip`
- `ACEsuit/mace`

### Fresh refresh note
- No new repo is promoted to strong evidence in this brief because repository fetch/deep-read was unavailable during this run.

## capability_gap
### Current capabilities
- strong local equivariant family
- validated two-block exploit
- reliable benchmark-complete gains
- internal scalar/vector coupling already improved over parent

### Required next capabilities
- richer terminal invariant summary than vector norms alone
- optional compact many-body/angular signal beyond pairwise aggregation
- preservation of clean optimization and energy-first contract

### Missing pieces
- bounded invariant readout features derived from vector structure beyond norms
- explicit compact body-order summary path
- source-matched control replicate for small-gain attribution

### Integration risk
- low to medium: richer invariant readout inside current head
- medium: ACE-inspired compact many-body summary added to scalar updates
- medium-high: anything that imitates SpookyNet-style nonlocal/electronic modeling in this benchmark phase
- medium-high: generic low-rank tricks that ignore equivariance constraints

## implementable_design_moves
1. **Primary bounded exploit: enrich the terminal invariant energy head**
   - principle: keep the winning two-block family, but let final atomwise energies see more invariant structure than vector norms alone
   - mathematical form: augment readout features with bounded invariant contractions such as self/aggregate vector alignment summaries, low-rank scalar-vector bilinears, or center-wise invariant products computed from existing vector channels
   - physical rationale: preserve rotationally invariant energy while retaining directional information relevant to stable surfaces
   - chemistry relevance: should improve discrimination of local angular environments in molecular benchmarks
   - code pattern: modify final readout inputs in `model/model.py`, reusing already available vector states rather than adding a new framework
   - implementation friction: low to medium
   - expected effect: best chance of improving ISO17 and preserving current rMD17 energy quality
   - bounded control/ablation: same source model with current norm-only readout retained
2. **Secondary balanced jump: ACE-inspired compact body-order summary**
   - principle: add a small invariant many-body summary path without transplanting MACE or full ACE machinery
   - mathematical form: low-order neighbor-pair or recursive invariant basis summaries injected into scalar updates
   - physical rationale: capture angular/body-order structure the current pairwise aggregation may blur
   - chemistry relevance: plausible for conformational discrimination in both datasets
   - code pattern: add a narrow helper around local neighbor features in `model/model.py`
   - implementation friction: medium
   - expected effect: higher upside than readout-only enrichment, but more stability risk
   - bounded control/ablation: identical backbone with summary path toggled off
3. **Deprioritized move: nonlocal/electronic branch**
   - principle: borrow from SpookyNet-style nonlocal chemistry modeling
   - mathematical form: self-attention or explicit electronic-state conditioning
   - physical rationale: useful when locality breaks
   - chemistry relevance: currently weak for this benchmark pair
   - code pattern: rewrite-heavy in this codebase
   - implementation friction: high
   - expected effect: poorly justified for the next bounded continuation
   - bounded control/ablation: not recommended for this round

## strong_evidence
### Newly added evidence
- Local PDF evidence now independently supports three things the prior brief did not freshly verify in this run:
  1. benchmark selection must remain stability-aware and not force-only (`Forces Are Not Enough`)
  2. bounded invariant/equivariant separation can improve stability without tensor-product-heavy rewrites (`SO3KRATES`)
  3. compact many-body enrichment is principled, but should stay symmetry-aware (`ACE`, `ELoRA`)

### Reused prior evidence
- `generation_004/proposal_001` is still the best benchmark-complete continuation source.
- Current runtime/reliability record is clean.
- Prior NequIP/MACE references still justify staying inside the local equivariant family.

## weak_but_relevant
### Newly added evidence
- SpookyNet shows that locality can fail in broader chemistry regimes, but current benchmark evidence does not point there yet.
- ELoRA is about fine-tuning pre-trained equivariant GNNs, not exactly this from-scratch compact model, so its value is architectural caution, not direct method transfer.

### Reused prior evidence
- Same-generation control evidence is still missing.
- ISO17 volatility suggests added capacity could still destabilize training if stacked too aggressively.

## background_context
- The source unit already validated balanced exploitation over speculative jumps.
- This fresh refresh strengthens that conclusion rather than overturning it.
- The new literature mainly narrows *how* to continue: richer invariant coupling first, compact many-body summary second, nonlocality later only if benchmark evidence changes.

## key_findings
1. The frontier decision remains benchmark-complete, not force-only.
2. Fresh local literature strengthens the case for a **bounded invariant readout upgrade** as the next best move.
3. A compact ACE-like body-order path is still the best higher-upside alternative, but it should remain narrow.
4. SpookyNet-style nonlocal/electronic machinery is scientifically interesting but not the right next bounded continuation for rMD17 plus ISO17.
5. Any low-rank or compressed coupling change should respect symmetry structure; generic cheap adaptation is not automatically safe.

## useful_patterns
- Separate invariant and equivariant streams, then recombine through invariant summaries.
- Prefer cheap invariant contractions over heavy irreps rewrites when the current family is already strong.
- Keep stability and energy quality visible during selection and interpretation.
- Use many-body enrichment as a narrow add-on, not a framework transplant.

## risks_or_mismatches
- Data/task mismatch: nonlocal or electronic-state branches are weakly justified by the present benchmarks.
- Method mismatch: a full ACE/MACE/SpookyNet transplant would exceed the bounded continuation budget.
- Codebase mismatch: irreps-heavy or transformer-nonlocal machinery is much larger than the current custom implementation surface.
- Dependency/runtime mismatch: extra symmetry frameworks or attention stacks would raise complexity and could disturb the currently clean runtime profile.
- Likely failure signs:
  - ISO17 energy spikes suggest capacity increases can destabilize training
  - readout-only changes are safer than simultaneous body-order plus nonlocal jumps
  - generic low-rank compression could break symmetry discipline if copied naively from non-equivariant settings

## implementation_fit
- Best fit: enrich the existing terminal invariant readout while keeping the two-block family intact.
- Next-best fit: add a compact ACE-inspired many-body summary path if a slightly higher-risk jump is desired.
- Poor fit now: SpookyNet-style nonlocality, explicit electronic degrees of freedom, or full irreps/transfomer rewrites.
- Overall fit judgment: continue from `generation_004/proposal_001` with a readout-centered exploit, not a family change.

## exploit_angles
- Primary exploit: replace norm-only terminal vector usage with a richer invariant scalar-vector summary in the energy head.
- Secondary exploit: minor schedule polish only after the representational exploit is isolated.
- Evidence-weighted recommendation: take the readout exploit before trying explicit body-order machinery.

## jump_angles
- Best bounded jump: compact ACE-like invariant many-body augmentation inside the current local family.
- Secondary jump: a light SO3KRATES-inspired separation/recombination refinement, but still without nonlocal attention.
- Deprioritized jump: full nonlocal/electronic architecture branch.

## followup_queries
- Can a richer invariant energy head improve ISO17 force/energy without losing rMD17 stability?
- Is a tiny ACE-like summary path measurably better than readout enrichment alone?
- Would a source-matched control replicate materially change confidence in a small gain from readout enrichment?
- Does the current dense neighbor builder become a real practical bottleneck only after representational gains plateau?

## confidence
**high for the continuation family, medium-high for the exact mechanism**

Reasoning: the benchmark dossier already strongly favored staying inside the current source family. The fresh refresh adds multiple new locally verified papers that all point in the same bounded direction: preserve benchmark-centric evaluation, keep symmetry-aware local geometry, and prefer a richer invariant readout before a heavier body-order or nonlocal jump.
