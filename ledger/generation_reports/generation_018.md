# generation_018 outcome report

- source_unit: `generation_016/proposal_002`
- parent_Q_total: `3.9425481167873127`
- margin: `0.03`
- did_any_child_beat_parent: `True`

## Best child

```json
{
  "unit": "generation_018/proposal_005",
  "Q_rmd17": 4.19973862829514,
  "Q_iso17": 3.771880716580485,
  "Q_total": 4.049988359195011,
  "outcome_class": "frontier_win"
}
```

## Outcome counts

```json
{
  "benchmark_tradeoff": 2,
  "control_replicate": 1,
  "frontier_win": 2,
  "neutral_variance": 3
}
```

## Lessons


## Units

| unit | outcome_class | run_state | Q_total | delta_Q_vs_parent | code_delta | notes |
|---|---|---|---:|---:|---|---|
| `generation_018/proposal_001` | neutral_variance | terminal_success | 3.9154362953288775 | -0.02711182145843516 | model/model.py +122/-1 | abs(delta_Q)=0.0271118 within margin=0.03 |
| `generation_018/proposal_002` | benchmark_tradeoff | terminal_success | 3.8745188631060277 | -0.06802925368128498 | model/model.py +88/-0 | some component metrics improved but other tracked metrics regressed strongly |
| `generation_018/proposal_003` | frontier_win | terminal_success | 4.025879265971764 | 0.08333114918445172 | model/model.py +97/-19 | delta_Q=0.0833311 exceeds margin=0.03 |
| `generation_018/proposal_005` | frontier_win | terminal_success | 4.049988359195011 | 0.10744024240769878 | model/model.py +115/-4 | delta_Q=0.10744 exceeds margin=0.03 |
| `generation_018/proposal_006` | benchmark_tradeoff | terminal_success | 3.870291391834116 | -0.07225672495319646 | model/model.py +88/-1 | some component metrics improved but other tracked metrics regressed strongly |
| `generation_018/proposal_007` | neutral_variance | terminal_success | 3.9515028431707533 | 0.008954726383440637 | model/model.py +37/-1; model/train.py +4/-0 | abs(delta_Q)=0.00895473 within margin=0.03 |
| `generation_018/proposal_008` | control_replicate | terminal_success | 3.9311432800092705 | None | no tracked code diff | unit is marked as a control replicate |
| `generation_018/proposal_009` | neutral_variance | terminal_success | 3.9249751728400435 | -0.01757294394726916 | model/model.py +45/-15 | abs(delta_Q)=0.0175729 within margin=0.03 |
