from __future__ import annotations

from pathlib import Path

import typer
from rich.console import Console
from rich.table import Table

from neuromed_xai_benchmark.pipeline import run_synthetic_benchmark

app = typer.Typer(help="NeuroMed-XAI Benchmark research prototype.")
console = Console()


@app.callback()
def main() -> None:
    """Command group for NeuroMed-XAI Benchmark."""


@app.command()
def demo(output: Path = Path("outputs/demo_report.md")) -> None:
    """Run a synthetic EEG benchmark demo and write a report."""
    run = run_synthetic_benchmark(output)

    table = Table(title="NeuroMed-XAI Synthetic Demo")
    table.add_column("Metric")
    table.add_column("Value")
    table.add_row("Task", run.dataset.task_name)
    table.add_row("Accuracy", f"{run.result.accuracy:.3f}")
    table.add_row("Macro F1", f"{run.result.macro_f1:.3f}")
    table.add_row("Train/Test", f"{run.result.split.n_train}/{run.result.split.n_test}")
    table.add_row("Top Channel", run.attribution.top_channels[0])
    table.add_row("Report", str(run.report_path))
    console.print(table)


if __name__ == "__main__":
    app()
