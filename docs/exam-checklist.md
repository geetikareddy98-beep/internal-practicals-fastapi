# Exam requirement checklist

Account-stage update: the GitHub repository (now public with user approval), source uploads, real successful main CI, valid owner rules, seven linked issues, five-column private board and an enforced main protection rule now exist. See `../evidence/github-progress.md` for verified URLs and exact limitations; the entries below now reflect verified progress, including the merged PR and private GHCR publication.

Source review: both supplied DOCX files were read completely, including their tables and footer text. Neither contains embedded media. They contain explanatory assignments and illustrative code rather than a separate numbered marking rubric. This checklist treats the described implementation and evidence as deliverables, while identifying suggestions and conditional features explicitly. A shared Python REST API is compatible with both documents; neither requires separate repositories.

Statuses: **Implemented** means files exist; **Verified locally** requires actual execution; **Pending** means an external action or evidence is still needed. The local results record supplies exact execution outcomes. No account action or screenshot is implied by source configuration alone.

## Exam 1 GitHub DevOps

| Document section | Deliverable | Status and location |
| --- | --- | --- |
| 1 Introduction and architecture | Explain CI, delivery/deployment and architecture flow | Implemented: `docs/devops.md` |
| 1 | Select GitHub Flow; explain short-lived branches and review | Implemented: `docs/devops.md`, `docs/github-setup.md`; verified feature PR #8 merged after passing checks |
| 1 | Define success metrics | Implemented: `docs/devops.md`; actual run links and durations in `evidence/github-progress.md` |
| 2 Repository setup | Source, dependencies, tests, Dockerfile, workflow, README | Implemented in project root |
| 2 | Actual organized GitHub repository | Verified public repository: geetikareddy98-beep/internal-practicals-fastapi; uploaded through authenticated browser |
| 2 | Stable main and focused feature branch | Verified main and feature/record-github-evidence; PR #8 merged; local/remote histories differ as documented |
| 2 | PR purpose, linked issue, validation, configuration changes | Verified PR #8 with purpose, linked issue #3, validation and configuration details |
| 2 | Protect main with PRs and passing actual checks | Verified enforced public-repository rule: PR required, up-to-date branch and actual lint/tests/container-build checks required |
| 2 | Approval count adapted to team; restrict force pushes/deletion; review bypass | Configured solo adaptation with no independent approval requirement; force pushes/deletion and admin bypass disallowed; enforced on public repository |
| 2 | CODEOWNERS using real write-access collaborators | Verified real owner @geetikareddy98-beep in CODEOWNERS; independent owner approval not required under the documented solo adaptation |
| 2 | Setup, local commands, configuration and startup README | Implemented: `README.md` |
| 3 Pipeline | PR and main-push triggers, clean Python 3.12 install | Verified main and pull_request runs; Python 3.12 clean hosted jobs |
| 3 | Ruff, pytest, Docker build | Verified locally: Ruff and 30 tests after Copilot review; historical CI: 28 tests; hosted Docker build and health smoke test pass; local Docker remains pending |
| 3 | Least privilege and timeouts | Implemented per-job permissions and timeouts |
| 3 | Publish only after passing trusted main push | Verified after explicit approval: main run 39027867693 published only after all three checks passed |
| 3 | GHCR token, package-write only for publisher, SHA tag, lowercase name | Verified private GHCR package with lowercase name and full SHA tag, published via temporary GITHUB_TOKEN |
| 3 | Test reports and useful failure logs | Verified test-reports and Docker build artifacts on the successful main run |
| 4 Containers | Multi-stage build and correct FastAPI startup | Hosted CI build and health smoke verified; required local build/run remains pending |
| 4 | Runtime uvicorn, non-root user, excluded caches/secrets | Implemented runtime dependency file, Dockerfile, `.dockerignore` |
| 4 | Build and run locally; request health; inspect failure logs | Pending: Docker unavailable on PATH |
| 4 | Registry visibility/settings and safe credentials | Verified Private package visibility after approved publication; no credentials in source |
| 4 | Image maintenance and hygiene | Documented in `docs/devops.md`; scanning/digest pinning are recommendations, not claimed executed |
| 5 Agile board | GitHub Projects with Backlog, Ready, In Progress, In Review, Done | Verified private Internal practicals board with all five statuses in order |
| 5 | Status, Priority, Assignee, Iteration, Due Date | Verified Status, Assignees, Priority (High/Medium/Low), Due Date and Iteration; no exam due dates invented |
| 5 | Issues with acceptance criteria, labels and linked PRs | Verified seven assigned issues; linked PR #8; bug/documentation/CI/CD/security labels available |
| 5 | Board automation and updates | Verified item-closed sets Done; PR merge closed issue #3 and moved completed items to Done |
| 5 | Short retrospective | Updated factual retrospective in `docs/devops.md` and execution record |
| 5 | Genuine board screenshot and successful Actions screenshot | Captured genuine board, Actions, merged PR, package and coverage screenshots in `evidence/screenshots/` |
| 1–5 | Conclusion and references | Implemented: `docs/devops.md` |

