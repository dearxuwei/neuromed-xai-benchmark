from __future__ import annotations

from dataclasses import dataclass

import numpy as np
from sklearn.model_selection import GroupShuffleSplit


@dataclass(frozen=True)
class SplitIndices:
    train_idx: np.ndarray
    test_idx: np.ndarray

    @property
    def n_train(self) -> int:
        return int(self.train_idx.size)

    @property
    def n_test(self) -> int:
        return int(self.test_idx.size)


def make_subject_group_split(
    features: np.ndarray,
    labels: np.ndarray,
    subjects: np.ndarray,
    test_size: float = 0.25,
    random_state: int = 7,
) -> SplitIndices:
    """Create a subject-wise train/test split to reduce EEG leakage risk."""

    splitter = GroupShuffleSplit(n_splits=1, test_size=test_size, random_state=random_state)
    train_idx, test_idx = next(splitter.split(features, labels, groups=subjects))
    return SplitIndices(train_idx=train_idx, test_idx=test_idx)
