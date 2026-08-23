import sys
sys.path.append('.')
from src.loader import load_mstar_chip
import glob
import matplotlib.pyplot as plt

sample_files = glob.glob('data/raw/mstar/*.JPG')

for i, f in enumerate(sample_files):
    chip = load_mstar_chip(f)
    print(f)
    print("Shape:", chip["magnitude"].shape, "Dtype:", chip["magnitude"].dtype)
    print("Min/Max/Mean:", chip["magnitude"].min(), chip["magnitude"].max(), chip["magnitude"].mean())
    print("---")

    plt.imshow(chip["magnitude"], cmap='gray')
    plt.title(f)
    plt.savefig(f"notebooks/preview_{i}.png")
    plt.close()

print("Done. Check notebooks/ folder for preview_0.png through preview_4.png")