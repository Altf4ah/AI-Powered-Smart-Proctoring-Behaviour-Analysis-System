from __future__ import annotations

from dataclasses import dataclass
from typing import Dict


@dataclass(frozen=True)
class ScoreWeights:
    gaze_away_frequency: float = 0.30
    face_absence_duration: float = 0.25
    phone_presence_ratio: float = 0.20
    multi_person_occurrence: float = 0.15
    sudden_motion_index: float = 0.10


def _clamp_01(value: float) -> float:
    return max(0.0, min(1.0, value))


def compute_suspicion_score(metrics: Dict[str, float], weights: ScoreWeights | None = None) -> float:
    """Compute a bounded suspicion score in [0, 1].

    Expected metric inputs are normalized to [0, 1].
    """
    w = weights or ScoreWeights()
    weighted_sum = (
        w.gaze_away_frequency * _clamp_01(metrics.get("gaze_away_frequency", 0.0))
        + w.face_absence_duration * _clamp_01(metrics.get("face_absence_duration", 0.0))
        + w.phone_presence_ratio * _clamp_01(metrics.get("phone_presence_ratio", 0.0))
        + w.multi_person_occurrence * _clamp_01(metrics.get("multi_person_occurrence", 0.0))
        + w.sudden_motion_index * _clamp_01(metrics.get("sudden_motion_index", 0.0))
    )
    return round(_clamp_01(weighted_sum), 4)


def explain_score(metrics: Dict[str, float], score: float) -> str:
    reasons = []

    if metrics.get("gaze_away_count", 0) >= 5:
        reasons.append(f"looked away {int(metrics['gaze_away_count'])} times")
    if metrics.get("face_absent_seconds", 0.0) >= 2.0:
        reasons.append(f"face absent {metrics['face_absent_seconds']:.1f}s")
    if metrics.get("phone_detected_frames", 0) > 0:
        reasons.append(f"phone in {int(metrics['phone_detected_frames'])} frames")
    if metrics.get("multi_person_frames", 0) > 0:
        reasons.append("multiple people detected")

    label = "LOW" if score < 0.35 else "MEDIUM" if score < 0.7 else "HIGH"
    suffix = ", ".join(reasons) if reasons else "no major suspicious events"
    return f"{label} ({score:.2f}): {suffix}"
