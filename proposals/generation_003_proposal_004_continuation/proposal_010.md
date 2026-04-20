# Proposal: Phase-5 Higher-Order Equivariant Bridge from Proposal_004

- family: higher_order_local_equivariant
- phase: 5
- jump_type: jump
- budget_class: medium_high
- expected_capability_gain: high
- evidence_mode: balanced

## Summary
Create a phase-5 jump from `generation_003/proposal_004` by preserving its strong local equivariant trunk but extending it with a bounded higher-order equivariant interaction bridge, testing whether explicit richer angular coupling can unlock further benchmark gains beyond the current phase-4 frontier.

## Motivation
`proposal_004` is already strong enough that further phase-4-only tweaks may face diminishing returns. A disciplined jump should therefore probe a higher-order equivariant mechanism while staying anchored to the winning local design and keeping the benchmark contract intact.

## Proposed change
- preserve the source unit's local neighborhood graph, cutoff logic, scalar total-energy contract, atomref baseline, and force-from-autograd path
- retain the existing phase-4 trunk for early representation building, then add a bounded higher-order equivariant refinement block late in the interaction stack
- keep the higher-order block shallow, with constrained channel counts and residual gating so this remains a controlled phase jump rather than an unbounded architecture explosion
- expose richer angular or tensor-order coupling only inside the late refinement path, followed by a return to the same scalar energy readout contract
- keep training stabilization conservative, including clipped gradients and scheduler settings close to the source unless implementation evidence requires a minor bounded adjustment

## Why this is a fit now
- satisfies the need for a stronger forward jump beyond the current best phase-4 architecture
- tests whether the frontier is limited more by representation order than by local optimization details
- remains scientifically interpretable because the source trunk is retained and the phase-5 addition is isolated to a bounded refinement stage

## Risks
- higher-order equivariant features may add implementation and optimization fragility relative to simpler phase-4 continuations
- extra tensor coupling may increase cost without delivering proportional benchmark improvements
- if the late refinement is too shallow, the jump may be too weak to reveal whether phase-5 structure truly helps

## Selection notes
This is the highest-upside jump in the set and should be considered alongside at least one lower-risk exploit and the source-matched control so later review can distinguish true phase-jump gains from ordinary continuation variance.
