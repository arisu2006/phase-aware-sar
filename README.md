<div align="center">

![Header](https://capsule-render.vercel.app/api?type=waving&color=0:0f2027,100:00e5ff&height=140&section=header&text=PhaseSAR-Net&fontSize=42&fontColor=ffffff&animation=fadeIn&fontAlignY=38)

[![Typing SVG](https://readme-typing-svg.demolab.com?font=Fira+Code&size=20&pause=1000&color=00E5FF&center=true&vCenter=true&width=600&lines=Phase-Aware+SAR+Intelligence+System;Complex-Valued+Neural+Networks+for+SAR;Robustness+Research+%7C+Defense-Sector+AI)](https://git.io/typing-svg)

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![PyTorch](https://img.shields.io/badge/PyTorch-EE4C2C?style=for-the-badge&logo=pytorch&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![Jupyter](https://img.shields.io/badge/Jupyter-F37626?style=for-the-badge&logo=jupyter&logoColor=white)
![WandB](https://img.shields.io/badge/Weights_&_Biases-FFBE00?style=for-the-badge&logo=weightsandbiases&logoColor=black)

</div>

---

### 🔎 Introduction

🛰️ Radar images can "see" through clouds, smoke, and darkness — even at night. But most AI models only look at part of that picture (just the brightness) and throw away useful hidden details (called **phase**).

**PhaseSAR-Net** teaches an AI to use the **full** radar signal — brightness *and* phase — so it still recognizes things correctly even when the image gets noisy, blurry, or squished. It's like giving the AI night-vision on top of a normal photo, instead of just the normal photo.

> **Question this project answers:** Does using the full signal actually help the AI stay accurate when the data gets messy — more than the usual "brightness-only" method does?

---

### 🎯 Objectives

- 🧩 Keep both brightness **and** phase information from the radar data
- 🏗️ Build a simple baseline model (the "usual" way) for comparison
- 🧠 Build a phase-aware model (the "new" way) that uses the full signal
- 🌪️ Simulate noisy, corrupted, and compressed radar data
- ⚖️ Compare how well each model holds up when things get messy
- 📊 Show it all on a simple, interactive dashboard

---

### 📂 Repo Structure

```
phase-aware-sar/
├── data/            # raw & processed SAR datasets
├── src/             # model, preprocessing, training code
├── notebooks/       # exploratory analysis & visualization
├── configs/         # experiment configs (YAML/JSON)
├── tests/           # unit & integration tests
├── docs/            # research notes, primers, write-ups
└── requirements.txt
```

---

### ⚙️ Quickstart

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

---

<div align="center">

![Footer](https://capsule-render.vercel.app/api?type=waving&color=0:00e5ff,100:0f2027&height=100&section=footer)

<sub>Built solo · <a href="https://github.com/arisu2006/phase-aware-sar">github.com/arisu2006/phase-aware-sar</a></sub>
</div>
