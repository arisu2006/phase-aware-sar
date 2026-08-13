\# Summary: Complex-Valued CNNs for Phase-Aware SAR Classification



\## Key Takeaways

\- \*\*Complex-Valued Representation:\*\* Standard CNNs discard phase information by only utilizing magnitude. Complex-Valued CNNs (CV-CNNs) retain both amplitude and phase to capture rich scattering dynamics in Synthetic Aperture Radar (SAR) imagery.

\- \*\*Activation Function:\*\* Uses complex non-linear activation functions, specifically magnitude-based scaling:

&#x20; 

&#x20; $$f(A, B) = \\sqrt{A^2 + B^2}$$



&#x20; where $A$ is the real component and $B$ is the imaginary component of the complex pixel value.

\- \*\*Performance Gain:\*\* Reconstructing phase structure improves class separation, especially for target recognition under structural speckle and non-stationary clutter.

\-

