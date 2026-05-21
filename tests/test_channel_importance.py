from neuromed_xai_benchmark.datasets.synthetic import make_synthetic_eeg
from neuromed_xai_benchmark.xai.channel_importance import estimate_channel_importance


def test_channel_importance_returns_ranked_channels() -> None:
    dataset = make_synthetic_eeg()
    attribution = estimate_channel_importance(dataset)

    assert attribution.top_channels
    assert set(attribution.channel_scores) == set(dataset.channel_names)
