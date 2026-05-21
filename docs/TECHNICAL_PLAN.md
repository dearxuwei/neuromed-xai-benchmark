# Technical Plan

## Architecture

```text
EEG dataset
-> preprocessing
-> leakage-aware split
-> baseline model
-> metrics
-> XAI attribution
-> report generator
```

## Modules

- `datasets`: data containers and future public dataset loaders.
- `models`: baseline feature extraction and classifiers.
- `xai`: attribution and evidence summaries.
- `reports`: Markdown/HTML report generation.

## Evaluation Principles

- Prefer subject-wise splits for biomedical EEG tasks.
- Track preprocessing parameters in reports.
- Report macro metrics, not only accuracy.
- Include error cases and interpretability outputs.
- Keep medical claims conservative.

## Interpreter

Target local interpreter:

```text
D:\AI_Env\dl_5060ti\Scripts\python.exe
```

The repository avoids committing virtual environments. Recreate dependencies from `pyproject.toml`.
