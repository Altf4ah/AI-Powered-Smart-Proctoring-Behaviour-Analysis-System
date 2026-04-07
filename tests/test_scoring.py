from smart_proctor import aggregate_window_metrics, compute_suspicion_score, explain_score


def test_compute_score_in_range() -> None:
    metrics = aggregate_window_metrics(
        {
            "gaze_away_count": 5,
            "face_absent_seconds": 2.5,
            "phone_detected_frames": 5,
            "multi_person_frames": 1,
            "sudden_motion_events": 2,
        },
        total_frames=50,
        window_seconds=10,
    )

    score = compute_suspicion_score(metrics)
    assert 0.0 <= score <= 1.0


def test_explanation_contains_reason() -> None:
    metrics = aggregate_window_metrics(
        {
            "gaze_away_count": 7,
            "face_absent_seconds": 4.0,
            "phone_detected_frames": 2,
            "multi_person_frames": 1,
        },
        total_frames=40,
        window_seconds=10,
    )
    score = compute_suspicion_score(metrics)
    explanation = explain_score(metrics, score)

    assert "looked away" in explanation
    assert "face absent" in explanation
