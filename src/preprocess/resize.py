import numpy as np

def center_crop_resize(chip: dict, target_size=128, pad_mode="reflect"):
    real, imag = chip["real"], chip["imag"]
    h, w = real.shape

    def crop_or_pad(arr):
        if h >= target_size and w >= target_size:
            top, left = (h - target_size) // 2, (w - target_size) // 2
            return arr[top:top + target_size, left:left + target_size]

        pad_h, pad_w = max(0, target_size - h), max(0, target_size - w)
        return np.pad(arr, ((pad_h // 2, pad_h - pad_h // 2),
                            (pad_w // 2, pad_w - pad_w // 2)), mode=pad_mode)

    return {"real": crop_or_pad(real), "imag": crop_or_pad(imag)}