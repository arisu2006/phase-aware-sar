import numpy as np

def add_gaussian_noise(chip: np.ndarray, sigma: float = 0.05) -> np.ndarray:
    """Additive Gaussian noise on real/imag components independently."""
    noise = (np.random.normal(0, sigma, chip.shape)
             + 1j * np.random.normal(0, sigma, chip.shape))
    return (chip + noise).astype(np.complex64)

if __name__ == "__main__":
    dummy = (np.ones((32, 32)) + 1j * np.ones((32, 32))).astype(np.complex64)
    out = add_gaussian_noise(dummy)
    assert out.shape == dummy.shape and out.dtype == np.complex64
    print("gaussian_noise.py test passed.")
