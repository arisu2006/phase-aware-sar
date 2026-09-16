# src/augment/corruptor.py
"""
SAR Corruption Library
Composes 1–2 random corruptions with configurable severity.
"""

from __future__ import annotations
import random
from typing import List, Tuple, Optional, Dict, Any
import numpy as np
import torch

# Import the individual corruption functions you already wrote
from src.augment.speckle_noise import add_speckle_noise
from src.augment.gaussian_noise import add_gaussian_noise
from src.augment.blur import apply_blur
from src.augment.phase_distortion import apply_phase_distortion


class SARCorruptionLibrary:
    """
    Applies a random composition of 1–2 SAR-specific corruptions.
    Severity controls the strength of each corruption.
    """

    AVAILABLE = ["speckle", "gaussian", "blur", "phase"]

    def __init__(
        self,
        severity: str = "mild",          # "mild" | "moderate" | "severe"
        max_corruptions: int = 2,
        seed: Optional[int] = None,
    ):
        assert severity in {"mild", "moderate", "severe"}
        self.severity = severity
        self.max_corruptions = max_corruptions
        self.rng = random.Random(seed)

        # Severity → strength parameters
        self.params = {
            "mild": {
                "speckle": {"looks": 8},
                "gaussian": {"std": 0.05},
                "blur": {"kernel_size": 3, "sigma": 0.8},
                "phase": {"std": 0.15},          # radians
            },
            "moderate": {
                "speckle": {"looks": 4},
                "gaussian": {"std": 0.12},
                "blur": {"kernel_size": 5, "sigma": 1.2},
                "phase": {"std": 0.35},
            },
            "severe": {
                "speckle": {"looks": 2},
                "gaussian": {"std": 0.25},
                "blur": {"kernel_size": 7, "sigma": 2.0},
                "phase": {"std": 0.70},
            },
        }[severity]

    def __call__(
        self,
        chip: np.ndarray | torch.Tensor,
        forced: Optional[List[str]] = None,
    ) -> Tuple[np.ndarray | torch.Tensor, List[str]]:
        """
        Parameters
        ----------
        chip : complex or real array / tensor
        forced : if provided, apply exactly these corruptions (for testing)

        Returns
        -------
        corrupted_chip, list_of_applied_corruptions
        """
        if forced is not None:
            chosen = forced
        else:
            k = self.rng.randint(1, self.max_corruptions)
            chosen = self.rng.sample(self.AVAILABLE, k=k)

        out = chip
        applied = []

        for name in chosen:
            if name == "speckle":
                out = add_speckle_noise(out, **self.params["speckle"])
            elif name == "gaussian":
                out = add_gaussian_noise(out, **self.params["gaussian"])
            elif name == "blur":
                out = apply_blur(out, **self.params["blur"])
            elif name == "phase":
                out = apply_phase_distortion(out, **self.params["phase"])
            applied.append(name)

        return out, applied


# ------------------------------------------------------------------
# Quick unit-test helper (run this once)
# ------------------------------------------------------------------
def _unit_test():
    print("Running SARCorruptionLibrary unit tests...")
    # Fake complex chip (H, W)
    chip = (np.random.randn(64, 64) + 1j * np.random.randn(64, 64)).astype(np.complex64)

    lib = SARCorruptionLibrary(severity="mild", seed=42)
    corrupted, applied = lib(chip)
    assert corrupted.shape == chip.shape
    assert len(applied) >= 1
    print(f"  mild OK → applied {applied}")

    lib = SARCorruptionLibrary(severity="severe", seed=123)
    corrupted, applied = lib(chip, forced=["speckle", "phase"])
    assert "speckle" in applied and "phase" in applied
    print(f"  severe + forced OK → applied {applied}")

    print("All unit tests passed.")


if __name__ == "__main__":
    _unit_test()