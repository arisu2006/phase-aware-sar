# Complex-Valued Neural Network Primer

Reference: Trabelsi et al., *"Deep Complex Networks"* (ICLR 2018)

## Motivation

Standard CNNs operate on real-valued tensors. SAR data is inherently complex-valued —
each pixel is $z = x + iy$, where $x$ is the in-phase (I) component and $y$ is the
quadrature (Q) component. Converting to magnitude-only ($|z| = \sqrt{x^2 + y^2}$)
discards the phase term $\theta = \arctan(y/x)$, which encodes scattering-mechanism
and path-length information. This primer covers the building blocks needed to build
a network that operates on $z$ directly, instead of on $|z|$.

## 1. Complex Convolution

A complex filter $W = A + iB$ applied to a complex input $h = x + iy$ is defined as:

$$
W * h = (A * x - B * y) + i(A * y + B * x)
$$

Since PyTorch has no native complex convolution layer, this is implemented using
**four real-valued convolutions**, combined algebraically:

- Real output: `conv(A, x) - conv(B, y)`
- Imaginary output: `conv(A, y) + conv(B, x)`

Each of `A` and `B` is an ordinary `nn.Conv2d`, and the real/imaginary parts of the
input/output are tracked as a pair of tensors throughout the network.

## 2. Complex Batch Normalization

Naively normalizing the real and imaginary channels independently is incorrect,
because $x$ and $y$ are statistically correlated (they come from the same underlying
complex signal). Trabelsi et al. instead **whiten** the 2D (real, imaginary)
covariance matrix per channel:

$$
V = \begin{pmatrix} V_{rr} & V_{ri} \\ V_{ri} & V_{ii} \end{pmatrix}
$$

where $V_{rr} = \text{Var}(x)$, $V_{ii} = \text{Var}(y)$, and $V_{ri} = \text{Cov}(x, y)$.
The normalized output is:

$$
\tilde{z} = V^{-1/2}(z - \mathbb{E}[z])
$$

This decorrelates real/imaginary components and normalizes their joint variance to
identity, rather than treating them as two independent real channels.

## 3. Complex Activation Functions

**modReLU** — applies ReLU to magnitude only, leaving phase untouched:

$$
\text{modReLU}(z) = \text{ReLU}(|z| + b) \cdot \frac{z}{|z|}
$$

where $b$ is a learnable bias. This is phase-preserving by construction, since only
the magnitude term is thresholded.

**CReLU** — applies ReLU independently to real and imaginary parts:

$$
\text{CReLU}(z) = \text{ReLU}(x) + i\,\text{ReLU}(y)
$$

Simpler to implement, but can distort phase, since real and imaginary parts are
zeroed independently rather than jointly.

**Chosen for this project: modReLU** — because phase preservation is the project's
core hypothesis, an activation that can silently corrupt phase (CReLU) undermines the
premise being tested. modReLU keeps phase intact through every layer, which is
necessary if we want to later measure phase-related robustness/corruption effects
cleanly.

## 4. Why This Matters for PhaseSAR-Net

Every design choice above exists for one reason: keep the real/imaginary (equivalently,
magnitude/phase) relationship intact through the *entire* forward pass, not just at
the input. A real-valued CNN discards phase at the input layer — this project tests
whether that loss measurably degrades classification robustness under noise,
compression, and corruption.

## Layers to Implement in `src/complex_layers.py`

- [x] `ComplexConv2d` — scaffolded, import-tested
- [ ] `ComplexBatchNorm2d` — not yet implemented
- [x] `ModReLU` — scaffolded, import-tested
- [ ] `ComplexMaxPool2d` — not yet implemented (needed for a full CV-CNN block)