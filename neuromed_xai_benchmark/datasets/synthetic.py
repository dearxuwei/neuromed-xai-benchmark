from __future__ import annotations

import numpy as np

from neuromed_xai_benchmark.datasets.base import EEGDataset


def make_synthetic_eeg(
    n_samples: int = 120,
    n_channels: int = 8,
    n_times: int = 256,
    sampling_rate: float = 128.0,
    seed: int = 42,
) -> EEGDataset:
    rng = np.random.default_rng(seed)
    labels = rng.integers(0, 2, size=n_samples)
    signals = rng.normal(0, 1, size=(n_samples, n_channels, n_times))

    time = np.linspace(0, 1, n_times)
    disease_pattern = np.sin(2 * np.pi * 10 * time)
    signals[labels == 1, 2, :] += 1.2 * disease_pattern
    signals[labels == 1, 3, :] += 0.8 * disease_pattern

    subjects = np.repeat(np.arange(n_samples // 10), 10)
    channel_names = [f"Ch{idx + 1}" for idx in range(n_channels)]

    return EEGDataset(
        task_name="synthetic-seizure-like-binary",
        signals=signals,
        labels=labels,
        subjects=subjects,
        channel_names=channel_names,
        sampling_rate=sampling_rate,
    )
