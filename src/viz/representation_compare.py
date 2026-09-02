from pathlib import Path
import sys
import matplotlib.pyplot as plt
import numpy as np

sys.path.append(str(Path(__file__).resolve().parents[2]))
from src.preprocess.representation import get_representation


def load_sample_chips(n=3, size=64, seed=3):
    rng = np.random.default_rng(seed)
    chips = []
    for _ in range(n):
        chip = (
            rng.normal(size=(size, size)) + 1j * rng.normal(size=(size, size))
        ).astype(np.complex64)
        chip[
            size // 2 - 3 : size // 2 + 3, size // 2 - 3 : size // 2 + 3
        ] *= rng.uniform(20, 60)
        chips.append(chip)
    return chips


def plot_comparison(chips, out_path="representation_compare.png"):
    fig, axes = plt.subplots(len(chips), 5, figsize=(20, 4 * len(chips)))
    for i, chip in enumerate(chips):
        ap = get_representation(chip, mode="ap")
        ri = get_representation(chip, mode="ri")

        axes[i, 0].imshow(ap[0], cmap="gray")
        axes[i, 0].set_title(f"S{i+1}: amplitude")

        axes[i, 1].imshow(np.arctan2(ap[1], ap[2]), cmap="twilight")
        axes[i, 1].set_title(f"S{i+1}: phase (from sin/cos)")

        axes[i, 2].imshow(ri[0], cmap="RdBu")
        axes[i, 2].set_title(f"S{i+1}: real")

        axes[i, 3].imshow(ri[1], cmap="RdBu")
        axes[i, 3].set_title(f"S{i+1}: imag")

        # Mathematical sanity check: sqrt(real^2 + imag^2) must equal amplitude
        recon_amp = np.sqrt(ri[0] ** 2 + ri[1] ** 2)
        diff = np.abs(recon_amp - ap[0])

        im = axes[i, 4].imshow(diff, cmap="hot", vmin=0, vmax=1e-5)
        axes[i, 4].set_title(f"S{i+1}: diff (max={diff.max():.1e})")

        for ax in axes[i]:
            ax.axis("off")

    plt.tight_layout()
    plt.savefig(out_path, dpi=150)
    print(f"Saved comparison to {out_path}")


if __name__ == "__main__":
    plot_comparison(load_sample_chips(n=3))