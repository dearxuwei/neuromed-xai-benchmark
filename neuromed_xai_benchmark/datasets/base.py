from __future__ import annotations

from dataclasses import dataclass

import numpy as np


@dataclass(frozen=True)
class EEGDataset:
    task_name: str
    signals: np.ndarray
    labels: np.ndarray
    subjects: np.ndarray
    channel_names: list[str]
    sampling_rate: float

    @property
    def n_samples(self) -> int:
        return int(self.signals.shape[0])
