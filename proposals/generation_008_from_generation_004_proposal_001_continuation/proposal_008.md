# Proposal 008: Exact source-matched control replicate

- family: balanced_local_equivariant
- phase: 4
- jump_type: control
- budget_class: small
- expected_capability_gain: none

## Hypothesis
An exact control replicate is necessary because generation_007's control-like result was weak, and the next round needs a clean anchor to separate real gains from variance or imperfect source fidelity.

## Benchmark rationale
The continuation source remains the best completed benchmark unit, but control interpretation is noisy. A true control branch improves attribution for any claimed gain in `Q_rmd17`, `Q_iso17`, `Q_total`, gap behavior, or training trend stability.

## Proposed change
- replicate the source architecture and training regime with no intended proposal-specific change
- preserve all current local, energy-first, and autograd-force semantics
- allow only minimal materialization paperwork later

## Why this is worth trying
It fulfills the required control slot and makes the round's exploit and jump results easier to trust.

## Main risks
- no new capability by design
- may again underperform due to variance, which is informative but not frontier-advancing

## Best-case signal
A faithful benchmark reference that sharpens round-level attribution of small improvements.
