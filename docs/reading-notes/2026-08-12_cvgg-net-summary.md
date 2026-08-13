\# Reading Summary: CVGG-Net — Complex-Valued CNN for SAR Ship Recognition



\*\*Source:\*\* Zhao, D. et al., "CVGG-Net: Ship Recognition for SAR Images Based on 

Complex-Valued Convolutional Neural Network," arXiv:2305.07918



\## Problem

Most SAR target recognition CNNs operate only on magnitude (amplitude) images, 

throwing away the phase component of the raw complex-valued SAR signal. The 

authors argue this discards information that is physically meaningful for 

target discrimination.



\## Method

\- Proposes CVGG-Net: a VGG16-style architecture where every layer — convolution, 

&#x20; batch norm, activation, pooling — operates natively in the complex domain, so 

&#x20; both amplitude and phase flow through the network.

\- Complex convolution is implemented by treating each filter and input as a 

&#x20; complex number (real + imaginary parts) and expanding the convolution algebraically, 

&#x20; which is equivalent to four real-valued convolutions combined.

\- Introduces "Complex Area Max-Pooling" — a new pooling rule that picks the 

&#x20; pooling location based on the area of the real/imaginary rectangle (|x·y|) 

&#x20; rather than just picking the largest-magnitude value. This tends to retain 

&#x20; points where both real and imaginary parts are strong, rather than pixels 

&#x20; that are large in only one component.

\- Compares CReLU, CTanh, CElu, CPReLU as complex activation functions; CReLU 

&#x20; (ReLU applied separately to real and imaginary parts) performs best.



\## Results

\- Tested on two real SAR ship datasets (CSRSDD and OpenSARShip).

\- CVGG-Net outperforms real-valued baselines (Vnet5, ResNet18, VGG16) on both 

&#x20; datasets (e.g., 79.57% vs. 75.57% for ResNet18 on CSRSDD).

\- The new area-based pooling consistently beats the older amplitude-based 

&#x20; pooling by \~0.3–0.9 percentage points across architectures.



\## Why it matters for PhaseSAR-Net

This is direct empirical evidence that preserving phase information — rather 

than collapsing to magnitude-only grayscale — measurably improves SAR target 

recognition accuracy. It validates the core premise of a phase-aware approach 

and gives a concrete architectural pattern (complex conv + complex batchnorm + 

complex activation + complex pooling) that I can reference when designing my 

own pipeline.

