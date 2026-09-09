import numpy as np

def add_phase_distortion(chip: np.ndarray, max_shift: float = 0.3) -> np.ndarray:
    """Random phase perturbation, re-wrapped to [-pi, pi]."""
    amplitude = np.abs(chip)
    phase = np.angle(chip)
    perturb = np.random.uniform(-max_shift, max_shift, phase.shape)
    new_phase = np.angle(np.exp(1j * (phase + perturb)))  # wraps correctly
    return (amplitude * np.exp(1j * new_phase)).astype(np.complex64)

if __name__ == "__main__":
    dummy = (np.ones((32, 32)) + 1j * np.ones((32, 32))).astype(np.complex64)
    out = add_phase_distortion(dummy)
    assert out.shape == dummy.shape and out.dtype == np.complex64
    print("phase_distortion.py test passed.")
