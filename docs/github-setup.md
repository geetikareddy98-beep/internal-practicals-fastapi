# GitHub setup and continuation

The approved private repository now exists at https://github.com/geetikareddy98-beep/internal-practicals-fastapi. PR #8 was merged with approval, CI/CD succeeded and a private GHCR image was published. The board is https://github.com/users/geetikareddy98-beep/projects/1. See ../evidence/github-progress.md for exact results and remaining limitations.

For future terminal work, authenticate using the normal Git browser/credential-manager flow and clone into a fresh folder. Do not push the separate local initial history over the browser-created remote history. Never force push.

```powershell
git clone https://github.com/geetikareddy98-beep/internal-practicals-fastapi.git
Set-Location internal-practicals-fastapi
git switch -c feature/copilot-review
# Perform and review actual Copilot work, then run README verification commands.
git add .
git commit -m "Record reviewed Copilot assistance"
git push -u origin feature/copilot-review
```

Only make that commit after the stated Copilot activity actually occurs. Open a PR into main, link its real issue and wait for checks. The publisher is enabled with user approval; main pushes publish private SHA-tagged images.

## Original setup walkthrough

The following is the initial walkthrough for reference. Those repository/board/CI/publication steps are already completed; do not repeat the initialization or remote-add commands in the existing repository. Plan-supported enforcement, local Docker and Copilot remain unfinished.

## 1 Create the repository

Use the GitHub integration when connected, or sign in directly at https://github.com/new. Never send credentials to chat. Choose the approved name and visibility; leave README, license and gitignore initialization unchecked because the files already exist locally. Private is a reasonable starting choice, subject to course and account feature requirements. Branch protection availability depends on account plan and repository visibility; verify the current GitHub UI rather than silently making the repository public.

## 2 Push the files

Open PowerShell in the project folder. Check `git status` and `git remote -v` first. The delivered folder has an isolated repository initialized on main, with no commits or remote yet. Commit using your own confirmed author identity. Replace OWNER and REPOSITORY with actual values; the URL below is intentionally a template.

```powershell
git status
git config user.name 'Your actual commit name'
git config user.email 'Your GitHub verified or noreply commit email'
git add .
git commit -m "Add shared FastAPI practical project"
git remote add origin https://github.com/OWNER/REPOSITORY.git
git push -u origin main
git switch -c feature/copilot-review
```

Run these only after approving the remote upload. Use Git Credential Manager/browser sign-in when Git prompts; never embed a token in the URL. If an `origin` already exists, inspect it before changing it. If identity is already correct, omit the two `git config` lines. Do not force push.

## 3 Add real review ownership and perform a feature change

Edit `.github/CODEOWNERS` with real GitHub accounts that have write access. Replace the entire comment-only file with the following pattern, substituting the real username(s):

```text
* @ACTUAL_MAINTAINER
/.github/workflows/ @ACTUAL_CI_MAINTAINER
```

Run the real Copilot review procedure in `docs/copilot-evidence.md` on this feature branch. Record prompts, suggestions, accepted changes and test results honestly. Then:

```powershell
git add .
git commit -m "Record Copilot review and configure code ownership"
git push -u origin feature/copilot-review
```

Create a pull request into `main`. Fill the provided PR template with actual results and link the matching real issue using `Closes #number`. Request a collaborator review where available. Never claim self-review is an independent approval.

## 4 Inspect Actions and protect main

Wait for real Actions jobs to finish; fix failures before merging. Open repository Settings, Branches or Rulesets (depending on the UI), and create a rule targeting `main`. Require PRs and the actual reported checks `lint`, `tests`, `container-build`. Choose check names after their first run. Require one approval if a separate collaborator is available; use the assignment's allowed solo adaptation otherwise. Enable dismissing stale approvals when applicable. Restrict force pushes and deletion. Review and document bypass rights and whether administrators are covered. Save a genuine screenshot of the effective settings. If the plan does not support enforcement, record the limitation accurately and ask the instructor about an acceptable alternative.

## 5 Build/run and publish only after approval

Docker is not available on PATH in the inspected environment. Install Docker Desktop from the official vendor if authorized, complete its engine/virtualization setup yourself where system prompts require it, and verify `docker version` shows both client and server. Then run the README's build and run commands and request `/health`. Capture the real output. A CI build does not substitute for the document's local build/run evidence.

Before publication, review package visibility, workflow token permissions and intended image name. With explicit approval to publish, create repository Actions variable `ENABLE_GHCR_PUBLISH` with value `true`. A subsequent approved push/PR merge to `main` runs publication after all checks pass. The image will be `ghcr.io/owner/repository:FULL_COMMIT_SHA`, in lowercase. Check the real package page, digest and successful publish log; record links. No separate personal token is needed by the workflow. Keep package visibility as approved. A skipped publish job is not publication evidence.

## 6 Projects board

Create a GitHub Projects board named `Internal practicals`, link the repository and add statuses Backlog, Ready, In Progress, In Review, Done. Suggested fields: Priority, Assignee, Iteration, Due Date; select real dates and assignees rather than inventing them. Add labels `bug`, `documentation`, `CI/CD`, `security`. Create these issues, each with the listed acceptance criteria, and add them to the board:

| Issue | Acceptance criteria |
| --- | --- |
| Implement Items API | Health 200; valid item 201; invalid names 422; limitations documented |
| Add unit tests and refactor total | Boundary and validation tests pass; total ignores None; coverage above 80% |
| Create CI workflow | Actual PR and main runs pass lint, tests and container-build |
| Build Docker image | Local multi-stage build succeeds; container health returns status ok; non-root runtime |
| Publish image to GHCR | Approved main run publishes SHA tag; package digest and log recorded |
| Record Copilot development | Real prompts/suggestions/review captured; tests rerun after accepted changes |
| Complete documentation and evidence | README, OpenAPI, checklists and genuine screenshots available |

Enable supported built-in workflows to mark closed issues Done; use actual linked PRs with closing keywords. Review the available project workflows before promising automatic intermediate transitions: set In Progress/In Review manually if the UI does not support the desired rule. Move cards according to actual state. Record what is automated and what is manual. Do not mark unfinished GitHub/Docker/Copilot work Done.

Capture the board with all five statuses and example issues visible, plus one issue showing acceptance criteria and a linked PR. Update the retrospective and requirement checklist after completing the external actions.

## Official references

- https://docs.github.com/en/actions/tutorials/publish-packages/publish-docker-images
- https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository
- https://docs.github.com/en/issues/planning-and-tracking-with-projects
- https://docs.docker.com/desktop/setup/install/windows-install/
