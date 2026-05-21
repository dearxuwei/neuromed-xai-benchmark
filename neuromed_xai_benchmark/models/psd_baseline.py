from __future__ import annotations

from dataclasses import dataclass

import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, f1_score
from sklearn.model_selection import GroupShuffleSplit

from neuromed_xai_benchmark.datasets.base import EEGDataset


@dataclass(frozen=True)
class BaselineResult:
    accuracy: float
    macro_f1: float
    y_true: np.ndarray
    y_pred: np.ndarray


def _simple_bandpower(signals: np.ndarray) -> np.ndarray:
    spectrum = np.abs(np.fft.rfft(signals, axis=-1)) ** 2
    return spectrum.mean(axis=-1)


def fit_psd_baseline(dataset: EEGDataset) -> BaselineResult:
    features = _simple_bandpower(dataset.signals)
    splitter = GroupShuffleSplit(n_splits=1, test_size=0.25, random_state=7)
    train_idx, test_idx = next(splitter.split(features, dataset.labels, groups=dataset.subjects))

    model = RandomForestClassifier(n_estimators=100, random_state=7)
    model.fit(features[train_idx], dataset.labels[train_idx])
    y_pred = model.predict(features[test_idx])
    y_true = dataset.labels[test_idx]

    return BaselineResult(
        accuracy=float(accuracy_score(y_true, y_pred)),
        macro_f1=float(f1_score(y_true, y_pred, average="macro")),
        y_true=y_true,
        y_pred=y_pred,
    )
