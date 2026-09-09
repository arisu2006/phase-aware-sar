# Data Pipeline and Regeneration Guide

## Overview
This directory manages raw MSTAR complex radar chips and their transformation pipeline.

## Regeneration Steps
1. Place raw MSTAR files into `data/raw/`.
2. Run metadata extraction:
   ```bash
   python create_metadata.py
   ```
3. The PyTorch data pipeline (`src/data/sar_dataset.py`) chains:
   - **Raw Loading**: `src.data.loader.load_mstar_chip`
   - **Cropping**: `src.preprocess.resize.center_crop_resize` (Target: 128x128)
   - **Representation & Normalization**: `src.preprocess.representation.get_representation`
     - `ap`: 3-channel [Normalized Amplitude, Phase Sin, Phase Cos]
     - `ri`: 2-channel [Normalized Real, Normalized Imaginary]

## Expected Output Structure
- Output batch shape (`ap` mode): `[B, 3, 128, 128]`
- Output batch shape (`ri` mode): `[B, 2, 128, 128]`
- Tensor dtype: `torch.float32`
