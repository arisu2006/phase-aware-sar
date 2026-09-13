"""
src/augment/corruptor.py

SARCorruptionLibrary: applies clean / mild / severe corruption presets
to SAR chip images (noise + blur + composed corruptions).

Run this file directly to execute the built-in unit tests:
    python src/augment/corruptor.py
"""

import numpy as np


class SARCorruptionLibrary:
    """
    Bundles the individual corruption functions (noise, blur, composition)
    into named severity presets: 'clean', 'mild', 'severe'.
    """

    def __init__(self, seed: int = 42):
        self.rng = np.random.default_rng(seed)

    # ---- individual corruption primitives ----

    def add_speckle_noise(self, img: np.ndarray, level: float) -> np.ndarray:
        """Multiplicative speckle noise, typical of SAR imagery.
        Higher `level` => stronger, more visible distortion."""
        noise = self.rng.standard_normal(size=img.shape)
        return np.clip(img * (1.0 + level * noise), 0, 1)

    def blur(self, img: np.ndarray, kernel_size: int) -> np.ndarray:
        """Simple box blur to simulate resolution degradation."""
        if kernel_size <= 1:
            return img
        pad = kernel_size // 2
        padded = np.pad(img, pad, mode="reflect")
        out = np.zeros_like(img)
        for i in range(img.shape[0]):
            for j in range(img.shape[1]):
                out[i, j] = padded[i:i + kernel_size, j:j + kernel_size].mean()
        return out

    def compose(self, img: np.ndarray, ops: list) -> np.ndarray:
        """Apply a list of (function, kwargs) pairs in sequence."""
        result = img.copy()
        for fn, kwargs in ops:
            result = fn(result, **kwargs)
        return result

    # ---- named severity presets ----

    def apply(self, img: np.ndarray, preset: str) -> np.ndarray:
        if preset == "clean":
            return img.copy()
        elif preset == "mild":
            return self.compose(img, [
                (self.add_speckle_noise, {"level": 0.05}),
                (self.blur, {"kernel_size": 2}),
            ])
        elif preset == "severe":
            return self.compose(img, [
                (self.add_speckle_noise, {"level": 0.25}),
                (self.blur, {"kernel_size": 4}),
            ])
        else:
            raise ValueError(f"Unknown preset: {preset}")


# ---- unit tests ----

def _make_test_image():
    rng = np.random.default_rng(0)
    return rng.uniform(0, 1, size=(32, 32))


def test_clean_is_unchanged():
    lib = SARCorruptionLibrary()
    img = _make_test_image()
    out = lib.apply(img, "clean")
    assert np.allclose(img, out), "clean preset should not modify the image"
    print("PASS: clean preset leaves image unchanged")


def test_mild_changes_image_but_stays_bounded():
    lib = SARCorruptionLibrary()
    img = _make_test_image()
    out = lib.apply(img, "mild")
    assert not np.allclose(img, out), "mild preset should change the image"
    assert out.min() >= 0 and out.max() <= 1, "output must stay in [0, 1]"
    print("PASS: mild preset changes image and stays in range")


def test_severe_is_more_distorted_than_mild():
    lib = SARCorruptionLibrary()
    img = _make_test_image()
    mild = lib.apply(img, "mild")
    severe = lib.apply(img, "severe")
    mild_diff = np.abs(img - mild).mean()
    severe_diff = np.abs(img - severe).mean()
    assert severe_diff > mild_diff, "severe should distort more than mild"
    print(f"PASS: severe distortion ({severe_diff:.4f}) > mild ({mild_diff:.4f})")


def test_unknown_preset_raises():
    lib = SARCorruptionLibrary()
    img = _make_test_image()
    try:
        lib.apply(img, "not_a_real_preset")
        raise AssertionError("expected ValueError for unknown preset")
    except ValueError:
        print("PASS: unknown preset raises ValueError as expected")


if __name__ == "__main__":
    test_clean_is_unchanged()
    test_mild_changes_image_but_stays_bounded()
    test_severe_is_more_distorted_than_mild()
    test_unknown_preset_raises()
    print("\nAll corruptor.py unit tests passed.")