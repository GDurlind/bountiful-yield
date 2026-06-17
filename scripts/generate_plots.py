from pathlib import Path
import math

from src.curves.curve import YieldCurve
from src.curves.interpolation import (
    LogLinearDiscountFactorInterpolator,
)

from plotting.curves import (
    plot_discount_curve,
    plot_zero_curve,
    plot_forward_curve,
)


OUTPUT = Path(".plots")


def build_example_curve():
    times = [0.0, 1.0, 5.0, 10.0]

    discount_factors = [
        math.exp(-0.02 * t)
        for t in times
    ]

    interpolator = LogLinearDiscountFactorInterpolator()

    interpolator.fit(
        times,
        discount_factors
    )

    return YieldCurve(
        times=times,
        discount_factors=discount_factors,
        interpolator=interpolator,
    )


def main():

    OUTPUT.mkdir(exist_ok=True)

    curve = build_example_curve()

    plots = {
        "discount": plot_discount_curve,
        "zero": plot_zero_curve,
        "forward": plot_forward_curve,
    }

    for name, plot_fn in plots.items():

        fig = plot_fn(curve)

        fig.savefig(
            OUTPUT / f"{name}.png",
            dpi=150,
            bbox_inches="tight",
        )

    print(
        f"Saved plots to {OUTPUT}"
    )


if __name__ == "__main__":
    main()