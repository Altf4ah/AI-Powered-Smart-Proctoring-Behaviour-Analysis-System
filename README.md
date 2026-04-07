# AI-Powered Smart Proctoring & Behaviour Analysis System

A real-time, modular AI platform that monitors exam/interview sessions and detects suspicious behaviour using computer vision + temporal reasoning.

## Why this project is valuable

This project demonstrates end-to-end engineering:
- **Computer vision inference** (face, gaze, object/person detection)
- **Temporal behaviour intelligence** (events over windows of time)
- **Decision engine design** (rule-based + ML scoring)
- **Full-stack product thinking** (backend APIs + dashboard + storage)
- **Deployment readiness** (containerized services)

---

## System architecture

```text
[ Webcam/Mic ]
      |
      v
[ Ingestion Service ]
      |
      v
[ AI Inference Pipeline ] ---> [ Event Buffer ] ---> [ Decision Engine ]
      |                                |                    |
      |                                v                    v
      |                         [ Session DB ]       [ Suspicion Score ]
      |                                                     |
      +------------------------> [ WebSocket Gateway ] <----+
                                      |
                                      v
                               [ React Dashboard ]
```

### Core modules

1. **Input Layer**
   - Webcam stream (required)
   - Mic stream (optional)

2. **AI Processing Layer**
   - Face detection + tracking
   - Eye gaze estimation
   - Head pose estimation
   - Person count detection (multi-person flag)
   - Phone/object detection
   - Face presence/absence tracking

3. **Temporal Analysis Layer**
   - Sliding-window event aggregation
   - Frequency + duration features
   - Behaviour timelines (e.g., “looked away 5 times in 10s”)

4. **Decision Engine**
   - Rule-based thresholds (interpretable)
   - Optional ML classifier on temporal features
   - Suspicion score and event explanations

5. **Backend + Data Layer**
   - FastAPI for APIs
   - WebSockets for live updates
   - PostgreSQL/SQLite for events and metadata
   - Object storage for snapshots/clips

6. **Frontend Dashboard**
   - Live stream status
   - Real-time alerts
   - Timeline of events
   - Session playback + explanation panel

---

## Recommended folder structure

```text
smart-proctor/
├── apps/
│   ├── api/                     # FastAPI app
│   │   ├── main.py
│   │   ├── routes/
│   │   ├── schemas/
│   │   └── services/
│   └── dashboard/               # React/Next.js frontend
├── services/
│   ├── ingestion/               # webcam/mic capture adapters
│   ├── inference/               # CV models & frame processors
│   ├── temporal/                # windowing + feature generation
│   ├── scoring/                 # decision logic + suspicion scoring
│   └── notifier/                # websocket/broker publisher
├── models/
│   ├── yolo/                    # object detector weights/config
│   ├── gaze/
│   └── anti_spoof/
├── data/
│   ├── raw/
│   ├── processed/
│   └── samples/
├── infra/
│   ├── docker/
│   ├── compose/
│   └── monitoring/
├── tests/
│   ├── unit/
│   ├── integration/
│   └── e2e/
├── scripts/
│   ├── run_local.sh
│   ├── benchmark_fps.py
│   └── seed_demo_session.py
└── README.md
```

---

## Build roadmap (execution plan)

### Phase 1 — MVP CV pipeline (Week 1)
- Capture webcam frames in real-time
- Add face detection + face-missing detection
- Add basic event logging (timestamp, event_type, confidence)
- Output simple alerts in terminal

**Deliverable:** Real-time processing loop with basic flags.

### Phase 2 — Behaviour intelligence (Week 2)
- Add gaze + head-pose estimation
- Add person-count and phone detection
- Build temporal aggregation (`N events per time window`)
- Define explainable rules for suspicion scoring

**Deliverable:** Interpretable score + reason strings.

### Phase 3 — Backend + dashboard (Week 3)
- FastAPI endpoints for sessions/events
- WebSocket stream for live alerts
- Dashboard with timeline and suspicion graph
- Persist event data to DB

**Deliverable:** Live monitor UI with historical timeline.

### Phase 4 — Hardening + evaluation (Week 4)
- Add anti-spoofing baseline checks
- Tune thresholds to reduce false positives
- Run benchmark: FPS, latency, precision/recall per event
- Dockerize full stack

**Deliverable:** Demo-ready, measurable system.

---

## Suspicion score (reference design)

```text
score =
  w1 * gaze_away_frequency
+ w2 * face_absence_duration
+ w3 * phone_presence_ratio
+ w4 * multi_person_occurrence
+ w5 * sudden_motion_index
```

### Example alert explanation
- `HIGH (0.86): looked away 7 times in 15s, face absent 4.2s, phone detected in 6 frames`

This keeps decisions transparent and interview-friendly.

---

## KPI targets for resume claims

Track and report:
- End-to-end latency (ms/frame)
- Inference throughput (FPS)
- False positive rate by event type
- Precision/recall for suspicious-session classification
- Uptime/reliability for long sessions

Example claim format:
- “Processed live video at **24 FPS** with <**120ms** end-to-end latency.”
- “Reduced false positives by **18%** using temporal rule tuning.”

---

## Recruiter-ready project narrative

> Built a real-time behavioural intelligence system for remote proctoring using modular CV inference, temporal event analysis, and explainable suspicion scoring, deployed as a full-stack application with live alerting and session analytics.

---

## Future upgrades (startup-level)

- Identity verification + liveness (challenge-response)
- Speaker diarization + whisper-based transcript anomalies
- Federated/privacy-preserving on-device inference
- Human-in-the-loop review workflow
- Adaptive scoring personalized per session profile

---

## Quick start (planned)

```bash
# backend
cd apps/api
uvicorn main:app --reload

# frontend
cd apps/dashboard
npm install && npm run dev
```

(Scaffold to be added in subsequent commits.)
