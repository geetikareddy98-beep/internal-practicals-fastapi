# Copilot development and evidence procedure

## Current account status

GitHub is signed in and account settings show Copilot Free. Browser prompt attempts returned no assistant output; the browser reports CopilotAuthTokenUnlicensedError (404). Earlier setup redirected to Pro signup; no payment or subscription was made. Resolve the Copilot account/editor access before recording actual suggestions. This remains incomplete.

## Actual provenance

The initial local implementation, tests and documentation were produced with Codex in this chat. This is not evidence of GitHub Copilot use. GitHub Copilot was not detected in the inspected VS Code extension inventory. No Copilot prompt, suggestion acceptance, timing gain or successful CLI invocation is claimed here.

Use genuine Copilot assistance on the feature branch, keep small reviewed changes, and rerun the entire suite. Do not replace this record with a fictional past session.

## Setup

Open this folder in VS Code. Follow the official setup page: https://docs.github.com/en/copilot/how-tos/copilot-in-your-ide/set-up-copilot/install-copilot-extension. Install/enable the supported official GitHub Copilot experience and sign in directly yourself. Confirm account entitlement; never share tokens or passwords here. Record the editor and Copilot version visible in the installed environment. Copilot Chat is distinct from the Microsoft Windows Copilot app.

## Small verifiable tasks

For each task, capture the actual prompt and response, inspect the proposal, record accepted/rejected parts and why, and rerun lint/tests/coverage. Where a slash command is absent, use the equivalent ordinary-language prompt.

1. API review or generation: “Review this FastAPI teaching API. GET /health must return 200 and {status: ok}. POST /items must accept a required string name of 1–100 characters, return 201 with id and name, and return 422 for invalid input. Preserve whitespace and Unicode as the assignment example does. Explain assumptions, propose a focused improvement only if needed, and do not add secrets or unrelated endpoints.” For genuine generation evidence, ask Copilot to independently draft a small module in a scratch file and compare it to the current contract; retain only reviewed changes, with provenance recorded.
2. Tests: “Review tests/test_main.py against this contract. Suggest a meaningful uncovered validation case, explain what bug it would detect, and generate one pytest test. Keep state isolated and check both status and body.” Review and integrate a useful test or record why no change was needed. Capture real output rather than presupposing its content.
3. Refactor exercise: put this original example in a scratch editor, ask Copilot to explain it, then request the typed refactor. Keep screenshots of both versions and the real response.

```python
def total(values):
    result = 0
    for i in range(len(values)):
        if values[i] != None:
            result = result + values[i]
    return result
```

Prompt: “Explain this numeric function and its assumptions. Refactor using Python type hints so it sums int/float values and ignores None using an identity check. Empty/all-None input must return zero. Do not silently convert strings. Provide tests for empty, all-None, mixed, negative and decimal values. Explain correctness and time/space complexity without claiming measured speed or complexity-score improvements.”

4. Documentation: “Review README.md and the generated OpenAPI schema against app/main.py. Confirm request types, 201/422 responses, the 100-character boundary, setup commands and in-memory limitations. Suggest precise corrections.” Check every claim before accepting it.
5. CLI (conditional): inspect the product/version actually installed, check the current official GitHub Copilot CLI documentation, and use its supported help/interface to explain a small test command. Do not assume an old `gh copilot` command is present. Record exact installed syntax and real output, or mark CLI unavailable and explain the product limitation as permitted by the document. Avoid commands that disclose environment variables, delete files or change account permissions.

## Review principles

Generated code remains a draft. Check validation, defaults, exception handling, dependencies and licensing when incorporating external code. Keep secrets and private material out of prompts. A passing coverage number cannot replace meaningful assertions. Record task duration and review iterations only when measured; compare similar tasks before asserting productivity improvement. Profiling and representative benchmarks are needed before asserting optimization gains. No benchmark improvement is claimed for the generator-expression refactor.

## Session record to complete after actual use

| Field | Actual record |
| --- | --- |
| Date, editor version and Copilot version | Pending |
| Task and exact prompt | Pending |
| Suggestion and screenshot filename | Pending |
| Accepted/rejected code and reason | Pending |
| Commit/PR connecting the reviewed change | Pending |
| Actual verification commands and results | Pending |
| Measured duration/review iterations, if tracked | Pending |

Do not mark the Copilot practical complete until real interaction and the required review/verification evidence have been recorded.
