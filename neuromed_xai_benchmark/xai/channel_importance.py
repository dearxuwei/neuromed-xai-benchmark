from __future__ import annotations

from dataclasses import dataclass

import numpy as np

from neuromed_xai_benchmark.datasets.base import EEGDataset


@dataclass(frozen=True)
class ChannelAttribution:
    channel_scores: dict[str, float]
    top_channels: list[str]


def estimate_channel_importance(dataset: EEGDataset) -> ChannelAttribution:
    class_0 = dataset.signals[dataset.labels == 0]
    class_1 = dataset.signals[dataset.labels == 1]
    score = np.abs(class_1.mean(axis=(0, 2)) - class_0.mean(axis=(0, 2)))
    if len(dataset.channel_names) != len(score):
        raise ValueError("channel_names and channel importance scores must have the same length")
    channel_scores = {channel: float(value) for channel, value in zip(dataset.channel_names, score)}
    top_channels = sorted(channel_scores, key=channel_scores.get, reverse=True)
    return ChannelAttribution(channel_scores=channel_scores, top_channels=top_channels)
