from neuromed_xai_benchmark.datasets.synthetic import make_synthetic_eeg


def test_synthetic_dataset_shape() -> None:
    dataset = make_synthetic_eeg(n_samples=20, n_channels=4, n_times=64)

    assert dataset.signals.shape == (20, 4, 64)
    assert dataset.labels.shape == (20,)
    assert len(dataset.channel_names) == 4
