# MLIP Evidence Brief

## question
What bounded continuation brief should guide `generation_009` from source unit `generation_004/proposal_001` in balanced mode, after `generation_008` again failed to surpass the parent and the continuation direction is constrained to (1) tiny invariant/equivariant stream refinement inside `BalancedInteractionBlock`, or, only as a bounded jump, (2) a very narrow late ACE-like invariant many-body summary?

## local_context
- Request scope: evidence-only continuation brief for `generation_009`.
- Source unit: `generation_004/proposal_001`.
- Completed target review generation: `generation_008`.
- Continuation decision: `research_runtime/ledger/generation_009_continuation_decision.json` again selects `generation_004/proposal_001` with `Q_rmd17 = 3.0291`, `Q_iso17 = 3.3267`, `Q_total = 3.1333`.
- Best completed `generation_008` child was `generation_008/proposal_007` at `Q_total = 2.6332`, still materially below the source.
- Request constraints: prioritize tiny stream refinement inside `BalancedInteractionBlock`; if keeping one bounded jump, only a very narrow late invariant summary is allowed. Avoid readout-only retries, SpookyNet-style nonlocal/electronic branches, and full irreps/framework rewrites.
- This brief is evidence-only. No round-state changes, no runnable edits, no materialization, no launch.

## current_unit_profile
- Model family: compact custom local equivariant MLIP with scalar and vector channels.
- Phase: exploit-family continuation from a validated source, not a family jump.
- Present capabilities in `research_runtime/generations/generation_004/proposal_001/model/model.py`:
  - atom embedding plus atomref baseline
  - local cutoff graph from Cartesian positions
  - Gaussian RBF basis plus cosine cutoff envelope
  - two `BalancedInteractionBlock`s
  - in-block scalar/vector coupling through `directional_invariant`, `agg_norm`, and `vector_alignment`
  - energy-first prediction with autograd forces
- Missing capabilities:
  - no explicit product-basis / irreps machinery
  - no explicit triplet recursion or structured many-body basis
  - no nonlocal or electronic-state branch
  - late energy path still consumes compressed invariant summaries only
- Likely bottleneck now:
  - preserving the source’s unusually good rMD17 energy calibration while recovering any additional local angular signal
  - not a lack of gross capacity, because nearly all generation_008 children regressed despite plausible mechanisms
- Likely implementation surface:
  - `BalancedInteractionBlock` in `model/model.py`
  - only one optional tiny late invariant helper if a jump slot is retained

## benchmark_dossier
### Source: `generation_004/proposal_001`
- Runtime state: `terminal_success`
- Reliability: one launch, zero retries, zero repairs, smoke passed, synced
- rMD17:
  - `mixed_force_mae = 0.10485`
  - `mixed_energy_mae = 0.59274`
  - `gap_penalty = 0.00429`
  - `Q_dataset = 3.02911`
- ISO17:
  - `mixed_force_mae = 0.18666`
  - `mixed_energy_mae = 0.77982`
  - `gap_penalty = 0.04911`
  - `Q_dataset = 3.32669`
- Cross-dataset:
  - `Q_total = 3.13326`
  - `G_delta = 0.26450`
- Training dynamics:
  - both datasets recovered from mid-training energy spikes and ended improving
  - source is strong but calibration-sensitive

### Generation_008 child evidence most relevant to generation_009
- `proposal_007` backward-simplify ablation, best child, `Q_total = 2.63324`
  - rMD17 stayed closest to the parent (`Q_rmd17 = 2.65548`, `mixed_energy_mae = 0.63741`) but ISO17 energy collapsed (`mixed_energy_mae = 5.74494`)
  - evidence: smaller in-block edits are less damaging than broader additions, but still not sufficient
- `proposal_004` ultra-narrow invariant summary jump, `Q_total = 2.53900`
  - best bounded-jump result, but still clearly below parent
  - evidence: an ultra-narrow late invariant summary remains the only defensible jump, yet current local evidence is negative overall
- `proposal_008` exact source-matched control replicate, `Q_total = 2.53052`
  - strong underperformance indicates nontrivial variance / fidelity noise
  - but not enough to overturn the parent’s large margin
- `proposal_001` scalar interpolation micro-exploit, `Q_total = 2.41082`
  - broad regression on both datasets, especially energy
  - evidence against retrying this style directly
