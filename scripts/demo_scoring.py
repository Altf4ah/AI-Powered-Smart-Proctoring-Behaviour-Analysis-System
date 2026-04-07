import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))

from smart_proctor import aggregate_window_metrics, compute_suspicion_score, explain_score


def main() -> None:
    sample_events = {
        "gaze_away_count": 7,
        "face_absent_seconds": 4.2,
        "phone_detected_frames": 6,
        "multi_person_frames": 2,
        "sudden_motion_events": 3,
    }

    metrics = aggregate_window_metrics(sample_events, total_frames=60, window_seconds=15)
    score = compute_suspicion_score(metrics)
    explanation = explain_score(metrics, score)

    print("Metrics:", metrics)
    print("Score:", score)
    print("Explanation:", explanation)


if __name__ == "__main__":
    main()
