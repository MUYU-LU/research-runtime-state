# generation_007 outcome report

- source_unit: `generation_004/proposal_001`
- parent_Q_total: `3.1332622612787073`
- margin: `0.03`
- did_any_child_beat_parent: `False`

## Best child

```json
{
  "unit": "generation_007/proposal_004",
  "Q_rmd17": 2.7536850677446942,
  "Q_iso17": 2.730948435297518,
  "Q_total": 2.7457272463881828,
  "outcome_class": "benchmark_tradeoff"
}
```

## Outcome counts

```json
{
  "benchmark_tradeoff": 8
}
```

## Lessons

- No child beat parent generation_004/proposal_001; keep parent unless a reviewed override is chosen.

## Units

| unit | outcome_class | run_state | Q_total | delta_Q_vs_parent | code_delta | notes |
|---|---|---|---:|---:|---|---|
| `generation_007/proposal_001` | benchmark_tradeoff | terminal_success | 2.6652029548619685 | -0.4680593064167389 | model/model.py +26/-1 | some component metrics improved but other tracked metrics regressed strongly |
| `generation_007/proposal_002` | benchmark_tradeoff | terminal_success | 2.456319733079132 | -0.6769425281995751 | model/model.py +29/-5 | some component metrics improved but other tracked metrics regressed strongly |
| `generation_007/proposal_004` | benchmark_tradeoff | terminal_success | 2.7457272463881828 | -0.38753501489052455 | model/model.py +49/-2 | some component metrics improved but other tracked metrics regressed strongly |
| `generation_007/proposal_005` | benchmark_tradeoff | terminal_success | 1.9431550880340727 | -1.1901071732446347 | model/model.py +35/-2; model/train.py +6/-3 | some component metrics improved but other tracked metrics regressed strongly |
| `generation_007/proposal_006` | benchmark_tradeoff | terminal_success | 2.6736276126885388 | -0.45963464859016856 | model/model.py +36/-2 | some component metrics improved but other tracked metrics regressed strongly |
| `generation_007/proposal_007` | benchmark_tradeoff | terminal_success | 2.061310040839651 | -1.0719522204390564 | model/model.py +3/-9 | some component metrics improved but other tracked metrics regressed strongly |
| `generation_007/proposal_008` | benchmark_tradeoff | terminal_success | 2.316663081377458 | -0.8165991799012495 | no tracked code diff | some component metrics improved but other tracked metrics regressed strongly |
| `generation_007/proposal_009` | benchmark_tradeoff | terminal_success | 0.9215644321280054 | -2.211697829150702 | model/train.py +134/-1 | some component metrics improved but other tracked metrics regressed strongly |
