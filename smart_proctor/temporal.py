from __future__ import annotations

from typing import Dict


def _safe_ratio(count: float, total: float) -> float:
    return 0.0 if total <= 0 else count / total


def aggregate_window_metrics(events: Dict[str, float], total_frames: int, window_seconds: float) -> Dict[str, float]:
    """Aggregate raw event counters into normalized features for scoring."""
    total_frames = max(total_frames, 1)
    window_seconds = max(window_seconds, 1e-6)

    gaze_away_count = events.get("gaze_away_count", 0)
    face_absent_seconds = events.get("face_absent_seconds", 0.0)
    phone_detected_frames = events.get("phone_detected_frames", 0)
    multi_person_frames = events.get("multi_person_frames", 0)
    sudden_motion_events = events.get("sudden_motion_events", 0)

    return {
        "gaze_away_frequency": min(gaze_away_count / max(window_seconds, 10.0), 1.0),
        "face_absence_duration": min(face_absent_seconds / window_seconds, 1.0),
        "phone_presence_ratio": _safe_ratio(phone_detected_frames, total_frames),
        "multi_person_occurrence": _safe_ratio(multi_person_frames, total_frames),
        "sudden_motion_index": min(sudden_motion_events / 10.0, 1.0),
        "gaze_away_count": gaze_away_count,
        "face_absent_seconds": face_absent_seconds,
        "phone_detected_frames": phone_detected_frames,
        "multi_person_frames": multi_person_frames,
    }
