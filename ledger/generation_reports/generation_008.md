# generation_008 outcome report

- source_unit: `generation_004/proposal_001`
- parent_Q_total: `3.1332622612787073`
- margin: `0.03`
- did_any_child_beat_parent: `False`

## Best child

```json
{
  "unit": "generation_008/proposal_007",
  "Q_rmd17": 2.6554765181411053,
  "Q_iso17": 2.5919548010280273,
  "Q_total": 2.6332439171515283,
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
| `generation_008/proposal_001` | benchmark_tradeoff | terminal_success | 2.4108221000765306 | -0.7224401612021767 | model/model.py +12/-2 | some component metrics improved but other tracked metrics regressed strongly |
| `generation_008/proposal_002` | benchmark_tradeoff | terminal_success | 2.309302563405874 | -0.8239596978728332 | model/model.py +14/-2 | some component metrics improved but other tracked metrics regressed strongly |
| `generation_008/proposal_004` | benchmark_tradeoff | terminal_success | 2.538999013550601 | -0.5942632477281062 | model/model.py +80/-2 | some component metrics improved but other tracked metrics regressed strongly |
| `generation_008/proposal_005` | benchmark_tradeoff | terminal_success | 2.4399389217184857 | -0.6933233395602216 | model/model.py +33/-2 | some component metrics improved but other tracked metrics regressed strongly |
| `generation_008/proposal_006` | benchmark_tradeoff | terminal_success | 2.4899809765957803 | -0.643281284682927 | model/train.py +25/-7 | some component metrics improved but other tracked metrics regressed strongly |
| `generation_008/proposal_007` | benchmark_tradeoff | terminal_success | 2.6332439171515283 | -0.500018344127179 | model/model.py +1/-2 | some component metrics improved but other tracked metrics regressed strongly |
| `generation_008/proposal_008` | benchmark_tradeoff | terminal_success | 2.5305173620797556 | -0.6027448991989517 | no tracked code diff | some component metrics improved but other tracked metrics regressed strongly |
| `generation_008/proposal_010` | benchmark_tradeoff | terminal_success | 2.031430482396093 | -1.1018317788826142 | model/model.py +64/-2; model/train.py +22/-2 | some component metrics improved but other tracked metrics regressed strongly |
