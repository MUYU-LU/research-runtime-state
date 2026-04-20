# Proposal 004: Narrow ACE-like invariant summary jump

- family: local_invariant_manybody_hybrid
- phase: 5
- jump_type: jump
- budget_class: medium
- expected_capability_gain: high


## Hypothesis
A small ACE-inspired invariant many-body summary, inserted as a narrow helper rather than a framework transplant, can add useful local angular/body-order information that the current source lacks while staying within a bounded implementation envelope.

## Benchmark rationale
The source already wins across both datasets, so any jump must justify itself by targeting a plausible missing capability. The evidence brief points to exactly one such gap: stronger invariant many-body summarization than `vector_norm` and alignment alone. This is benchmark-relevant because ISO17 may benefit from richer local discrimination, but the design must preserve the source's clean rMD17 energy and stable runtime.

## Proposed change
- keep the existing local equivariant trunk and force-from-energy contract
- add one low-width invariant summary path based on local neighbor geometry
- feed that summary into scalar updates or a late pre-readout summary
- do not introduce irreps bookkeeping, tensor products, or full symmetric contraction machinery

## Why this is worth trying
This is the most evidence-supported jump that still fits the codebase. It tests a real capability extension, not just another calibration tweak.

## Main risks
- even a narrow many-body helper may destabilize energy calibration
- bounded approximations may be too weak to matter if they do not capture enough structure

## Best-case signal
ISO17 improves without sacrificing rMD17 energy or gap behavior, producing a clear `Q_total` gain over the source.
