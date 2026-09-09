import torch
from torch.utils.data import Dataset
import numpy as np
from src.preprocess.resize import center_crop_resize
from src.preprocess.representation import get_representation

try:
    from src.data.loader import load_mstar_chip
except ImportError:
    load_mstar_chip = None

class SARDataset(Dataset):
    def __init__(self, file_paths: list[str], labels: list[int], target_size: int = 128, rep_mode: str = "ap"):
        self.file_paths = file_paths
        self.labels = labels
        self.target_size = target_size
        self.rep_mode = rep_mode

    def __len__(self) -> int:
        return len(self.file_paths)

    def _load_raw(self, path: str) -> np.ndarray:
        if load_mstar_chip is not None:
            return load_mstar_chip(path)
        raise NotImplementedError("Connect _load_raw to your existing loader")

    def __getitem__(self, idx: int):
        chip = self._load_raw(self.file_paths[idx])
        chip = center_crop_resize(chip, self.target_size)
        rep = get_representation(chip, mode=self.rep_mode)
        return torch.from_numpy(rep).float(), self.labels[idx]

if __name__ == "__main__":
    print("sar_dataset.py defined successfully")
