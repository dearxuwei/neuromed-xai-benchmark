# Technical Plan

## Architecture

```text
EEG dataset
-> subject-wise leakage-aware split
-> feature extraction
-> baseline or deep model
-> metrics
-> XAI attribution / prototype evidence
-> report generator
```

## Modules

- `datasets`: data containers and future public dataset loaders.
- `features`: signal feature extraction such as PSD / bandpower.
- `splits`: leakage-aware subject or group splits.
- `models`: baseline classifiers and future deep models.
- `pipeline`: end-to-end benchmark orchestration.
- `xai`: attribution and evidence summaries.
- `reports`: Markdown/HTML report generation.

## Research Pain Points

| Pain Point | Why It Matters | Current Open-Source Route |
|---|---|---|
| Subject leakage | EEG windows from the same subject can make models look unrealistically strong. | `make_subject_group_split()` keeps subjects grouped. |
| Accuracy-only reporting | High accuracy without split details or evidence is difficult to audit. | Reports include split sizes, macro F1, and channel attribution. |
| Black-box medical AI | Clinical users need evidence, not only class labels. | `xai` module ranks channel evidence and can host SHAP/prototype methods. |
| Non-comparable pipelines | Preprocessing and feature choices vary across papers. | Feature extraction is modular and explicitly named. |
| Overclaiming diagnosis | Research benchmarks should not imply clinical deployment. | Report and README state research-only boundaries. |

## Algorithmic Route

1. Load or synthesize an `EEGDataset` with signals, labels, subjects, channels, and sampling rate.
2. Extract transparent features, currently FFT mean power per channel.
3. Split by subject group, not by individual epoch.
4. Train a baseline classifier and report accuracy plus macro F1.
5. Estimate channel-level evidence and rank top channels.
6. Write a persistent report with dataset metadata, metrics, split information, and attribution.

## Evaluation Principles

- Prefer subject-wise splits for biomedical EEG tasks.
- Track preprocessing parameters in reports.
- Report macro metrics, not only accuracy.
- Include error cases and interpretability outputs.
- Keep medical claims conservative.

## Interpreter

Target local interpreter:

```text
D:\AI_Env\dl_5060ti\python.exe
```

The repository avoids committing virtual environments. Recreate dependencies from `pyproject.toml`.
