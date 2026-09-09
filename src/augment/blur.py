import numpy as np
from scipy.ndimage import gaussian_filter

def add_blur(chip: np.ndarray, sigma: float = 1.0) -> np.ndarray:
    """Platform-jitter-style blur, applied independently to real/imag."""
    real = gaussian_filter(chip.real, sigma=sigma)
    imag = gaussian_filter(chip.imag, sigma=sigma)
    return (real + 1j * imag).astype(np.complex64)

if __name__ == "__main__":
    dummy = (np.ones((32, 32)) + 1j * np.ones((32, 32))).astype(np.complex64)
    out = add_blur(dummy)
    assert out.shape == dummy.shape and out.dtype == np.complex64
    print("blur.py test passed.")
