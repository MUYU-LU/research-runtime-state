# Proposal context for generation_004/proposal_001

## Current unit
- unit: generation_004/proposal_001
- source unit: generation_003/proposal_004

## Active evidence
- path: /home/lmy/.openclaw/workspace/research_runtime/knowledge/briefs/evidence_brief_20260419T012900Z_generation006_proposal001_continuation.md
- source unit: generation_004/proposal_001
- mode: balanced

```markdown
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

```

## Current runtime summary
```json
{
  "implementation_status": {
    "implementation_state": "launch_ready",
    "source_unit": "generation_003/proposal_004",
    "proposal_file": "/home/lmy/.openclaw/workspace/research_runtime/proposals/generation_003_proposal_004_continuation/proposal_001.md",
    "control_replicate": false,
    "changed_files": [
      {
        "path": "model/model.py",
        "sha256": "aa6c16d26fa72de792c66b24eaf2f583373a66eabc338ebae04872489f581ef4"
      },
      {
        "path": "model/train.py",
        "sha256": "a2e5336c32b379cbd3fe183c41a893225992061849571b639d65185d8846e64d"
      }
    ],
    "repair_attempts": 0,
    "same_failure_class_repairs": 0,
    "last_failure_class": "unknown_failure",
    "remote_synced": true,
    "remote_smoke_passed": true,
    "remote_path": "/public/home/lmy/MLIP_EVOLUTION/research_runtime/generations/generation_004/proposal_001",
    "smoke_log_local": "/home/lmy/.openclaw/workspace/research_runtime/generations/generation_004/proposal_001/outputs/smoke_rmd17.log",
    "smoke_log_remote": "/public/home/lmy/MLIP_EVOLUTION/research_runtime/generations/generation_004/proposal_001/outputs/smoke_rmd17.log",
    "last_actor": "remote_collect_unit.py",
    "last_updated_utc": "2026-04-17T23:22:58.791549+00:00"
  },
  "run_status": {
    "run_state": "terminal_success",
    "launch_count": 1,
    "retry_count": 0,
    "pid": "3008347",
    "host": "210.45.70.177",
    "launch_log_local": "/home/lmy/.openclaw/workspace/research_runtime/generations/generation_004/proposal_001/outputs/launch.log",
    "launch_log_remote": "/public/home/lmy/MLIP_EVOLUTION/research_runtime/generations/generation_004/proposal_001/outputs/launch.log",
    "failure_class": null,
    "launched_at_utc": "2026-04-17T23:13:18.849079+00:00",
    "finished_at_utc": "2026-04-18T02:11:13.011712+00:00",
    "last_actor": "remote_collect_unit.py",
    "last_state_change_utc": "2026-04-18T02:11:13.011754+00:00"
  },
  "unit_summary": {
    "unit": "generation_004/proposal_001",
    "unit_meta": {
      "source_unit": "generation_003/proposal_004",
      "generation_round": "generation_004",
      "proposal_unit": "proposal_001",
      "proposal_file": "/home/lmy/.openclaw/workspace/research_runtime/proposals/generation_003_proposal_004_continuation/proposal_001.md",
      "control_replicate": false
    },
    "proposal_metadata": {
      "family": null,
      "phase": null,
      "jump_type": null,
      "budget_class": null,
      "expected_capability_gain": [],
      "proposal_file": "/home/lmy/.openclaw/workspace/research_runtime/proposals/generation_003_proposal_004_continuation/proposal_001.md",
      "control_replicate": false
    },
    "runtime_summary": {
      "run_state": "terminal_success",
      "failure_class": null,
      "launch_count": 1,
      "retry_count": 0,
      "implementation_state": "launch_ready",
      "remote_synced": true,
      "remote_smoke_passed": true,
      "repair_attempts": 0,
      "same_failure_class_repairs": 0,
      "last_failure_class": "unknown_failure"
    },
    "datasets": {
      "rmd17": {
        "metrics_path": "generations/generation_004/proposal_001/outputs/rmd17/benchmark_metrics.json",
        "history_path": "generations/generation_004/proposal_001/outputs/rmd17/train_history.json",
        "metrics": {
          "mild_ood_energy_mae": 0.5929720458984375,
          "mild_ood_force_mae": 0.10458182134397793,
          "hard_ood_energy_mae": 0.5925932006835938,
          "hard_ood_force_mae": 0.10503137192176655,
          "mixed_force_mae": 0.1048515516906511,
          "mixed_energy_mae": 0.5927447387695313,
          "gap_penalty": 0.004287495707365973,
          "Q_dataset": 3.0291108938796594,
          "device": "cuda"
        },
        "history_summary": {
          "epochs": 8,
          "last_epoch": {
            "epoch": 8,
            "train": {
              "loss": 3.979856164485216,
              "energy_mae": 1.8791643676757812,
              "force_mae": 0.10503459000156727
            },
            "val": {
              "loss": 2.684609644584358,
              "energy_mae": 0.5929732666015625,
              "force_mae": 0.10458181903103832
            },
            "device": "cuda",
            "learning_rate": 0.0,
            "energy_weight": 1.0,
            "force_weight": 20.0,
            "grad_clip": 3.0
          },
          "best_val_force_mae": 0.10458181903103832,
          "best_val_energy_mae": 0.5929732666015625,
          "force_trend": "improving",
          "energy_trend": "improving"
        },
        "Q_dataset": 3.0291108938796594
      },
      "iso17": {
        "metrics_path": "generations/generation_004/proposal_001/outputs/iso17/benchmark_metrics.json",
        "history_path": "generations/generation_004/proposal_001/outputs/iso17/train_history.json",
        "metrics": {
          "within_energy_mae": 0.7550254293007426,
          "within_force_mae": 0.1811587671813841,
          "other_energy_mae": 0.7963562950721154,
          "other_force_mae": 0.19032591961324216,
          "mixed_force_mae": 0.18665905864049892,
          "mixed_energy_mae": 0.7798239487635663,
          "gap_penalty": 0.04911174683177137,
          "Q_dataset": 3.32668622930551,
          "device": "cuda"
        },
        "history_summary": {
          "epochs": 8,
          "last_epoch": {
            "epoch": 8,
            "train": {
              "loss": 6.050462749246323,
              "energy_mae": 2.3952547281095296,
              "force_mae": 0.18276040118077014
            },
            "val": {
              "loss": 4.2366401354471845,
              "energy_mae": 1.0377604166666667,
              "force_mae": 0.15994398792584738
            },
            "device": "cuda",
            "learning_rate": 0.0,
            "energy_weight": 1.0,
            "force_weight": 20.0,
            "grad_clip": 3.0
          },
          "best_val_force_mae": 0.15994398792584738,
          "best_val_energy_mae": 1.0377604166666667,
          "force_trend": "improving",
          "energy_trend": "improving"
        },
        "Q_dataset": 3.32668622930551
      }
    },
    "Q_rmd17": 3.0291108938796594,
    "Q_iso17": 3.32668622930551,
    "Q_total": 3.1332622612787073,
    "G_delta": 0.26449992779357956,
    "generation_summary": "ledger/generation_004_summary.json",
    "frontier_record": "ledger/frontier.jsonl"
  }
}
```

