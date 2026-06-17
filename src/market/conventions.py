"""Market conventions and common enums.

Keep this module lightweight; real projects encode calendars, daycount
conventions and business-day adjustments here.
"""
from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class DayCount:
    name: str


ACT_365 = DayCount("ACT/365")
ACT_360 = DayCount("ACT/360")
