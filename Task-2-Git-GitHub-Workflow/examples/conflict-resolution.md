# Conflict resolution example

The isolated walkthrough starts with this line in `conflict-demo.md`:

```text
Resolution: choose one agreed sentence after comparing both branch edits.
```

In separate local branches, replace that same line with two different alternatives. A merge should then require a choice. Git marks conflicting regions with `<<<<<<<`, `=======`, and `>>>>>>>`. Review both alternatives, edit the file to the agreed final text, remove all markers, and verify with `git status`, `git diff`, and `git diff --check` before staging or committing.

This describes a reproducible exercise; it does not claim that a conflict has already been produced or resolved.