## Source runtime summary
```json
{
  "implementation_status": {
    "implementation_state": "launch_ready",
    "source_unit": "generation_002/proposal_005",
    "proposal_file": "04_jump_nequip_style_recalibrated_refactor.md",
    "control_replicate": false,
    "changed_files": [
      {
        "path": "model/model.py",
        "sha256": "89361d68c606e0bbdf030493ed7d46cbeb2c583ee5c8648f59ffbf5e7f3d16c5"
      },
      {
        "path": "model/train.py",
        "sha256": "abe39d2214fb9139bd9d079866464e5c7c0b3b183c6b9b0f19513ccfbfcc588a"
      }
    ],
    "repair_attempts": 0,
    "same_failure_class_repairs": 0,
    "last_failure_class": null,
    "remote_synced": true,
    "remote_smoke_passed": true,
    "remote_path": "/public/home/lmy/MLIP_EVOLUTION/research_runtime/generations/generation_003/proposal_004",
    "smoke_log_local": "/home/lmy/.openclaw/workspace/research_runtime/generations/generation_003/proposal_004/outputs/smoke_rmd17.log",
    "smoke_log_remote": "/public/home/lmy/MLIP_EVOLUTION/research_runtime/generations/generation_003/proposal_004/outputs/smoke_rmd17.log",
    "last_actor": "remote_smoke_unit.py",
    "last_updated_utc": "2026-04-17T14:10:22.098297+00:00",
    "notes": [
      "Implemented a bounded NequIP-style recalibrated refactor while preserving the benchmark contract, local neighbor interactions, scalar energy readout, atomref baseline, and autograd-derived forces.",
      "Replaced the prior low-rank stage stack with a cleaner interaction refactor using cosine cutoff envelopes, gated scalar residual updates, tempered vector residual updates, and normalized scalar state updates.",
      "Recalibrated training with AdamW, cosine LR scheduling, gradient clipping, stronger energy emphasis, and short energy-weight warmup for a more benchmark-balanced regime."
    ]
  },
  "run_status": {
    "run_state": "terminal_success",
    "launch_count": 1,
    "retry_count": 0,
    "pid": "2904438",
    "host": "210.45.70.177",
    "launch_log_local": "/home/lmy/.openclaw/workspace/research_runtime/generations/generation_003/proposal_004/outputs/launch.log",
    "launch_log_remote": "/public/home/lmy/MLIP_EVOLUTION/research_runtime/generations/generation_003/proposal_004/outputs/launch.log",
    "failure_class": null,
    "launched_at_utc": "2026-04-17T16:20:38.837492+00:00",
    "finished_at_utc": "2026-04-17T17:50:58.624304+00:00",
    "last_actor": "remote_collect_unit.py",
    "last_state_change_utc": "2026-04-17T17:50:58.624351+00:00"
  },
  "unit_summary": {
    "unit": "generation_003/proposal_004",
    "unit_meta": {
      "source_unit": "generation_002/proposal_005",
      "generation_round": "generation_003",
      "proposal_unit": "proposal_004",
      "proposal_file": "04_jump_nequip_style_recalibrated_refactor.md",
      "control_replicate": false
    },
    "proposal_metadata": {
      "family": null,
      "phase": null,
      "jump_type": null,
      "budget_class": null,
      "expected_capability_gain": [],
      "proposal_file": "04_jump_nequip_style_recalibrated_refactor.md",
      "control_replicate": false
    },
    "runtime_summary": {
      "run_state": "terminal_success",
      "failure_class": null,
      "launch_count": 1,
      "retry_count": 0,
      "implementation_state": "launch_ready",
      "remote_synced": true,
      "remote_smoke_passed": true,
      "repair_attempts": 0,
      "same_failure_class_repairs": 0,
      "last_failure_class": null
    },
    "datasets": {
      "rmd17": {
        "metrics_path": "generations/generation_003/proposal_004/outputs/rmd17/benchmark_metrics.json",
        "history_path": "generations/generation_003/proposal_004/outputs/rmd17/train_history.json",
        "metrics": {
          "mild_ood_energy_mae": 2.2845567626953125,
          "mild_ood_force_mae": 0.10615500151272864,
          "hard_ood_energy_mae": 2.28490185546875,
          "hard_ood_force_mae": 0.10682270545721985,
          "mixed_force_mae": 0.10655562387942336,
          "mixed_energy_mae": 2.2847638183593753,
          "gap_penalty": 0.006266247807253327,
          "Q_dataset": 2.6795083100762995,
          "device": "cuda"
        },
        "history_summary": {
          "epochs": 8,
          "last_epoch": {
            "epoch": 8,
            "train": {
              "loss": 3.974056053943932,
              "energy_mae": 1.8268427124023439,
              "force_mae": 0.10736066733044572
            },
            "val": {
              "loss": 4.4076569082736965,
              "energy_mae": 2.2845567626953125,
              "force_mae": 0.10615500762383454
            },
            "device": "cuda",
            "learning_rate": 0.0,
            "energy_weight": 1.0,
            "force_weight": 20.0,
            "grad_clip": 5.0
          },
          "best_val_force_mae": 0.10615500762383454,
          "best_val_energy_mae": 1.4970237426757813,
          "force_trend": "improving",
          "energy_trend": "improving"
        },
        "Q_dataset": 2.6795083100762995
      },
      "iso17": {
        "metrics_path": "generations/generation_003/proposal_004/outputs/iso17/benchmark_metrics.json",
        "history_path": "generations/generation_003/proposal_004/outputs/iso17/train_history.json",
        "metrics": {
          "within_energy_mae": 1.6992206837871286,
          "within_force_mae": 0.1626173206374492,
          "other_energy_mae": 1.5159589092548076,
          "other_force_mae": 0.17375626559440907,
          "mixed_force_mae": 0.16930068761162512,
          "mixed_energy_mae": 1.589263619067736,
          "gap_penalty": 0.06579385538260052,
          "Q_dataset": 3.22023409124438,
          "device": "cuda"
        },
        "history_summary": {
          "epochs": 8,
          "last_epoch": {
            "epoch": 8,
            "train": {
              "loss": 5.9520263052075215,
              "energy_mae": 2.6536815681079826,
              "force_mae": 0.16491723685055085
            },
            "val": {
              "loss": 3.3838011423746743,
              "energy_mae": 0.24772135416666666,
              "force_mae": 0.15680398543675741
            },
            "device": "cuda",
            "learning_rate": 0.0,
            "energy_weight": 1.0,
            "force_weight": 20.0,
            "grad_clip": 5.0
          },
          "best_val_force_mae": 0.15680398543675741,
          "best_val_energy_mae": 0.24772135416666666,
          "force_trend": "improving",
          "energy_trend": "improving"
        },
        "Q_dataset": 3.22023409124438
      }
    },
    "Q_rmd17": 2.6795083100762995,
    "Q_iso17": 3.22023409124438,
    "Q_total": 2.8687623334851278,
    "G_delta": 1.1558621409606864,
    "generation_summary": "ledger/generation_003_summary.json",
    "frontier_record": "ledger/frontier.jsonl"
  }
}
```

