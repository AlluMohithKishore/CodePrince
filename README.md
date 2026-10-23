# DSA Forge

Local-first, personalized DSA practice platform. It uses FastAPI + SQLite and a React/Vite client; no paid APIs or cloud services are required.

## Quick start

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r backend/requirements.txt
uvicorn app.main:app --app-dir backend --reload --port 8000

cd frontend
npm install
npm run dev
```

Open `http://localhost:5173`. The API is available at `http://localhost:8000/docs`.

## Execution security

`POST /api/run` and `POST /api/submit` use a short-lived Docker container when Docker is installed. The supplied executor disables networking, drops capabilities, runs as an unprivileged user, has read-only root storage, and applies CPU/memory/process/output/time limits. Docker is not installed in this environment, so the API reports `503` instead of falling back to unsafe in-process execution.

For public use, put the executor on isolated hosts/VMs and add queueing, per-user rate limits, image scanning, kernel hardening, observability, and a stronger sandbox such as gVisor or Firecracker.

## Data and import format

The SQLite database is stored at `backend/dsa_forge.db` (or `DATABASE_URL`). Seed data is created automatically on first start. `GET /api/export` returns versioned JSON; `POST /api/import` accepts `{ "version": 1, "questions": [...] }` and validates required fields.

## Test

```powershell
pytest backend/tests
cd frontend; npm run build
```
