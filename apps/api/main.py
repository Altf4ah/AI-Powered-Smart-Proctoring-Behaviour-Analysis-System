from __future__ import annotations

from datetime import datetime, timezone
from typing import Dict, List

from fastapi import FastAPI
from pydantic import BaseModel, Field

from smart_proctor import aggregate_window_metrics, compute_suspicion_score, explain_score

app = FastAPI(title="Smart Proctor API", version="0.1.0")

SESSIONS: Dict[str, List[dict]] = {}


class EventPayload(BaseModel):
    session_id: str = Field(..., min_length=2)
    total_frames: int = Field(..., ge=1)
    window_seconds: float = Field(..., gt=0)
    events: Dict[str, float]


@app.get("/health")
def health() -> dict:
    return {"status": "ok", "timestamp": datetime.now(timezone.utc).isoformat()}


@app.post("/score")
def score_window(payload: EventPayload) -> dict:
    metrics = aggregate_window_metrics(
        events=payload.events,
        total_frames=payload.total_frames,
        window_seconds=payload.window_seconds,
    )
    score = compute_suspicion_score(metrics)
    explanation = explain_score(metrics, score)

    record = {
        "ts": datetime.now(timezone.utc).isoformat(),
        "score": score,
        "metrics": metrics,
        "explanation": explanation,
    }
    SESSIONS.setdefault(payload.session_id, []).append(record)

    return {
        "session_id": payload.session_id,
        "score": score,
        "explanation": explanation,
        "metrics": metrics,
    }


@app.get("/sessions/{session_id}")
def get_session(session_id: str) -> dict:
    return {"session_id": session_id, "records": SESSIONS.get(session_id, [])}
