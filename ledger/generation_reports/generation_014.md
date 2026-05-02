# generation_014 outcome report

- source_unit: `generation_013/proposal_007`
- parent_Q_total: `3.75578478119853`
- margin: `0.03`
- did_any_child_beat_parent: `True`

## Best child

```json
{
  "unit": "generation_014/proposal_009",
  "Q_rmd17": 4.054452268569513,
  "Q_iso17": 3.609934903921426,
  "Q_total": 3.8988711909426823,
  "outcome_class": "frontier_win"
}
```

## Outcome counts

```json
{
  "frontier_win": 7,
  "neutral_variance": 1
}
```

## Lessons


## Units

| unit | outcome_class | run_state | Q_total | delta_Q_vs_parent | code_delta | notes |
|---|---|---|---:|---:|---|---|
| `generation_014/proposal_001` | frontier_win | terminal_success | 3.8083339252161257 | 0.052549144017595584 | model/model.py +4/-2 | delta_Q=0.0525491 exceeds margin=0.03 |
| `generation_014/proposal_002` | frontier_win | terminal_success | 3.821525130181927 | 0.06574034898339676 | model/model.py +6/-2 | delta_Q=0.0657403 exceeds margin=0.03 |
| `generation_014/proposal_003` | frontier_win | terminal_success | 3.8029619007008915 | 0.047177119502361364 | model/train.py +2/-2 | delta_Q=0.0471771 exceeds margin=0.03 |
| `generation_014/proposal_004` | frontier_win | terminal_success | 3.788700279008153 | 0.032915497809622885 | model/model.py +6/-2; model/train.py +1/-3 | delta_Q=0.0329155 exceeds margin=0.03 |
| `generation_014/proposal_006` | frontier_win | terminal_success | 3.8054786930843165 | 0.049693911885786424 | model/train.py +20/-6 | delta_Q=0.0496939 exceeds margin=0.03 |
| `generation_014/proposal_007` | frontier_win | terminal_success | 3.825955941893789 | 0.07017116069525908 | model/train.py +3/-1 | delta_Q=0.0701712 exceeds margin=0.03 |
| `generation_014/proposal_008` | neutral_variance | terminal_success | 3.762904134770926 | 0.007119353572395681 | no tracked code diff | abs(delta_Q)=0.00711935 within margin=0.03 |
| `generation_014/proposal_009` | frontier_win | terminal_success | 3.8988711909426823 | 0.1430864097441522 | model/model.py +5/-2 | delta_Q=0.143086 exceeds margin=0.03 |
