# generation_006 outcome report

- source_unit: `generation_004/proposal_001`
- parent_Q_total: `3.1332622612787073`
- margin: `0.03`
- did_any_child_beat_parent: `False`

## Best child

```json
{
  "unit": "generation_006/proposal_008",
  "Q_rmd17": 2.5163806336477292,
  "Q_iso17": 3.0028870650654294,
  "Q_total": 2.686657884643924,
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
| `generation_006/proposal_001` | benchmark_tradeoff | terminal_success | 2.56796905495266 | -0.5652932063260474 | model/model.py +18/-4 | some component metrics improved but other tracked metrics regressed strongly |
| `generation_006/proposal_002` | benchmark_tradeoff | terminal_success | 2.289494973258815 | -0.8437672880198925 | model/model.py +19/-2 | some component metrics improved but other tracked metrics regressed strongly |
| `generation_006/proposal_003` | benchmark_tradeoff | terminal_success | 2.382130647971323 | -0.7511316133073844 | model/model.py +45/-2 | some component metrics improved but other tracked metrics regressed strongly |
| `generation_006/proposal_004` | benchmark_tradeoff | terminal_success | 2.095364913294265 | -1.0378973479844422 | model/model.py +72/-0; model/train.py +6/-6 | some component metrics improved but other tracked metrics regressed strongly |
| `generation_006/proposal_005` | benchmark_tradeoff | terminal_success | 2.173250758963486 | -0.9600115023152211 | model/model.py +91/-4; model/train.py +1/-0 | some component metrics improved but other tracked metrics regressed strongly |
| `generation_006/proposal_006` | benchmark_tradeoff | terminal_success | 1.876962993131852 | -1.2562992681468552 | model/model.py +143/-5; model/train.py +14/-1 | some component metrics improved but other tracked metrics regressed strongly |
| `generation_006/proposal_008` | benchmark_tradeoff | terminal_success | 2.686657884643924 | -0.44660437663478314 | no tracked code diff | some component metrics improved but other tracked metrics regressed strongly |
| `generation_006/proposal_009` | benchmark_tradeoff | terminal_success | 2.4254283170784934 | -0.707833944200214 | model/model.py +33/-11 | some component metrics improved but other tracked metrics regressed strongly |
