# generation_011 outcome report

- source_unit: `generation_010/proposal_007`
- parent_Q_total: `2.774737936253514`
- margin: `0.03`
- did_any_child_beat_parent: `False`

## Best child

```json
{
  "unit": "generation_011/proposal_003",
  "Q_rmd17": 2.4668969047676126,
  "Q_iso17": 2.9340930574775967,
  "Q_total": 2.6304155582161073,
  "outcome_class": "negative_method"
}
```

## Outcome counts

```json
{
  "benchmark_tradeoff": 6,
  "control_replicate": 1,
  "negative_method": 1
}
```

## Lessons

- No child beat parent generation_010/proposal_007; keep parent unless a reviewed override is chosen.
- Negative methods should not be repeated unless the proposal addresses the recorded failure pattern.

## Units

| unit | outcome_class | run_state | Q_total | delta_Q_vs_parent | code_delta | notes |
|---|---|---|---:|---:|---|---|
| `generation_011/proposal_001` | benchmark_tradeoff | terminal_success | 2.4392729530159314 | -0.33546498323758245 | model/model.py +13/-1 | some component metrics improved but other tracked metrics regressed strongly |
| `generation_011/proposal_002` | benchmark_tradeoff | terminal_success | 2.149511618939582 | -0.6252263173139316 | model/train.py +17/-5 | some component metrics improved but other tracked metrics regressed strongly |
| `generation_011/proposal_003` | negative_method | terminal_success | 2.6304155582161073 | -0.14432237803740655 | model/model.py +17/-1 | Q_total lost and no tracked component metric improved relative to parent |
| `generation_011/proposal_004` | benchmark_tradeoff | terminal_success | 2.456076671718356 | -0.31866126453515786 | model/model.py +18/-1 | some component metrics improved but other tracked metrics regressed strongly |
| `generation_011/proposal_005` | benchmark_tradeoff | terminal_success | 2.556833016460838 | -0.21790491979267568 | model/model.py +30/-2 | some component metrics improved but other tracked metrics regressed strongly |
| `generation_011/proposal_006` | benchmark_tradeoff | terminal_success | 2.5372274181565473 | -0.23751051809696655 | model/model.py +8/-6 | some component metrics improved but other tracked metrics regressed strongly |
| `generation_011/proposal_007` | benchmark_tradeoff | terminal_success | 2.6110967401910914 | -0.16364119606242244 | model/model.py +2/-3 | some component metrics improved but other tracked metrics regressed strongly |
| `generation_011/proposal_008` | control_replicate | terminal_success | 2.483480607175906 | None | no tracked code diff | unit is marked as a control replicate |
