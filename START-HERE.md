# Start here

The code and GitHub pipeline are working. Actual Copilot assistance is now recorded and the user-approved public repository supports enforced main protection. Local Docker execution still needs the Windows setup described below.

## Verified deliverables

- Public repository (approved): https://github.com/geetikareddy98-beep/internal-practicals-fastapi
- Feature PR #8 passed all three checks and was merged with user approval.
- Main CI/CD run: https://github.com/geetikareddy98-beep/internal-practicals-fastapi/actions/runs/39027867693
- Ruff passes; 30 tests pass with 100% coverage locally after Copilot review; earlier hosted CI verified 28 tests.
- Live local API returns health 200, creation 201 and validation 422.
- Hosted Docker image build and health smoke test pass.
- Approved GHCR publication succeeded; actual package visibility verified Private.
- Private board: https://github.com/users/geetikareddy98-beep/projects/1
- Seven issues, five ordered statuses, assignees, Priority, Due Date, Iteration and completion automation are configured.
- Genuine repository, PR, Actions, coverage, board, GHCR and API screenshots are saved under evidence/screenshots.

Read docs/exam-checklist.md for every requirement and evidence/github-progress.md for verified URLs, image tag/digest and exact limitations.

## Run on this computer

PowerShell commands using the working environment created during this session:

```powershell
Set-Location 'C:\Users\geetika\Documents\Codex\2026-10-17\hi-3\outputs\shared-exam-project'
$examPython = 'C:\Users\geetika\Documents\Codex\2026-10-17\hi-3\work\.venv\Scripts\python.exe'
& $examPython -m ruff check .
& $examPython -m ruff format --check .
& $examPython -m pytest -q --cov=app --cov-branch --cov-report=term-missing
& $examPython -m uvicorn app.main:app --reload
```

Open http://127.0.0.1:8000/docs. Stop with Ctrl+C. The ZIP excludes the virtual environment and Git metadata. On another computer, follow README.md with a working Python 3.12 installation.

## Remaining personal steps

1. Complete the official Windows WSL/Docker setup in `docs/setup-docker.md`. Administrator prompts, agreements and any restart need the computer owner. Then run the actual local Docker build, container and health request, and capture the result. Hosted container CI is genuine but does not replace local execution.
2. Confirm the submission name before editing an exam cover sheet. The original documents name Sudheesh Vinnakota; they remain unchanged.

## Continue Git work safely

Browser commits created the actual remote history after terminal authentication failed. The local folder has an independent initial commit. Do not force push it over GitHub. Once terminal authentication works, clone the repository into a fresh folder:

```powershell
git clone https://github.com/geetikareddy98-beep/internal-practicals-fastapi.git
Set-Location internal-practicals-fastapi
git switch -c feature/copilot-review
```

Use the browser/credential manager for sign-in; never paste tokens or passwords into chat or commit them. Future pushes to main will run CI and publish a private SHA-tagged image because ENABLE_GHCR_PUBLISH is now true with user approval.
