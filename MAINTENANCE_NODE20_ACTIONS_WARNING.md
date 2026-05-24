# Node.js 20 GitHub Actions Runtime Warning

## Status

```text
NODE20_DEPRECATION_WARNING: OBSERVED
CI_STATUS: PASSED_OBSERVED
PUBLIC_RELEASE: BLOCKED
HUMAN_APPROVAL: NOT_GIVEN
```

## Observed

GitHub Actions emitted a Node.js 20 deprecation warning for:

- actions/checkout@v4
- actions/setup-python@v5

## Current Impact

The warning did not fail the observed CI run.

## Risk

Future GitHub Actions runtime changes may require updating action versions.

## Conservative Handling

Do not update action major versions blindly.
Only update after confirming the official action versions support the newer runtime and the workflow still passes.

## Required Before Public Release

- Re-check official action release notes.
- Update workflow only if needed.
- Run GitHub Actions again.
- Keep deploy steps absent.
- Keep repository private until Human Approval.

## Current Decision

```text
NODE20_WARNING_STATUS: TRACKED_NOT_BLOCKING_PRIVATE_RC
PUBLIC_RELEASE: BLOCKED
```