- `proposal_002` vector residual micro-exploit, `Q_total = 2.30930`
  - even narrower vector-only recalibration still regressed
- `proposal_005` single-site pre-readout invariant jump, `Q_total = 2.43994`
  - readout-adjacent late summary underperformed
  - direct local evidence against readout-only retries
- `proposal_006` another late-summary jump, `Q_total = 2.48998`
  - ISO17 energy improved relative to some siblings, but rMD17 force/energy degraded too much

### Continuation-level conclusion
The parent survived another full child generation. Generation_008 adds stronger local evidence than generation_007 that the safe frontier is now even narrower: favor source-faithful in-block stream refinement or source-tightening simplification; keep at most one very narrow late invariant-summary diagnostic jump.

## mathematical_evidence
1. **Current source code mechanism**
   - `BalancedInteractionBlock` already uses invariant/equivariant separation through:
     - `directional_invariant = sum(src_vector * unit)`
     - `agg_norm = ||agg_vector||`
     - `vector_alignment = <self_vector, mixed_agg_vector>`
   - This is already a concrete SO3KRATES-like pattern: directional information is processed equivariantly, then reintroduced through invariant summaries.
2. **SO3KRATES local PDF**
   - Verified from `/mnt/c/Users/1/Desktop/文献/MLIP/MLIP分子力场 - 欧氏Transformer快速稳定力场.pdf`.
   - Concrete mechanism: separate invariant and equivariant information, avoid expensive tensor products, and project equivariant responses onto the most relevant invariant component.
   - Transferable implication: the best bounded move is a tinier invariant/equivariant stream refinement inside the existing block, not a framework jump.
3. **ACE local PDF**
   - Verified from `/mnt/c/Users/1/Desktop/文献/MLIP/MLIP理论基础 - ACE完备性效率与稳定性.pdf`.
   - Concrete mechanism: atomic body-order expansion and invariant polynomial basis with recursive evaluation and explicit stability concerns.
   - Transferable implication: if a jump is kept, it should be a very narrow invariant many-body statistic, ideally one helper summary rather than a branch family.
4. **MACE repo evidence**
   - `mace/modules/symmetric_contraction.py` implements Eq. 10/11 style symmetric contractions for product-basis correlations.
   - `mace/modules/models.py` shows tight coupling among irreps, spherical harmonics, product blocks, and specialized readouts.
   - Transferable implication: true higher-order product-basis behavior is not drop-in here and should not be treated as bounded.

## physical_evidence
- **Forces Are Not Enough** local PDF, verified from `/mnt/c/Users/1/Desktop/文献/MLIP/MLIP力场基准 - Forces Are Not Enough分子模拟评测.pdf`:
  - concrete claim: force/energy test accuracy alone is not aligned with MD usefulness; stability is key
  - implication: the parent’s balanced energy, gap, and recovery profile must remain first-class continuation criteria
- The source preserves force-from-energy consistency and strict locality, and that regime is already validated on rMD17 plus ISO17.
- Nothing in the benchmark dossier points to missing nonlocal physics as the next bottleneck.

## chemical_evidence
- Active benchmarks are molecular and local-angular, not a strong charge-transfer or explicit-electronic regime.
- Local many-body/angular enrichment is chemically more plausible than nonlocal/electronic branches.
- But generation_008 again shows that chemistry plausibility alone is not enough; preserving balanced calibration dominates.

## textual_evidence
- `generation_009_continuation_decision.json` explicitly keeps the parent over every completed generation_008 child.
- The best child was the backward-simplify ablation, not a richer jump. That is important new evidence: source-tightening beat all larger exploit/jump attempts, even though it still lost to the parent.
- The pre-readout invariant jump and exact-control replicate both underperformed materially, which weakens both readout-only retries and overinterpretation of replicate noise.

## code_evidence
### Local source code
- `research_runtime/generations/generation_004/proposal_001/model/model.py`
  - compact, coherent, already contains meaningful scalar/vector recombination
  - safest insertion point is inside `BalancedInteractionBlock`
- `research_runtime/generations/generation_008/proposal_007/model/model.py`
  - removes the auxiliary `scalar_mix_norm` blend and keeps the core scalar/vector coupling
  - best child result suggests overshoot risk is real and simpler source-faithful edits are comparatively safer
