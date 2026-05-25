from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

from neuromed_xai_benchmark.datasets.base import EEGDataset
from neuromed_xai_benchmark.datasets.synthetic import make_synthetic_eeg
from neuromed_xai_benchmark.models.psd_baseline import BaselineResult, fit_psd_baseline
from neuromed_xai_benchmark.reports.markdown import write_markdown_report
from neuromed_xai_benchmark.xai.channel_importance import ChannelAttribution, estimate_channel_importance


@dataclass(frozen=True)
class BenchmarkRun:
    dataset: EEGDataset
    result: BaselineResult
    attribution: ChannelAttribution
    report_path: Path


def run_synthetic_benchmark(output: Path = Path("outputs/demo_report.md")) -> BenchmarkRun:
    """Run the current end-to-end EEG benchmark slice."""

    dataset = make_synthetic_eeg()
    result = fit_psd_baseline(dataset)
    attribution = estimate_channel_importance(dataset)
    report_path = write_markdown_report(output, dataset, result, attribution)
    return BenchmarkRun(
        dataset=dataset,
        result=result,
        attribution=attribution,
        report_path=report_path,
    )
