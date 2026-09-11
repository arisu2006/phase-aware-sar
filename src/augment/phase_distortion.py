# src/augment/phase_distortion.py
import numpy as np

def add_phase_distortion(chip: np.ndarray, max_shift: float = 0.3) -> np.ndarray:
    amplitude = np.abs(chip)
    phase = np.angle(chip)
    perturb = np.random.uniform(-max_shift, max_shift, phase.shape)
    new_phase = np.angle(np.exp(1j * (phase + perturb)))
    return (amplitude * np.exp(1j * new_phase)).astype(np.complex64)