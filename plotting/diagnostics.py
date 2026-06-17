"""Diagnostic plotting helpers that combine multiple curve visualisations."""
from __future__ import annotations

import matplotlib.pyplot as plt
import numpy as np

try:
    from curves.curve import YieldCurve  # type: ignore
except Exception:
    from src.curves.curve import YieldCurve  # type: ignore


def plot_curve_diagnostics(curve: YieldCurve, max_years: float = 30.0) -> plt.Figure:
    """Create a 3-panel diagnostic plot: discount, zero, forward.

    Returns the matplotlib Figure instance.
    """
    ts = np.linspace(0.01, max_years, 200)
    dfs = np.array([curve.discount_factor(t) for t in ts])
    zeros = np.array([curve.zero_rate(t) for t in ts])
    fwds = np.empty_like(ts)
    dt = 0.5
    for i, t in enumerate(ts):
        t2 = min(t + dt, max_years)
        try:
            fwds[i] = curve.forward_rate(t, t2)
        except Exception:
            fwds[i] = np.nan

    fig, axes = plt.subplots(3, 1, figsize=(8, 10), sharex=True)
    axes[0].plot(ts, dfs)
    axes[0].set_ylabel("Discount Factor")
    axes[0].set_title("Discount Factors")

    axes[1].plot(ts, zeros * 100.0)
    axes[1].set_ylabel("Zero Rate (%)")
    axes[1].set_title("Zero Curve")

    axes[2].plot(ts, fwds * 100.0)
    axes[2].set_ylabel("Forward Rate (%)")
    axes[2].set_xlabel("Time (years)")
    axes[2].set_title("Forward Curve (dt=0.5y)")

    fig.tight_layout()
    return fig
