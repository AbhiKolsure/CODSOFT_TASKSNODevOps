# Practical Git workflow guide

Run repository-level commands from `C:\Users\kolsu\task-1-dockerized-web-app`. This guide does not perform Git operations for you. Preserve existing changes; never use `git reset --hard`, `git clean`, or force-push as a shortcut.

## Feature branch

After confirming a clean worktree and current base branch:

```powershell
git status --short --branch
git switch main
git pull --ff-only origin main
git switch -c task-2/example-feature-note
Add-Content -LiteralPath 'Task-2-Git-GitHub-Workflow/examples/feature-note.md' -Value "`nFeature-branch exercise: reviewed change."
git diff -- Task-2-Git-GitHub-Workflow/examples/feature-note.md
git diff --check
git status --short
```

Review scope and content before staging. If authorized, stage only intended files and inspect the staged diff before making a descriptive commit. Push and open a PR only when ready and permitted. The actual review and merge are manual GitHub actions.

## Isolated conflict exercise in a temporary clone

This exercise uses local disposable clones and branches; it does not push. It requires network access. Run from PowerShell:

```powershell
$source = 'C:\Users\kolsu\task-1-dockerized-web-app'
$temp = Join-Path $env:TEMP ('codsoft-task2-conflict-' + [guid]::NewGuid().ToString('N'))
$seed = Join-Path $temp 'seed'
$left = Join-Path $temp 'left'
$right = Join-Path $temp 'right'
$relative = 'Task-2-Git-GitHub-Workflow/examples/conflict-demo.md'
$example = Join-Path $source $relative
New-Item -ItemType Directory -Path $temp | Out-Null
git clone --no-hardlinks $source $seed
$seedTarget = Join-Path $seed $relative
New-Item -ItemType Directory -Path (Split-Path -Parent $seedTarget) -Force | Out-Null
Copy-Item -LiteralPath $example -Destination $seedTarget
git -C $seed switch -c conflict-base
git -C $seed add -- $relative
git -C $seed -c user.name='Task 2 Demo' -c user.email='task2-demo@example.invalid' commit -m 'docs(task-2): add baseline conflict example'
git clone --no-hardlinks --branch conflict-base $seed $left
git clone --no-hardlinks --branch conflict-base $seed $right
git -C $left switch -c conflict-left
git -C $right switch -c conflict-right
```

Cloning copies committed history only; it does not copy uncommitted Task 2 files. The commands therefore copy only the conflict example into a temporary seed clone and make a local baseline commit there. The left and right clones start at that baseline, so their different edits to the existing sentence produce a content conflict (not an add/add conflict). All setup commits and branches remain in the temporary directory and do not alter the real repository or its history. Replace the same sentence in the example with different alternatives:

```powershell
@('# Conflict demo', '', 'Resolution: keep the left-hand example for this walkthrough.') | Set-Content -LiteralPath (Join-Path $left $relative)
@('# Conflict demo', '', 'Resolution: keep the right-hand example for this walkthrough.') | Set-Content -LiteralPath (Join-Path $right $relative)
git -C $left add -- $relative
git -C $left -c user.name='Task 2 Demo' -c user.email='task2-demo@example.invalid' commit -m 'docs(task-2): change conflict example from left branch'
git -C $right add -- $relative
git -C $right -c user.name='Task 2 Demo' -c user.email='task2-demo@example.invalid' commit -m 'docs(task-2): change conflict example from right branch'
```

The clones have separate branch namespaces. Fetch the left clone's local branch into the right clone, then merge it to trigger a content conflict:

```powershell
git -C $right fetch $left conflict-left:conflict-left
git -C $right merge conflict-left
git -C $right status
git -C $right diff -- $relative
Get-Content -LiteralPath (Join-Path $right $relative)
```

Git should report conflicting edits. Inspect markers `<<<<<<<`, `=======`, and `>>>>>>>`, then resolve the example to the agreed content and verify before completing the local merge:

```powershell
@('# Conflict demo', '', 'Resolution: keep the agreed final example after reviewing both alternatives.') | Set-Content -LiteralPath (Join-Path $right $relative)
git -C $right diff --check
git -C $right diff -- $relative
git -C $right status --short
git -C $right add -- $relative
git -C $right diff --cached --check
git -C $right -c user.name='Task 2 Demo' -c user.email='task2-demo@example.invalid' commit -m 'docs(task-2): resolve isolated example conflict'
git -C $right log --oneline --graph --decorate --all
```

Record success only after observing the actual results. If behavior differs, stop and inspect. The temporary directory is left for your review; remove it manually only after confirming it contains no needed work.

## Pull request and review lifecycle

1. Push a reviewed feature branch only when authorized.
2. Open a GitHub PR with `main` as base and the feature branch as compare.
3. Complete the Task 2 PR template, request a reviewer, and provide reproducible test evidence.
4. Reviewer uses `code-review-checklist.md`, leaves actionable feedback, and records an approval or requested changes on GitHub.
5. Author responds; reviewer checks the latest diff and status checks.
6. Merge under repository policy and verify the PR state and resulting history.

Opening, reviewing, approving, and merging are manual actions and are not performed by this guide.