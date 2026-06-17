"""Tests for diagnostics module."""
from __future__ import annotations

import math

from src.curves.interpolation import LinearInterpolator
from src.curves.curve import YieldCurve
from src.curves.diagnostics import CurveReport, ArbitrageCheck, MonotonicityCheck


def test_report_creation() -> None:
    x = [0.0, 1.0]
    y = [1.0, math.exp(-0.01)]
    itp = LinearInterpolator()
    itp.fit(x, y)
    curve = YieldCurve(itp)
    report = CurveReport(curve)
    summary = report.summary()
    assert isinstance(summary, dict)


def test_checks() -> None:
    x = [0.0, 1.0]
    y = [1.0, math.exp(-0.01)]
    itp = LinearInterpolator()
    itp.fit(x, y)
    curve = YieldCurve(itp)
    assert ArbitrageCheck.run(curve)
    assert MonotonicityCheck.run(curve)
