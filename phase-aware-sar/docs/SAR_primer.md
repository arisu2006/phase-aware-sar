# SAR Primer — Day 1 Notes

**Project:** PhaseSAR-Net — Phase-Aware SAR Intelligence for Robust Scene Classification
**Date:** 10 Aug 2026
**Author:** Gourav

## What SAR is, and how it differs from optical imaging

Synthetic Aperture Radar (SAR) is an active imaging system: it transmits its own microwave
pulses and images by measuring what bounces back, rather than passively capturing reflected
sunlight like an optical camera. Because it supplies its own illumination and works at
microwave wavelengths (typically 1 cm – 1 m), it can image through cloud cover, smoke, and
darkness — conditions that make optical sensors useless.

"Synthetic aperture" refers to how the platform (usually a satellite or aircraft) synthesizes
a very large virtual antenna by combining radar echoes collected as it moves along its flight
path. This gives SAR far finer spatial resolution than a physically small real antenna could
achieve on its own.

## All-weather, day-night capability

Because SAR doesn't depend on sunlight or clear skies, it can acquire imagery on a fixed
revisit schedule regardless of weather or time of day. This is the core reason SAR is used
for defense, disaster response, and maritime monitoring — domains where optical imagery might
simply be unavailable when it's needed most.

## Amplitude vs. complex-valued (I/Q) data

Every SAR pixel is measured as a complex number, typically stored as **I** (in-phase) and
**Q** (quadrature) components, or equivalently as amplitude and phase:

- **Amplitude** (magnitude of the complex value) reflects how strongly a surface backscatters
  the radar signal — this is what conventional SAR classifiers (and most public datasets)
  use, since it can be rendered as a grayscale image similar to an optical photo.
- **Phase** encodes the precise timing/path-length of the return signal. It's usually
  discarded in amplitude-only pipelines, but it carries information about surface structure,
  sub-pixel displacement, and coherence that amplitude alone loses.

**This distinction is the central hypothesis of PhaseSAR-Net**: standard SAR scene
classifiers that only use amplitude may be discarding phase information that could make
classification more robust to noise/corruption — this project tests whether a phase-aware
(complex-valued) model is measurably more robust than an amplitude-only baseline.

## Basic radar imaging geometry

- The radar looks **sideways** (side-looking geometry), not straight down, to avoid the
  left-right ambiguity that would occur with a nadir-pointing beam.
- **Range** is the across-track direction (distance from sensor to target); **azimuth** is the
  along-track (flight direction).
- **Incidence angle** (angle between the radar beam and vertical) affects backscatter
  strength and causes geometric distortions specific to SAR: **foreshortening** (slopes facing
  the radar appear compressed), **layover** (tall objects appear to lean toward the sensor),
  and **shadow** (areas blocked from the beam show no return).
- **Speckle** is a grainy, multiplicative noise pattern inherent to coherent imaging systems
  like SAR — distinct from the additive noise typical in optical sensors, and a key
  corruption type this project may need to simulate/test against.

## Why this matters for the project

PhaseSAR-Net is framed as **AI reliability / robustness research**: does model compression or
input corruption break phase-aware SAR classification more or less than it breaks a standard
amplitude-only baseline? Today's primer establishes the minimum domain vocabulary
(amplitude/phase, geometry, speckle) needed to read papers and design experiments for the
rest of Phase 1.
