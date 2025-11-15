# Synthetic fMRI Connectivity Analysis

This project generates a small synthetic fMRI-like dataset and demonstrates how correlation and partial correlation describe relationships between brain regions (ROIs). The goal is to provide a minimal, transparent example of functional connectivity analysis without relying on real neuroimaging data.

## Overview

The project simulates three ROI time series using a simple generative model:
- AR(1) dynamics for each ROI  
- A shared global drive affecting all ROIs  
- A directed influence from ROI1 → ROI2   

Two connectivity measures are computed:
- Correlation -> captures shared cofluctuations  
- Partial correlation —> estimates direct associations while removing shared and indirect effects  

Both methods are visualized and compared.

## Repository Structure


## Repository Structure

```
synthetic_fmri_connectivity/
│
├── data/
│   └── simulated_ar_rois.csv
│
├── figures/
│   └── connectivity_matrices.png
│
├── notebooks/
│   └── synthetic_fmri_connectivity_walkthrough.ipynb
│
├── src/
│   ├── simulate_signals.py
│   └── connectivity_analysis.py
│
├── tests/
│
├── .gitignore
├── README.md
└── requirements.txt
```



## How It Works

### 1. Signal Simulation
`src/simulate_signals.py` generates a `(300 × 3)` matrix of synthetic ROI signals.  
Running the script produces:

### 2. Connectivity Computation
`src/connectivity_analysis.py` implements:
- correlation
- partial correlation

### Walkthrough Notebook

notebooks/synthetic_fmri_connectivity_walkthrough.ipynb provides:

simulation demonstration

time-series visualization

correlation matrix

partial correlation matrix

interpretation of results

### Requirements

Install dependencies:

pip install -r requirements.txt
