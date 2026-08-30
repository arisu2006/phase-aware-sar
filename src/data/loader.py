from PIL import Image
import numpy as np
import os

def load_mstar_chip(filepath):
    """Loads a JPG-format MSTAR chip and returns it as a numpy array."""
    img = Image.open(filepath).convert('L')  # 'L' = grayscale (amplitude only)
    array = np.array(img)
    return {"magnitude": array, "filepath": filepath}