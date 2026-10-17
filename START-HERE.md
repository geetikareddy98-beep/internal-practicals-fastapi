# Start here on this computer

The local project is implemented and verified, but the exams are not yet ready for final submission. GitHub repository settings, board, Actions/GHCR results, local Docker execution and real Copilot evidence are still pending. The original exam documents were read fully and were not edited.

## What already passed

- 28 pytest tests; 100% measured application coverage; minimum enforced at 81%.
- Ruff lint and formatting checks.
- Dependency compatibility check.
- Live HTTP requests: GET health 200, POST item 201, invalid item 422.
- Five legacy/refactored numeric comparisons.
- OpenAPI assertions and saved generated schema.
- Actual browser rendering of API docs, with a genuine saved screenshot.

See `evidence/local/results.txt`, `evidence/local/http-smoke.json`, `evidence/local/refactor-comparison.json`, `docs/openapi.json` and `evidence/screenshots/11-api-docs.jpg`. `first-run-results.txt` preserves an earlier passing run with a deprecation warning; the final run uses the documented httpx2 dependency and has no warnings. These are local results, not GitHub run records.

## Run now with the working environment

The environment created during this session lives outside the deliverable folder in the workspace `work` directory. These commands work on the current computer without relying on its broken default `python` alias:

```powershell
Set-Location 'C:\Users\geetika\Documents\Codex\2026-10-17\hi-3\outputs\shared-exam-project'
$examPython = 'C:\Users\geetika\Documents\Codex\2026-10-17\hi-3\work\.venv\Scripts\python.exe'
& $examPython -m ruff check .
& $examPython -m ruff format --check .
& $examPython -m pytest -q --cov=app --cov-branch --cov-report=term-missing
& $examPython -m uvicorn app.main:app --reload
```

Open http://127.0.0.1:8000/docs. Stop the server with Ctrl+C. A preview server was also started during this session on port 18765; availability after the session depends on the app's process lifecycle. Use these startup commands if the preview stops.

For a portable setup after moving/unzipping the project, follow `README.md` using an installed working Python 3.12. The ZIP does not include a virtual environment, Git metadata or secrets.

## Remaining access and user decisions

1. Add and connect the suggested GitHub integration, or sign in directly to GitHub in the available browser. The inspected in-app session is signed out. Do not share credentials here.
2. Confirm the GitHub owner, repository name and visibility. Proposed name: `internal-practicals-fastapi`. Repository publication and GHCR publication require your approval. The publisher stays disabled meanwhile.
3. Confirm the commit author and student name: the supplied documents name Sudheesh Vinnakota; the machine's Git identity belongs to a different account. No commit has been made with an assumed identity.
4. Open VS Code manually if automation cannot launch it. Install/enable the official GitHub Copilot experience and sign in yourself. Then follow the small tasks in `docs/copilot-evidence.md`; record real results and rerun checks.
5. Provide a working Docker engine for the required local build/run. Docker was not found on PATH; no local container success is claimed.
6. Follow `docs/github-setup.md` for exact push commands, real CODEOWNERS rules, PR, protection, board, issues, automation and approved publication. `docs/exam-checklist.md` tracks every document section; `evidence/README.md` lists each screenshot still needed.

The API preserves the illustrative document contract, including accepting whitespace-only names as non-empty strings. This assumption is explicit in the README and tests. Ask the instructor if they intend trimmed nonblank names instead.
