import sys
import os
import numpy as np
import matplotlib.pyplot as plt

sys.path.append(os.getcwd())  # so `src` imports work when run from project root

from src.augment.blur import add_blur
from src.augment.phase_distortion import add_phase_distortion

# --- Load a sample chip ---
# Replace this with your actual loader, e.g.:
# from src.data.sar_dataset import SARDataset
# chip = ...load one real MSTAR chip as a complex64 array...

# Placeholder synthetic chip so the script runs even before you wire a real loader:
chip = (np.random.randn(128, 128) + 1j * np.random.randn(128, 128)).astype(np.complex64)

blurred = add_blur(chip)
distorted = add_phase_distortion(chip)

os.makedirs("results", exist_ok=True)

fig, axes = plt.subplots(1, 3, figsize=(12, 4))
axes[0].imshow(np.abs(chip)); axes[0].set_title("Clean")
axes[1].imshow(np.abs(blurred)); axes[1].set_title("Blurred")
axes[2].imshow(np.abs(distorted)); axes[2].set_title("Phase-distorted")
plt.savefig("results/blur_phase_before_after.png")
print("Saved results/blur_phase_before_after.png")