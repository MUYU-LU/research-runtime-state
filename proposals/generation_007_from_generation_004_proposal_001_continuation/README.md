# generation_007 proposals for generation_004/proposal_001 continuation

This directory contains exactly 10 benchmark-centric proposals for continuing `generation_004/proposal_001`.

## Source anchor
- Source unit: `generation_004/proposal_001`
- Parent source of anchor: `generation_003/proposal_004`
- Evidence brief: `research_runtime/knowledge/briefs/evidence_brief_20260419T1957_generation007_proposal001_continuation.md`
- Evidence mode: `balanced`

## Benchmark anchor
- Source `Q_rmd17 = 3.0291`
- Source `Q_iso17 = 3.3267`
- Source `Q_total = 3.1333`
- `G_delta = +0.2645` vs parent source
- Runtime was reliable: terminal success, 1 launch, 0 retries, 0 repairs, smoke passed
- All completed `generation_006` children underperformed the source, including the best control-like replicate at `Q_total = 2.6867`

## Proposal mix
The set is intentionally constructed so later selection constraints remain satisfiable:
- Exploit: proposals 001, 002, 003
- Jump: proposals 004, 005, 006
- Backward-simplify: proposal 007
- Control: proposal 008
- Wildcard: proposals 009, 010

## Design stance
These proposals stay benchmark-centric rather than force-only. Each proposal reasons about energy, force, gap behavior, training stability, and runtime reliability, with emphasis on preserving the source unit's validated local force-from-energy contract while probing bounded improvements.

## Validator-facing metadata
Each `proposal_00X.md` file now exposes the required validator-readable metadata as leading markdown bullets:
- `family`
- `phase`
- `jump_type`
- `budget_class`
- `expected_capability_gain`
