\# Radar Chip Resizing \& Cropping Strategy (2026-08-29)



\- \*\*Target Dimensions\*\*: Standardize all chips to 128x128 pixels.

\- \*\*Center-Cropping\*\*: Since vehicle targets in MSTAR chips are centered, cropping symmetrically retains target scatterers while discarding surrounding background clutter.

\- \*\*Padding\*\*: For chips smaller than 128x128, apply symmetric reflection padding (`pad\_mode="reflect"`) instead of stretching to prevent spatial distortion.

\- \*\*Complex Domain Integrity\*\*: Process the Cartesian components (`real` and `imag`) directly rather than interpolating polar phase angles to prevent phase-wrapping artifacts.

