import torch
import torch.nn.functional as F

class SARCorruptionLibrary:
    def __init__(self, severity: str = "moderate"):
        self.severity = severity
        self.severity_scales = {
            "mild": 0.1,
            "moderate": 0.3,
            "severe": 0.5
        }
        self.scale = self.severity_scales.get(severity, 0.3)

    def add_speckle_noise(self, x: torch.Tensor) -> torch.Tensor:
        # Multiplicative Gamma/Rayleigh-like speckle noise for SAR
        noise = torch.randn_like(x) * self.scale
        return x * (1.0 + noise)

    def add_gaussian_noise(self, x: torch.Tensor) -> torch.Tensor:
        noise = torch.randn_like(x) * self.scale
        return x + noise

    def apply_blur(self, x: torch.Tensor) -> torch.Tensor:
        # Platform-jitter blur via local averaging
        kernel_size = 3 if self.scale < 0.2 else 5
        padding = kernel_size // 2

        if x.ndim == 2:
            x_in = x.unsqueeze(0).unsqueeze(0)
            kernel = torch.ones((1, 1, kernel_size, kernel_size), dtype=x.dtype, device=x.device) / (kernel_size * kernel_size)
            out = F.conv2d(x_in, kernel, padding=padding)
            return out.squeeze(0).squeeze(0)
        elif x.ndim == 3:
            channels = x.shape[0]
            x_in = x.unsqueeze(0)  # Shape: [1, C, H, W]
            kernel = torch.ones((channels, 1, kernel_size, kernel_size), dtype=x.dtype, device=x.device) / (kernel_size * kernel_size)
            out = F.conv2d(x_in, kernel, padding=padding, groups=channels)
            return out.squeeze(0)
        return x

    def corrupt(self, x: torch.Tensor, corruption_type: str) -> torch.Tensor:
        if corruption_type == "speckle":
            return self.add_speckle_noise(x)
        elif corruption_type == "gaussian":
            return self.add_gaussian_noise(x)
        elif corruption_type == "blur":
            return self.apply_blur(x)
        else:
            raise ValueError(f"Unknown corruption type: {corruption_type}")