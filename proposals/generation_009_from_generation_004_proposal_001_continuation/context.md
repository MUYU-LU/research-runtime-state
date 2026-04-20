# Proposal context for generation_004/proposal_001

## Current unit
- unit: generation_004/proposal_001
- source unit: generation_003/proposal_004

## Active evidence
- path: /home/lmy/.openclaw/workspace/research_runtime/knowledge/briefs/evidence_brief_20260420T0613Z_generation009_continuation_generation004_proposal001.md
- source unit: generation_004/proposal_001
- mode: balanced

```markdown
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
- generation_007/proposal_005 | family=None | phase=None | Q_rmd17=1.4897931255458434 | Q_iso17=2.7851130183693558 | Q_total=1.9431550880340727 | G_delta=-1.1901071732446347 | status=terminal_success
- generation_007/proposal_006 | family=None | phase=None | Q_rmd17=2.5588683862168615 | Q_iso17=2.8867518904216536 | Q_total=2.6736276126885388 | G_delta=-0.45963464859016856 | status=terminal_success
- generation_007/proposal_008 | family=None | phase=None | Q_rmd17=2.201867102394039 | Q_iso17=2.529855613775236 | Q_total=2.316663081377458 | G_delta=-0.8165991799012495 | status=terminal_success
- generation_007/proposal_009 | family=None | phase=None | Q_rmd17=0.879962316300981 | Q_iso17=0.9988255043781936 | Q_total=0.9215644321280054 | G_delta=-2.211697829150702 | status=terminal_success
- generation_008/proposal_007 | family=None | phase=None | Q_rmd17=2.6554765181411053 | Q_iso17=2.5919548010280273 | Q_total=2.6332439171515283 | G_delta=-0.500018344127179 | status=terminal_success
- generation_008/proposal_001 | family=None | phase=None | Q_rmd17=2.2988201398514767 | Q_iso17=2.618825740494488 | Q_total=2.4108221000765306 | G_delta=-0.7224401612021767 | status=terminal_success
- generation_008/proposal_002 | family=None | phase=None | Q_rmd17=2.085943090522952 | Q_iso17=2.724113013045587 | Q_total=2.309302563405874 | G_delta=-0.8239596978728332 | status=terminal_success
- generation_008/proposal_004 | family=None | phase=None | Q_rmd17=2.358661314499094 | Q_iso17=2.8739118832176858 | Q_total=2.538999013550601 | G_delta=-0.5942632477281062 | status=terminal_success
- generation_008/proposal_005 | family=None | phase=None | Q_rmd17=2.2704311826888186 | Q_iso17=2.7547390084878676 | Q_total=2.4399389217184857 | G_delta=-0.6933233395602216 | status=terminal_success
- generation_008/proposal_006 | family=None | phase=None | Q_rmd17=2.246345882358951 | Q_iso17=2.942446151607035 | Q_total=2.4899809765957803 | G_delta=-0.643281284682927 | status=terminal_success
- generation_008/proposal_008 | family=None | phase=None | Q_rmd17=2.243605445735774 | Q_iso17=3.0633537781471505 | Q_total=2.5305173620797556 | G_delta=-0.6027448991989517 | status=terminal_success
- generation_008/proposal_010 | family=None | phase=None | Q_rmd17=1.5743738781027123 | Q_iso17=2.8802498903695155 | Q_total=2.031430482396093 | G_delta=-1.1018317788826142 | status=terminal_success

## Evidence brief path
- /home/lmy/.openclaw/workspace/research_runtime/knowledge/briefs/evidence_brief_20260420T0613Z_generation009_continuation_generation004_proposal001.md

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
