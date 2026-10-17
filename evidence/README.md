# Genuine evidence checklist

The actual execution record is [github-progress.md](github-progress.md). All screenshots listed as captured are real browser captures from this project; no Copilot output or local Docker success is fabricated.

| Evidence | Status |
| --- | --- |
| Local lint/tests/coverage | Captured in local/results-after-copilot.txt; 30 passed and 100% coverage (initial results.txt records 28) |
| Local live HTTP | Captured in local/http-smoke.json; 200/201/422 |
| API documentation | screenshots/11-api-docs.jpg and generated docs/openapi.json |
| Organized repository (now public by approval) | screenshots/01-repository-files.jpg |
| Merged feature PR | screenshots/02-pr-merged.jpg; PR #8 |
| Branch-protection configuration | screenshots/13-branch-protection-enforced.jpg and 15-protected-upload.jpg; earlier plan-limit image is historical |
| Successful main Actions | screenshots/04-actions-success.jpg |
| Hosted CI coverage | screenshots/10-ci-coverage.jpg and local/github-test-log-snapshot.txt |
| Private board | screenshots/05-board.jpg and 05-board-done.jpg show both horizontal sections |
| Successful GHCR publishing | screenshots/06-publish-success.jpg |
| Private package | screenshots/06-ghcr-private.jpg; SHA tag/digest recorded in github-progress.md |
| Local Docker build/run | Pending working Docker engine |
| Actual Copilot API/test/refactor/documentation work | Captured in screenshots/07, 08, 09 and 12 plus copilot/ raw responses and docs/copilot-evidence.md |
| Copilot CLI | Conditional on supported installed product; not executed |

The board's item-closed automation and merged linked PR moved completed API, test/refactor, CI and publisher work to Done. Docker and full-evidence tasks remain open; actual Copilot work is recorded in PR #9, which links issue #6. Keep the full-evidence task open until those missing sources are captured.

Original exam documents have not been modified. Check the submission identity before adding final evidence to them. The earlier failed attempt is historical; submit the later actual responses and reviewed changes.

## Subsequent verified update: 17 October 2026

User explicitly approved making the repository public to enforce protection. Visibility changed to Public; the main rule now applies to one branch without the earlier plan warning. PRs, up-to-date branches, lint/tests/container-build passing checks and administrator enforcement are configured; force pushes/deletion are disallowed. Independent approval remains off under the solo adaptation; CODEOWNERS still identifies the real owner. Earlier private/plan-limit screenshots are historical, superseded by 13-branch-protection-enforced.jpg and 14-public-repository.jpg.

Actual GitHub Copilot Free web assistance now succeeded: API, tests, numeric refactor, README/API reference and coverage-command explanation. See docs/copilot-evidence.md and evidence/copilot/ for genuine raw responses and accepted/rejected decisions. Two accepted tests bring the local suite to 30, all passing at 100% coverage; see evidence/local/results-after-copilot.txt. Earlier 28-test CI evidence remains historical. No IDE or Copilot CLI execution is claimed.

The remaining local Docker prerequisite is explicit: WSL and Docker Desktop were absent. User approved preparing official setup; docs/setup-docker.md supplies the exact owner steps. Administrator prompts, agreement and restart are for the user. Do not mark local Docker or the full-evidence issue complete until actual local execution succeeds. The private package/board have not been made public by the repository visibility change instruction.
