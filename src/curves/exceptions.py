"""Curve-related exceptions."""
from __future__ import annotations

class CurveError(Exception):
    """Base exception for curve-related errors."""


class BootstrapError(CurveError):
    """Raised when bootstrapping fails."""
