# generation_009 outcome report

- source_unit: `generation_004/proposal_001`
- parent_Q_total: `3.1332622612787073`
- margin: `0.03`
- did_any_child_beat_parent: `False`

## Best child

```json
{
  "unit": "generation_009/proposal_010",
  "Q_rmd17": 2.629111489463682,
  "Q_iso17": 3.0439324928229574,
  "Q_total": 2.774298840639428,
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
| `generation_009/proposal_001` | benchmark_tradeoff | terminal_success | 2.37671927732044 | -0.7565429839582674 | model/model.py +4/-1 | some component metrics improved but other tracked metrics regressed strongly |
| `generation_009/proposal_002` | benchmark_tradeoff | terminal_success | 2.4623493714129756 | -0.6709128898657317 | model/model.py +4/-1 | some component metrics improved but other tracked metrics regressed strongly |
| `generation_009/proposal_003` | benchmark_tradeoff | terminal_success | 2.2471718985708984 | -0.8860903627078089 | model/model.py +2/-1 | some component metrics improved but other tracked metrics regressed strongly |
| `generation_009/proposal_004` | benchmark_tradeoff | terminal_success | 2.3496327903439083 | -0.7836294709347991 | model/model.py +67/-0 | some component metrics improved but other tracked metrics regressed strongly |
| `generation_009/proposal_005` | benchmark_tradeoff | terminal_success | 2.3287713315881775 | -0.8044909296905298 | model/model.py +13/-1 | some component metrics improved but other tracked metrics regressed strongly |
| `generation_009/proposal_007` | benchmark_tradeoff | terminal_success | 2.6828924847245927 | -0.4503697765541146 | model/model.py +1/-2 | some component metrics improved but other tracked metrics regressed strongly |
| `generation_009/proposal_008` | benchmark_tradeoff | terminal_success | 2.609203153936184 | -0.5240591073425231 | no tracked code diff | some component metrics improved but other tracked metrics regressed strongly |
| `generation_009/proposal_010` | benchmark_tradeoff | terminal_success | 2.774298840639428 | -0.3589634206392791 | model/model.py +14/-3 | some component metrics improved but other tracked metrics regressed strongly |
