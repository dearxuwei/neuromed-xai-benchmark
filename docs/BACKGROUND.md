# Background

EEG-based biomedical AI has potential for seizure detection, sleep staging, cognitive impairment screening, anesthesia monitoring, and other clinical decision-support research. However, many experiments are difficult to compare because preprocessing, subject splits, model baselines, and interpretability methods differ.

This project combines benchmark infrastructure with explainable AI reporting:

- leakage-aware subject/session splits
- reproducible preprocessing and baselines
- channel, frequency-band, and temporal attribution
- error-case analysis
- report templates for research communication

The project is intentionally framed as clinical decision-support research infrastructure, not as an autonomous diagnostic product.

## Initial Task Scope

Month 1 should focus on two public-data directions:

- seizure detection
- sleep staging

Additional disease areas such as Alzheimer's disease, depression, Parkinson's disease, and disorders of consciousness can be added after the baseline pipeline is stable.
