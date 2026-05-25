# Literature Map: NeuroMed-XAI Benchmark

This file records papers that motivate the NeuroMed-XAI Benchmark visual and technical direction. Do not vendor copyrighted PDFs here; keep links, metadata, and concise design notes.

## Explainable EEG / BCI AI

1. Rajpura P, Cecotti H, Kumar Meena Y. **Explainable artificial intelligence approaches for brain-computer interfaces: a review and design space.** *Journal of Neural Engineering*. 2024. DOI: `10.1088/1741-2552/ad6593`.
   - PubMed: https://pubmed.ncbi.nlm.nih.gov/39029500/
   - Relevance: XAI methods, design space, interpretability needs for BCI.
   - Visual cues: attribution layers, decision pathways, explanation overlays on neural signals.

2. Shang S, Shi Y, Zhang Y, et al. **Artificial intelligence for brain disease diagnosis using electroencephalogram signals.** *Journal of Zhejiang University Science B*. 2024. DOI: `10.1631/jzus.B2400103`.
   - PubMed: https://pubmed.ncbi.nlm.nih.gov/39420525/
   - PMC: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11494159/
   - Relevance: broad disease diagnosis framing for EEG AI.
   - Visual cues: EEG biomarkers, disease-task spectrum, clinical decision support rather than autonomous diagnosis.

## Seizure Detection and Interpretable Models

3. Vieira JC, Guedes LA, Santos MR, et al. **Using Explainable Artificial Intelligence to Obtain Efficient Seizure-Detection Models Based on Electroencephalography Signals.** *Sensors*. 2023. DOI: `10.3390/s23249871`.
   - PubMed: https://pubmed.ncbi.nlm.nih.gov/38139715/
   - PMC: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10747117/
   - Relevance: explicit XAI + seizure detection.
   - Visual cues: saliency on EEG windows, efficient model selection, seizure-relevant segments.

4. Zhao X, Yoshida N, Ueda T, et al. **Epileptic seizure detection by using interpretable machine learning models.** *Journal of Neural Engineering*. 2023. DOI: `10.1088/1741-2552/acb089`.
   - PubMed: https://pubmed.ncbi.nlm.nih.gov/36603215/
   - Relevance: interpretable seizure detection.

5. Raeisi K, Khazaei M, Tamburro G, et al. **A Class-Imbalance Aware and Explainable Spatio-Temporal Graph Attention Network for Neonatal Seizure Detection.** *International Journal of Neural Systems*. 2023. DOI: `10.1142/S0129065723500466`.
   - PubMed: https://pubmed.ncbi.nlm.nih.gov/37497802/
   - Relevance: spatio-temporal graph attention and explanation for neonatal seizure detection.

## Sleep Staging and Explainability

6. Gagliardi G, Luca Alfeo A, Cimino MGCA, et al. **PhysioEx: a new Python library for explainable sleep staging through deep learning.** *Physiological Measurement*. 2025. DOI: `10.1088/1361-6579/adaf73`.
   - PubMed: https://pubmed.ncbi.nlm.nih.gov/39874654/
   - Relevance: very close to explainable EEG sleep staging tooling.

7. Pei Y, Xu J, Yu F, et al. **WaveSleepNet: An Interpretable Network for Expert-Like Sleep Staging.** *IEEE Journal of Biomedical and Health Informatics*. 2025. DOI: `10.1109/JBHI.2024.3498871`.
   - PubMed: https://pubmed.ncbi.nlm.nih.gov/40030379/
   - Relevance: interpretable model design for sleep staging.

8. Adey B, Habib A, Karmakar C. **Exploration of an intrinsically explainable self-attention based model for prototype generation on single-channel EEG sleep stage classification.** *Scientific Reports*. 2024. DOI: `10.1038/s41598-024-79139-y`.
   - PubMed: https://pubmed.ncbi.nlm.nih.gov/39528813/
   - PMC: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11555387/
   - Relevance: prototype-based/self-attention explanations for EEG sleep staging.

## Visual Translation

The cover image should foreground:

- EEG signal windows as living evidence, not decorative lines
- brain topography or 10-20 electrode layout
- transparent saliency/attention overlays
- disease tasks as benchmark nodes, not diagnostic claims
- a report/decision-support layer, with uncertainty and leakage-aware evaluation implied

## Avoid

- hospital stock imagery
- red emergency imagery that implies a clinical product
- one-click diagnostic claims
- generic AI brain icons without interpretable evidence
