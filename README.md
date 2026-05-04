# Hey Cindy

[![CI](https://github.com/DincyYang/HeyCindy/actions/workflows/test.yml/badge.svg)](https://github.com/DincyYang/HeyCindy/actions/workflows/test.yml)

A distributed voice-controlled automation system. Say **"Hey Cindy, turn on the light"** — the light turns on.

## Architecture

```
Local (Mac)             Cloud (AWS EC2)         Physical
────────────────        ───────────────         ────────
Wake word detect   →    FastAPI server      →   Smart plug
Speech-to-text          SQLite (state)           (coming soon)
NLP pipeline            REST API
Voice feedback          Token-based auth
```

## Tech Stack

- **Backend**: Python, FastAPI, AWS EC2 (t3.micro)
- **NLP**: Rule-based intent parser — normalizer + decision layer
- **Voice**: Porcupine wake word detection, Google Speech-to-Text
- **Auth**: Token-based authentication
- **Testing**: pytest, GitHub Actions CI (80%+ coverage)

## Project Structure

| File | Role |
|------|------|
| `wake_word.py` | Wake word detection (Porcupine) |
| `command_listener.py` | Speech-to-text via Google API |
| `normalizer.py` | Raw text → on / off / unknown |
| `decision.py` | Execute / clarify / reject / ignore |
| `cloud_client.py` | Send command to cloud via REST |
| `command.py` | Execute command + text-to-speech |
| `local_dashboard.py` | Web control panel (Flask) |
| `light_server.py` | Local light state server |

## Run Locally

```bash
# Clone and set up environment
git clone https://github.com/DincyYang/hey_cindy.git
cd hey_cindy
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

# Set environment variables
export HEY_CINDY_CLOUD=http://3.85.92.201:8000
export HEY_CINDY_TOKEN=cindy-dev-token-123

# Start local dashboard (web UI)
python local_dashboard.py
# Open http://127.0.0.1:6060

# Start voice controller
python voice_to_light_wakeword.py
```

## Run Tests

```bash
pytest --cov=. --cov-report=term-missing
```

## Environment Variables

| Variable | Default | Description |
|----------|---------|-------------|
| `HEY_CINDY_CLOUD` | `http://3.234.157.34:8000` | Cloud API base URL |
| `HEY_CINDY_TOKEN` | `cindy-dev-token-123` | Auth token |

## Roadmap

- [x] Wake word detection
- [x] Speech-to-text + NLP pipeline
- [x] Cloud API (FastAPI + AWS EC2)
- [x] Local dashboard
- [x] Unit tests + CI (GitHub Actions)
- [ ] PostgreSQL + Redis (Week 2)
- [ ] React frontend + WebSocket (Week 5–6)
- [ ] LLM fallback for ambiguous commands (Week 9)
- [ ] Physical smart plug integration (Week 10)
