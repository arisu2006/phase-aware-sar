# PhaseSAR-Net - Project Scope

## Objectives

This project investigates whether a phase-aware (complex-valued) SAR classification model degrades less than an amplitude-only baseline CNN when inputs are noisy or corrupted. It is framed as AI reliability / robustness research, not a deployment-ready defense system.

## In Scope

* Baseline amplitude-only CNN classifier
* Phase-aware / complex-valued classifier
* Noise and corruption simulation on SAR inputs
* Evaluation report comparing both models
* Streamlit dashboard for visualizing results
* Final written report and presentation slides

## Out of Scope

* Classified or restricted data of any kind
* Real radar hardware or sensor integration
* Real-time or operational deployment
* Field/operational testing

## Deliverables

* Trained baseline CNN model
* Trained phase-aware model
* RESULTS.md progress log
* Streamlit dashboard
* Final report (PDF/DOCX)
* Final presentation slides

## Timeline

12 phases across 10 Aug 2026 - 30 Nov 2026 (113 days, 2 hrs/day). See project execution calendar (PhaseSAR-Net\_2-Hour\_Daily\_Execution\_Calendar) for full phase-by-phase breakdown.

## Evaluation Plan

Compare baseline (amplitude-only) model vs. phase-aware (complex-valued) model, each tested on clean inputs vs. corrupted/noisy inputs. Core question: does the phase-aware model's accuracy degrade less than the baseline's under corruption?

