# MLIP Evidence Brief

## question
What bounded, benchmark-centric continuation should guide `generation_006` from source unit `generation_004/proposal_001` in balanced mode, after observing the full `generation_005` continuation set and re-checking locally verified literature under the fixed benchmark semantics?

## local_context
- Request target: `generation_006` continuation evidence, source anchored to `generation_004/proposal_001`.
- Continuation decision file: `research_runtime/ledger/generation_006_continuation_decision.json`.
- Selection outcome: parent source `generation_004/proposal_001` remained the continuation source for `generation_006` with `Q_rmd17 = 3.0291`, `Q_iso17 = 3.3267`, `Q_total = 3.1333`.
- Important round fact: no completed `generation_005` candidate beat the parent source. Best child was `generation_005/proposal_005` at `Q_total = 2.7464`.
- This dossier is evidence-only. It does not modify runnable units, launch runs, or decide selection.

## current_unit_profile
- Model family: compact local equivariant MLIP with scalar and vector channels, custom PyTorch implementation.
- Phase: exploit-family continuation, not a framework jump.
- Present capabilities in `research_runtime/generations/generation_004/proposal_001/model/model.py`:
  - atom embedding plus atomref baseline
  - local cutoff graph from Cartesian positions
  - Gaussian RBF plus cosine cutoff envelope
  - two `BalancedInteractionBlock`s
  - in-block scalar/vector fusion through `directional_invariant`, `agg_norm`, and `vector_alignment`
  - energy-first prediction with forces from autograd
- Missing capabilities:
  - no explicit triplet or product-basis body-order path
  - no irreps/tensor-product machinery
  - no sparse neighbor builder
  - no explicit nonlocal/electronic-state branch
- Likely bottlenecks now:
  - final energy readout still compresses vector content mostly to norms
  - capacity upgrades tried in `generation_005` did not surpass the parent, so naive “more mechanism” is not enough
  - the family appears calibration-sensitive, especially on rMD17 energy
- Likely implementation surface:
  - `model/model.py` for bounded representational edits
  - `model/train.py` only for narrowly justified schedule/loss controls

## benchmark_dossier
### Source-unit metrics (`generation_004/proposal_001`)
| dataset | split metrics | mixed force | mixed energy | gap penalty | Q_dataset |
|---|---|---:|---:|---:|---:|
| rMD17 | mild OOD F/E `0.10458 / 0.59297`, hard OOD F/E `0.10503 / 0.59259` | 0.10485 | 0.59274 | 0.00429 | 3.02911 |
| ISO17 | within F/E `0.18116 / 0.75503`, other F/E `0.19033 / 0.79636` | 0.18666 | 0.77982 | 0.04911 | 3.32669 |

### Cross-dataset view
- `Q_total = 3.13326`, still frontier after `generation_005`.
- `G_delta = 0.26450`, balanced rather than one-dataset-only.
- The parent source is therefore not just a temporary winner, it survived a full child continuation round.

### Training dynamics
- rMD17 ended very strong after an epoch-4 energy spike, finishing with best validation force and energy at epoch 8.
- ISO17 also had a large mid-training energy spike, then recovered to strong end-state metrics.
- Interpretation: the source can tolerate some turbulence, but extra capacity must recover cleanly by the end to matter.

### Runtime / reliability
- `run_state = terminal_success`
- `launch_count = 1`, `retry_count = 0`
- `repair_attempts = 0`, `remote_smoke_passed = true`, `remote_synced = true`
- Reliability remains a strength of this source.

### Generation_005 continuation outcomes relevant to `generation_006`
- `proposal_001` readout exploit: `Q_total = 2.0203`, severe energy regression.
- `proposal_003` late-fusion exploit: `Q_total = 2.6063`, improved ISO17 energy but weaker rMD17 than parent.
- `proposal_004` ACE-inspired compact body-order jump: `Q_total = 2.0663`, broad underperformance.
- `proposal_005` SO3KRATES-style stream separation jump: `Q_total = 2.7464`, best child, but still clearly below parent.
- `proposal_008` source-matched control proposal: `Q_total = 2.5185`, materially below parent, which is useful caution but not enough to dismiss the parent’s advantage.

