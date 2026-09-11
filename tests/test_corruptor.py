import numpy as np
from src.augment.corruptor import SARCorruptionLibrary

def test_apply_shapes_preserved():
    chip = (np.random.randn(64, 64) + 1j * np.random.randn(64, 64)).astype(np.complex64)
    lib = SARCorruptionLibrary(severity="mild")
    out = lib.apply(chip)
    assert out.shape == chip.shape
    assert out.dtype == np.complex64