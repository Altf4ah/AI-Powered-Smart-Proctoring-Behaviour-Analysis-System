"""Core package for Smart Proctor scoring and temporal analysis."""

from .scoring import compute_suspicion_score, explain_score
from .temporal import aggregate_window_metrics

__all__ = [
    "compute_suspicion_score",
    "explain_score",
    "aggregate_window_metrics",
]
