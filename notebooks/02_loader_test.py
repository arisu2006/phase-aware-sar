import sys
sys.path.append('.')
from src.loader import load_mstar_chip
import glob

sample_files = glob.glob('data/raw/mstar/*.JPG')

for f in sample_files:
    chip = load_mstar_chip(f)
    print(f)
    print("Shape:", chip["magnitude"].shape, "Dtype:", chip["magnitude"].dtype)
    print("Min/Max/Mean:", chip["magnitude"].min(), chip["magnitude"].max(), chip["magnitude"].mean())
    print("---")