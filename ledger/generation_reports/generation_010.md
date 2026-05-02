# generation_010 outcome report

- source_unit: `generation_004/proposal_001`
- parent_Q_total: `3.1332622612787073`
- margin: `0.03`
- did_any_child_beat_parent: `False`

## Best child

```json
{
  "unit": "generation_010/proposal_007",
  "Q_rmd17": 2.644823681825324,
  "Q_iso17": 3.016007265905866,
  "Q_total": 2.774737936253514,
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
| `generation_010/proposal_001` | benchmark_tradeoff | terminal_success | 2.3220258612820484 | -0.811236399996659 | model/model.py +13/-1 | some component metrics improved but other tracked metrics regressed strongly |
| `generation_010/proposal_002` | benchmark_tradeoff | terminal_success | 2.6699740329453236 | -0.4632882283333837 | model/model.py +10/-1 | some component metrics improved but other tracked metrics regressed strongly |
| `generation_010/proposal_003` | benchmark_tradeoff | terminal_success | 2.3558059481668483 | -0.777456313111859 | model/model.py +12/-1 | some component metrics improved but other tracked metrics regressed strongly |
| `generation_010/proposal_004` | benchmark_tradeoff | terminal_success | 2.400668731518487 | -0.7325935297602202 | model/model.py +18/-1 | some component metrics improved but other tracked metrics regressed strongly |
| `generation_010/proposal_005` | benchmark_tradeoff | terminal_success | 2.556444137286748 | -0.5768181239919592 | model/model.py +20/-1 | some component metrics improved but other tracked metrics regressed strongly |
| `generation_010/proposal_007` | benchmark_tradeoff | terminal_success | 2.774737936253514 | -0.3585243250251935 | model/model.py +1/-2 | some component metrics improved but other tracked metrics regressed strongly |
| `generation_010/proposal_008` | benchmark_tradeoff | terminal_success | 2.3221568915682442 | -0.8111053697104631 | no tracked code diff | some component metrics improved but other tracked metrics regressed strongly |
| `generation_010/proposal_010` | benchmark_tradeoff | terminal_success | 2.547616856416541 | -0.5856454048621664 | model/model.py +18/-1 | some component metrics improved but other tracked metrics regressed strongly |
