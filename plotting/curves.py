"""Curve plotting helpers using matplotlib.

These functions accept a `YieldCurve`-like object and return a
`matplotlib.figure.Figure`. They intentionally do not alter curve state.
"""
from __future__ import annotations

from typing import Iterable

import numpy as np

import matplotlib.pyplot as plt


try:
    # prefer top-level import when running from src on PYTHONPATH
    from curves.curve import YieldCurve  # type: ignore
except Exception:
    from src.curves.curve import YieldCurve  # type: ignore


def _sample_times(max_years: float = 30.0, n: int = 201) -> np.ndarray:
    return np.linspace(0.0, max_years, n)[1:]


def plot_discount_curve(curve: YieldCurve, max_years: float = 30.0) -> plt.Figure:
    """Plot the discount factor curve and return the figure."""
    ts = _sample_times(max_years)
    dfs = np.array([curve.discount_factor(t) for t in ts])
    fig, ax = plt.subplots(figsize=(8, 4))
    ax.plot(ts, dfs, label="Discount Factor")
    ax.set_xlabel("Time (years)")
    ax.set_ylabel("Discount Factor")
    ax.set_title("Discount Factor Curve")
    ax.grid(True)
    ax.legend()
    return fig


def plot_zero_curve(curve: YieldCurve, max_years: float = 30.0) -> plt.Figure:
    """Plot continuously compounded zero rates derived from the curve."""
    ts = _sample_times(max_years)
    zs = np.array([curve.zero_rate(t) for t in ts])
    fig, ax = plt.subplots(figsize=(8, 4))
    ax.plot(ts, zs * 100.0, label="Zero Rate")
    ax.set_xlabel("Time (years)")
    ax.set_ylabel("Zero Rate (%)")
    ax.set_title("Zero Rate Curve (continuous compounding)")
    ax.grid(True)
    ax.legend()
    return fig


def plot_forward_curve(curve: YieldCurve, max_years: float = 30.0, dt: float = 0.5) -> plt.Figure:
    """Plot simple forward rates f(t, t+dt) sampled across the curve."""
    ts = np.arange(dt, max_years, dt)
    fwds = np.array([curve.forward_rate(t, t + dt) for t in ts])
    fig, ax = plt.subplots(figsize=(8, 4))
    ax.plot(ts, fwds * 100.0, label=f"Forward {dt}y")
    ax.set_xlabel("Time (years)")
    ax.set_ylabel("Forward Rate (%)")
    ax.set_title("Forward Curve")
    ax.grid(True)
    ax.legend()
    return fig


def compare_curves(curves: Iterable[YieldCurve], labels: Iterable[str] | None = None, max_years: float = 30.0) -> plt.Figure:
    """Plot multiple discount curves for comparison.

    Args:
        curves: iterable of YieldCurve objects
        labels: optional iterable of labels; must match curves length
    """
    ts = _sample_times(max_years)
    fig, ax = plt.subplots(figsize=(8, 4))
    for i, curve in enumerate(curves):
        dfs = np.array([curve.discount_factor(t) for t in ts])
        label = None
        if labels is not None:
            try:
                label = list(labels)[i]
            except Exception:
                label = f"curve_{i}"
        ax.plot(ts, dfs, label=label)
    ax.set_xlabel("Time (years)")
    ax.set_ylabel("Discount Factor")
    ax.set_title("Discount Factor Comparison")
    ax.grid(True)
    ax.legend()
    return fig
