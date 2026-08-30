import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from src.data.loader import load_mstar_chip

metadata_df = pd.read_csv("data/metadata.csv")
file_col = "file_path" if "file_path" in metadata_df.columns else "filepath"

# 1. Class balance
metadata_df["class"].value_counts().plot(kind="bar", title="Class balance")
plt.tight_layout()
plt.savefig("notebooks/figs/class_balance.png")
plt.clf()

# 2. Chip-size distribution (sample first 200)
sample_paths = metadata_df[file_col].iloc[:200]
sizes = [load_mstar_chip(f)["magnitude"].shape for f in sample_paths]
heights, widths = zip(*sizes)
plt.hist(heights, bins=20, alpha=0.6, label="height")
plt.hist(widths, bins=20, alpha=0.6, label="width")
plt.legend()
plt.title("Chip size distribution")
plt.tight_layout()
plt.savefig("notebooks/figs/chip_sizes.png")
plt.clf()

# 3. Log-amplitude histogram (sample first 50)
sample_amp = np.concatenate([load_mstar_chip(f)["magnitude"].flatten() for f in metadata_df[file_col].iloc[:50]])
plt.hist(np.log1p(sample_amp), bins=100)
plt.title("Log-amplitude histogram")
plt.tight_layout()
plt.savefig("notebooks/figs/amp_hist.png")
plt.clf()

# 4. Amplitude + phase maps per class
sample_classes = metadata_df["class"].unique()[:4]
fig, axes = plt.subplots(2, len(sample_classes), figsize=(3 * len(sample_classes), 6))
for i, cls in enumerate(sample_classes):
    f = metadata_df[metadata_df["class"] == cls][file_col].iloc[0]
    chip = load_mstar_chip(f)
    axes[0, i].imshow(chip["magnitude"], cmap="gray")
    axes[0, i].set_title(f"{cls} - Mag")
    axes[0, i].axis("off")

    phase_map = chip.get("phase", np.zeros_like(chip["magnitude"]))
    axes[1, i].imshow(phase_map, cmap="twilight")
    axes[1, i].set_title(f"{cls} - Phase")
    axes[1, i].axis("off")

plt.tight_layout()
plt.savefig("notebooks/figs/class_samples.png")
plt.close()

print("EDA figures saved to notebooks/figs/")