# generation_013 outcome report

- source_unit: `generation_012/proposal_005`
- parent_Q_total: `3.8303014855045507`
- margin: `0.03`
- did_any_child_beat_parent: `False`

## Best child

```json
{
  "unit": "generation_013/proposal_001",
  "Q_rmd17": 4.006493599756958,
  "Q_iso17": 3.5320110599378505,
  "Q_total": 3.8404247108202707,
  "outcome_class": "neutral_variance"
}
```

## Outcome counts

```json
{
  "benchmark_tradeoff": 2,
  "negative_method": 2,
  "neutral_variance": 4
}
```

## Lessons

- No child beat parent generation_012/proposal_005; keep parent unless a reviewed override is chosen.
- Negative methods should not be repeated unless the proposal addresses the recorded failure pattern.

## Units

| unit | outcome_class | run_state | Q_total | delta_Q_vs_parent | code_delta | notes |
|---|---|---|---:|---:|---|---|
| `generation_013/proposal_001` | neutral_variance | terminal_success | 3.8404247108202707 | 0.010123225315719964 | model/train.py +3/-1 | abs(delta_Q)=0.0101232 within margin=0.03 |
| `generation_013/proposal_002` | neutral_variance | terminal_success | 3.8182317354850257 | -0.012069750019525038 | model/train.py +11/-3 | abs(delta_Q)=0.0120698 within margin=0.03 |
| `generation_013/proposal_003` | neutral_variance | terminal_success | 3.8326592187559783 | 0.0023577332514275184 | model/train.py +22/-3 | abs(delta_Q)=0.00235773 within margin=0.03 |
| `generation_013/proposal_004` | negative_method | terminal_success | 3.797164365451982 | -0.03313712005256875 | model/model.py +3/-2; model/train.py +3/-1 | Q_total lost and no tracked component metric improved relative to parent |
| `generation_013/proposal_005` | neutral_variance | terminal_success | 3.834896080209445 | 0.004594594704894206 | model/train.py +5/-3 | abs(delta_Q)=0.00459459 within margin=0.03 |
| `generation_013/proposal_006` | benchmark_tradeoff | terminal_success | 3.799110139950649 | -0.031191345553901684 | model/train.py +24/-4 | some component metrics improved but other tracked metrics regressed strongly |
| `generation_013/proposal_007` | benchmark_tradeoff | terminal_success | 3.75578478119853 | -0.07451670430602064 | model/model.py +2/-3; model/train.py +3/-1 | some component metrics improved but other tracked metrics regressed strongly |
| `generation_013/proposal_008` | negative_method | terminal_success | 3.7759032085538946 | -0.05439827695065613 | no tracked code diff | Q_total lost and no tracked component metric improved relative to parent |
