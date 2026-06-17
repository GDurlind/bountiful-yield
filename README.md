# bountiful-yield
Can't believe I fixed income

A modern Python library for fixed income analytics, curve construction, and quantitative research.

## Overview

bountiful-yield is an open-source quantitative finance library focused on building robust, transparent, and performant fixed income infrastructure.

The project begins with yield curve construction and will expand into bond pricing, interest rate derivatives, risk analytics, and relative value analysis.

Unlike many existing libraries, bountiful-yield places equal emphasis on:

* Numerical stability
* Market conventions
* Performance
* Diagnostics
* Testing
* Research workflows

The goal is to provide a production-quality framework similar to the internal tooling used by fixed income trading, risk, and quantitative research teams.

---

## Features

### Yield Curve Construction

* Zero curve bootstrapping
* Discount factor generation
* Spot rate calculations
* Forward rate calculations
* Curve interpolation and extrapolation

### Interpolation Models

* Linear
* Log-linear discount factor
* Cubic spline
* Monotonic cubic
* Nelson-Siegel
* Nelson-Siegel-Svensson

### Diagnostics

* Arbitrage detection
* Monotonicity validation
* Calibration diagnostics
* Forward curve analysis
* Reporting and visualisation

### Performance

* NumPy-based vectorisation
* Numba acceleration
* Benchmarking suite
* Future support for JAX-based differentiation and calibration

---

## Example

```python
from bountiful-yield.curves import YieldCurve
from bountiful-yield.interpolation import MonotonicCubic

curve = YieldCurve.bootstrap(
    instruments=instruments,
    interpolation=MonotonicCubic(),
)

curve.zero_rate(5.0)
curve.forward_rate(5.0, 10.0)
curve.discount_factor(7.0)

curve.check_arbitrage()
curve.check_monotonicity()
curve.report()
```

---

## Roadmap

### Phase 1 — Curve Engine

* Yield curve abstraction
* Discount factors
* Bootstrapping framework
* Interpolation models
* Diagnostics and validation

### Phase 2 — Fixed Income Instruments

* Bond cashflow generation
* Bond pricing
* Yield calculations
* Z-spreads
* OAS analytics

### Phase 3 — Interest Rate Derivatives

* OIS swaps
* Interest rate swaps
* Basis swaps
* Multi-curve frameworks

### Phase 4 — Risk Analytics

* DV01
* Key-rate duration
* Convexity
* Curve stress testing

### Phase 5 — Relative Value

* Rich/cheap analysis
* Curve trades
* Butterfly trades
* Spread analytics

---

## Project Philosophy

bountiful-yield is designed around a few core principles:

1. Discount factors are the fundamental representation of a curve.
2. Diagnostics are first-class citizens.
3. Numerical correctness takes priority over convenience.
4. Performance should be measurable and benchmarked.
5. APIs should be intuitive, explicit, and composable.

---

## Status

This project is currently under active development.

The initial focus is building a robust yield curve engine that serves as the foundation for future fixed income analytics modules.

Contributions, feedback, and discussion are welcome.
