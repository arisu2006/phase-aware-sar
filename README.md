<div align="center">

<img width="100%" src="https://capsule-render.vercel.app/api?type=waving&color=0:03a9f4,100:4db6ac&height=200&section=header&text=PhaseSAR-Net&fontSize=55&fontColor=ffffff&animation=fadeIn&fontAlignY=35&desc=Complex-Valued%20Neural%20Network%20for%20SAR%20Data&descAlignY=55&descSize=18" />

<br/>

<a href="https://github.com/arisu2006/phase-aware-sar">
  <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=600&size=22&duration=3000&pause=800&color=4DB6AC&center=true&vCenter=true&width=650&lines=Preserving+Phase+%2B+Amplitude+in+SAR+Imaging;Robust+CNNs+for+Noisy+%2F+Corrupted+Radar+Signals;Complex-Valued+Deep+Learning+%7C+PyTorch" alt="Typing SVG" />
</a>

<br/><br/>

<img src="https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white" />
<img src="https://img.shields.io/badge/PyTorch-Deep%20Learning-EE4C2C?style=for-the-badge&logo=pytorch&logoColor=white" />
<img src="https://img.shields.io/badge/Streamlit-Dashboard-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white" />
<img src="https://img.shields.io/badge/status-active-4DB6AC?style=for-the-badge" />

</div>

<img width="100%" src="https://capsule-render.vercel.app/api?type=rect&color=0:03a9f4,100:4db6ac&height=3" />

## 📌 Introduction

Radar images can "see" through clouds, smoke, and darkness — even at night. But most AI models only look at part of that picture (just the brightness/amplitude) and throw away useful hidden details called phase.

**PhaseSAR-Net** teaches an AI to use the full radar signal — brightness *and* phase — so it still recognizes things correctly even when the image gets noisy, blurry, or heavily compressed. It's like giving the AI night-vision on top of a normal photo, instead of just the normal photo.

<div align="center">
<img width="60%" src="https://capsule-render.vercel.app/api?type=rect&color=0:03a9f4,100:4db6ac&height=2" />
</div>

## 🎯 Objectives

- 🧠 **Preserve Intelligence** — Keep both amplitude and phase information from the radar data
- 📊 **Benchmark Performance** — Build a baseline model using only amplitude for comparison
- ⚡ **Advance the State-of-the-Art** — Implement and optimize a complex-valued neural network (CVNN) that operates directly on the full signal
- 🌪️ **Robustness Testing** — Simulate real-world interference like noise, corruption, and bandwidth compression
- 🖥️ **Visualization** — Show it all on a simple, interactive dashboard (built with Streamlit)

## 📂 Repo Structure

```text
phase-aware-sar/
├── data/            # Raw & processed SAR datasets
├── src/             # Model architecture, training scripts, preprocessing
├── notebooks/       # Exploratory data analysis & visualization
├── configs/         # YAML experiment configurations
├── checkpoints/     # Saved model weights
├── scripts/         # Automation scripts
├── tests/           # Unit tests
├── docs/            # Reports & documentation
├── README.md        # Project documentation
└── requirements.txt # Python dependencies
```

<div align="center">
<img width="100%" src="https://capsule-render.vercel.app/api?type=waving&color=0:4db6ac,100:03a9f4&height=100&section=footer" />
</div>