## mathematical_evidence
### Local code form
- In-block message rule uses
  - scalar gate on `(src_scalar + dst_scalar)`
  - directional invariant `sum(src_vector * unit)`
  - vector transport `src_vector * gate + direction_gate * unit`
- Scalar update uses invariant summaries `agg_norm` and `vector_alignment`.
- Final energy head still uses `torch.cat([scalar_state, vector_norm], dim=-1)`.

### Locally verified external mathematical evidence
1. **Atomic Cluster Expansion: Completeness, Efficiency and Stability**
   - local PDF extracted from `/mnt/c/Users/1/Desktop/文献/MLIP/MLIP理论基础 - ACE完备性效率与稳定性.pdf`
   - strong mechanism: invariant polynomial bases can be built systematically with completeness and efficient recursive evaluation
   - implication: compact invariant many-body summaries are principled, but basis choice and numerical stability matter
2. **A Euclidean transformer for fast and stable machine learned force fields**
   - local PDF extracted from `/mnt/c/Users/1/Desktop/文献/MLIP/MLIP分子力场 - 欧氏Transformer快速稳定力场.pdf`
   - strong mechanism: separate invariant and equivariant information, recombine via cheap invariant contractions, avoid expensive tensor products
   - implication: the current scalar/vector split is directionally right, but larger refactors must justify themselves by actual benchmark gains

## physical_evidence
1. **Forces are not Enough**
   - local PDF extracted from `/mnt/c/Users/1/Desktop/文献/MLIP/MLIP力场基准 - Forces Are Not Enough分子模拟评测.pdf`
   - direct claim: force/energy test error alone does not align with simulation usefulness, and stability matters
   - implication for this task: keep using mixed energy, mixed force, gap, Q, and train-history behavior together
2. Current source preserves force-from-energy consistency and locality, and its benchmark behavior says locality is adequate for rMD17 plus ISO17 at this phase.
3. The failure of several `generation_005` children suggests the limiting issue is not “missing nonlocality by default”, but preserving calibration while adding capacity.

## chemical_evidence
- Benchmark chemistry is molecular and local-angular, not an obvious charge/spin or long-range benchmark.
- **SpookyNet** was locally extracted from `/mnt/c/Users/1/Desktop/文献/MLIP/MLIP分子力场 - SpookyNet含电子自由度非局域力场.pdf`.
- SpookyNet gives useful background: explicit electronic degrees of freedom and nonlocal effects matter in broader chemistry regimes.
- But for the present benchmark pair, there is no local metric evidence that nonlocal/electronic modeling is the next bounded need.
- ACE-style many-body sensitivity remains chemically closer to the likely missing signal than a SpookyNet-style branch.

## textual_evidence
- `generation_006_continuation_decision.json` explicitly kept `generation_004/proposal_001` over every `generation_005` child.
- This means the previous evidence thesis needs refinement: richer invariant coupling is still plausible, but the exact readout-heavy implementations tried in `generation_005` were not sufficient.
- The strongest child result came from the SO3KRATES-style stream-separation jump, which supports the stream-separation idea as weak-to-moderate evidence, not decisive proof.
- The readout exploit family underperformed badly enough that another near-duplicate readout-only proposal is weakly justified.

## code_evidence
### Local source code
- `generation_004/proposal_001/model/model.py`
  - strongest existing mechanism is inside `BalancedInteractionBlock`, not just the head
  - final readout bottleneck remains real, but in-block scalar/vector coupling is already meaningful
- `generation_004/proposal_001/model/train.py`
  - AdamW, cosine schedule, energy warmup, force taper, grad clip 3.0
  - relatively plain optimizer stack, so child failures are unlikely to be solved by cosmetic schedule changes alone

### Local round evidence from generation_005 outcomes
- Pure or near-pure readout enrichment did not hold benchmark balance.
- The best child came from more explicit invariant/equivariant stream separation, but still did not recover parent-level rMD17 + ISO17 balance.
- Therefore, the next move should be narrower than a family rewrite but more structural than a head-only concat tweak.

