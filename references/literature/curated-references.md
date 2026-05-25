# Curated Literature References

This folder stores citation metadata, source links, and design notes. It intentionally does not vendor copyrighted PDFs or journal cover images.

## Core Technical Papers

| Theme | Citation | Source | Visual / Method Notes |
|---|---|---|---|
| Explainable BCI review | Rajpura P, Cecotti H, Kumar Meena Y. Explainable artificial intelligence approaches for brain-computer interfaces: a review and design space. Journal of Neural Engineering. 2024. | DOI: https://doi.org/10.1088/1741-2552/ad6593; PubMed: https://pubmed.ncbi.nlm.nih.gov/39029500/ | XAI design space, attribution overlays, interpretability pathways. |
| EEG disease AI review | Shang S, Shi Y, Zhang Y, et al. Artificial intelligence for brain disease diagnosis using electroencephalogram signals. Journal of Zhejiang University Science B. 2024. | DOI: https://doi.org/10.1631/jzus.B2400103; PMC: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11494159/ | EEG as non-invasive signal source; disease-task spectrum; research-only framing. |
| SHAP seizure detection | Vieira JC, Guedes LA, Santos MR, et al. Using explainable artificial intelligence to obtain efficient seizure-detection models based on electroencephalography signals. Sensors. 2023. | DOI: https://doi.org/10.3390/s23249871; PMC: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10747117/ | SHAP-guided feature/channel reduction; highlighted waveform evidence. |
| Ictal EEG XAI evaluation | Sanchez-Hernandez SE, Torres-Ramos S, Roman-Godinez I, et al. Evaluation of the relation between ictal EEG features and XAI explanations. Brain Sciences. 2024. | DOI: https://doi.org/10.3390/brainsci14040306; PMC: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11048537/ | Relates explanation outputs back to ictal EEG feature evidence. |
| Interpretable seizure models | Zhao X, Yoshida N, Ueda T, et al. Epileptic seizure detection by using interpretable machine learning models. Journal of Neural Engineering. 2023. | DOI: https://doi.org/10.1088/1741-2552/acb089; PubMed: https://pubmed.ncbi.nlm.nih.gov/36603215/ | Interpretable model rather than black-box diagnosis. |
| Low-complexity interpretable feature | Zanetti R, Pale U, Teijeiro T, et al. Approximate zero-crossing: a new interpretable, highly discriminative and low-complexity feature for EEG and iEEG seizure detection. Journal of Neural Engineering. 2022. | DOI: https://doi.org/10.1088/1741-2552/aca1e4; PubMed: https://pubmed.ncbi.nlm.nih.gov/36356314/ | Shows that simple interpretable features can be competitive and auditable. |
| Spatio-temporal graph attention | Raeisi K, Khazaei M, Tamburro G, et al. A class-imbalance aware and explainable spatio-temporal graph attention network for neonatal seizure detection. International Journal of Neural Systems. 2023. | DOI: https://doi.org/10.1142/S0129065723500466; PubMed: https://pubmed.ncbi.nlm.nih.gov/37497802/ | Graph attention over channels and time. |
| Prototype sleep staging | Adey B, Habib A, Karmakar C. Exploration of an intrinsically explainable self-attention based model for prototype generation on single-channel EEG sleep stage classification. Scientific Reports. 2024. | DOI: https://doi.org/10.1038/s41598-024-79139-y; PMC: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11555387/ | Prototype snippets, relevance weights, sleep biomarkers. |
| Interpretable sleep staging | Pei Y, Xu J, Yu F, et al. WaveSleepNet: an interpretable network for expert-like sleep staging. IEEE Journal of Biomedical and Health Informatics. 2025. | DOI: https://doi.org/10.1109/JBHI.2024.3498871; PubMed: https://pubmed.ncbi.nlm.nih.gov/40030379/ | Expert-like staging, interpretable wave patterns. |
| Neurologist-assist EEG annotation | Roy S, Kiral I, Mirmomeni M, et al. Evaluation of artificial intelligence systems for assisting neurologists with fast and accurate annotations of scalp electroencephalography data. EBioMedicine. 2021. | DOI: https://doi.org/10.1016/j.ebiom.2021.103275; PMC: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8105505/ | Important boundary: AI should support review workflows and speed, not replace clinical judgment. |

## Algorithmic Motifs To Carry Into The Project

| Literature Motif | Algorithm / Framework | Repository Mapping |
|---|---|---|
| Leakage-aware EEG evaluation | Subject-wise or group-wise split to avoid same-subject train/test leakage | `make_subject_group_split()` and `SplitIndices`. |
| Classical transparent baseline | PSD / bandpower features with conventional classifiers | `simple_bandpower()` and `fit_psd_baseline()`. |
| Model-agnostic explanation | SHAP/channel importance, feature reduction, evidence ranking | `estimate_channel_importance()` as initial channel evidence module. |
| Prototype explanation | Representative waveform snippets and relevance weights | Planned extension recorded in method figure and roadmap. |
| Reportable audit artifact | Metrics + split + attribution + caveats in a persistent report | `run_synthetic_benchmark()` and `write_markdown_report()`. |
| Conservative clinical framing | Decision-support research, not automated diagnosis | README, reports, and figure annotations. |

## Research Importance

EEG medical AI papers often fail at the same pressure points: leakage-prone evaluation, incomparable preprocessing choices, accuracy-only reporting, and explanations that are visually appealing but not tied to physiological evidence. This project turns those pressure points into first-class benchmark objects: split policy, features, model metrics, attribution, and report text are explicit, testable, and open-source.

## Figure Design Implications

| Layer | What To Show | What To Avoid |
|---|---|---|
| Signal | Multichannel EEG traces and time-frequency hints | Decorative random waves |
| Explanation | Channel heat, SHAP bars, highlighted windows, prototype snippets | Generic magic AI glow |
| Benchmark rigor | Subject-wise split lanes and report cards | One-click diagnosis imagery |
| Clinical boundary | Research benchmark, uncertainty, leakage-aware evaluation | Hospital advertisement or diagnostic product claims |
