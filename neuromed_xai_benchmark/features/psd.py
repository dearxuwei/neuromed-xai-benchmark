from __future__ import annotations

import numpy as np


def simple_bandpower(signals: np.ndarray) -> np.ndarray:
    """Return mean FFT power per channel for each sample."""

    spectrum = np.abs(np.fft.rfft(signals, axis=-1)) ** 2
    return spectrum.mean(axis=-1)