## relevant_papers
1. *Forces are not Enough: Benchmark and Critical Evaluation for Machine Learning Force Fields with Molecular Simulations*
2. *A Euclidean transformer for fast and stable machine learned force fields*
3. *Atomic Cluster Expansion: Completeness, Efficiency and Stability*
4. *SpookyNet: Learning force fields with electronic degrees of freedom and nonlocal effects*
5. Prior background anchor: *Higher Order Equivariant Message Passing Neural Networks for Fast and Accurate Force Fields* (MACE)
6. Prior background anchor: *SE(3)-Equivariant Graph Neural Networks for Data-Efficient and Accurate Interatomic Potentials* (NequIP)

## local_literature
- Verified by local extraction:
  - `/mnt/c/Users/1/Desktop/文献/MLIP/MLIP力场基准 - Forces Are Not Enough分子模拟评测.pdf`
  - `/mnt/c/Users/1/Desktop/文献/MLIP/MLIP分子力场 - 欧氏Transformer快速稳定力场.pdf`
  - `/mnt/c/Users/1/Desktop/文献/MLIP/MLIP理论基础 - ACE完备性效率与稳定性.pdf`
  - `/mnt/c/Users/1/Desktop/文献/MLIP/MLIP分子力场 - SpookyNet含电子自由度非局域力场.pdf`
- Reused prior local brief context:
  - NequIP and MACE remain family-level anchors, but not fresh decisive evidence for a full transplant

## relevant_repos
- Reused prior repo background only:
  - `mir-group/nequip`
  - `ACEsuit/mace`
- No new repository is promoted to strong evidence in this run because local round evidence and local PDFs were already enough to bound the recommendation.

## mechanism_ledger
| mechanism | source | concrete equation / code / pattern | current-code insertion point | proposal relevance | risk |
|---|---|---|---|---|---|
| invariant/equivariant stream separation | SO3KRATES local PDF + `generation_005/proposal_005` outcome | distinct invariant/equivariant pathways with cheap invariant recombination | `BalancedInteractionBlock` internal scalar/vector update | strongest surviving child-family clue | medium |
| compact invariant many-body summary | ACE local PDF | low-order invariant basis / recursive many-body summary | add narrow summary path near scalar update or pre-readout summary | bounded jump with scientific upside | medium |
| force-from-energy contract | local source code | scalar energy, autograd forces | must remain untouched | hard requirement | low |
| benchmark-stability-aware interpretation | Forces are not Enough local PDF | force error alone is insufficient, stability matters | evaluation logic, not code | prevents wrong proposal justification | low |
| nonlocal/electronic branch | SpookyNet local PDF | self-attention plus explicit electronic degrees | rewrite-heavy, outside bounded surface | background only, not current recommendation | high |

## capability_gap
### Current code capabilities
- good local equivariant trunk
- validated scalar/vector coupling inside blocks
- strong benchmark-complete balance

### Required next capabilities
- stronger directional information retention without destabilizing energy calibration
- if added capacity is used, it must improve both datasets enough to beat the parent, not just produce a plausible mechanism
- better source-matched attribution remains helpful

### Missing pieces
- a proven bounded mechanism between head-only enrichment and rewrite-level stream refactor
- robust body-order or cross-channel summary that preserves the source’s rMD17 energy advantage

### Integration risk
- low-to-medium: small internal stream-separation refinement inside existing blocks
- medium: narrow ACE-like many-body summary path
- high: nonlocal/electronic or irreps-heavy rewrite

## implementable_design_moves
1. **Primary exploit**
   - mechanism source: SO3KRATES local PDF + best `generation_005` child signal
   - concrete mechanism: small internal stream-separation refinement inside `BalancedInteractionBlock`, not a readout-only enrichment
   - current-code insertion point: replace or refine `scalar_input` / `vector_mix` pathways in `model/model.py`
   - minimal bounded edit: add one extra invariant recombination path using existing `self_vector`, `mixed_agg_vector`, and gated scalar summaries before the residual update
   - expected effect: better use of vector structure while keeping the trunk familiar
   - bounded control/ablation: same block with added recombination path toggled off
2. **Secondary jump**
   - mechanism source: ACE local PDF
   - concrete mechanism: narrow low-order invariant many-body summary, injected once near the late scalar update rather than throughout the stack
   - current-code insertion point: one helper path in `model/model.py` feeding scalar update or pre-readout summary
   - minimal bounded edit: low-width summary from neighbor-pair geometry, no framework transplant
   - expected effect: extra angular/body-order signal if the trunk is capacity-limited
   - bounded control/ablation: same model with summary path zeroed or disabled
