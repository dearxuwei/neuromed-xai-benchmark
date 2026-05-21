from __future__ import annotations

from pathlib import Path

import typer
from rich.console import Console
from rich.table import Table

from neuromed_xai_benchmark.datasets.synthetic import make_synthetic_eeg
from neuromed_xai_benchmark.models.psd_baseline import fit_psd_baseline
from neuromed_xai_benchmark.reports.markdown import write_markdown_report
from neuromed_xai_benchmark.xai.channel_importance import estimate_channel_importance

app = typer.Typer(help="NeuroMed-XAI Benchmark research prototype.")
console = Console()


@app.command()
def demo(output: Path = Path("outputs/demo_report.md")) -> None:
    """Run a synthetic EEG benchmark demo and write a report."""
    dataset = make_synthetic_eeg()
    result = fit_psd_baseline(dataset)
    attribution = estimate_channel_importance(dataset)
    report_path = write_markdown_report(output, dataset, result, attribution)

    table = Table(title="NeuroMed-XAI Synthetic Demo")
    table.add_column("Metric")
    table.add_column("Value")
    table.add_row("Task", dataset.task_name)
    table.add_row("Accuracy", f"{result.accuracy:.3f}")
    table.add_row("Macro F1", f"{result.macro_f1:.3f}")
    table.add_row("Top Channel", attribution.top_channels[0])
    table.add_row("Report", str(report_path))
    console.print(table)


if __name__ == "__main__":
    app()
