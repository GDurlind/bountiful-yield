"""Interpolation interfaces and basic implementations."""
from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Sequence

import numpy as np


class Interpolator(ABC):
    """Abstract interpolator interface.

    Subclasses must implement `fit` and `evaluate`.
    """

    @abstractmethod
    def fit(self, x: Sequence[float], y: Sequence[float]) -> None:
        """Fit the interpolator to (x, y) data.

        Args:
            x: independent variable (times)
            y: dependent variable (discount factors)
        """

    @abstractmethod
    def evaluate(self, t: float) -> float:
        """Evaluate the interpolator at time `t`.

        Returns:
            Interpolated value.
        """


class LinearInterpolator(Interpolator):
    """Simple linear interpolator using numpy.interp.

    This is intentionally small and robust; it is suitable for initial
    development and tests. For production use, extend with extrapolation
    behaviour and error handling.
    """

    def __init__(self) -> None:
        self._x = np.array([])
        self._y = np.array([])

    def fit(self, x: Sequence[float], y: Sequence[float]) -> None:
        arr_x = np.asarray(x, dtype=float)
        arr_y = np.asarray(y, dtype=float)
        order = np.argsort(arr_x)
        self._x = arr_x[order]
        self._y = arr_y[order]

    def evaluate(self, t: float) -> float:
        if self._x.size == 0:
            raise ValueError("Interpolator has not been fitted")
        # numpy.interp will return edge values for out-of-range t
        return float(np.interp(t, self._x, self._y))


class LogLinearDiscountFactorInterpolator(LinearInterpolator):
    """Log-linear interpolation on discount factors.

    Internally interpolates on log(df) then exponentiates. This preserves
    positivity but is a simple approximation; replace with more sophisticated
    methods as needed.
    """

    def fit(self, x: Sequence[float], y: Sequence[float]) -> None:
        arr_y = np.asarray(y, dtype=float)
        if np.any(arr_y <= 0.0):
            raise ValueError("Discount factors must be positive for log interpolation")
        super().fit(x, np.log(arr_y))

    def evaluate(self, t: float) -> float:
        log_df = super().evaluate(t)
        return float(np.exp(log_df))


class MonotonicCubicInterpolator(Interpolator):
    """Placeholder for a monotonic cubic interpolator.

    A proper implementation (e.g., Fritsch-Carlson) should be added later.
    """

    def fit(self, x: Sequence[float], y: Sequence[float]) -> None:
        # TODO: implement monotonic cubic interpolation
        raise NotImplementedError("MonotonicCubicInterpolator is a placeholder")

    def evaluate(self, t: float) -> float:
        raise NotImplementedError("MonotonicCubicInterpolator is a placeholder")
