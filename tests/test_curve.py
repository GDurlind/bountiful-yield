"""Tests for the YieldCurve API."""
from __future__ import annotations

import math

import numpy as np

from src.curves.interpolation import LinearInterpolator
from src.curves.curve import YieldCurve


def test_yieldcurve_basic_rates() -> None:
    # simple exponential-like discount factors for testing
    x = [0.0, 1.0, 2.0]
    y = [1.0, math.exp(-0.02), math.exp(-0.04)]
    itp = LinearInterpolator()
    itp.fit(x, y)
    curve = YieldCurve(itp)

    df1 = curve.discount_factor(1.0)
    assert df1 > 0.0
    z1 = curve.zero_rate(1.0)
    assert np.isclose(z1, 0.02, atol=1e-3)

    fwd = curve.forward_rate(1.0, 2.0)
    assert np.isclose(fwd, 0.02, atol=1e-3)
