"""
src/models/baseline_cnn.py

A plain, magnitude-only CNN — the "standard deep learning" comparison
point for the phase-aware model. Nothing exotic: ~5-6 conv blocks,
batch norm, ReLU, global pooling, and a linear classifier head.

Run this file directly for a forward-pass sanity check + parameter count:
    python src/models/baseline_cnn.py
"""

import torch
import torch.nn as nn


class ConvBlock(nn.Module):
    """One conv -> batchnorm -> relu block."""

    def __init__(self, in_channels: int, out_channels: int, stride: int = 1):
        super().__init__()
        self.conv = nn.Conv2d(in_channels, out_channels, kernel_size=3,
                               stride=stride, padding=1, bias=False)
        self.bn = nn.BatchNorm2d(out_channels)
        self.act = nn.ReLU(inplace=True)

    def forward(self, x):
        return self.act(self.bn(self.conv(x)))


class BaselineCNN(nn.Module):
    """
    Magnitude-only baseline CNN.
    Input:  (B, 1, H, W) real-valued magnitude images.
    Output: (B, num_classes) logits.
    """

    def __init__(self, num_classes: int = 10, in_channels: int = 1):
        super().__init__()
        channels = [in_channels, 16, 32, 64, 64, 128, 128]
        blocks = []
        for i in range(len(channels) - 1):
            # downsample every other block to keep spatial size manageable
            stride = 2 if i % 2 == 1 else 1
            blocks.append(ConvBlock(channels[i], channels[i + 1], stride=stride))
        self.features = nn.Sequential(*blocks)
        self.pool = nn.AdaptiveAvgPool2d(1)
        self.classifier = nn.Linear(channels[-1], num_classes)

    def forward(self, x):
        x = self.features(x)
        x = self.pool(x).flatten(1)
        return self.classifier(x)


def count_parameters(model: nn.Module) -> int:
    return sum(p.numel() for p in model.parameters() if p.requires_grad)


if __name__ == "__main__":
    model = BaselineCNN(num_classes=10, in_channels=1)

    # Forward-pass sanity check on a fake batch of SAR-sized chips.
    dummy_input = torch.randn(4, 1, 128, 128)  # (batch, channel, H, W)
    output = model(dummy_input)

    print(f"Input shape:  {tuple(dummy_input.shape)}")
    print(f"Output shape: {tuple(output.shape)}")
    assert output.shape == (4, 10), "unexpected output shape"

    total_params = count_parameters(model)
    print(f"Total trainable parameters: {total_params:,}")
    print("\nBaselineCNN forward-pass sanity check passed.")