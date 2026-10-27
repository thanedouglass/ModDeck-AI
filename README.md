# ModDeck-AI

Real-time Twitch stream co-production engine that helps moderators approve and route community picks to an OBS-friendly overlay.

## Backend

```bash
cd backend
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

## Overlay

```bash
cd overlay
npm install
npm run dev
```

The overlay polls `GET /api/queue` once per second and renders a compact glassmorphism floating dock for OBS browser sources.
