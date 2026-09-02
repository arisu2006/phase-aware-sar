import numpy as np

EPS = 1e-6


def log_amplitude_normalize(amplitude: np.ndarray, amp_max: float | None = None):
    log_amp = np.log1p(amplitude.astype(np.float64))  # log(1+x), stable at 0
    if amp_max is None:
        amp_max = float(log_amp.max() + EPS)
    normalized = np.clip(log_amp / amp_max, 0.0, 1.0)
    return normalized.astype(np.float32), amp_max


def wrap_phase(phase: np.ndarray) -> np.ndarray:
    return (phase + np.pi) % (2 * np.pi) - np.pi


def phase_to_sin_cos(phase: np.ndarray):
    phase = wrap_phase(phase)
    return np.sin(phase).astype(np.float32), np.cos(phase).astype(np.float32)


def normalize_complex_chip(
    complex_chip: np.ndarray, amp_max: float | None = None
):
    amplitude = np.abs(complex_chip)
    phase = np.angle(complex_chip)  # already in [-pi, pi]

    amp_norm, amp_max_used = log_amplitude_normalize(amplitude, amp_max=amp_max)
    phase_wrapped = wrap_phase(phase)
    sin_p, cos_p = phase_to_sin_cos(phase_wrapped)

    return {
        "amplitude_norm": amp_norm,
        "phase_wrapped": phase_wrapped,
        "phase_sin": sin_p,
        "phase_cos": cos_p,
        "amp_max": amp_max_used,
    }


if __name__ == "__main__":
    rng = np.random.default_rng(0)
    fake_chip = (
        rng.normal(size=(64, 64)) + 1j * rng.normal(size=(64, 64))
    ).astype(np.complex64)
    fake_chip[20:24, 20:24] *= 50.0  # simulate a strong scatterer

    out = normalize_complex_chip(fake_chip)
    assert 0.0 <= out["amplitude_norm"].min() and out["amplitude_norm"].max() <= 1.0
    assert (
        -np.pi <= out["phase_wrapped"].min()
        and out["phase_wrapped"].max() <= np.pi
    )
    print("normalize.py self-test passed.")