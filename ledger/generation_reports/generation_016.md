# generation_016 outcome report

- source_unit: `generation_015/proposal_004`
- parent_Q_total: `3.9176951158891966`
- margin: `0.03`
- did_any_child_beat_parent: `False`

## Best child

```json
{
  "unit": "generation_016/proposal_002",
  "Q_rmd17": 4.127178951686343,
  "Q_iso17": 3.599662280546256,
  "Q_total": 3.9425481167873127,
  "outcome_class": "neutral_variance"
}
```

## Outcome counts

```json
{
  "benchmark_tradeoff": 3,
  "control_replicate": 1,
  "implementation_failure": 1,
  "negative_method": 1,
  "neutral_variance": 2
}
```

## Lessons

- No child beat parent generation_015/proposal_004; keep parent unless a reviewed override is chosen.
- Negative methods should not be repeated unless the proposal addresses the recorded failure pattern.

## Units

| unit | outcome_class | run_state | Q_total | delta_Q_vs_parent | code_delta | notes |
|---|---|---|---:|---:|---|---|
| `generation_016/proposal_001` | negative_method | terminal_success | 3.851885386792431 | -0.06580972909676541 | model/model.py +116/-1 | Q_total lost and no tracked component metric improved relative to parent |
| `generation_016/proposal_002` | neutral_variance | terminal_success | 3.9425481167873127 | 0.02485300089811604 | model/model.py +144/-1 | abs(delta_Q)=0.024853 within margin=0.03 |
| `generation_016/proposal_003` | neutral_variance | terminal_success | 3.918883058849291 | 0.0011879429600942792 | model/model.py +113/-1 | abs(delta_Q)=0.00118794 within margin=0.03 |
| `generation_016/proposal_004` | benchmark_tradeoff | terminal_success | 3.886565986954662 | -0.031129128934534567 | model/model.py +45/-20 | some component metrics improved but other tracked metrics regressed strongly |
| `generation_016/proposal_005` | benchmark_tradeoff | terminal_success | 3.887455498249798 | -0.03023961763939864 | model/model.py +40/-2 | some component metrics improved but other tracked metrics regressed strongly |
| `generation_016/proposal_006` | implementation_failure | terminal_success | None | None | model/model.py +134/-1 | missing Q_total for child or parent |
| `generation_016/proposal_007` | benchmark_tradeoff | terminal_success | 3.8526652705638647 | -0.06502984532533196 | model/model.py +113/-1; model/train.py +2/-2 | some component metrics improved but other tracked metrics regressed strongly |
| `generation_016/proposal_009` | control_replicate | terminal_success | 3.886831178837718 | None | no tracked code diff | unit is marked as a control replicate |
