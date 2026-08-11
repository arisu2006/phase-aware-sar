# PhaseSAR-Net

**Phase-Aware SAR Intelligence for Robust Scene Classification and Change Analysis**

Solo research project investigating whether phase-aware (complex-valued) SAR models are more
robust to noise, corruption, and compression than standard amplitude-only SAR classifiers.
Framed as AI reliability / robustness research for a defense-sector audience.

## Status

🚧 Day 1 of 113 — Phase 1: Foundation, SAR Basics & Scope Lock (10–19 Aug 2026)

## Repo structure

```
phase-aware-sar/
├── data/         # raw and processed SAR datasets (gitignored, see data/README if added)
├── src/          # model, preprocessing, and training code
├── notebooks/    # exploratory analysis and visualization
├── configs/      # experiment configs (YAML/JSON)
├── tests/        # unit and integration tests
├── docs/         # research notes, primers, write-ups
├── requirements.txt
└── README.md
```

## Project framing

This project asks: **does compression or corruption break phase-aware SAR classification more
than it breaks a standard amplitude-only baseline?** It is positioned as AI reliability /
robustness research, not a remote-sensing application paper — the goal is to quantify failure
modes under compression and corruption, with results reported via a tagged GitHub release and
`RESULTS.md` update at the end of every phase.

## Setup

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Progress log

See `docs/` for daily research notes, starting with `docs/SAR_primer.md` (Day 1).
