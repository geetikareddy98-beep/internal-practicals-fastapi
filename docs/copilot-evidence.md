# Actual Copilot assistance and review

On 17 October 2026, signed-in GitHub Copilot Free web chat returned real suggestions. Earlier authentication failures are historical and have been resolved for web chat. The interface selected Auto and identified gpt-5-mini in its retry control. This is browser Copilot evidence, not VS Code or Copilot CLI evidence.

Session: https://github.com/copilot/c/e6e25885-8b7b-44a1-8d2e-cef62261f0a2 (account access may be required). Exact prompts and visible responses are preserved in `evidence/copilot/session-visible.txt`; generated source and actual browser screenshots are retained alongside it.

## Provenance and reviewed decisions

The initial application, tests and documentation were produced with Codex. They are not retroactively attributed to Copilot. Copilot then independently generated an API module, pytest suite, numeric refactor and README/API reference for comparison and review.

1. Refactor prompt described the legacy index loop and requested typed summation ignoring None, zero for empty/all-None, and empty/mixed/negative/decimal tests. Copilot generated `sum(v for v in values if v is not None)`. The existing project already used that correct algorithm; its narrower list type hint was retained. Accepted the useful `pytest.approx(0.3)` case for `[0.1, 0.2, None]` in `tests/test_numeric.py`. Rejected optional always-float conversion and unnecessary runtime coercion. Five baseline comparisons remain in `evidence/local/refactor-comparison.json`. No measured speed gain is claimed.
2. API/test prompt supplied exact health/items contract, whitespace behavior and validation cases. Copilot generated `main.py` and `test_main.py`, saved in `evidence/copilot/`. Accepted its top-level JSON-array rejection case, adapted to existing fixtures, adding assertions for validation location and unchanged state. Retained the existing typed application rather than introduce the generated deprecated startup-event handler and untyped route returns. Its claim that plain Pydantic str would coerce numbers is incorrect for this installed Pydantic 2 configuration; existing numeric-input tests verify 422. Extra endpoints/database suggestions were outside scope and rejected.
3. Documentation prompt supplied actual module path, Python version, API responses, in-memory limitation and coverage command. Copilot produced a README/API reference and explained `--cov=app` and `--cov-report=term-missing`. Accepted the explanation that executed lines do not prove correct assertions or concurrency behavior, added to README. Corrected its generic dependency advice: this project uses pinned supported httpx test dependencies, not requests as a substitute; the actual utility is `app/numeric.py`, not suggested utils.py. Extra fields are ignored under the real model default, so its single-property phrasing is not treated as rejection of all additional fields. Windows examples remain PowerShell-compatible.

## Evidence and validation

- `07-copilot-api.jpg`, `08-copilot-tests.jpg`, `09-copilot-refactor.jpg`, `12-copilot-documentation.jpg`: genuine browser captures.
- `evidence/copilot/`: raw visible conversation and independently generated drafts. Drafts use .txt to avoid confusing them with accepted production code.
- `evidence/local/results-after-copilot.txt`: actual Ruff check/format and full suite after accepted changes. 30 tests pass with 100% application line/branch coverage, enforcing minimum 81%.
- Initial hosted evidence shows 28 tests; this remains accurate historical evidence. New remote CI must verify the added cases.

No Copilot extension or CLI was installed/detected in the inspected environment. Product-specific slash commands/CLI integration are conditional in the exam. Ordinary-language web prompts exercised generation, explanation, refactoring and documentation. The test command was explained by actual Copilot, but no Copilot CLI invocation is claimed. If the instructor requires IDE/CLI specifically, complete an additional real session in that supported product.

Review was human-led in scope and performed with Codex assistance: check contract, dependencies, security, test assertions and limitations before accepting changes. No secrets or original private exam documents were sent to Copilot; prompts contained the small teaching contract only. No time savings, benchmark improvements or independent human approval are invented. Source documents retain their original submission name; confirm identity before adding a cover sheet.
