# Proposal Context for base_unit

## Source unit
- Unit: `base_unit`
- Path: `/home/lmy/.openclaw/workspace/research_runtime/base_unit`
- Current phase estimate: Phase 1 to early Phase 2, relative-geometry pair model
- Fixed contracts to preserve:
  - benchmark data and splits
  - eval semantics for rMD17 and ISO17
  - benchmark metric field names
  - runnable unit entrypoint contract

## Verified source-unit profile
- Present:
  - atom embedding
  - pairwise distance Gaussian RBF features
  - hard-cutoff local pair scoring
  - atomref baseline
  - forces via autograd
  - benchmark-aligned train and eval plumbing for rMD17 and ISO17
- Missing:
  - neighbor message passing
  - angular or triplet structure
  - equivariance
  - periodic or cell handling
  - long-range head
  - uncertainty or adaptation mechanisms

## Concrete source details
- `model/model.py` embeds atom types, computes all pair distances inside a 5.0 cutoff, forms `[emb_i, emb_j, rbf(d_ij)]`, runs an MLP, and sums pair energies.
- `model/train.py` uses the existing simple energy-plus-force objective with `energy_weight=1.0` and `force_weight=20.0`.
- `model/eval.py` is tightly aligned to the current benchmark contract and writes anchored benchmark metrics for rMD17 and ISO17.
- `outputs/summary.json` shows benchmark outputs exist, but `Q_dataset` stayed null, so milestone append was deferred. Proposal writing should not change evaluation semantics to work around this.

## Fresh evidence summary
Evidence artifacts used:
- `/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/evidence_run_20260416T090833Z.json`
- `/home/lmy/.openclaw/workspace/research_runtime/knowledge/briefs/evidence_brief_20260416T090833Z.md`

### Strong exploit signal
The strongest justified exploit direction is to improve local structure modeling, specifically:
1. lightweight scalar neighbor message passing over cutoff neighbors
2. angular or triplet structure on top of distance features
3. richer local interaction parameterization rather than shallow schedule or loss tuning

Why this dominates:
- verified NequIP and MACE paper plus repo evidence point to interaction layers as the main structural gain over pair-only models
- verified MACE and CACE evidence point to body-order and directional structure as the most obvious missing inductive bias
- the current benchmark gap is better explained by missing local geometry structure than by missing long-range or adaptation machinery

### Strong jump signal
The strongest justified jump direction is:
1. a minimal local equivariant model in the NequIP or MACE family
2. a CACE-style higher-body bridge as a less irreps-heavy step toward richer geometry

### Side-branch status
- LES-style long-range augmentation is evidence-backed, but lower priority for the current benchmark and source-unit gap
- TAIP-style test-time adaptation is benchmark-relevant in principle, but it is a high-risk fit mismatch for the current minimalist codebase and should remain a side branch only

## Constraints for selection and later materialization
- Do not change benchmark formulas, split semantics, metric field names, or entrypoint contract.
- Proposal implementations should preserve scalar energy prediction with force derivation from autograd unless a selected jump explicitly changes internal representation while keeping external contract unchanged.
- Exploit proposals should emphasize local neighbor aggregation and angular or triplet structure, not mere optimizer schedules or cosmetic depth tweaks.
- Jump proposals should include at least one minimal equivariant local model and may include one CACE-style higher-body bridge.
- LES and TAIP branches may appear only as higher-risk side proposals with clear justification.
- Control proposal should be an exact replicate of the source unit.
- Backward-simplify proposal should reduce complexity or variance risk without changing external evaluation behavior.

## Proposal-set intent for this round
Write a balanced set of 10 proposals that:
- covers exploit, jump, control, backward-simplify, and wildcard requirements from round policy
- concentrates exploit mass on lightweight message passing and angular structure
- uses jump slots to probe the next phase rather than overfitting the current pair-only family
- keeps at least one high-risk but bounded side branch for optional exploration later
