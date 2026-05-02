from __future__ import annotations

import json
import math
import random
from pathlib import Path

import torch
from ase.io import iread
from torch.utils.data import DataLoader, Dataset

KCAL_MOL_TO_EV = 0.0433641153087705
ROOT = Path(__file__).resolve().parents[1]
CONFIG = json.loads((ROOT / "config.json").read_text(encoding="utf-8"))


def _sample_from_atoms(atoms, *, energy_scale: float = 1.0, force_scale: float = 1.0):
    calc = getattr(atoms, "calc", None)
    results = getattr(calc, "results", {})
    energy = float(results["energy"]) * energy_scale
    forces = torch.tensor(results["forces"], dtype=torch.float32) * force_scale
    numbers = torch.tensor(atoms.numbers, dtype=torch.long)
    positions = torch.tensor(atoms.positions, dtype=torch.float32)
    return {
        "numbers": numbers,
        "positions": positions,
        "energy": torch.tensor(energy, dtype=torch.float32),
        "forces": forces,
    }


def _count_frames(split_path: Path) -> int:
    total = 0
    for file_path in sorted(split_path.glob("*.extxyz")):
        total += sum(1 for _ in iread(file_path, format="extxyz", index=":"))
    return total


def _dataset_sample_ratio(dataset: str) -> float | None:
    if dataset == "iso17":
        return CONFIG.get("iso17_sample_ratio")
    return None


def _dataset_sample_seed(dataset: str) -> int:
    if dataset == "iso17":
        return int(CONFIG.get("iso17_sample_seed", 17))
    return 0


def _sidecar_name(ratio: float) -> str:
    label = f"{ratio:.6g}".replace(".", "p")
    return f".sample_indices_{label}.json"


def _resolve_selected_indices(split_path: Path, *, dataset: str, max_samples: int | None = None) -> set[int] | None:
    ratio = _dataset_sample_ratio(dataset)
    total = _count_frames(split_path)
    if total == 0:
        return set()

    target = None
    if ratio is not None:
        if not (0.0 < float(ratio) <= 1.0):
            raise ValueError(f"sample_ratio must be in (0, 1], got {ratio!r}")
        target = max(1, math.ceil(total * float(ratio)))

    if max_samples is not None:
        target = min(target, max_samples) if target is not None else max_samples

    if target is None or target >= total:
        return None

    seed = f"{_dataset_sample_seed(dataset)}:{split_path.name}:{total}"
    if dataset == "iso17" and max_samples is None and ratio is not None:
        sidecar_path = split_path.parent / _sidecar_name(float(ratio))
        sidecar = {}
        if sidecar_path.exists():
            sidecar = json.loads(sidecar_path.read_text(encoding="utf-8"))
            entry = sidecar.get(split_path.name, {})
            if (
                entry.get("total") == total
                and entry.get("target") == target
                and entry.get("seed") == seed
                and isinstance(entry.get("indices"), list)
            ):
                return set(int(index) for index in entry["indices"])

        rng = random.Random(seed)
        picked = sorted(rng.sample(range(total), target))
        sidecar[split_path.name] = {
            "dataset": dataset,
            "split": split_path.name,
            "ratio": float(ratio),
            "total": total,
            "target": target,
            "seed": seed,
            "indices": picked,
        }
        sidecar_path.write_text(json.dumps(sidecar, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
        return set(picked)

    rng = random.Random(seed)
    picked = sorted(rng.sample(range(total), target))
    return set(picked)


class ExtXYZDataset(Dataset):
    def __init__(
        self,
        dataset: str,
        split_dir: str | Path,
        *,
        energy_scale: float = 1.0,
        force_scale: float = 1.0,
        max_samples: int | None = None,
    ):
        self.samples = []
        split_path = Path(split_dir)
        selected = _resolve_selected_indices(split_path, dataset=dataset, max_samples=max_samples)

        global_idx = 0
        for file_path in sorted(split_path.glob("*.extxyz")):
            for atoms in iread(file_path, format="extxyz", index=":"):
                keep = selected is None or global_idx in selected
                if keep:
                    self.samples.append(_sample_from_atoms(atoms, energy_scale=energy_scale, force_scale=force_scale))
                global_idx += 1

    def __len__(self):
        return len(self.samples)

    def __getitem__(self, index: int):
        return self.samples[index]


def make_dataset(dataset: str, split_dir: str | Path, *, max_samples: int | None = None) -> ExtXYZDataset:
    if dataset == "rmd17":
        return ExtXYZDataset(dataset, split_dir, energy_scale=KCAL_MOL_TO_EV, force_scale=KCAL_MOL_TO_EV, max_samples=max_samples)
    if dataset == "iso17":
        return ExtXYZDataset(dataset, split_dir, energy_scale=1.0, force_scale=1.0, max_samples=max_samples)
    if dataset == "mad10k":
        return ExtXYZDataset(dataset, split_dir, energy_scale=1.0, force_scale=1.0, max_samples=max_samples)
    raise KeyError(dataset)


def identity_collate(batch):
    return batch


def make_dataloader(dataset: str, split_dir: str | Path, *, batch_size: int = 1, shuffle: bool = False, max_samples: int | None = None):
    ds = make_dataset(dataset, split_dir, max_samples=max_samples)
    return DataLoader(ds, batch_size=batch_size, shuffle=shuffle, collate_fn=identity_collate)
