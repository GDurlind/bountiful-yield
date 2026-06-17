"""Tests for interpolation implementations."""
from __future__ import annotations

import numpy as np

from src.curves.interpolation import Interpolator, LinearInterpolator, LogLinearDiscountFactorInterpolator


def test_interpolator_inheritance() -> None:
    assert issubclass(LinearInterpolator, Interpolator)
    assert issubclass(LogLinearDiscountFactorInterpolator, Interpolator)


def test_linear_interpolation_basic() -> None:
    x = [0.0, 1.0, 2.0]
    y = [1.0, 0.95, 0.9]
    itp = LinearInterpolator()
    itp.fit(x, y)
    assert np.isclose(itp.evaluate(1.0), 0.95)
    assert itp.evaluate(1.5) < 0.95 and itp.evaluate(1.5) > 0.9


def test_loglinear_preserves_positivity() -> None:
    x = [0.0, 1.0, 2.0]
    y = [1.0, 0.95, 0.9]
    itp = LogLinearDiscountFactorInterpolator()
    itp.fit(x, y)
    val = itp.evaluate(1.5)
    assert val > 0.0
