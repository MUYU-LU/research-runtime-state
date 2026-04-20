from __future__ import annotations

import argparse
import json
from pathlib import Path

from model.eval import evaluate
from model.train import train

ROOT = Path(__file__).resolve().parent
CONFIG = json.loads((ROOT / "config.json").read_text(encoding="utf-8"))
OUTPUTS = (ROOT / CONFIG.get("outputs_root", "outputs")).resolve()
BENCHMARK = ((ROOT / CONFIG["benchmark_root"]).resolve() / "data")


def run_one(dataset: str, epochs: int, batch_size: int, max_samples: int | None):
    benchmark_root = BENCHMARK / dataset
    output_dir = OUTPUTS / dataset

    train_result = train(
        dataset=dataset,
        train_dir=benchmark_root / "train",
        val_dir=benchmark_root / "val",
        output_dir=output_dir,
        epochs=epochs,
        batch_size=batch_size,
        max_samples=max_samples,
    )

    eval_result = evaluate(
        dataset=dataset,
        model_path=train_result["model_path"],
        benchmark_root=benchmark_root,
        output_dir=output_dir,
        max_samples=max_samples,
    )

    print(output_dir)
    print(train_result["history_path"])
    print(eval_result["metrics_path"])


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--dataset", choices=["rmd17", "iso17", "both"], default="both")
    parser.add_argument("--epochs", type=int, default=8)
    parser.add_argument("--batch-size", type=int, default=1)
    parser.add_argument("--max-samples", type=int, default=None)
    args = parser.parse_args()

    datasets = ["rmd17", "iso17"] if args.dataset == "both" else [args.dataset]
    for dataset in datasets:
        run_one(dataset, args.epochs, args.batch_size, args.max_samples)


if __name__ == "__main__":
    main()
