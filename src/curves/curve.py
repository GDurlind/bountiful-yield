"""Yield curve core API.

The `YieldCurve` stores discount factors implicitly via an `Interpolator`.
All rates are derived from discount factors to avoid inconsistent state.
"""
from __future__ import annotations

from dataclasses import dataclass
from typing import Protocol

import numpy as np

from .interpolation import Interpolator
from . import exceptions
from .. import math as _math  # type: ignore


@dataclass(frozen=True)
class YieldCurve:
    """Canonical yield curve representation backed by discount factors.

    The curve delegates interpolation to an `Interpolator` instance which
    must be fitted before passing to the curve.
    """

    _interpolator: Interpolator

    def discount_factor(self, t: float) -> float:
        """Return discount factor for time `t` (in years).

        Args:
            t: time in years

        Returns:
            discount factor (positive float)
        """
        df = float(self._interpolator.evaluate(t))
        if df <= 0.0:
            raise exceptions.CurveError("Discount factor must be positive")
        return df

    def zero_rate(self, t: float) -> float:
        """Continuously compounded zero rate for maturity `t`.

        r = -ln(df)/t. For t == 0 returns 0.0.
        """
        if t <= 0.0:
            return 0.0
        df = self.discount_factor(t)
        return float(-np.log(df) / t)

    def forward_rate(self, t1: float, t2: float) -> float:
        """Continuously compounded forward rate between t1 and t2.

        f = -(ln(df2)-ln(df1)) / (t2 - t1)
        """
        if t2 <= t1:
            raise ValueError("t2 must be greater than t1")
        df1 = self.discount_factor(t1)
        df2 = self.discount_factor(t2)
        return float(-(np.log(df2) - np.log(df1)) / (t2 - t1))

    def check_arbitrage(self) -> bool:
        """Run simple arbitrage checks.

        Returns True if no obvious arbitrage detected. This performs basic
        validations (positivity, monotonicity). More sophisticated checks
        should be added in diagnostics modules.
        """
        # sample a small grid
        xs = np.linspace(0.0, 30.0, 61)[1:]
        dfs = np.array([self._interpolator.evaluate(x) for x in xs])
        if np.any(dfs <= 0.0):
            return False
        # discount factors should be non-increasing
        return np.all(np.diff(dfs) <= 1e-12)

    def check_monotonicity(self) -> bool:
        """Return True if discount factors are non-increasing with time."""
        xs = np.linspace(0.0, 30.0, 61)[1:]
        dfs = np.array([self._interpolator.evaluate(x) for x in xs])
        return bool(np.all(np.diff(dfs) <= 1e-12))

    def report(self) -> dict:
        """Return a basic report dictionary with key diagnostics.

        Replace with `diagnostics.CurveReport` when report complexity grows.
        """
        return {
            "arbitrage_free": self.check_arbitrage(),
            "monotonic": self.check_monotonicity(),
        }