## rmd17 benchmark dossier
```json
{
  "metrics": {
    "mild_ood_energy_mae": 0.5929720458984375,
    "mild_ood_force_mae": 0.10458182134397793,
    "hard_ood_energy_mae": 0.5925932006835938,
    "hard_ood_force_mae": 0.10503137192176655,
    "mixed_force_mae": 0.1048515516906511,
    "mixed_energy_mae": 0.5927447387695313,
    "gap_penalty": 0.004287495707365973,
    "Q_dataset": 3.0291108938796594,
    "device": "cuda"
  },
  "history": [
    {
      "epoch": 6,
      "train": {
        "loss": 15.348967134423553,
        "energy_mae": 12.71894921875,
        "force_mae": 0.131500896028243
      },
      "val": {
        "loss": 6.038513257011771,
        "energy_mae": 3.4658735961914062,
        "force_mae": 0.1286319831525907
      },
      "device": "cuda",
      "learning_rate": 0.0001464466094067263,
      "energy_weight": 1.0,
      "force_weight": 20.0,
      "grad_clip": 3.0
    },
    {
      "epoch": 7,
      "train": {
        "loss": 8.394697527773678,
        "energy_mae": 6.084681396484375,
        "force_mae": 0.11550080670998432
      },
      "val": {
        "loss": 4.677032755553722,
        "energy_mae": 2.4347793579101564,
        "force_mae": 0.1121126701454632
      },
      "device": "cuda",
      "learning_rate": 3.8060233744356646e-05,
      "energy_weight": 1.0,
      "force_weight": 20.0,
      "grad_clip": 3.0
    },
    {
      "epoch": 8,
      "train": {
        "loss": 3.979856164485216,
        "energy_mae": 1.8791643676757812,
        "force_mae": 0.10503459000156727
      },
      "val": {
        "loss": 2.684609644584358,
        "energy_mae": 0.5929732666015625,
        "force_mae": 0.10458181903103832
      },
      "device": "cuda",
      "learning_rate": 0.0,
      "energy_weight": 1.0,
      "force_weight": 20.0,
      "grad_clip": 3.0
    }
  ],
  "history_summary": {
    "epochs": 8,
    "last_epoch": {
      "epoch": 8,
      "train": {
        "loss": 3.979856164485216,
        "energy_mae": 1.8791643676757812,
        "force_mae": 0.10503459000156727
      },
      "val": {
        "loss": 2.684609644584358,
        "energy_mae": 0.5929732666015625,
        "force_mae": 0.10458181903103832
      },
      "device": "cuda",
      "learning_rate": 0.0,
      "energy_weight": 1.0,
      "force_weight": 20.0,
      "grad_clip": 3.0
    },
    "best_val_force_mae": 0.10458181903103832,
    "best_val_energy_mae": 0.5929732666015625
  }
}
```

## iso17 benchmark dossier
```json
{
  "metrics": {
    "within_energy_mae": 0.7550254293007426,
    "within_force_mae": 0.1811587671813841,
    "other_energy_mae": 0.7963562950721154,
    "other_force_mae": 0.19032591961324216,
    "mixed_force_mae": 0.18665905864049892,
    "mixed_energy_mae": 0.7798239487635663,
    "gap_penalty": 0.04911174683177137,
    "Q_dataset": 3.32668622930551,
    "device": "cuda"
  },
  "history": [
    {
      "epoch": 6,
      "train": {
        "loss": 16.691313417978805,
        "energy_mae": 12.704586097037438,
        "force_mae": 0.1993363660833992
      },
      "val": {
        "loss": 6.187129020690918,
        "energy_mae": 2.5341796875,
        "force_mae": 0.18264745672543845
      },
      "device": "cuda",
      "learning_rate": 0.0001464466094067263,
      "energy_weight": 1.0,
      "force_weight": 20.0,
      "grad_clip": 3.0
    },
    {
      "epoch": 7,
      "train": {
        "loss": 11.12258027201832,
        "energy_mae": 7.344810803101795,
        "force_mae": 0.18888847393232702
      },
      "val": {
        "loss": 6.189233144124349,
        "energy_mae": 2.9222005208333335,
        "force_mae": 0.1633516401052475
      },
      "device": "cuda",
      "learning_rate": 3.8060233744356646e-05,
      "energy_weight": 1.0,
      "force_weight": 20.0,
      "grad_clip": 3.0
    },
    {
      "epoch": 8,
      "train": {
        "loss": 6.050462749246323,
        "energy_mae": 2.3952547281095296,
        "force_mae": 0.18276040118077014
      },
      "val": {
        "loss": 4.2366401354471845,
        "energy_mae": 1.0377604166666667,
        "force_mae": 0.15994398792584738
      },
      "device": "cuda",
      "learning_rate": 0.0,
      "energy_weight": 1.0,
      "force_weight": 20.0,
      "grad_clip": 3.0
    }
  ],
  "history_summary": {
    "epochs": 8,
    "last_epoch": {
      "epoch": 8,
      "train": {
        "loss": 6.050462749246323,
        "energy_mae": 2.3952547281095296,
        "force_mae": 0.18276040118077014
      },
      "val": {
        "loss": 4.2366401354471845,
        "energy_mae": 1.0377604166666667,
        "force_mae": 0.15994398792584738
      },
      "device": "cuda",
      "learning_rate": 0.0,
      "energy_weight": 1.0,
      "force_weight": 20.0,
      "grad_clip": 3.0
    },
    "best_val_force_mae": 0.15994398792584738,
    "best_val_energy_mae": 1.0377604166666667
  }
}
```

