# Pull request code-review checklist

Review the latest PR revision. Mark items not applicable when appropriate and explain significant exceptions.

## Correctness

- [ ] The change meets its stated purpose and handles relevant edge cases.
- [ ] Behavior and examples match the documentation.
- [ ] Error handling and interfaces are appropriate.

## Scope and safety

- [ ] The diff is focused; unrelated Task 1 files and user changes are untouched.
- [ ] No generated caches, build outputs, credentials, tokens, `.env` files, or private data are included.
- [ ] No destructive commands or unsafe defaults were introduced.

## Security and privacy

- [ ] Inputs, secrets, permissions, and sensitive output are handled appropriately.
- [ ] Logs, screenshots, and documentation do not expose credentials or private information.

## Maintainability

- [ ] Names, structure, and documentation are clear and consistent.
- [ ] Changes are small enough to understand and maintain.
- [ ] New dependencies or workflow permissions are justified and reviewed.

## Tests and verification

- [ ] Relevant automated tests pass, or limitations are clearly stated.
- [ ] Manual verification steps and expected results are reproducible.
- [ ] `git diff --check` passes; no unresolved conflict markers remain.
- [ ] Required CI/status checks pass where configured.

## Review outcome

- [ ] Feedback is specific, respectful, and actionable.
- [ ] The latest revision—not only an earlier diff—was reviewed.
- [ ] Approval is recorded only if the reviewer actually approves on GitHub.