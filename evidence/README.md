# Genuine evidence checklist

For the current GitHub results, see [GitHub execution record](github-progress.md). The initial pending entries below predate account sign-in.

Local logs are created by execution and saved under `local/`. They are evidence of local commands only, not screenshots or remote Actions/Copilot success. The original exam documents contain no screenshots. Do not submit this project as fully complete until the pending account tasks and evidence are finished.

| Evidence | What to capture | Status |
| --- | --- | --- |
| Local Ruff and pytest | Full command, successful output, coverage percentage | See `local/results.txt` after execution |
| Live API | Real health response, successful POST, 422 invalid request | See `local/http-smoke.json` after execution; browser screenshot pending |
| Local Docker | Build output, running container, real health response | Pending Docker engine |
| Repository | Actual URL, organized files, main and feature branch | Pending GitHub setup |
| Pull request | Linked issue, real changes, review and passing checks | Pending |
| Branch protection | Actual effective main settings and required check names | Pending |
| Actions run | Green run with lint/tests/container jobs and commit SHA | Pending |
| GHCR image | Successful publisher, package URL, SHA tag and digest | Pending approval and publication |
| Projects board | All five statuses and example real issues visible | Pending |
| Issue automation | Acceptance criteria, linked PR, genuine resulting status | Pending |
| Copilot API/test generation | Actual prompt and visible suggestion in VS Code | Pending real Copilot session |
| Copilot refactor | Original, actual explain/refactor response, accepted result | Pending |
| Copilot documentation/CLI | Actual review; installed CLI help/output if supported | Pending |
| OpenAPI | Interactive /docs and real generated schema | Captured: `screenshots/11-api-docs.jpg`; schema in `docs/openapi.json` |

Keep screenshots in `screenshots/` only after capturing them from the actual project. Suggested names: `01-repository.png`, `02-pr-checks.png`, `03-branch-protection.png`, `04-actions-success.png`, `05-board.png`, `06-ghcr.png`, `07-copilot-api.png`, `08-copilot-tests.png`, `09-copilot-refactor.png`, `10-coverage.png`, `11-api-docs.png`, `12-local-docker.png`. These are planned names, not existing files.

Record URLs and commit SHAs alongside screenshots; avoid credentials in view. Complete the session record in `docs/copilot-evidence.md`. Keep pending items visibly pending until verified. Original source assignment documents have not been modified, and no student identity or signature has been fabricated.
