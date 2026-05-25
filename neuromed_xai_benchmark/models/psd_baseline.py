from __future__ import annotations

from dataclasses import dataclass

import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, f1_score

from neuromed_xai_benchmark.datasets.base import EEGDataset
from neuromed_xai_benchmark.features.psd import simple_bandpower
from neuromed_xai_benchmark.splits import SplitIndices, make_subject_group_split


@dataclass(frozen=True)
class BaselineResult:
    accuracy: float
    macro_f1: float
    y_true: np.ndarray
    y_pred: np.ndarray
    split: SplitIndices


def fit_psd_baseline(dataset: EEGDataset) -> BaselineResult:
    features = simple_bandpower(dataset.signals)
    split = make_subject_group_split(features, dataset.labels, dataset.subjects)

    model = RandomForestClassifier(n_estimators=100, random_state=7)
    model.fit(features[split.train_idx], dataset.labels[split.train_idx])
    y_pred = model.predict(features[split.test_idx])
    y_true = dataset.labels[split.test_idx]

    return BaselineResult(
        accuracy=float(accuracy_score(y_true, y_pred)),
        macro_f1=float(f1_score(y_true, y_pred, average="macro")),
        y_true=y_true,
        y_pred=y_pred,
        split=split,
    )
