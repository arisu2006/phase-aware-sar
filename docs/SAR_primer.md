# SAR Primer

## 1. What SAR Is, and How It Differs From Optical Imaging
Synthetic Aperture Radar (SAR) is an active imaging system: it transmits its own microwave pulses toward the ground and builds an image from the echoes that bounce back, rather than passively recording reflected sunlight like an optical camera. Because it supplies its own illumination, SAR does not depend on the sun and is unaffected by cloud cover, haze, or smoke.

A SAR platform has a physically small antenna, which would normally give poor angular resolution. SAR overcomes this by exploiting platform motion: as it flies along its track, it takes many measurements of the same ground patch from different positions and combines them coherently (using amplitude AND phase) to synthesize a much larger "virtual" antenna — hence "synthetic aperture."

SAR images record radar backscatter (surface roughness, dielectric properties, geometry), not reflected color like optical sensors. A metal object or wet rough surface can appear bright in SAR while looking unremarkable optically; smooth surfaces (water, asphalt) appear dark due to specular reflection.

## 2. All-Weather, Day-Night Capability
Because SAR is active and uses microwave wavelengths, it works identically at night and through most weather conditions. This is the primary operational reason SAR is favored for defense and disaster-monitoring — optical/infrared sensors are often blind under cloud cover or at night.

## 3. Amplitude vs. Complex-Valued (I/Q) Data
Raw SAR data at each pixel is a complex number: I/Q components, or equivalently amplitude and phase (z = I + jQ = A·e^(jφ)).

- **Amplitude-only (magnitude):** captures backscatter strength; most public datasets (e.g. MSTAR chips) are distributed this way. Phase is lost.
- **Complex-valued (I/Q):** captures both strength and phase — full raw information.

Phase encodes sub-wavelength path-length differences (enabling interferometry) and fine scattering-mechanism detail — this is the core motivation for a phase-aware/complex-valued model.

## 4. Basic Radar Imaging Geometry
- **Side-looking geometry:** SAR looks obliquely, not straight down, to resolve range ambiguity.
- **Range direction:** across-track; resolution comes from pulse bandwidth.
- **Azimuth direction:** along-track; resolution comes from the synthetic aperture.
- **Depression/incidence angle:** affects shadowing, layover, foreshortening.
- **Layover & shadow:** tall objects can lean toward the sensor (layover); areas behind them go radar-dark (shadow).