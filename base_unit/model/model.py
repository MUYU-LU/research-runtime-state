from __future__ import annotations

import torch
from torch import nn


class EvolutionMLIP(nn.Module):
    def __init__(
        self,
        max_atomic_number: int = 100,
        hidden_dim: int = 96,
        num_rbf: int = 32,
        cutoff: float = 5.0,
    ):
        super().__init__()
        self.hidden_dim = hidden_dim
        self.num_rbf = num_rbf
        self.cutoff = cutoff

        self.embedding = nn.Embedding(max_atomic_number + 1, hidden_dim)
        self.atomref = nn.Embedding(max_atomic_number + 1, 1)

        centers = torch.linspace(0.0, cutoff, num_rbf)
        widths = torch.full((num_rbf,), (cutoff / max(num_rbf - 1, 1)) + 1e-6)
        self.register_buffer("rbf_centers", centers)
        self.register_buffer("rbf_widths", widths)

        self.pair_mlp = nn.Sequential(
            nn.Linear(hidden_dim * 2 + num_rbf, hidden_dim),
            nn.SiLU(),
            nn.Linear(hidden_dim, hidden_dim),
            nn.SiLU(),
            nn.Linear(hidden_dim, hidden_dim),
            nn.SiLU(),
        )
        self.pair_out = nn.Linear(hidden_dim, 1)

    def _rbf(self, distances: torch.Tensor) -> torch.Tensor:
        diff = distances.unsqueeze(-1) - self.rbf_centers
        return torch.exp(-0.5 * (diff / self.rbf_widths) ** 2)

    def forward_energy(self, numbers: torch.Tensor, positions: torch.Tensor) -> torch.Tensor:
        emb = self.embedding(numbers)
        atomref = self.atomref(numbers).sum()

        rij = positions[:, None, :] - positions[None, :, :]
        dij = torch.linalg.norm(rij, dim=-1)

        n_atoms = numbers.shape[0]
        eye = torch.eye(n_atoms, device=positions.device, dtype=torch.bool)
        mask = (~eye) & (dij < self.cutoff)

        if not mask.any():
            return atomref

        i_idx, j_idx = torch.where(mask)
        dij_flat = dij[i_idx, j_idx]
        rbf = self._rbf(dij_flat)

        pair_feat = torch.cat([emb[i_idx], emb[j_idx], rbf], dim=-1)
        pair_hidden = self.pair_mlp(pair_feat)
        pair_energy = self.pair_out(pair_hidden).squeeze(-1)

        total_pair_energy = 0.5 * pair_energy.sum()
        return atomref + total_pair_energy

    def forward(self, batch: dict) -> tuple[torch.Tensor, torch.Tensor]:
        positions = batch["positions"].clone().detach().requires_grad_(True)
        energy = self.forward_energy(batch["numbers"], positions)
        forces = -torch.autograd.grad(energy, positions, create_graph=True)[0]
        return energy, forces
