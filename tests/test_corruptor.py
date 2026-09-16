import torch
from src.augment.corruptor import SARCorruptionLibrary

def test_corruptor():
    corruptor = SARCorruptionLibrary(severity="moderate")
    dummy_tensor = torch.randn(2, 64, 64)

    for c_type in ["speckle", "gaussian", "blur"]:
        out = corruptor.corrupt(dummy_tensor, c_type)
        assert out.shape == dummy_tensor.shape, f"Shape mismatch for {c_type}"
    print("All corruption unit tests passed.")

if __name__ == "__main__":
    test_corruptor()