# Genuine evidence checklist

The actual execution record is [github-progress.md](github-progress.md). All screenshots listed as captured are real browser captures from this project; no Copilot output or local Docker success is fabricated.

| Evidence | Status |
| --- | --- |
| Local lint/tests/coverage | Captured in local/results.txt; 28 passed and 100% coverage |
| Local live HTTP | Captured in local/http-smoke.json; 200/201/422 |
| API documentation | screenshots/11-api-docs.jpg and generated docs/openapi.json |
| Organized private repository | screenshots/01-repository-files.jpg |
| Merged feature PR | screenshots/02-pr-merged.jpg; PR #8 |
| Branch-protection configuration | screenshots/03-branch-protection-plan-limit.jpg; plan prevents enforcement |
| Successful main Actions | screenshots/04-actions-success.jpg |
| Hosted CI coverage | screenshots/10-ci-coverage.jpg and local/github-test-log-snapshot.txt |
| Private board | screenshots/05-board.jpg and 05-board-done.jpg show both horizontal sections |
| Successful GHCR publishing | screenshots/06-publish-success.jpg |
| Private package | screenshots/06-ghcr-private.jpg; SHA tag/digest recorded in github-progress.md |
| Local Docker build/run | Pending working Docker engine |
| Actual Copilot API/test/refactor/documentation work | Pending working Copilot authentication |
| Copilot CLI | Conditional on supported installed product; not executed |

The board's item-closed automation and merged linked PR moved completed API, test/refactor, CI and publisher work to Done. Incomplete Docker, Copilot and full-evidence tasks remain open. Keep the full-evidence task open until those missing sources are captured.

Original exam documents have not been modified. Check the submission identity before adding final evidence to them. Never submit the attempted Copilot prompt as successful Copilot assistance.
