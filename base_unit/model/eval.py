from __future__ import annotations

import json
import math
from pathlib import Path

import torch

from .dataloader import make_dataloader
from .model import EvolutionMLIP
from .train import get_cuda_device, run_epoch

ROOT = Path(__file__).resolve().parents[1]
BENCHMARK_ROOT = (ROOT / "../benchmark").resolve()
ANCHOR_PATH = BENCHMARK_ROOT / "anchors.json"
EPS = 1e-12


def load_anchors():
    if not ANCHOR_PATH.exists():
        return {}
    return json.loads(ANCHOR_PATH.read_text(encoding="utf-8"))


def progress(metric: float, anchor: float) -> float:
    return math.log((anchor + EPS) / (metric + EPS))


def anchored_q(mixed_force: float, mixed_energy: float, gap: float, anchors: dict) -> float | None:
    if not anchors:
        return None
    anchor_force = float(anchors.get("mixed_force_mae", 0.0))
    anchor_energy = float(anchors.get("mixed_energy_mae", 0.0))
    if anchor_force <= 0.0 or anchor_energy <= 0.0:
        return None
    return (
        0.75 * progress(mixed_force, anchor_force)
        + 0.25 * progress(mixed_energy, anchor_energy)
        - 0.10 * gap
    )


def eval_rmd17(model, val_dir: str | Path, test_dir: str | Path, max_samples: int | None = None, device: torch.device | None = None):
    val_loader = make_dataloader("rmd17", val_dir, batch_size=1, shuffle=False, max_samples=max_samples)
    test_loader = make_dataloader("rmd17", test_dir, batch_size=1, shuffle=False, max_samples=max_samples)

    val_metrics = run_epoch(model, val_loader, optimizer=None, device=device)
    test_metrics = run_epoch(model, test_loader, optimizer=None, device=device)

    mixed_force = 0.4 * val_metrics["force_mae"] + 0.6 * test_metrics["force_mae"]
    mixed_energy = 0.4 * val_metrics["energy_mae"] + 0.6 * test_metrics["energy_mae"]
    gap = max(0.0, test_metrics["force_mae"] - val_metrics["force_mae"]) / (mixed_force + EPS)

    anchors = load_anchors().get("seed_anchor", {}).get("rmd17", {})
    q_dataset = anchored_q(mixed_force, mixed_energy, gap, anchors)

    return {
        "mild_ood_energy_mae": val_metrics["energy_mae"],
        "mild_ood_force_mae": val_metrics["force_mae"],
        "hard_ood_energy_mae": test_metrics["energy_mae"],
        "hard_ood_force_mae": test_metrics["force_mae"],
        "mixed_force_mae": mixed_force,
        "mixed_energy_mae": mixed_energy,
        "gap_penalty": gap,
        "Q_dataset": q_dataset,
    }


def eval_iso17(model, within_dir: str | Path, other_dir: str | Path, max_samples: int | None = None, device: torch.device | None = None):
    within_loader = make_dataloader("iso17", within_dir, batch_size=1, shuffle=False, max_samples=max_samples)
    other_loader = make_dataloader("iso17", other_dir, batch_size=1, shuffle=False, max_samples=max_samples)

    within_metrics = run_epoch(model, within_loader, optimizer=None, device=device)
    other_metrics = run_epoch(model, other_loader, optimizer=None, device=device)

    mixed_force = 0.4 * within_metrics["force_mae"] + 0.6 * other_metrics["force_mae"]
    mixed_energy = 0.4 * within_metrics["energy_mae"] + 0.6 * other_metrics["energy_mae"]
    gap = max(0.0, other_metrics["force_mae"] - within_metrics["force_mae"]) / (mixed_force + EPS)

    anchors = load_anchors().get("seed_anchor", {}).get("iso17", {})
    q_dataset = anchored_q(mixed_force, mixed_energy, gap, anchors)

    return {
        "within_energy_mae": within_metrics["energy_mae"],
        "within_force_mae": within_metrics["force_mae"],
        "other_energy_mae": other_metrics["energy_mae"],
        "other_force_mae": other_metrics["force_mae"],
        "mixed_force_mae": mixed_force,
        "mixed_energy_mae": mixed_energy,
        "gap_penalty": gap,
        "Q_dataset": q_dataset,
    }


def eval_mad10k(model, val_dir: str | Path, test_dir: str | Path, max_samples: int | None = None, device: torch.device | None = None):
    val_loader = make_dataloader("mad10k", val_dir, batch_size=1, shuffle=False, max_samples=max_samples)
    test_loader = make_dataloader("mad10k", test_dir, batch_size=1, shuffle=False, max_samples=max_samples)

    val_metrics = run_epoch(model, val_loader, optimizer=None, device=device)
    test_metrics = run_epoch(model, test_loader, optimizer=None, device=device)

    return {
        "val_energy_mae": val_metrics["energy_mae"],
        "val_force_mae": val_metrics["force_mae"],
        "test_energy_mae": test_metrics["energy_mae"],
        "test_force_mae": test_metrics["force_mae"],
        "mixed_force_mae": 0.25 * val_metrics["force_mae"] + 0.75 * test_metrics["force_mae"],
        "mixed_energy_mae": 0.25 * val_metrics["energy_mae"] + 0.75 * test_metrics["energy_mae"],
        "Q_dataset": None,
        "profile_only": True,
    }


def evaluate(*, dataset: str, model_path: str | Path, benchmark_root: str | Path, output_dir: str | Path, max_samples: int | None = None):
    device = get_cuda_device()
    model = EvolutionMLIP().to(device)
    model.load_state_dict(torch.load(model_path, map_location=device))
    model.eval()

    benchmark_root = Path(benchmark_root)
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    if dataset == "rmd17":
        metrics = eval_rmd17(model, benchmark_root / "val", benchmark_root / "test", max_samples=max_samples, device=device)
    elif dataset == "iso17":
        metrics = eval_iso17(model, benchmark_root / "test_within", benchmark_root / "test_other", max_samples=max_samples, device=device)
    elif dataset == "mad10k":
        metrics = eval_mad10k(model, benchmark_root / "val", benchmark_root / "test", max_samples=max_samples, device=device)
    else:
        raise KeyError(dataset)

    metrics["device"] = str(device)
    metrics_path = output_dir / "benchmark_metrics.json"
    metrics_path.write_text(json.dumps(metrics, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    return {
        "metrics_path": str(metrics_path),
        "metrics": metrics,
    }
