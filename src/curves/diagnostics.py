"""Diagnostics utilities for yield curves.

This module contains lightweight placeholder diagnostics that can be
expanded into comprehensive checks and reports.
"""
from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Dict

from .curve import YieldCurve


@dataclass
class CurveReport:
    """Basic container for curve diagnostics results."""

    curve: YieldCurve

    def summary(self) -> Dict[str, Any]:
        return self.curve.report()


class ArbitrageCheck:
    """Simple arbitrage check wrapper."""

    @staticmethod
    def run(curve: YieldCurve) -> bool:
        return curve.check_arbitrage()


class MonotonicityCheck:
    """Simple monotonicity check wrapper."""

    @staticmethod
    def run(curve: YieldCurve) -> bool:
        return curve.check_monotonicity()
