"""Plotting utilities for bountiful-yield research notebooks.

The plotting package provides simple matplotlib-based visualisations for
YieldCurve objects. Importing is tolerant of project layout: notebooks
commonly add `src/` to `sys.path`, but the plotting functions attempt to
import from both `curves` and `src.curves` locations.
"""

__all__ = ["curves", "diagnostics"]
