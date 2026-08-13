\# Problem Statement (Refined — Day 3)



Standard SAR Automatic Target Recognition pipelines convert complex-valued 

radar returns into magnitude-only grayscale images before feeding them to a 

CNN, discarding the phase component of the signal. Phase encodes fine-grained, 

physically meaningful information — including scattering-mechanism differences 

(surface, double-bounce, volume scattering) and sub-wavelength positional 

precision — that magnitude alone cannot capture. Recent work on complex-valued 

CNNs (e.g., CVGG-Net) shows that models which process amplitude and phase 

jointly outperform real-valued baselines on real SAR datasets, suggesting 

phase-aware processing carries genuine discriminative value rather than being 

redundant with magnitude.



At the same time, the field's dominant benchmark, MSTAR, is known to reward 

shortcut learning: its centered targets, fixed chip dimensions, minimal 

clutter, and single-object framing let models achieve high accuracy without 

learning robust, physically grounded target representations. High MSTAR 

accuracy alone is therefore not sufficient evidence that a model — phase-aware 

or otherwise — has learned meaningful SAR-specific features.



This project (PhaseSAR-Net) aims to build a phase-aware SAR classification 

approach that demonstrably benefits from preserved phase information, while 

being explicit and rigorous about what MSTAR-based accuracy numbers can and 

cannot claim — including, where feasible, evaluation beyond MSTAR's Standard 

Operating Condition to test whether phase-awareness improves robustness under 

more realistic, perturbed conditions.