## Generation summary
```json
{
  "generation": "generation_004",
  "created_at_utc": "2026-04-18T12:30:20.867464+00:00",
  "units": [
    {
      "unit": "generation_004/proposal_001",
      "proposal_file": "/home/lmy/.openclaw/workspace/research_runtime/proposals/generation_003_proposal_004_continuation/proposal_001.md",
      "control_replicate": false,
      "run_state": "terminal_success",
      "failure_class": null,
      "launch_count": 1,
      "retry_count": 0,
      "implementation_state": "launch_ready",
      "remote_synced": true,
      "remote_smoke_passed": true,
      "repair_attempts": 0,
      "same_failure_class_repairs": 0,
      "last_failure_class": "unknown_failure",
      "Q_rmd17": 3.0291108938796594,
      "Q_iso17": 3.32668622930551,
      "Q_total": 3.1332622612787073,
      "rmd17_metrics_present": true,
      "rmd17_history_present": true,
      "rmd17_mild_ood_energy_mae": 0.5929720458984375,
      "rmd17_mild_ood_force_mae": 0.10458182134397793,
      "rmd17_hard_ood_energy_mae": 0.5925932006835938,
      "rmd17_hard_ood_force_mae": 0.10503137192176655,
      "rmd17_mixed_force_mae": 0.1048515516906511,
      "rmd17_mixed_energy_mae": 0.5927447387695313,
      "rmd17_gap_penalty": 0.004287495707365973,
      "rmd17_Q_dataset": 3.0291108938796594,
      "rmd17_device": "cuda",
      "rmd17_epochs": 8,
      "rmd17_force_trend": "improving",
      "rmd17_energy_trend": "improving",
      "rmd17_best_val_force_mae": 0.10458181903103832,
      "rmd17_best_val_energy_mae": 0.5929732666015625,
      "iso17_metrics_present": true,
      "iso17_history_present": true,
      "iso17_within_energy_mae": 0.7550254293007426,
      "iso17_within_force_mae": 0.1811587671813841,
      "iso17_other_energy_mae": 0.7963562950721154,
      "iso17_other_force_mae": 0.19032591961324216,
      "iso17_mixed_force_mae": 0.18665905864049892,
      "iso17_mixed_energy_mae": 0.7798239487635663,
      "iso17_gap_penalty": 0.04911174683177137,
      "iso17_Q_dataset": 3.32668622930551,
      "iso17_device": "cuda",
      "iso17_epochs": 8,
      "iso17_force_trend": "improving",
      "iso17_energy_trend": "improving",
      "iso17_best_val_force_mae": 0.15994398792584738,
      "iso17_best_val_energy_mae": 1.0377604166666667
    },
    {
      "unit": "generation_004/proposal_002",
      "proposal_file": "/home/lmy/.openclaw/workspace/research_runtime/proposals/generation_003_proposal_004_continuation/proposal_002.md",
      "control_replicate": false,
      "run_state": "terminal_success",
      "failure_class": null,
      "launch_count": 1,
      "retry_count": 0,
      "implementation_state": "launch_ready",
      "remote_synced": true,
      "remote_smoke_passed": true,
      "repair_attempts": 0,
      "same_failure_class_repairs": 0,
      "last_failure_class": null,
      "Q_rmd17": 2.9728719438179514,
      "Q_iso17": 3.3666897160680302,
      "Q_total": 3.110708164105479,
      "rmd17_metrics_present": true,
      "rmd17_history_present": true,
      "rmd17_mild_ood_energy_mae": 0.5796865844726562,
      "rmd17_mild_ood_force_mae": 0.11346382295736111,
      "rmd17_hard_ood_energy_mae": 0.5807351684570312,
      "rmd17_hard_ood_force_mae": 0.1140345740816556,
      "rmd17_mixed_force_mae": 0.11380627363193781,
      "rmd17_mixed_energy_mae": 0.5803157348632813,
      "rmd17_gap_penalty": 0.005015111259466622,
      "rmd17_Q_dataset": 2.9728719438179514,
      "rmd17_device": "cuda",
      "rmd17_epochs": 8,
      "rmd17_force_trend": "improving",
      "rmd17_energy_trend": "improving",
      "rmd17_best_val_force_mae": 0.11346382210240699,
      "rmd17_best_val_energy_mae": 0.579689208984375,
      "iso17_metrics_present": true,
      "iso17_history_present": true,
      "iso17_within_energy_mae": 0.650325359684406,
      "iso17_within_force_mae": 0.17873083827740485,
      "iso17_other_energy_mae": 0.6927433894230769,
      "iso17_other_force_mae": 0.18977487115046152,
      "iso17_mixed_force_mae": 0.18535725800123884,
      "iso17_mixed_energy_mae": 0.6757761775276085,
      "iso17_gap_penalty": 0.05958241393991309,
      "iso17_Q_dataset": 3.3666897160680302,
      "iso17_device": "cuda",
      "iso17_epochs": 8,
      "iso17_force_trend": "improving",
      "iso17_energy_trend": "improving",
      "iso17_best_val_force_mae": 0.15553108851114908,
      "iso17_best_val_energy_mae": 0.771484375
    },
    {
      "unit": "generation_004/proposal_003",
      "proposal_file": "/home/lmy/.openclaw/workspace/research_runtime/proposals/generation_003_proposal_004_continuation/proposal_003.md",
      "control_replicate": false,
      "run_state": "terminal_success",
      "failure_class": null,
      "launch_count": 1,
      "retry_count": 0,
      "implementation_state": "launch_ready",
      "remote_synced": true,
      "remote_smoke_passed": true,
      "repair_attempts": 0,
      "same_failure_class_repairs": 0,
      "last_failure_class": null,
      "Q_rmd17": 2.91278187287435,
      "Q_iso17": 3.3500470650609744,
      "Q_total": 3.065824690139668,
      "rmd17_metrics_present": true,
      "rmd17_history_present": true,
      "rmd17_mild_ood_energy_mae": 1.5685512084960938,
      "rmd17_mild_ood_force_mae": 0.08815841447329148,
      "rmd17_hard_ood_energy_mae": 1.5686265258789063,
      "rmd17_hard_ood_force_mae": 0.08872427424951457,
      "rmd17_mixed_force_mae": 0.08849793033902534,
      "rmd17_mixed_energy_mae": 1.5685963989257812,
      "rmd17_gap_penalty": 0.006394045307601548,
      "rmd17_Q_dataset": 2.91278187287435,
      "rmd17_device": "cuda",
      "rmd17_epochs": 8,
      "rmd17_force_trend": "improving",
      "rmd17_energy_trend": "improving",
      "rmd17_best_val_force_mae": 0.08815835198748391,
      "rmd17_best_val_energy_mae": 1.5685526123046876,
      "iso17_metrics_present": true,
      "iso17_history_present": true,
      "iso17_within_energy_mae": 0.7745948715965346,
      "iso17_within_force_mae": 0.16707400126327382,
      "iso17_other_energy_mae": 0.8995567908653846,
      "iso17_other_force_mae": 0.18059184630043232,
      "iso17_mixed_force_mae": 0.17518470828556892,
      "iso17_mixed_energy_mae": 0.8495720231578445,
      "iso17_gap_penalty": 0.07716338468906699,
      "iso17_Q_dataset": 3.3500470650609744,
      "iso17_device": "cuda",
      "iso17_epochs": 8,
      "iso17_force_trend": "improving",
      "iso17_energy_trend": "improving",
      "iso17_best_val_force_mae": 0.1483928163846334,
      "iso17_best_val_energy_mae": 1.9970703125
    },
    {
      "unit": "generation_004/proposal_004",
      "proposal_file": "/home/lmy/.openclaw/workspace/research_runtime/proposals/generation_003_proposal_004_continuation/proposal_004.md",
      "control_replicate": false,
      "run_state": "terminal_success",
      "failure_class": null,
      "launch_count": 1,
      "retry_count": 0,
      "implementation_state": "launch_ready",
      "remote_synced": true,
      "remote_smoke_passed": true,
      "repair_attempts": 0,
      "same_failure_class_repairs": 0,
      "last_failure_class": null,
      "Q_rmd17": 2.7935780322122152,
      "Q_iso17": 3.1721084802597064,
      "Q_total": 2.926063689028837,
      "rmd17_metrics_present": true,
      "rmd17_history_present": true,
      "rmd17_mild_ood_energy_mae": 1.5460761108398438,
      "rmd17_mild_ood_force_mae": 0.1041935924035497,
      "rmd17_hard_ood_energy_mae": 1.5454930419921875,
      "rmd17_hard_ood_force_mae": 0.10439481916511431,
      "rmd17_mixed_force_mae": 0.10431432846048846,
      "rmd17_mixed_energy_mae": 1.54572626953125,
      "rmd17_gap_penalty": 0.0019290423907479411,
      "rmd17_Q_dataset": 2.7935780322122152,
      "rmd17_device": "cuda",
      "rmd17_epochs": 8,
      "rmd17_force_trend": "improving",
      "rmd17_energy_trend": "improving",
      "rmd17_best_val_force_mae": 0.10419358538102824,
      "rmd17_best_val_energy_mae": 1.5460751342773438,
      "iso17_metrics_present": true,
      "iso17_history_present": true,
      "iso17_within_energy_mae": 2.1062002049814357,
      "iso17_within_force_mae": 0.15504878737622557,
      "iso17_other_energy_mae": 2.02951171875,
      "iso17_other_force_mae": 0.17135219249587794,
      "iso17_mixed_force_mae": 0.164830830448017,
      "iso17_mixed_energy_mae": 2.060187113242574,
      "iso17_gap_penalty": 0.09890992525633782,
      "iso17_Q_dataset": 3.1721084802597064,
      "iso17_device": "cuda",
      "iso17_epochs": 8,
      "iso17_force_trend": "improving",
      "iso17_energy_trend": "improving",
      "iso17_best_val_force_mae": 0.1616599460442861,
      "iso17_best_val_energy_mae": 1.9599609375
    },
    {
      "unit": "generation_004/proposal_006",
      "proposal_file": "/home/lmy/.openclaw/workspace/research_runtime/proposals/generation_003_proposal_004_continuation/proposal_006.md",
      "control_replicate": false,
      "run_state": "terminal_success",
      "failure_class": null,
      "launch_count": 1,
      "retry_count": 0,
      "implementation_state": "launch_ready",
      "remote_synced": true,
      "remote_smoke_passed": true,
      "repair_attempts": 0,
      "same_failure_class_repairs": 0,
      "last_failure_class": null,
      "Q_rmd17": 2.7891460794531704,
      "Q_iso17": 3.19258956279737,
      "Q_total": 2.9303512986236404,
      "rmd17_metrics_present": true,
      "rmd17_history_present": true,
      "rmd17_mild_ood_energy_mae": 0.7956778564453125,
      "rmd17_mild_ood_force_mae": 0.1304198621364776,
      "rmd17_hard_ood_energy_mae": 0.7945776977539063,
      "rmd17_hard_ood_force_mae": 0.13121199369966052,
      "rmd17_mixed_force_mae": 0.13089514107438735,
      "rmd17_mixed_energy_mae": 0.7950177612304687,
      "rmd17_gap_penalty": 0.006051649867787686,
      "rmd17_Q_dataset": 2.7891460794531704,
      "rmd17_device": "cuda",
      "rmd17_epochs": 8,
      "rmd17_force_trend": "improving",
      "rmd17_energy_trend": "improving",
      "rmd17_best_val_force_mae": 0.13041987771121785,
      "rmd17_best_val_energy_mae": 0.7956788330078125,
      "iso17_metrics_present": true,
      "iso17_history_present": true,
      "iso17_within_energy_mae": 0.615505588644802,
      "iso17_within_force_mae": 0.23030208365456892,
      "iso17_other_energy_mae": 0.7170564152644231,
      "iso17_other_force_mae": 0.2374924047004718,
      "iso17_mixed_force_mae": 0.23461627628211068,
      "iso17_mixed_energy_mae": 0.6764360846165747,
      "iso17_gap_penalty": 0.030647153555648267,
      "iso17_Q_dataset": 3.19258956279737,
      "iso17_device": "cuda",
      "iso17_epochs": 8,
      "iso17_force_trend": "improving",
      "iso17_energy_trend": "improving",
      "iso17_best_val_force_mae": 0.17855258782704672,
      "iso17_best_val_energy_mae": 0.84765625
    },
    {
      "unit": "generation_004/proposal_007",
      "proposal_file": "/home/lmy/.openclaw/workspace/research_runtime/proposals/generation_003_proposal_004_continuation/proposal_007.md",
      "control_replicate": false,
      "run_state": "terminal_success",
      "failure_class": null,
      "launch_count": 1,
      "retry_count": 0,
      "implementation_state": "launch_ready",
      "remote_synced": true,
      "remote_smoke_passed": true,
      "repair_attempts": 0,
      "same_failure_class_repairs": 0,
      "last_failure_class": null,
      "Q_rmd17": 2.643650904041294,
      "Q_iso17": 2.992901620987732,
      "Q_total": 2.765888654972547,
      "rmd17_metrics_present": true,
      "rmd17_history_present": true,
      "rmd17_mild_ood_energy_mae": 2.9046622314453123,
      "rmd17_mild_ood_force_mae": 0.10228787045367062,
      "rmd17_hard_ood_energy_mae": 2.9042823486328126,
      "rmd17_hard_ood_force_mae": 0.10362321079778485,
      "rmd17_mixed_force_mae": 0.10308907466013915,
      "rmd17_mixed_energy_mae": 2.9044343017578127,
      "rmd17_gap_penalty": 0.012953267341894207,
      "rmd17_Q_dataset": 2.643650904041294,
      "rmd17_device": "cuda",
      "rmd17_epochs": 8,
      "rmd17_force_trend": "improving",
      "rmd17_energy_trend": "improving",
      "rmd17_best_val_force_mae": 0.10228787088301033,
      "rmd17_best_val_energy_mae": 2.771561950683594,
      "iso17_metrics_present": true,
      "iso17_history_present": true,
      "iso17_within_energy_mae": 4.733235999381188,
      "iso17_within_force_mae": 0.14789471405715046,
      "iso17_other_energy_mae": 4.754584585336539,
      "iso17_other_force_mae": 0.16518870505862512,
      "iso17_mixed_force_mae": 0.15827110865803526,
      "iso17_mixed_energy_mae": 4.746045150954399,
      "iso17_gap_penalty": 0.10926814848268517,
      "iso17_Q_dataset": 2.992901620987732,
      "iso17_device": "cuda",
      "iso17_epochs": 8,
      "iso17_force_trend": "improving",
      "iso17_energy_trend": "improving",
      "iso17_best_val_force_mae": 0.16258423030376434,
      "iso17_best_val_energy_mae": 0.6845703125
    },
    {
      "unit": "generation_004/proposal_009",
      "proposal_file": "/home/lmy/.openclaw/workspace/research_runtime/proposals/generation_003_proposal_004_continuation/proposal_009.md",
      "control_replicate": false,
      "run_state": "terminal_success",
      "failure_class": null,
      "launch_count": 1,
      "retry_count": 0,
      "implementation_state": "launch_ready",
      "remote_synced": true,
      "remote_smoke_passed": true,
      "repair_attempts": 0,
      "same_failure_class_repairs": 0,
      "last_failure_class": null,
      "Q_rmd17": 2.9469981144853343,
      "Q_iso17": 3.1930018040184973,
      "Q_total": 3.0330994058219414,
      "rmd17_metrics_present": true,
      "rmd17_history_present": true,
      "rmd17_mild_ood_energy_mae": 0.8238478393554688,
      "rmd17_mild_ood_force_mae": 0.10441879377444274,
      "rmd17_hard_ood_energy_mae": 0.8239492797851562,
      "rmd17_hard_ood_force_mae": 0.10505035342252814,
      "rmd17_mixed_force_mae": 0.10479772956329397,
      "rmd17_mixed_energy_mae": 0.8239087036132813,
      "rmd17_gap_penalty": 0.00602646307998428,
      "rmd17_Q_dataset": 2.9469981144853343,
      "rmd17_device": "cuda",
      "rmd17_epochs": 8,
      "rmd17_force_trend": "improving",
      "rmd17_energy_trend": "improving",
      "rmd17_best_val_force_mae": 0.10441878858709243,
      "rmd17_best_val_energy_mae": 0.823847412109375,
      "iso17_metrics_present": true,
      "iso17_history_present": true,
      "iso17_within_energy_mae": 1.4352606745049505,
      "iso17_within_force_mae": 0.17065073818632281,
      "iso17_other_energy_mae": 1.5959761868990385,
      "iso17_other_force_mae": 0.18243517211996593,
      "iso17_mixed_force_mae": 0.1777213985465087,
      "iso17_mixed_energy_mae": 1.5316899819414034,
      "iso17_gap_penalty": 0.06630846949188782,
      "iso17_Q_dataset": 3.1930018040184973,
      "iso17_device": "cuda",
      "iso17_epochs": 8,
      "iso17_force_trend": "improving",
      "iso17_energy_trend": "improving",
      "iso17_best_val_force_mae": 0.16228397687276205,
      "iso17_best_val_energy_mae": 2.6100260416666665
    },
    {
      "unit": "generation_004/proposal_010",
      "proposal_file": "/home/lmy/.openclaw/workspace/research_runtime/proposals/generation_003_proposal_004_continuation/proposal_010.md",
      "control_replicate": false,
      "run_state": "terminal_success",
      "failure_class": null,
      "launch_count": 1,
      "retry_count": 0,
      "implementation_state": "launch_ready",
      "remote_synced": true,
      "remote_smoke_passed": true,
      "repair_attempts": 0,
      "same_failure_class_repairs": 0,
      "last_failure_class": null,
      "Q_rmd17": 1.3983855053348244,
      "Q_iso17": 2.4214479029721154,
      "Q_total": 1.7564573445078762,
      "rmd17_metrics_present": true,
      "rmd17_history_present": true,
      "rmd17_mild_ood_energy_mae": 70.2859429321289,
      "rmd17_mild_ood_force_mae": 0.1873397207027301,
      "rmd17_hard_ood_energy_mae": 70.28322552490235,
      "rmd17_hard_ood_force_mae": 0.18801690035872162,
      "rmd17_mixed_force_mae": 0.18774602849632502,
      "rmd17_mixed_energy_mae": 70.28431248779296,
      "rmd17_gap_penalty": 0.003606892041400276,
      "rmd17_Q_dataset": 1.3983855053348244,
      "rmd17_device": "cuda",
      "rmd17_epochs": 8,
      "rmd17_force_trend": "improving",
      "rmd17_energy_trend": "improving",
      "rmd17_best_val_force_mae": 0.1788369550886564,
      "rmd17_best_val_energy_mae": 6.002201232910156,
      "iso17_metrics_present": true,
      "iso17_history_present": true,
      "iso17_within_energy_mae": 29.370098333075497,
      "iso17_within_force_mae": 0.1791941095918122,
      "iso17_other_energy_mae": 29.509729191706732,
      "iso17_other_force_mae": 0.1901377670925397,
      "iso17_mixed_force_mae": 0.1857603040922487,
      "iso17_mixed_energy_mae": 29.45387684825424,
      "iso17_gap_penalty": 0.058912788467626376,
      "iso17_Q_dataset": 2.4214479029721154,
      "iso17_device": "cuda",
      "iso17_epochs": 8,
      "iso17_force_trend": "improving",
      "iso17_energy_trend": "worsening",
      "iso17_best_val_force_mae": 0.17838659385840097,
      "iso17_best_val_energy_mae": 25.415364583333332
    }
  ],
  "best_control_Q_total": null
}
```

