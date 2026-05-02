# generation_023 outcome report

- source_unit: `generation_022/proposal_006`
- parent_Q_total: `4.042395946355124`
- margin: `0.06157465641983695`
- did_any_child_beat_parent: `False`

## Best child

```json
{
  "unit": "generation_023/proposal_004",
  "Q_rmd17": 4.206413224218935,
  "Q_iso17": 3.7570626760477586,
  "Q_total": 4.049140532359024,
  "outcome_class": "neutral_variance"
}
```

## Outcome counts

```json
{
  "control_replicate": 2,
  "neutral_variance": 6
}
```

## Lessons

- No child beat parent generation_022/proposal_006; keep parent unless a reviewed override is chosen.

## Units

| unit | outcome_class | run_state | Q_total | delta_Q_vs_parent | code_delta | notes |
|---|---|---|---:|---:|---|---|
| `generation_023/proposal_001` | neutral_variance | terminal_success | 4.002040760757263 | -0.04035518559786144 | model/model.py +18/-0 | abs(delta_Q)=0.0403552 within margin=0.0615747 |
| `generation_023/proposal_002` | neutral_variance | terminal_success | 4.038110125277138 | -0.004285821077986363 | model/model.py +17/-0 | abs(delta_Q)=0.00428582 within margin=0.0615747 |
| `generation_023/proposal_003` | neutral_variance | terminal_success | 4.011920871107206 | -0.03047507524791815 | model/model.py +20/-0 | abs(delta_Q)=0.0304751 within margin=0.0615747 |
| `generation_023/proposal_004` | neutral_variance | terminal_success | 4.049140532359024 | 0.006744586003899933 | model/model.py +23/-0 | abs(delta_Q)=0.00674459 within margin=0.0615747 |
| `generation_023/proposal_005` | control_replicate | terminal_success | 3.959348166111848 | None | no tracked code diff | unit is marked as a control replicate |
| `generation_023/proposal_006` | control_replicate | terminal_success | 4.020922822531685 | None | no tracked code diff | unit is marked as a control replicate |
| `generation_023/proposal_007` | neutral_variance | terminal_success | 4.0235279346651245 | -0.01886801168999952 | model/model.py +29/-0 | abs(delta_Q)=0.018868 within margin=0.0615747 |
| `generation_023/proposal_009` | neutral_variance | terminal_success | 3.9888491715441643 | -0.05354677481095971 | model/model.py +28/-0 | abs(delta_Q)=0.0535468 within margin=0.0615747 |
