from pathlib import Path

from neuromed_xai_benchmark.pipeline import run_synthetic_benchmark


def test_synthetic_benchmark_pipeline_writes_report(tmp_path: Path) -> None:
    run = run_synthetic_benchmark(tmp_path / "report.md")

    assert run.dataset.task_name == "synthetic-seizure-like-binary"
    assert run.result.split.n_train > run.result.split.n_test
    assert run.attribution.top_channels
    assert run.report_path.exists()