## Diff vs source: model.py
- +        self.scalar_mix_norm = nn.LayerNorm(hidden_dim)
- +        self.vector_residual_scale = nn.Parameter(torch.tensor(0.35))
- +        num_nodes = scalar_state.shape[0]
- +        neighbor_count = torch.zeros(num_nodes, device=scalar_state.device, dtype=scalar_state.dtype)
- +        neighbor_count.index_add_(0, i_idx, torch.ones_like(i_idx, dtype=scalar_state.dtype))
- +        neighbor_scale = neighbor_count.clamp_min(1.0).rsqrt().unsqueeze(-1)
- +        agg_scalar = agg_scalar * neighbor_scale
- +        agg_vector = agg_vector * neighbor_scale.unsqueeze(-1)
- +
- -        new_scalar = self.layer_norm(scalar_state + scalar_gate * delta_scalar)
- +        mixed_scalar = scalar_state + scalar_gate * delta_scalar
- +        new_scalar = self.layer_norm(0.7 * mixed_scalar + 0.3 * self.scalar_mix_norm(scalar_state + agg_scalar))
- -        new_vector = vector_state + 0.5 * delta_vector
- +        residual_scale = 0.15 + 0.35 * torch.sigmoid(self.vector_residual_scale)
- +        new_vector = vector_state + residual_scale * delta_vector

