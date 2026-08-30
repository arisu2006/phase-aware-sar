\# Data Pipeline Documentation



This document describes the end-to-end pipeline for loading, splitting, and inspecting the MSTAR radar dataset.



\## Pipeline Architecture

`Raw MSTAR files` → `src/data/loader.py` (parsing) → `src/data/splits.py` (SOC split) → `notebooks/01\_eda.py` (inspection)



\---



\## 1. Loader (`src/data/loader.py`)

\- Reads raw SAR image files into magnitude and phase arrays.

\- Normalizes dimensions and returns numerical numpy representations.



\*\*Validation Command:\*\*

```bash

python -m notebooks.validate\_loader

