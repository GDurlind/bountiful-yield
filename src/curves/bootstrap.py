"""Bootstrapping engine interfaces.

This module contains the `BootstrapEngine` which will orchestrate
curve building from market instruments and an interpolation strategy.
The current implementation provides interfaces and TODO markers for
future numeric algorithms.
"""
from __future__ import annotations

from typing import Iterable

from .interpolation import Interpolator
from .curve import YieldCurve
from .exceptions import BootstrapError


class BootstrapEngine:
    """Engine that converts market instruments to a `YieldCurve`.

    Args:
        instruments: iterable of market instruments (implementing the
            `CurveInstrument` interface).
        interpolator: interpolation strategy used to represent discount factors.
    """

    def __init__(self, instruments: Iterable, interpolator: Interpolator) -> None:
        self._instruments = list(instruments)
        self._interpolator = interpolator

    def produce(self) -> YieldCurve:
        """Produce a `YieldCurve` from the instruments.

        This is a high-level placeholder. Real implementation will implement
        a proper iterative bootstrap that solves for discount factors consistent
        with instrument market quotes.
        """
        # TODO: implement bootstrapping algorithm
        raise BootstrapError("Bootstrapping not implemented yet")
