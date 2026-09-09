import numpy as np

def add_speckle_noise(chip: np.ndarray, look_number: int = 4) -> np.ndarray:
    """Multiplicative Gamma-distributed speckle, applied to amplitude.
    look_number controls speckle severity (lower = noisier).
    """
    amplitude = np.abs(chip)
    phase = np.angle(chip)
    speckle = np.random.gamma(shape=look_number, scale=1.0 / look_number, size=amplitude.shape)
    noisy_amp = amplitude * speckle
    return (noisy_amp * np.exp(1j * phase)).astype(np.complex64)

if __name__ == "__main__":
    dummy = (np.ones((32, 32)) + 1j * np.ones((32, 32))).astype(np.complex64)
    out = add_speckle_noise(dummy)
    assert out.shape == dummy.shape and out.dtype == np.complex64
    print("speckle_noise.py test passed.")
