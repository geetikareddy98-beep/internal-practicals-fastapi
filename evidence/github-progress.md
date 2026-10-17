# GitHub execution record

Updated 17 October 2026 after signing in through the browser. This record supersedes the earlier pending GitHub statuses in the initial setup guides.

## Verified external work

- Private repository: https://github.com/geetikareddy98-beep/internal-practicals-fastapi
- Source, tests, dependency manifests, Dockerfile, CI workflow, CODEOWNERS, PR template, documentation and local logs uploaded through the authenticated GitHub web interface.
- Successful main workflow: https://github.com/geetikareddy98-beep/internal-practicals-fastapi/actions/runs/39026777026
- Verified run commit: c3f856a94ebe2198521099416ee2f524c2b3b712.
- Run summary reports success for lint, tests and container-build; publish-ghcr is skipped because publication is disabled. Test-reports artifact is present.
- GitHub annotations report deprecation of Node 20 in the example action versions and an upcoming ubuntu-latest runner migration. These are warnings/notices, not failed checks.
- Private Projects board: https://github.com/users/geetikareddy98-beep/projects/1
- Board statuses: Backlog, Ready, In Progress, In Review, Done, in that order.
- Seven real repository issues with acceptance criteria and the signed-in account as assignee are linked to the board: API (#1), tests/refactor (#2), CI (#3), local Docker (#4), GHCR (#5), Copilot (#6), documentation/evidence (#7).
- Priority field created with High, Medium, Low options. Default repository verified and project visibility verified private.
- Item-closed automation is enabled and sets Status to Done. API issue #1 and tests issue #2 were closed only after their acceptance criteria were verified. Remaining tasks stay open.
- A classic protection rule for main was saved with PRs, up-to-date branches, required lint/tests/container-build checks, no administrator bypass, and force pushes/deletion disallowed. Required independent approvals are disabled under the exam's solo adaptation.

## Limitations that still matter

GitHub explicitly says these protection rules will NOT be enforced for this private repository on the current account plan. Required CODEOWNERS review is also plan-gated. The file has valid owner rules, but enforcement is not claimed. Resolve the plan/instructor requirement without changing visibility unless the user separately approves it.

The Copilot web interface initially reported license setup in progress. A real refactoring prompt was attempted, but no assistant response appeared; after reload, the interface redirected to Copilot Pro signup. No subscription was started and no billing information was entered. This attempt is not accepted as completed Copilot-assisted development. Enable an eligible Copilot experience before recording real suggestions.

Docker is not available locally. The successful hosted container-build job does not replace the requested local Docker build/run evidence. GHCR publication remains disabled and needs explicit approval.

## Local Git and remote history

The local project was committed as 854c117 using the already configured identity matching the signed-in GitHub account. Terminal push failed because the credential helper could not run in the restricted environment. The remote therefore has genuine browser-created commits with a different history. Do not force push the independent local history over the remote. When terminal Git authentication is available, clone the private repository into a fresh folder to continue from its actual history.

## Evidence files

- `screenshots/01-private-repository.jpg`: repository created as private (initial empty state).
- `screenshots/03-branch-protection-plan-limit.jpg`: saved rule and GitHub plan limitation.
- `screenshots/04-actions-success.jpg`: actual successful Actions run.
- `screenshots/11-api-docs.jpg`: actual local API documentation.

Feature PR, board screenshot and any later work are recorded in subsequent updates. No successful publication, independent review or Copilot output is fabricated.
