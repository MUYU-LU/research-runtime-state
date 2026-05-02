# generation_019 outcome report

- source_unit: `generation_018/proposal_005`
- parent_Q_total: `4.049988359195011`
- margin: `0.03`
- did_any_child_beat_parent: `False`

## Best child

```json
{
  "unit": "generation_019/proposal_003",
  "Q_rmd17": 4.166948386496077,
  "Q_iso17": 3.764324633467114,
  "Q_total": 4.02603007293594,
  "outcome_class": "neutral_variance"
}
```

## Outcome counts

```json
{
  "benchmark_tradeoff": 5,
  "control_replicate": 1,
  "negative_method": 1,
  "neutral_variance": 1
}
```

## Lessons

- No child beat parent generation_018/proposal_005; keep parent unless a reviewed override is chosen.
- Negative methods should not be repeated unless the proposal addresses the recorded failure pattern.

## Units

| unit | outcome_class | run_state | Q_total | delta_Q_vs_parent | code_delta | notes |
|---|---|---|---:|---:|---|---|
| `generation_019/proposal_001` | negative_method | terminal_success | 3.970510731562775 | -0.07947762763223665 | model/model.py +48/-7 | Q_total lost and no tracked component metric improved relative to parent |
| `generation_019/proposal_002` | benchmark_tradeoff | terminal_success | 4.009504799041654 | -0.04048356015335752 | model/model.py +65/-1 | some component metrics improved but other tracked metrics regressed strongly |
| `generation_019/proposal_003` | neutral_variance | terminal_success | 4.02603007293594 | -0.023958286259071038 | model/model.py +17/-2 | abs(delta_Q)=0.0239583 within margin=0.03 |
| `generation_019/proposal_004` | benchmark_tradeoff | terminal_success | 3.958631192564253 | -0.09135716663075844 | model/model.py +72/-9 | some component metrics improved but other tracked metrics regressed strongly |
| `generation_019/proposal_005` | benchmark_tradeoff | terminal_success | 4.004145585308249 | -0.04584277388676217 | model/model.py +68/-9 | some component metrics improved but other tracked metrics regressed strongly |
| `generation_019/proposal_006` | benchmark_tradeoff | terminal_success | 3.997740571013307 | -0.05224778818170428 | model/model.py +59/-8; model/train.py +1/-1 | some component metrics improved but other tracked metrics regressed strongly |
| `generation_019/proposal_007` | benchmark_tradeoff | terminal_success | 3.9516629729102073 | -0.09832538628480414 | model/model.py +4/-1 | some component metrics improved but other tracked metrics regressed strongly |
| `generation_019/proposal_008` | control_replicate | terminal_success | 4.023487021453425 | None | no tracked code diff | unit is marked as a control replicate |