- `research_runtime/generations/generation_008/proposal_005/model/model.py` and related late-summary proposals
  - generation-level outcomes show late-summary or readout-adjacent additions remain risky even when narrowed

### External repo evidence
- `research_runtime/knowledge/repo_cache/ACEsuit__mace/README.md`
  - higher-order equivariant message passing depends on irreps, correlation order, and dedicated training/config surfaces
- `research_runtime/knowledge/repo_cache/ACEsuit__mace/mace/modules/symmetric_contraction.py`
  - confirms product-basis behavior requires dedicated contraction machinery
- `research_runtime/knowledge/repo_cache/ACEsuit__mace/mace/modules/models.py`
  - confirms those methods are not bounded drop-ins for this compact codebase

## relevant_papers
1. *Forces are not Enough: Benchmark and Critical Evaluation for Machine Learning Force Fields with Molecular Simulations*
2. *A Euclidean transformer for fast and stable machine learned force fields*
3. *Atomic Cluster Expansion: Completeness, Efficiency and Stability*

## local_literature
- Verified locally by extraction:
  - `/mnt/c/Users/1/Desktop/文献/MLIP/MLIP力场基准 - Forces Are Not Enough分子模拟评测.pdf`
  - `/mnt/c/Users/1/Desktop/文献/MLIP/MLIP分子力场 - 欧氏Transformer快速稳定力场.pdf`
  - `/mnt/c/Users/1/Desktop/文献/MLIP/MLIP理论基础 - ACE完备性效率与稳定性.pdf`
- Prior brief anchors reused:
  - `research_runtime/knowledge/briefs/evidence_brief_20260418T081500Z_generation004_proposal001_continuation_refresh.md`
  - `research_runtime/knowledge/briefs/evidence_brief_20260419T2020Z_generation008_proposal001_continuation.md`

## relevant_repos
- `research_runtime/knowledge/repo_cache/ACEsuit__mace`

## mechanism_ledger
| mechanism | source | concrete equation / code / pattern | current-code insertion point | proposal relevance | risk |
|---|---|---|---|---|---|
| force-from-energy contract | source code | scalar energy, forces by autograd | must remain unchanged | hard requirement | low |
| invariant/equivariant stream recombination | source code + SO3KRATES | `directional_invariant`, `agg_norm`, `vector_alignment`, invariant projection of equivariant responses | `BalancedInteractionBlock` | primary continuation mechanism | medium |
| source-tightening simplification | local generation_008 evidence | remove one auxiliary mix while keeping core stream coupling | `BalancedInteractionBlock` scalar mix path | strongest local exploit-style signal from children | medium |
| very narrow invariant many-body summary | ACE | one low-width invariant body-order statistic, recursively motivated but tiny | single late helper near scalar update or just before readout | only defensible jump | medium-high |
| full product-basis contraction | MACE repo | symmetric contractions + irreps + correlation-order stack | rewrite-heavy across model | not bounded here | high |

## capability_gap
### Current code capabilities
- strong local equivariant trunk
- validated benchmark-complete balance
- runtime-clean source
- existing internal scalar/vector coupling

### Required capabilities from evidence
- any new capacity must preserve the parent’s rMD17 energy regime
- any added directional retention must be more fallback-friendly than generation_008 children

### Missing pieces
- a truly tiny stream-refinement edit that behaves like source-tightening rather than new capacity injection
- a diagnostic late invariant summary that is narrower than the already negative generation_008 late-summary variants

### Integration risk
- low-to-medium: source-tight in-block stream refinement or simplification
- medium-high: renewed late-summary helper
- high: irreps/product-basis/nonlocal branches

## implementable_design_moves
1. **Primary continuation: source-tight in-block stream refinement / simplification**
   - mechanism source: current source code, SO3KRATES invariant/equivariant separation, and local generation_008 outcome from `proposal_007`
   - concrete mechanism: refine only one existing invariant/equivariant mixing path inside `BalancedInteractionBlock`, preferably by reducing or tightly gating an auxiliary scalar mix rather than adding new features
   - current-code insertion point: scalar blend / normalization path in `BalancedInteractionBlock`
   - minimal bounded edit: one source-faithful gate, interpolation cap, or simplification that can collapse toward parent behavior
   - expected effect: best chance of preserving rMD17 energy while probing whether the source is slightly over-mixed rather than underpowered
   - bounded control / ablation: exact source replicate
