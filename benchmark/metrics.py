from __future__ import annotations

BENCHMARK_METRICS = {
    "iso17": {
        "units": {
            "energy": "eV",
            "force": "eV/angstrom",
        },
        "splits": ["train", "val", "test_within", "test_other"],
        "metrics": {
            "within_energy_mae": "Mean absolute error of total energy on test_within.",
            "within_force_mae": "Mean absolute error of atomic forces on test_within.",
            "other_energy_mae": "Mean absolute error of total energy on test_other.",
            "other_force_mae": "Mean absolute error of atomic forces on test_other.",
            "mixed_force_mae": "0.4 * within_force_mae + 0.6 * other_force_mae.",
            "mixed_energy_mae": "0.4 * within_energy_mae + 0.6 * other_energy_mae.",
            "gap_penalty": "Normalized generalization gap: max(0, other_force_mae - within_force_mae) / mixed_force_mae.",
            "Q_dataset": "Alias for Q_iso17 in benchmark output: 0.75 * log(F0_iso17 / mixed_force_mae) + 0.25 * log(E0_iso17 / mixed_energy_mae) - 0.10 * gap_penalty. Higher is better.",
        },
    },
    "rmd17": {
        "units": {
            "energy": "eV",
            "force": "eV/angstrom",
        },
        "splits": ["train", "val", "test"],
        "metrics": {
            "mild_ood_energy_mae": "Mean absolute error of total energy on val.",
            "mild_ood_force_mae": "Mean absolute error of atomic forces on val.",
            "hard_ood_energy_mae": "Mean absolute error of total energy on test.",
            "hard_ood_force_mae": "Mean absolute error of atomic forces on test.",
            "mixed_force_mae": "0.4 * mild_ood_force_mae + 0.6 * hard_ood_force_mae.",
            "mixed_energy_mae": "0.4 * mild_ood_energy_mae + 0.6 * hard_ood_energy_mae.",
            "gap_penalty": "Normalized generalization gap: max(0, hard_ood_force_mae - mild_ood_force_mae) / mixed_force_mae.",
            "Q_dataset": "Alias for Q_rmd17 in benchmark output: 0.75 * log(F0_rmd17 / mixed_force_mae) + 0.25 * log(E0_rmd17 / mixed_energy_mae) - 0.10 * gap_penalty. Higher is better.",
        },
    },
    "total_fitness": {
        "Q_total": "0.65 * Q_rmd17 + 0.35 * Q_iso17. Higher is better.",
        "G_delta": "Q_total_child - Q_total_parent. Positive means progress.",
    },
    "profiles": {
        "mad10k_adaptation": {
            "role": "External architecture/train-code adaptation diagnostic. Not part of Q_total.",
            "splits": ["train", "val", "test"],
            "metrics": {
                "test_force_mae_eV_per_A": "Mean absolute component force error on full MAD test split.",
                "test_energy_mae_meV_per_atom": "Mean absolute total-energy error normalized by atom count on full MAD test split.",
                "test_failure_rate": "Failed frames divided by attempted MAD test frames.",
            },
        },
    },
}