## Diff vs source: train.py
- +        betas=(0.9, float(CONFIG.get("adam_beta2", 0.97))),
- -    energy_weight = float(CONFIG.get("energy_weight", 2.0))
- -    force_weight = float(CONFIG.get("force_weight", 12.0))
- -    grad_clip = float(CONFIG.get("grad_clip", 5.0))
- -    energy_warmup_epochs = max(1, int(CONFIG.get("energy_warmup_epochs", 2)))
- +    energy_weight = float(CONFIG.get("energy_weight", 2.4))
- +    force_weight = float(CONFIG.get("force_weight", 10.0))
- +    grad_clip = float(CONFIG.get("grad_clip", 3.0))
- +    energy_warmup_epochs = max(1, int(CONFIG.get("energy_warmup_epochs", 3)))
- -        epoch_energy_weight = energy_weight * min(1.0, epoch / energy_warmup_epochs)
- -        epoch_force_weight = force_weight
- +        warmup_ratio = min(1.0, epoch / energy_warmup_epochs)
- +        epoch_energy_weight = energy_weight * (0.6 + 0.4 * warmup_ratio)
- +        epoch_force_weight = force_weight * (1.1 - 0.1 * warmup_ratio)

## Frontier tail
- generation_004/proposal_006 | family=None | phase=None | Q_rmd17=2.7891460794531704 | Q_iso17=3.19258956279737 | Q_total=2.9303512986236404 | G_delta=0.06158896513851264 | status=terminal_success
- generation_004/proposal_007 | family=None | phase=None | Q_rmd17=2.643650904041294 | Q_iso17=2.992901620987732 | Q_total=2.765888654972547 | G_delta=-0.10287367851258056 | status=terminal_success
- generation_004/proposal_009 | family=None | phase=None | Q_rmd17=2.9469981144853343 | Q_iso17=3.1930018040184973 | Q_total=3.0330994058219414 | G_delta=0.1643370723368136 | status=terminal_success
- generation_004/proposal_010 | family=None | phase=None | Q_rmd17=1.3983855053348244 | Q_iso17=2.4214479029721154 | Q_total=1.7564573445078762 | G_delta=-1.1123049889772516 | status=terminal_success
- generation_005/proposal_001 | family=None | phase=None | Q_rmd17=1.8565889013647636 | Q_iso17=2.3243181278456317 | Q_total=2.0202941306330673 | G_delta=-1.11296813064564 | status=terminal_success
- generation_005/proposal_002 | family=None | phase=None | Q_rmd17=-1.0089093938969729 | Q_iso17=-0.19179184478015165 | Q_total=-0.7229182517060855 | G_delta=-3.8561805129847926 | status=terminal_success
- generation_005/proposal_003 | family=None | phase=None | Q_rmd17=2.3357376890939596 | Q_iso17=3.1086620556682725 | Q_total=2.606261217394969 | G_delta=-0.5270010438837383 | status=terminal_success
- generation_005/proposal_005 | family=None | phase=None | Q_rmd17=2.613647162193783 | Q_iso17=2.993035293931611 | Q_total=2.7464330083020227 | G_delta=-0.3868292529766846 | status=terminal_success
- generation_005/proposal_006 | family=None | phase=None | Q_rmd17=2.189522058478086 | Q_iso17=2.7493034470410787 | Q_total=2.3854455444751337 | G_delta=-0.7478167168035736 | status=terminal_success
- generation_005/proposal_007 | family=None | phase=None | Q_rmd17=1.2203477119216792 | Q_iso17=2.4803267557895508 | Q_total=1.6613403772754343 | G_delta=-1.471921884003273 | status=terminal_success
- generation_005/proposal_008 | family=None | phase=None | Q_rmd17=2.331278488695947 | Q_iso17=2.8662515100948727 | Q_total=2.518519046185571 | G_delta=-0.6147432150931365 | status=terminal_success
- generation_005/proposal_004 | family=None | phase=None | Q_rmd17=1.792177270947261 | Q_iso17=2.5753946019130107 | Q_total=2.0663033367852734 | G_delta=-1.0669589244934339 | status=terminal_success

## Evidence brief path
- /home/lmy/.openclaw/workspace/research_runtime/knowledge/briefs/evidence_brief_20260419T012900Z_generation006_proposal001_continuation.md

## Proposal writing rule
- proposal decisions must be benchmark-centric, not force-only
- discuss energy, force, gap_penalty, Q fields, train trends, runtime/failure, and control comparison when relevant

