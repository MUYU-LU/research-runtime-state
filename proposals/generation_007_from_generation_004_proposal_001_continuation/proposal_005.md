# Proposal 005: Dual-stage recombination jump inside the interaction block

- family: balanced_local_equivariant
- phase: 5
- jump_type: jump
- budget_class: medium
- expected_capability_gain: medium_high


## Hypothesis
The source may still underuse vector-derived invariants because it performs a single scalar update from aggregated statistics. A bounded jump is to add a second lightweight recombination stage inside the same block, allowing scalar and vector streams to interact twice before readout.

## Benchmark rationale
This is a phase-5 style jump in expressivity, but still local and benchmark-safe. It is justified only because generation_006 variants failed to improve the anchor, suggesting the next step may require more than one extra summary statistic while still avoiding a rewrite-heavy irreps stack.

## Proposed change
- preserve the current neighbor builder, basis, cutoff, and energy-readout contract
- keep the overall block family
- introduce a second compact invariant/equivariant mixing step per block
- cap width and residual magnitude so the source behavior remains a fallback regime

## Why this is worth trying
It probes whether the missing gain is due to insufficient internal interaction depth rather than missing entirely new physics. That makes it a useful jump between tiny exploits and ACE-like many-body additions.

## Main risks
- extra in-block depth may overfit or destabilize energy
- more mixing could improve one dataset while worsening the other, lowering `Q_total`

## Best-case signal
Simultaneous small improvements in force and energy on ISO17 with flat rMD17 energy, indicating the source was interaction-depth limited.
