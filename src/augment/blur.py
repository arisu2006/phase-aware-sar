# src/augment/blur.py
import numpy as np
from scipy.ndimage import gaussian_filter

def add_blur(chip: np.ndarray, sigma: float = 1.0) -> np.ndarray:
    real = gaussian_filter(chip.real, sigma=sigma)
    imag = gaussian_filter(chip.imag, sigma=sigma)
    return (real + 1j * imag).astype(np.complex64)