## Current model.py
```python
from __future__ import annotations

import math

import torch
from torch import nn


class BalancedInteractionBlock(nn.Module):
    def __init__(self, hidden_dim: int, num_rbf: int):
        super().__init__()
        self.hidden_dim = hidden_dim

        self.edge_mlp = nn.Sequential(
            nn.Linear(num_rbf, hidden_dim),
            nn.SiLU(),
            nn.Linear(hidden_dim, hidden_dim * 4),
        )

        self.src_scalar = nn.Linear(hidden_dim, hidden_dim)
        self.dst_scalar = nn.Linear(hidden_dim, hidden_dim)
        self.src_vector = nn.Linear(hidden_dim, hidden_dim)
        self.self_vector = nn.Linear(hidden_dim, hidden_dim)
        self.agg_vector = nn.Linear(hidden_dim, hidden_dim)

        self.scalar_update = nn.Sequential(
            nn.Linear(hidden_dim * 4, hidden_dim),
            nn.SiLU(),
            nn.Linear(hidden_dim, hidden_dim),
        )
        self.scalar_residual_gate = nn.Sequential(
            nn.Linear(hidden_dim * 2, hidden_dim),
            nn.SiLU(),
            nn.Linear(hidden_dim, hidden_dim),
        )
        self.vector_gate = nn.Sequential(
            nn.Linear(hidden_dim * 2, hidden_dim * 2),
            nn.SiLU(),
            nn.Linear(hidden_dim * 2, hidden_dim * 2),
        )
        self.layer_norm = nn.LayerNorm(hidden_dim)
        self.scalar_mix_norm = nn.LayerNorm(hidden_dim)
        self.vector_residual_scale = nn.Parameter(torch.tensor(0.35))

    def _apply_linear_to_vector(self, linear: nn.Linear, vector: torch.Tensor) -> torch.Tensor:
        return linear(vector.transpose(1, 2)).transpose(1, 2)

    def forward(
        self,
        scalar_state: torch.Tensor,
        vector_state: torch.Tensor,
        i_idx: torch.Tensor,
        j_idx: torch.Tensor,
        unit: torch.Tensor,
        edge_basis: torch.Tensor,
        cutoff_weight: torch.Tensor,
    ) -> tuple[torch.Tensor, torch.Tensor]:
        edge_params = self.edge_mlp(edge_basis)
        scalar_gate, invariant_gate, vector_gate, direction_gate = edge_params.chunk(4, dim=-1)

        scalar_gate = scalar_gate * cutoff_weight.unsqueeze(-1)
        invariant_gate = invariant_gate * cutoff_weight.unsqueeze(-1)
        vector_gate = vector_gate * cutoff_weight.unsqueeze(-1)
        direction_gate = direction_gate * cutoff_weight.unsqueeze(-1)

        src_scalar = self.src_scalar(scalar_state[j_idx])
        dst_scalar = self.dst_scalar(scalar_state[i_idx])
        src_vector = self._apply_linear_to_vector(self.src_vector, vector_state[j_idx])

        directional_invariant = torch.sum(src_vector * unit.unsqueeze(1), dim=-1)
        scalar_message = (src_scalar + dst_scalar) * scalar_gate + directional_invariant * invariant_gate
        vector_message = src_vector * vector_gate.unsqueeze(-1) + direction_gate.unsqueeze(-1) * unit.unsqueeze(1)

        agg_scalar = torch.zeros_like(scalar_state)
        agg_vector = torch.zeros_like(vector_state)
        agg_scalar.index_add_(0, i_idx, scalar_message)
        agg_vector.index_add_(0, i_idx, vector_message)

        num_nodes = scalar_state.shape[0]
        neighbor_count = torch.zeros(num_nodes, device=scalar_state.device, dtype=scalar_state.dtype)
        neighbor_count.index_add_(0, i_idx, torch.ones_like(i_idx, dtype=scalar_state.dtype))
        neighbor_scale = neighbor_count.clamp_min(1.0).rsqrt().unsqueeze(-1)
        agg_scalar = agg_scalar * neighbor_scale
        agg_vector = agg_vector * neighbor_scale.unsqueeze(-1)

        self_vector = self._apply_linear_to_vector(self.self_vector, vector_state)
        mixed_agg_vector = self._apply_linear_to_vector(self.agg_vector, agg_vector)

        agg_norm = torch.linalg.norm(agg_vector, dim=-1)
        vector_alignment = torch.sum(self_vector * mixed_agg_vector, dim=-1)
        scalar_input = torch.cat([scalar_state, agg_scalar, agg_norm, vector_alignment], dim=-1)
        delta_scalar = self.scalar_update(scalar_input)
        scalar_gate = torch.sigmoid(self.scalar_residual_gate(torch.cat([scalar_state, agg_scalar], dim=-1)))
        mixed_scalar = scalar_state + scalar_gate * delta_scalar
        new_scalar = self.layer_norm(0.7 * mixed_scalar + 0.3 * self.scalar_mix_norm(scalar_state + agg_scalar))

        vector_mix = torch.tanh(self.vector_gate(torch.cat([new_scalar, agg_scalar], dim=-1)))
        self_mix, agg_mix = vector_mix.chunk(2, dim=-1)
        delta_vector = self_mix.unsqueeze(-1) * self_vector + agg_mix.unsqueeze(-1) * mixed_agg_vector
        residual_scale = 0.15 + 0.35 * torch.sigmoid(self.vector_residual_scale)
        new_vector = vector_state + residual_scale * delta_vector
        return new_scalar, new_vector


class EvolutionMLIP(nn.Module):
    def __init__(
        self,
        max_atomic_number: int = 100,
        hidden_dim: int = 96,
        num_rbf: int = 32,
        cutoff: float = 5.0,
        num_interactions: int = 2,
    ):
        super().__init__()
        self.hidden_dim = hidden_dim
        self.num_rbf = num_rbf
        self.cutoff = cutoff

        self.embedding = nn.Embedding(max_atomic_number + 1, hidden_dim)
        self.atomref = nn.Embedding(max_atomic_number + 1, 1)

        centers = torch.linspace(0.0, cutoff, num_rbf)
        widths = torch.full((num_rbf,), (cutoff / max(num_rbf - 1, 1)) + 1e-6)
        self.register_buffer("rbf_centers", centers)
        self.register_buffer("rbf_widths", widths)

        self.interactions = nn.ModuleList(
            [BalancedInteractionBlock(hidden_dim=hidden_dim, num_rbf=num_rbf) for _ in range(num_interactions)]
        )
        self.readout = nn.Sequential(
            nn.Linear(hidden_dim * 2, hidden_dim),
            nn.SiLU(),
            nn.Linear(hidden_dim, hidden_dim),
            nn.SiLU(),
            nn.Linear(hidden_dim, 1),
        )

    def _rbf(self, distances: torch.Tensor) -> torch.Tensor:
        diff = distances.unsqueeze(-1) - self.rbf_centers
        return torch.exp(-0.5 * (diff / self.rbf_widths) ** 2)

    def _cutoff_weight(self, distances: torch.Tensor) -> torch.Tensor:
        scaled = distances / max(self.cutoff, 1e-6)
        envelope = 0.5 * (torch.cos(math.pi * scaled.clamp(max=1.0)) + 1.0)
        return envelope * (distances < self.cutoff).to(distances.dtype)

    def _build_neighbor_list(self, positions: torch.Tensor) -> tuple[torch.Tensor, torch.Tensor, torch.Tensor]:
        rij = positions[:, None, :] - positions[None, :, :]
        dij = torch.linalg.norm(rij, dim=-1)

        n_atoms = positions.shape[0]
        eye = torch.eye(n_atoms, device=positions.device, dtype=torch.bool)
        mask = (~eye) & (dij < self.cutoff)
        i_idx, j_idx = torch.where(mask)
        return i_idx, j_idx, rij[i_idx, j_idx]

    def forward_energy(self, numbers: torch.Tensor, positions: torch.Tensor) -> torch.Tensor:
        scalar_state = self.embedding(numbers)
        vector_state = torch.zeros(numbers.shape[0], self.hidden_dim, 3, device=positions.device, dtype=positions.dtype)
        atomref = self.atomref(numbers).sum()

        i_idx, j_idx, rij = self._build_neighbor_list(positions)
        if i_idx.numel() == 0:
            return atomref

        dij = torch.linalg.norm(rij, dim=-1)
        unit = rij / dij.unsqueeze(-1).clamp_min(1e-9)
        rbf = self._rbf(dij)
        cutoff_weight = self._cutoff_weight(dij)
        edge_basis = rbf * cutoff_weight.unsqueeze(-1)

        for interaction in self.interactions:
            scalar_state, vector_state = interaction(
                scalar_state=scalar_state,
                vector_state=vector_state,
                i_idx=i_idx,
                j_idx=j_idx,
                unit=unit,
                edge_basis=edge_basis,
                cutoff_weight=cutoff_weight,
            )

        vector_norm = torch.linalg.norm(vector_state, dim=-1)
        per_atom_energy = self.readout(torch.cat([scalar_state, vector_norm], dim=-1)).squeeze(-1)
        return atomref + per_atom_energy.sum()

    def forward(self, batch: dict) -> tuple[torch.Tensor, torch.Tensor]:
        positions = batch["positions"].clone().detach().requires_grad_(True)
        energy = self.forward_energy(batch["numbers"], positions)
        forces = -torch.autograd.grad(energy, positions, create_graph=True)[0]
        return energy, forces

```

