# Reading Notes for Promotional Visuals

## Downloaded Local Papers

- `papers/AI_EEG_brain_disease_diagnosis_2024_PMC11494159.html`
- `papers/XAI_seizure_detection_Sensors_2023_PMC10747117.html`
- `papers/EEG_SESM_sleep_staging_SciRep_2024_PMC11555387.html`

## Review: AI for Brain Disease Diagnosis Using EEG, 2024

Source: Shang S, Shi Y, Zhang Y, et al. *Journal of Zhejiang University Science B*. DOI: `10.1631/jzus.B2400103`.

### Methods and Framing

- EEG is positioned as a non-invasive signal source for neurological disease research.
- AI methods include machine learning and deep learning for classification and prediction.
- The project should frame itself as decision-support research infrastructure, not as a diagnostic product.

### Design Translation

Show multiple disease/task nodes around one evidence pipeline:

- seizure detection
- sleep staging
- cognitive screening
- neurological disease AI benchmark

## Research Article: XAI for Efficient Seizure Detection, Sensors, 2023

Source: Vieira JC, Guedes LA, Santos MR, et al. DOI: `10.3390/s23249871`.

### Methods Worth Reflecting in Visuals

- Public EEG epilepsy data.
- Binary classification of interictal and ictal EEG windows.
- Time-domain feature extraction.
- XGBoost and other ML classifiers.
- SHAP values for feature/channel selection and model explanation.
- Reduced feature/channel models are a key contribution.

### Results Worth Reflecting in Visuals

- Full XGBoost model reported `97.43%` test accuracy using `247` attribute vectors.
- SHAP-guided reduction achieved `>95%` accuracy with far fewer inputs.
- The paper reports `95.93%` accuracy using only `6` features and `5` channels in the second phase.
- Selected channels included `Fz`, `C4`, `T5`, `F3`, and `Fp2`, spatially related to focal regions in the dataset.

### Design Translation

Use a visual chain:

`EEG window -> SHAP attribution -> reduced electrodes/features -> interpretable report`

Evidence labels:

- `SHAP-guided channel selection`
- `5 channels / 6 features`
- `>95% seizure detection accuracy`

Frame these as prior-work evidence.

## Research Article: EEG-SESM Sleep Staging, Scientific Reports, 2024

Source: Adey B, Habib A, Karmakar C. DOI: `10.1038/s41598-024-79139-y`.

### Methods Worth Reflecting in Visuals

- Single-channel EEG sleep stage classification.
- Self-attention-based prototype method.
- Intrinsic explainability through selected prototypical signal segments.
- Relevance weights identify which prototypes support the class prediction.
- The paper compares prototype selections with expected sleep biomarkers such as spindles and slow waves.

### Results Worth Reflecting in Visuals

- The model performed comparably to EEGNet in the studied setting.
- Prototype segments sometimes aligned with expected biomarkers such as sleep spindles and slow waves.
- Limitations: time-domain-only explanations miss important spectral information.

### Design Translation

Add prototype tiles or highlighted waveform snippets:

- `prototype evidence`
- `spindles / slow waves`
- `biomarker-aligned explanations`

Do not imply clinical-grade diagnosis.
