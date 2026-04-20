# Proposal 006: Single-statistic geometric moment jump

- family: local_invariant_manybody_hybrid
- phase: 5
- jump_type: jump
- budget_class: medium
- expected_capability_gain: medium

## Hypothesis
A single geometric moment summary, narrower than prior ACE-like helpers and derived only from local neighbor distances and directions, may add the smallest useful many-body cue still consistent with the evidence.

## Benchmark rationale
The parent dominates every completed generation_008 child, but the evidence brief still permits one bounded jump diagnostic. The only viable version is a one-statistic helper that is clearly smaller than prior late-summary attempts and evaluated against full `Q_total`, energy MAE, force MAE, gap penalty, and trend behavior.

## Proposed change
- keep the current local graph and interaction stack unchanged
- compute one invariant geometric moment from existing local neighbor features
- feed it into a single late scalar correction pathway with tight width and bounded gain
- avoid readout-only retries, nonlocal branches, and framework rewrites

## Why this is worth trying
It preserves jump diversity for round policy while honoring the very narrow implementation-fit window.

## Main risks
- may simply repeat the negative jump evidence in a smaller form
- can improve one dataset while still lowering `Q_total`

## Best-case signal
Modest ISO17 energy improvement with little rMD17 deterioration, supporting a tightly bounded many-body helper.
