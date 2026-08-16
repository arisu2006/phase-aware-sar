## Aug 13, 2026
- Read + summarized 2 papers on phase-aware/complex-valued SAR classification
- Refined problem statement
- Files: notes/paper1_complex_cnn_summary.md, notes/paper2_mstar_benchmark_summary.md, notes/problem_statement.md

## Aug 14
* Registered for MSTAR dataset access on AFRL/SDMS portal (pending clearance).
* Downloaded and isolated fallback sample `bulkcarrier_1.tiff` into `data/raw/`.
* Created and executed `src/inspect_data.py` to inspect file header.
* Confirmed TIFF standard image payload (`II*` magic bytes) and logged specifications in `notes/dataset_notes.md`.

## Aug 17, 2026 (Day 6)
- Studied complex-valued NN fundamentals (Trabelsi et al., Deep Complex Networks)
- Wrote notes/complex_nn_primer.md covering complex conv, complex batchnorm, modReLU/CReLU
- Scaffolded src/complex_layers.py (ComplexConv2d, ModReLU) — verified import works
- MSTAR access still pending; continuing on FUSAR-Ship backup sample