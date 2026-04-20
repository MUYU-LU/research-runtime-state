# Proposal 006: Late invariant summary jump before readout

- family: local_equivariant_readout_hybrid
- phase: 5
- jump_type: jump
- budget_class: medium
- expected_capability_gain: medium


## Hypothesis
The main bottleneck may sit not in message construction but in the final compression to `torch.cat([scalar_state, vector_norm])`. A bounded jump is to inject one late invariant summary head that preserves more directional information before atomwise energy prediction.

## Benchmark rationale
The evidence brief warns that readout-only retries are weakly supported, so this should not be a readout-only rewrite. Instead, it is a late-summary jump paired with the existing winning trunk. The goal is benchmark improvement through better energy calibration and cross-dataset generalization, not raw force gains alone.

## Proposed change
- preserve the current interaction stack
- keep force-from-energy and local graph construction unchanged
- extend the pre-readout feature summary with one narrow invariant projection derived from vector state
- avoid large head expansion or training-only compensation

## Why this is worth trying
It isolates one specific hypothesis about the observed bottleneck: that the current model learns useful directional structure but discards too much of it at the final atomwise energy map.

## Main risks
- prior evidence suggests head-only changes may be too weak
- extra late features may disturb the source's strong rMD17 energy calibration

## Best-case signal
Meaningful gain in ISO17 or `Q_total` with minimal runtime risk, clarifying whether late compression is the limiting factor.
