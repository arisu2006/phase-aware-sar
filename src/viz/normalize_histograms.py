import sys
from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np

# Ensure root directory is in python search path
sys.path.append(str(Path(__file__).resolve().parents[2]))
from src.preprocess.normalize import normalize_complex_chip


def load_sample_chips(n=3, size=64, seed=0):
    rng = np.random.default_rng(seed)
    chips = []
    for _ in range(n):
        chip = (
            rng.normal(size=(size, size)) + 1j * rng.normal(size=(size, size))
        ).astype(np.complex64)
        # Simulate a bright target in the center
        chip[size // 3 : size // 3 + 4, size // 3 : size // 3 + 4] *= (
            rng.uniform(20, 80)
        )
        chips.append(chip)
    return chips


def plot_histograms(chips, out_path="normalize_histograms.png"):
    fig, axes = plt.subplots(len(chips), 4, figsize=(16, 4 * len(chips)))
    for i, chip in enumerate(chips):
        amp_raw = np.abs(chip)
        phase_raw = np.angle(chip)
        out = normalize_complex_chip(chip)

        # Col 0: Raw Amplitude
        axes[i, 0].hist(amp_raw.ravel(), bins=50, color="steelblue")
        axes[i, 0].set_title(f"Chip {i+1}: Raw Amplitude")

        # Col 1: Normalized Amplitude
        axes[i, 1].hist(
            out["amplitude_norm"].ravel(), bins=50, color="darkorange"
        )
        axes[i, 1].set_title(f"Chip {i+1}: Log Normalized Amp [0, 1]")

        # Col 2: Raw Phase
        axes[i, 2].hist(phase_raw.ravel(), bins=50, color="seagreen")
        axes[i, 2].set_title(f"Chip {i+1}: Raw Phase")

        # Col 3: Wrapped Phase
        axes[i, 3].hist(
            out["phase_wrapped"].ravel(), bins=50, color="indianred"
        )
        axes[i, 3].set_title(f"Chip {i+1}: Wrapped Phase [-\\pi, \\pi]")

    plt.tight_layout()
    plt.savefig(out_path, dpi=150)
    print(f"Saved histogram plot to {out_path}")


if __name__ == "__main__":
    plot_histograms(load_sample_chips(n=3))