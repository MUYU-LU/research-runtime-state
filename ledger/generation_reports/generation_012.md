# generation_012 outcome report

- source_unit: `generation_011/proposal_007`
- parent_Q_total: `2.6110967401910914`
- margin: `0.03`
- did_any_child_beat_parent: `True`

## Best child

```json
{
  "unit": "generation_012/proposal_005",
  "Q_rmd17": 3.98542952465656,
  "Q_iso17": 3.5422065556508207,
  "Q_total": 3.8303014855045507,
  "outcome_class": "frontier_win"
}
```

## Outcome counts

```json
{
  "benchmark_tradeoff": 2,
  "frontier_win": 5,
  "neutral_variance": 1
}
```

## Lessons


## Units

| unit | outcome_class | run_state | Q_total | delta_Q_vs_parent | code_delta | notes |
|---|---|---|---:|---:|---|---|
| `generation_012/proposal_001` | frontier_win | terminal_success | 3.0877379312170343 | 0.47664119102594293 | model/train.py +25/-0 | delta_Q=0.476641 exceeds margin=0.03 |
| `generation_012/proposal_002` | neutral_variance | terminal_success | 2.6347065519808517 | 0.023609811789760293 | model/train.py +7/-0 | abs(delta_Q)=0.0236098 within margin=0.03 |
| `generation_012/proposal_003` | frontier_win | terminal_success | 2.8507277512574696 | 0.23963101106637819 | model/train.py +35/-0 | delta_Q=0.239631 exceeds margin=0.03 |
| `generation_012/proposal_005` | frontier_win | terminal_success | 3.8303014855045507 | 1.2192047453134593 | model/train.py +55/-0 | delta_Q=1.2192 exceeds margin=0.03 |
| `generation_012/proposal_006` | benchmark_tradeoff | terminal_success | 2.5241753052266063 | -0.08692143496448512 | model/model.py +11/-2; model/train.py +8/-0 | some component metrics improved but other tracked metrics regressed strongly |
| `generation_012/proposal_007` | frontier_win | terminal_success | 2.6469717798904995 | 0.035875039699408084 | model/model.py +4/-1; model/train.py +7/-0 | delta_Q=0.035875 exceeds margin=0.03 |
| `generation_012/proposal_008` | benchmark_tradeoff | terminal_success | 2.355509733154056 | -0.2555870070370352 | model/model.py +3/-2 | some component metrics improved but other tracked metrics regressed strongly |
| `generation_012/proposal_010` | frontier_win | terminal_success | 2.67296633950119 | 0.06186959931009861 | no tracked code diff | delta_Q=0.0618696 exceeds margin=0.03 |
