from typing import Literal
import numpy as np
from src.preprocess.normalize import normalize_complex_chip

Representation = Literal["ap", "ri"]


def to_amplitude_phase(norm_out: dict) -> np.ndarray:
    # (3, H, W): [amplitude, sin(phase), cos(phase)]
    return np.stack(
        [
            norm_out["amplitude_norm"],
            norm_out["phase_sin"],
            norm_out["phase_cos"],
        ],
        axis=0,
    )


def to_real_imag(complex_chip: np.ndarray, amp_max: float) -> np.ndarray:
    amplitude = np.abs(complex_chip)
    phase = np.angle(complex_chip)
    amp_norm = np.clip(np.log1p(amplitude) / amp_max, 0.0, 1.0)
    real = amp_norm * np.cos(phase)
    imag = amp_norm * np.sin(phase)
    return np.stack([real, imag], axis=0).astype(np.float32)  # (2, H, W)


def get_representation(
    complex_chip: np.ndarray,
    mode: Representation = "ap",
    amp_max: float | None = None,
):
    norm_out = normalize_complex_chip(complex_chip, amp_max=amp_max)
    if mode == "ap":
        return to_amplitude_phase(norm_out)
    elif mode == "ri":
        return to_real_imag(complex_chip, amp_max=norm_out["amp_max"])
    raise ValueError(f"Unknown mode: {mode!r}")


if __name__ == "__main__":
    rng = np.random.default_rng(2)
    fake_chip = (
        rng.normal(size=(64, 64)) + 1j * rng.normal(size=(64, 64))
    ).astype(np.complex64)
    fake_chip[10:14, 10:14] *= 40.0

    ap = get_representation(fake_chip, mode="ap")
    ri = get_representation(fake_chip, mode="ri")

    assert ap.shape == (3, 64, 64)
    assert ri.shape == (2, 64, 64)
    print("representation.py self-test passed.")