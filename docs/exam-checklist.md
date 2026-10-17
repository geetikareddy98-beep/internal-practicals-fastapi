# Exam requirement checklist

Source review: both supplied DOCX files were read completely, including their tables and footer text. Neither contains embedded media. They contain explanatory assignments and illustrative code rather than a separate numbered marking rubric. This checklist treats the described implementation and evidence as deliverables, while identifying suggestions and conditional features explicitly. A shared Python REST API is compatible with both documents; neither requires separate repositories.

Statuses: **Implemented** means files exist; **Verified locally** requires actual execution; **Pending** means an external action or evidence is still needed. The local results record supplies exact execution outcomes. No account action or screenshot is implied by source configuration alone.

## Exam 1 GitHub DevOps

| Document section | Deliverable | Status and location |
| --- | --- | --- |
| 1 Introduction and architecture | Explain CI, delivery/deployment and architecture flow | Implemented: `docs/devops.md` |
| 1 | Select GitHub Flow; explain short-lived branches and review | Implemented: `docs/devops.md`, `docs/github-setup.md`; real feature PR pending |
| 1 | Define success metrics | Implemented: `docs/devops.md`; real workflow metrics pending |
| 2 Repository setup | Source, dependencies, tests, Dockerfile, workflow, README | Implemented in project root |
| 2 | Actual organized GitHub repository | Pending account setup and initial push |
| 2 | Stable main and focused feature branch | Local Git initialized on main; first commit, feature branch and remote PR pending |
| 2 | PR purpose, linked issue, validation, configuration changes | Implemented PR template; actual issue and PR pending |
| 2 | Protect main with PRs and passing actual checks | Pending GitHub settings after first run |
| 2 | Approval count adapted to team; restrict force pushes/deletion; review bypass | Pending account/team decision and settings verification |
| 2 | CODEOWNERS using real write-access collaborators | File prepared; active rules pending actual GitHub username(s) |
| 2 | Setup, local commands, configuration and startup README | Implemented: `README.md` |
| 3 Pipeline | PR and main-push triggers, clean Python 3.12 install | Implemented: `.github/workflows/ci.yml`; remote execution pending |
| 3 | Ruff, pytest, Docker build | Ruff and 28 tests verified locally; Docker build and remote jobs pending |
| 3 | Least privilege and timeouts | Implemented per-job permissions and timeouts |
| 3 | Publish only after passing trusted main push | Implemented guarded `publish` job; disabled pending publication approval |
| 3 | GHCR token, package-write only for publisher, SHA tag, lowercase name | Implemented; actual registry publication pending |
| 3 | Test reports and useful failure logs | Implemented report upload and container logs; remote reports pending |
| 4 Containers | Multi-stage build and correct FastAPI startup | Implemented Dockerfile; build/run pending Docker access |
| 4 | Runtime uvicorn, non-root user, excluded caches/secrets | Implemented runtime dependency file, Dockerfile, `.dockerignore` |
| 4 | Build and run locally; request health; inspect failure logs | Pending: Docker unavailable on PATH |
| 4 | Registry visibility/settings and safe credentials | Pending settings review before publishing; no credentials in source |
| 4 | Image maintenance and hygiene | Documented in `docs/devops.md`; scanning/digest pinning are recommendations, not claimed executed |
| 5 Agile board | GitHub Projects with Backlog, Ready, In Progress, In Review, Done | Pending GitHub access; setup plan in `docs/github-setup.md` |
| 5 | Status, Priority, Assignee, Iteration, Due Date | Suggested fields recorded; pending board creation |
| 5 | Issues with acceptance criteria, labels and linked PRs | Drafts in `docs/github-setup.md`; actual creation pending |
| 5 | Board automation and updates | Pending real project settings and linked issue activity |
| 5 | Short retrospective | Initial factual entry in `docs/devops.md`; finish after remote work |
| 5 | Genuine board screenshot and successful Actions screenshot | Pending; see `evidence/README.md` |
| 1–5 | Conclusion and references | Implemented: `docs/devops.md` |

Conditional/optional: develop branch and merge queue are explicitly optional; database service containers apply only if using a database (this project does not). Docker Hub is an alternative to GHCR, not an additional registry requirement. Deployment is described as occurring when approved; no deployment target is specified. Latest/release tags, production controls, mutation testing and security scanners are improvements rather than mandatory additions. The CI container health smoke test implements the document's suggested extra validation.

## Exam 2 GitHub Copilot

| Document section | Deliverable | Status and location |
| --- | --- | --- |
| 1 Methodology | Human-led prompts, review, tests, transparency and privacy | Documented: `docs/copilot-evidence.md`; actual Copilot session pending |
| 1 | Discuss limitations, ethics and productivity measures | Documented in Copilot procedure; no invented time-saving claim |
| 2 Prompt engineering | Specific example prompt, assumptions, focused generation and review | Prepared prompts; Copilot-generated output pending |
| 2 API | FastAPI GET /health returns 200 and status ok | Verified locally: `evidence/local/http-smoke.json` |
| 2 | POST /items, required non-empty name, 201 and validation errors | Verified locally: 201/422 live HTTP responses and passing tests |
| 2 | Type hints, concise docstrings, no hard-coded secrets | Implemented |
| 2 | In-memory limitations and OpenAPI review | Documented; schema assertions included in tests |
| 3 Tests | Health, success, empty/missing name, status and body assertions | Verified locally: passing suite in `evidence/local/results.txt` |
| 3 | Maximum length, Unicode, non-string, malformed JSON, repeated requests | Implemented with boundary and no-side-effect assertions |
| 3 | Fixtures reset state | Implemented autouse fixture |
| 3 | Coverage greater than 80% | Verified locally: 28 tests pass; measured coverage 100%; enforced minimum 81% |
| 3 | Review generated tests; rerun after refactor and in CI | Local tests implemented; Copilot review and remote CI pending |
| 4 Refactoring | Preserve legacy baseline, explain/fix/optimize with available interface | Legacy code and prompt procedure recorded; actual Copilot interaction pending |
| 4 | Typed total ignores None using identity check | Implemented: `app/numeric.py` |
| 4 | Empty, all-None, mixed, negative, decimal tests | Implemented: `tests/test_numeric.py`, plus mutation/unsupported-string tests |
| 4 | Verify behavior before/after, avoid unmeasured complexity/speed claims | Verified five before/after cases: `evidence/local/refactor-comparison.json`; no speed improvement claimed |
| 5 Documentation | README Python version, installation, startup, examples, limitations | Implemented: `README.md` |
| 5 | Docstrings and API documentation including schemas/status/configuration | Implemented: `app/`, `docs/api.md` |
| 5 | Review generated OpenAPI and save artifact | Verified schema assertions; saved `docs/openapi.json` |
| 5 CLI | Check installed Copilot product; verify current CLI syntax where supported | Copilot not detected in extension inventory; user sign-in/setup pending |
| 1–5 | Genuine Copilot usage evidence and human review record | Pending actual Copilot use; Codex work is disclosed separately |

Conditional/optional: `/explain`, `/fix`, `/optimize` and CLI features depend on the installed product. Plain-language prompts can serve the same purpose when slash commands are absent. Production authentication, persistent database, rate limits and pagination are outside this teaching example. Profiling is necessary before claiming a performance optimization; no such claim is made here.

## Source identity

Both provided documents name Sudheesh Vinnakota. No identity has been inferred from the computer account, and the supplied documents have not been edited. Confirm the submission name before finalizing any exam cover sheet.
