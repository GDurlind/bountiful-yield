"""Market instrument interfaces used for bootstrapping.

This module defines the `CurveInstrument` abstract base and a couple of
small example instruments. In production the instruments module would
contain full valuation logic for deposits, FRAs, swaps and bonds.
"""
from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass


class CurveInstrument(ABC):
    """Abstract interface for instruments used in curve construction."""

    @abstractmethod
    def maturity(self) -> float:
        """Return time to maturity in years."""

    @abstractmethod
    def market_quote(self) -> float:
        """Return market quote (rate or price) for the instrument."""


@dataclass
class Deposit(CurveInstrument):
    """Simple deposit instrument used as an example.

    Real implementations should include daycount conventions, compounding
    and notional.
    """

    tenor: float
    rate: float

    def maturity(self) -> float:
        return float(self.tenor)

    def market_quote(self) -> float:
        return float(self.rate)