3. **Interpretation control**
   - mechanism source: round evidence plus Forces-are-not-Enough caution
   - concrete mechanism: source-matched replicate or near-replicate remains valuable for attribution
   - current-code insertion point: none, evaluation design only
   - minimal bounded edit: none to model family if a control branch is allocated
   - expected effect: cleaner confidence on small gains
   - bounded control/ablation: direct source replicate

## strong_evidence
- `generation_004/proposal_001` survived a full continuation round and remained best.
- Readout-centered `generation_005` exploit branches did not validate themselves.
- The best child signal came from explicit stream separation, not from simple head enrichment.
- Local PDF evidence still supports staying local, symmetry-aware, and benchmark-complete.

## weak_but_relevant
- ACE-like compact body-order remains plausible, but `generation_005/proposal_004` underperformed, so evidence is not cleanly positive for that exact implementation style.
- The low-performing source-matched control proposal is suggestive but not fully trustworthy as variance evidence without checking fidelity.
- SpookyNet is scientifically relevant background, but weak direct evidence for this benchmark phase.

## background_context
- Earlier evidence pushed toward readout enrichment first and compact body-order second.
- `generation_005` updated that map: head-only enrichment looks over-recommended in hindsight, while internal stream discipline looks relatively stronger.
- The parent source still defines the reliable local frontier.

## key_findings
1. `generation_004/proposal_001` is still the right family anchor for `generation_006`.
2. Another near-duplicate readout-only exploit is weakly justified because the `generation_005` versions lost too much benchmark balance.
3. The strongest surviving mechanism clue is internal invariant/equivariant stream refinement, not full architectural jump.
4. ACE-like many-body enrichment remains the main higher-upside jump, but only as a very narrow add-on.
5. Nonlocal/electronic modeling is still a mismatch for the next bounded continuation.

## useful_patterns
- Preserve the parent trunk and energy-first contract.
- Prefer edits inside the existing interaction block over a readout-only concat change.
- Keep added structure narrow enough that the model can fall back toward parent behavior.
- Judge every move by mixed energy, mixed force, gap, Q, and train-history recovery together.

## risks_or_mismatches
- Data/task mismatch: nonlocal/electronic branches remain poorly justified.
- Method mismatch: another broad readout redesign may repeat `generation_005` regressions.
- Codebase mismatch: full irreps or transformer rewrite exceeds bounded continuation scope.
- Runtime mismatch: larger refactors could sacrifice the parent’s clean reliability without enough upside.
- Likely failure signs:
  - rMD17 energy degrades sharply while ISO17 improves a bit
  - train histories show spikes without late recovery
  - gains appear on force only while mixed energy or gaps worsen

## implementation_fit
- Best fit now: small internal stream-separation exploit inside the current block family.
- Next-best fit: one narrow ACE-like summary path added late.
- Poor fit now: readout-only retry, nonlocal/electronic branch, full framework transplant.
- Overall fit judgment: exploit the parent internally, jump only in one very bounded many-body dimension.

## exploit_angles
- Refine scalar/vector recombination inside `BalancedInteractionBlock`.
- Keep the final readout simple unless supported by stronger internal summaries.
- If only one exploit is chosen, prefer in-block stream refinement over head-only enrichment.

## jump_angles
- Best jump: narrow ACE-like late summary path.
- Secondary jump: slightly stronger SO3KRATES-style stream discipline, but still local and lightweight.
- Deprioritized jump: SpookyNet-style nonlocality or full irreps migration.

## followup_queries
- Can a tiny in-block stream-refinement exploit beat the parent without harming rMD17 energy?
- Is a late one-shot ACE-like summary path safer than repeating a full body-order branch?
- Was `generation_005/proposal_008` a faithful enough control to interpret its low score as variance evidence?
- Which exact `generation_005` child code change caused the severe readout-exploit regressions?

## confidence
**medium-high**

Reasoning: confidence is high that the continuation should stay anchored to `generation_004/proposal_001` and remain benchmark-complete. Confidence is medium-high, not high, on the exact next mechanism because `generation_005` falsified the strongest prior readout-first hypothesis and only weakly endorsed stream separation as the next exploit.
