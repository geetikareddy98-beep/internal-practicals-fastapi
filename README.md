# Shared FastAPI internal practical project

This teaching project supports Exam 1 GitHub DevOps and Exam 2 GitHub Copilot. It provides an in-memory Items API, validation tests, numeric refactoring, and CI/container configuration. See [the requirement checklist](docs/exam-checklist.md) for the distinction between implemented work and remaining account/evidence tasks.

## Verified GitHub results

The private repository, feature PR #8, main/PR CI checks, private Projects board and approved private GHCR publication are complete. See [the execution record](evidence/github-progress.md) for actual run links, image tag/digest and screenshots. Local Docker execution, genuine Copilot output and plan-supported branch-protection enforcement remain unfinished.

## Setup on Windows

Use Python 3.12. From this project folder in PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe -m uvicorn app.main:app --reload
```

No environment variables or secrets are required by the API. If `python` does not run, install Python from its official source or use a working Python 3.12 executable. Activation is optional because these commands use the environment's interpreter directly.

Open http://127.0.0.1:8000/docs to try the API. `/redoc` provides alternative documentation and `/openapi.json` provides its schema. Stop the server with Ctrl+C.

## API contract

| Request | Successful response | Validation |
| --- | --- | --- |
| GET `/health` | 200, `{"status":"ok"}` | No input |
| POST `/items`, `{"name":"Notebook"}` | 201, `{"id":1,"name":"Notebook"}` | Required string, 1–100 characters; invalid requests return 422 |

```powershell
Invoke-RestMethod http://127.0.0.1:8000/health
Invoke-RestMethod http://127.0.0.1:8000/items -Method Post -ContentType 'application/json' -Body '{"name":"Notebook"}'
```

Names are preserved exactly, including Unicode and whitespace, following the document's length-based example. A whitespace-only string has nonzero length and is accepted. Extra request fields are ignored under Pydantic's default policy. Items are stored in memory: data and identifiers reset on process restart. This is a single-process classroom demonstration with no persistence, authentication or concurrency guarantees; it is unsuitable for production writes.

## Verify locally

```powershell
.\.venv\Scripts\python.exe -m ruff check .
.\.venv\Scripts\python.exe -m ruff format --check .
.\.venv\Scripts\python.exe -m pytest -q --cov=app --cov-branch --cov-report=term-missing
```

Coverage must be at least 81%, which enforces the exam's greater-than-80% target. Tests reset shared state and check response bodies, invalid input, boundary values, Unicode, malformed JSON, sequential identifiers, OpenAPI, and sum behavior. `app.numeric.total` sums integers/floats while ignoring `None`; empty/all-None input returns zero. Unsupported strings raise `TypeError`; Python's normal numeric behavior applies to booleans and floating-point rounding.

## Container and CI

```powershell
docker build -t sample-api:local .
docker run --rm -p 8000:8000 sample-api:local
```

The multi-stage image contains runtime dependencies only and runs as a non-root user. CI runs on pull requests to `main`, pushes to `main`, and manual dispatch. Its check names are `lint`, `tests`, and `container-build`; the container check builds and smoke-tests `/health`. CI uploads coverage, JUnit and OpenAPI artifacts.

Publishing requires successful checks on a push to `main` AND repository variable `ENABLE_GHCR_PUBLISH=true`. Leave it unset until publication is approved. The workflow uses lowercase GHCR naming, the full commit SHA tag, and GitHub's temporary `GITHUB_TOKEN` with package-write access limited to the publishing job. No personal token needs to be committed or shared. See [GitHub setup](docs/github-setup.md).

## Practical records

- [API details](docs/api.md)
- [Every exam deliverable and its status](docs/exam-checklist.md)
- [GitHub setup and board issues](docs/github-setup.md)
- [Copilot prompts and evidence procedure](docs/copilot-evidence.md)
- [Architecture, metrics and retrospective](docs/devops.md)
- [Evidence to capture](evidence/README.md)

Code initially produced with Codex must not be presented as Copilot-generated. Actual Copilot sessions, GitHub runs, container execution and board screenshots must be recorded when they occur.