## Current train.py
```python
from __future__ import annotations

import json
from pathlib import Path

import torch

from .dataloader import make_dataloader
from .model import EvolutionMLIP

ROOT = Path(__file__).resolve().parents[1]
CONFIG = json.loads((ROOT / "config.json").read_text(encoding="utf-8"))


def mae(values):
    vals = [abs(float(v)) for v in values]
    return sum(vals) / max(1, len(vals))


def energy_mae(pred, target):
    return abs(float(pred) - float(target))


def force_mae(pred, target):
    return float(torch.mean(torch.abs(pred - target)).detach().cpu().item())


def get_cuda_device() -> torch.device:
    if not torch.cuda.is_available():
        raise SystemExit("CUDA is required for benchmark runs, but no CUDA device is available.")
    return torch.device("cuda")


def sample_to_device(sample: dict, device: torch.device) -> dict:
    return {
        "numbers": sample["numbers"].to(device),
        "positions": sample["positions"].to(device),
        "energy": sample["energy"].to(device),
        "forces": sample["forces"].to(device),
    }


def run_epoch(
    model,
    loader,
    optimizer=None,
    energy_weight: float = 1.0,
    force_weight: float = 20.0,
    device: torch.device | None = None,
    grad_clip: float | None = None,
):
    if device is None:
        device = get_cuda_device()
    training = optimizer is not None
    energy_errors = []
    force_errors = []
    losses = []

    for batch in loader:
        batch_loss = 0.0
        batch_size = len(batch)
        if training:
            optimizer.zero_grad(set_to_none=True)

        for sample in batch:
            sample = sample_to_device(sample, device)
            pred_energy, pred_forces = model(sample)
            loss_energy = torch.abs(pred_energy - sample["energy"])
            loss_force = torch.mean(torch.abs(pred_forces - sample["forces"]))
            loss = energy_weight * loss_energy + force_weight * loss_force
            batch_loss = batch_loss + loss

            energy_errors.append(energy_mae(pred_energy.detach(), sample["energy"]))
            force_errors.append(force_mae(pred_forces.detach(), sample["forces"]))

        batch_loss = batch_loss / max(batch_size, 1)

        if training:
            batch_loss.backward()
            if grad_clip is not None and grad_clip > 0:
                torch.nn.utils.clip_grad_norm_(model.parameters(), grad_clip)
            optimizer.step()

        losses.append(float(batch_loss.detach().cpu().item()))

    return {
        "loss": mae(losses),
        "energy_mae": mae(energy_errors),
        "force_mae": mae(force_errors),
    }


def train(
    *,
    dataset: str,
    train_dir: str | Path,
    val_dir: str | Path,
    output_dir: str | Path,
    epochs: int = 8,
    lr: float | None = None,
    batch_size: int = 8,
    max_samples: int | None = None,
):
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    train_loader = make_dataloader(dataset, train_dir, batch_size=batch_size, shuffle=True, max_samples=max_samples)
    val_loader = make_dataloader(dataset, val_dir, batch_size=batch_size, shuffle=False, max_samples=max_samples)

    device = get_cuda_device()
    model = EvolutionMLIP(
        hidden_dim=int(CONFIG.get("hidden_dim", 96)),
        num_rbf=int(CONFIG.get("num_rbf", 32)),
        cutoff=float(CONFIG.get("cutoff", 5.0)),
    ).to(device)

    learning_rate = float(lr if lr is not None else CONFIG.get("learning_rate", 1e-3))
    optimizer = torch.optim.AdamW(
        model.parameters(),
        lr=learning_rate,
        weight_decay=float(CONFIG.get("weight_decay", 1e-5)),
        betas=(0.9, float(CONFIG.get("adam_beta2", 0.97))),
    )
    scheduler = torch.optim.lr_scheduler.CosineAnnealingLR(optimizer, T_max=max(epochs, 1))

    energy_weight = float(CONFIG.get("energy_weight", 2.4))
    force_weight = float(CONFIG.get("force_weight", 10.0))
    grad_clip = float(CONFIG.get("grad_clip", 3.0))
    energy_warmup_epochs = max(1, int(CONFIG.get("energy_warmup_epochs", 3)))

    history = []
    for epoch in range(1, epochs + 1):
        warmup_ratio = min(1.0, epoch / energy_warmup_epochs)
        epoch_energy_weight = energy_weight * (0.6 + 0.4 * warmup_ratio)
        epoch_force_weight = force_weight * (1.1 - 0.1 * warmup_ratio)

        model.train()
        train_metrics = run_epoch(
            model,
            train_loader,
            optimizer=optimizer,
            energy_weight=epoch_energy_weight,
            force_weight=epoch_force_weight,
            device=device,
            grad_clip=grad_clip,
        )

        model.eval()
        with torch.enable_grad():
            val_metrics = run_epoch(
                model,
                val_loader,
                optimizer=None,
                energy_weight=epoch_energy_weight,
                force_weight=epoch_force_weight,
                device=device,
                grad_clip=None,
            )

        scheduler.step()

        row = {
            "epoch": epoch,
            "train": train_metrics,
            "val": val_metrics,
            "device": str(device),
            "learning_rate": float(optimizer.param_groups[0]["lr"]),
            "energy_weight": epoch_energy_weight,
            "force_weight": epoch_force_weight,
            "grad_clip": grad_clip,
        }
        history.append(row)

    torch.save(model.state_dict(), output_dir / "model.pt")
    (output_dir / "train_history.json").write_text(json.dumps(history, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    return {
        "model_path": str(output_dir / "model.pt"),
        "history_path": str(output_dir / "train_history.json"),
        "last_epoch": history[-1],
    }

```