2. **Secondary continuation, only if one jump slot is required: ultra-narrow late ACE-like invariant summary**
   - mechanism source: ACE body-order invariant basis + generation_008 `proposal_004`
   - concrete mechanism: one low-width invariant statistic derived from local neighbor geometry, injected once late
   - current-code insertion point: single late helper after final interaction or immediately before energy mapping
   - minimal bounded edit: one helper feature only, easy to disable
   - expected effect: diagnostic test for missing local many-body summary
   - bounded control / ablation: same trunk with helper disabled
3. **Explicitly deprioritized**
   - readout-only retries, because `proposal_005` and related late-summary/readout-adjacent moves already underperformed
   - SpookyNet-style nonlocal/electronic branches, because benchmark mismatch remains clear
   - full MACE-like product-basis / irreps rewrites, because code fit is poor and not bounded

## strong_evidence
- `generation_004/proposal_001` remains the best completed benchmark unit after another full continuation generation.
- The best generation_008 child was the backward-simplify ablation, not a richer exploit or jump.
- Generation_008 provides direct local negative evidence against readout-only retries and against broader late-summary enrichments.
- Local literature still supports symmetry-aware local geometry, but local benchmark evidence now strongly favors preservation over novelty.

## weak_but_relevant
- Control replicate underperformance suggests variance/fidelity noise exists, but it does not erase the parent’s lead.
- ACE still supports a narrow local many-body helper, but local round evidence keeps confidence modest.

## background_context
- Earlier briefs had already narrowed the frontier toward bounded local exploits.
- Generation_008 tightened the funnel further: the search is now in “do less, but do it more source-faithfully” territory.
- The new local signal is not a fresh paper-driven mechanism, but stronger falsification of broader modifications.

## key_findings
1. `generation_004/proposal_001` remains the only justified continuation anchor for `generation_009`.
2. Generation_008 says the safest useful direction is now **source-tight in-block stream refinement or simplification**, not added head/readout machinery.
3. If a jump is retained, only one **ultra-narrow late invariant ACE-like summary** remains defensible.
4. Readout-only retries are locally disfavored by completed evidence, not just by prior caution.
5. Nonlocal/electronic and product-basis rewrites remain poor implementation fits.

## useful_patterns
- preserve the winning trunk and force-from-energy contract
- prefer edits that can collapse back toward source behavior
- judge every move on balanced `Q_total`, not isolated force or ISO17 gains
- treat late-summary helpers as diagnostics, not new branch families

## risks_or_mismatches
- Data/task mismatch: nonlocal or electronic-state branches remain weakly justified.
- Method mismatch: another readout-only retry is directly disfavored by generation_008 results.
- Codebase mismatch: full product-basis or irreps migration is rewrite-heavy.
- Runtime mismatch: broader edits risk disturbing the source’s clean reliability.
- Likely failure signs:
  - rMD17 energy regresses while ISO17 moves only modestly
  - ISO17 energy improves but force trend worsens late
  - any claimed gain depends on force-only reading while `Q_total` still falls

## implementation_fit
- Best fit: tiny source-tight in-block stream refinement or simplification inside `BalancedInteractionBlock`.
- Acceptable but weaker fit: one ultra-narrow late invariant summary helper.
- Poor fit: readout-only retry, nonlocal/electronic branch, or MACE-style transplant.

## exploit_angles
- Simplify or tightly gate one existing scalar/vector mixing path.
- Keep the edit smaller than generation_008 `proposal_001` and `proposal_002`.
- Always pair with a true source control for attribution.

## jump_angles
- Only one bounded jump remains defensible: a very narrow late ACE-like invariant summary.
- It should be diagnostic and easy to disable, not a new representational branch.

## followup_queries
- Can one existing scalar-mix path inside `BalancedInteractionBlock` be weakened or source-capped to improve reproducibility without sacrificing ISO17?
- Is the best next exploit actually a subtraction/simplification rather than an addition?
- Can a single late invariant helper be made narrower than generation_008 `proposal_004` while still being measurable?

## confidence
**high** on the continuation anchor and on deprioritizing readout-only retries, **medium-high** on recommending source-tight in-block refinement as the primary next move, **medium** on the residual value of a very narrow late ACE-like jump.
