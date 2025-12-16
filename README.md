# EEGCanon-ML 🧠⚡

EEGCanon-ML is a Python framework that converts heterogeneous EEG data
(EDF, CSV) into a **canonical, standardized representation** for
reproducible machine learning and signal analysis.

It provides a **common EEG data language** so that models, features,
and experiments can be compared fairly across datasets.

---

## Why EEGCanon-ML?

Today, EEG pipelines suffer from:
- dataset-specific preprocessing scripts
- inconsistent channel naming
- incompatible sampling rates
- poor reproducibility across studies

**EEGCanon-ML solves this by enforcing a standard EEG contract.**

---

## Key Features

- Unified EEG loading (EDF, CSV)
- Canonical 10–20 channel mapping
- Sampling-rate normalization
- Structured warnings & provenance tracking
- Epoching support
- Feature extraction (PSD, Bandpower, Hjorth)
- PyTorch dataset integration
- ML-ready output without custom preprocessing

---

## Installation

```bash
pip install eegcanon-ml


## Quick Example
from eegcanon.pipeline import load_eeg

eeg = load_eeg("sample.edf")

print(eeg.data.shape)
print(eeg.channels)
print(eeg.sampling_rate)
print(eeg.warnings)


## Design Philosophy

EEGCanon-ML focuses on standardization, not model accuracy.

## The goal is to:

remove preprocessing variance
enable fair ML benchmarking
improve reproducibility in EEG research and industry
Artifact removal and model design are intentionally kept modular.

## Supported Formats
EDF (clinical EEG)
CSV (research / Kaggle / lab datasets)

Note: FIF/MEG formats are intentionally not supported in v0.1.0
to avoid ambiguity from mixed MEG/EEG pipelines.

## Roadmap

Planned future improvements:
Artifact detection (ICA-based)
Epoch labeling utilities
BIDS / MNE export
Cloud-friendly formats (HDF5 / Parquet)