Conditional/optional: develop branch and merge queue are explicitly optional; database service containers apply only if using a database (this project does not). Docker Hub is an alternative to GHCR, not an additional registry requirement. Deployment is described as occurring when approved; no deployment target is specified. Latest/release tags, production controls, mutation testing and security scanners are improvements rather than mandatory additions. The CI container health smoke test implements the document's suggested extra validation.

## Exam 2 GitHub Copilot

| Document section | Deliverable | Status and location |
| --- | --- | --- |
| 1 Methodology | Human-led prompts, review, tests, transparency and privacy | Documented: `docs/copilot-evidence.md`; actual Copilot web session recorded |
| 1 | Discuss limitations, ethics and productivity measures | Documented in Copilot procedure; no invented time-saving claim |
| 2 Prompt engineering | Specific example prompt, assumptions, focused generation and review | Verified real specific prompts and generated API/tests/refactor/docs; see docs/copilot-evidence.md |
| 2 API | FastAPI GET /health returns 200 and status ok | Verified locally: `evidence/local/http-smoke.json` |
| 2 | POST /items, required non-empty name, 201 and validation errors | Verified locally: 201/422 live HTTP responses and passing tests |
| 2 | Type hints, concise docstrings, no hard-coded secrets | Implemented |
| 2 | In-memory limitations and OpenAPI review | Documented; schema assertions included in tests |
| 3 Tests | Health, success, empty/missing name, status and body assertions | Verified locally: passing suite in `evidence/local/results.txt` |
| 3 | Maximum length, Unicode, non-string, malformed JSON, repeated requests | Implemented with boundary and no-side-effect assertions |
| 3 | Fixtures reset state | Implemented autouse fixture |
| 3 | Coverage greater than 80% | Verified locally after Copilot: 30 tests, 100% coverage; historical hosted CI: 28 tests, 100%; minimum 81% |
| 3 | Review generated tests; rerun after refactor and in CI | Verified actual Copilot review and two accepted tests; local suite rerun; new remote CI pending |
| 4 Refactoring | Preserve legacy baseline, explain/fix/optimize with available interface | Verified real Copilot refactor and explanation; draft, review and baseline comparison retained |
| 4 | Typed total ignores None using identity check | Implemented: `app/numeric.py` |
| 4 | Empty, all-None, mixed, negative, decimal tests | Implemented: `tests/test_numeric.py`, plus mutation/unsupported-string tests |
| 4 | Verify behavior before/after, avoid unmeasured complexity/speed claims | Verified five before/after cases: `evidence/local/refactor-comparison.json`; no speed improvement claimed |
| 5 Documentation | README Python version, installation, startup, examples, limitations | Implemented: `README.md` |
| 5 | Docstrings and API documentation including schemas/status/configuration | Implemented: `app/`, `docs/api.md` |
| 5 | Review generated OpenAPI and save artifact | Verified schema assertions; saved `docs/openapi.json` |
| 5 CLI | Check installed Copilot product; verify current CLI syntax where supported | Actual Copilot web command explanation recorded; CLI not installed, conditional feature not claimed executed |
| 1–5 | Genuine Copilot usage evidence and human review record | Verified actual browser Copilot suggestions, screenshots and accepted/rejected review; initial Codex provenance disclosed |

Conditional/optional: `/explain`, `/fix`, `/optimize` and CLI features depend on the installed product. Plain-language prompts can serve the same purpose when slash commands are absent. Production authentication, persistent database, rate limits and pagination are outside this teaching example. Profiling is necessary before claiming a performance optimization; no such claim is made here.

## Source identity

Both provided documents name Sudheesh Vinnakota. No identity has been inferred from the computer account, and the supplied documents have not been edited. Confirm the submission name before finalizing any exam cover sheet.
