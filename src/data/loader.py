import numpy as np
from PIL import Image

def load_mstar_chip(filepath):
    # Load amplitude / magnitude
    img = Image.open(filepath).convert("L")
    magnitude = np.array(img, dtype=np.float32)

    # If complex phase is not embedded in standard image files, create a phase array
    phase = np.zeros_like(magnitude, dtype=np.float32)

    return {
        "magnitude": magnitude,
        "phase": phase
    }