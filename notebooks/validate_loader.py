from src.data.loader import load_mstar_chip
import glob

sample_files = glob.glob("data/raw/**/*.001", recursive=True)[:5]
for f in sample_files:
    chip = load_mstar_chip(f)
    print(f, {k: (v.shape, v.dtype, float(v.min()), float(v.max())) for k, v in chip.items()})