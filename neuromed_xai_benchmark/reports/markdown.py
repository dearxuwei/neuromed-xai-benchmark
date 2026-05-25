from __future__ import annotations

from pathlib import Path

from neuromed_xai_benchmark.datasets.base import EEGDataset
from neuromed_xai_benchmark.models.psd_baseline import BaselineResult
from neuromed_xai_benchmark.xai.channel_importance import ChannelAttribution


def write_markdown_report(
    path: Path,
    dataset: EEGDataset,
    result: BaselineResult,
    attribution: ChannelAttribution,
) -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    scores = "\n".join(
        f"- {channel}: {score:.4f}" for channel, score in attribution.channel_scores.items()
    )
    path.write_text(
        "\n".join(
            [
                "# NeuroMed-XAI Benchmark Demo Report",
                "",
                "Research prototype only. Not for clinical diagnosis.",
                "",
                "## Dataset",
                "",
                f"- Task: {dataset.task_name}",
                f"- Samples: {dataset.n_samples}",
                f"- Channels: {len(dataset.channel_names)}",
                f"- Sampling rate: {dataset.sampling_rate} Hz",
                "",
                "## Baseline Metrics",
                "",
                f"- Accuracy: {result.accuracy:.3f}",
                f"- Macro F1: {result.macro_f1:.3f}",
                f"- Train samples: {result.split.n_train}",
                f"- Test samples: {result.split.n_test}",
                "",
                "## Channel Attribution",
                "",
                scores,
                "",
                "## Leakage-Aware Evaluation",
                "",
                "This demo uses grouped subject splits to avoid mixing the same subject across train and test partitions.",
                "",
            ]
        ),
        encoding="utf-8",
    )
    return path
