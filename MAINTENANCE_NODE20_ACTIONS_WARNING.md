# Node.js 20 GitHub Actions Runtime Warning

## Status

```text
NODE20_DEPRECATION_WARNING: OBSERVED
CI_STATUS: PASSED_OBSERVED
NODE24_ACTIONS_UPDATE_STATUS: PENDING_CI_OBSERVATION
PUBLIC_RELEASE: BLOCKED
HUMAN_APPROVAL: NOT_GIVEN
```

## Observed

GitHub Actions emitted a Node.js 20 deprecation warning for:

- actions/checkout@v4
- actions/setup-python@v5

## Current Impact

The warning did not fail the observed CI run.

## Official Release Check

The official GitHub releases and tags for `actions/checkout@v6` and `actions/setup-python@v6` were checked before changing workflow versions.

- `actions/checkout` release `v6.0.0` documents Node.js 24 support details.
- `actions/setup-python` release `v6.0.0` documents an upgrade to Node.js 24 and requires runner `v2.327.1` or later.

GitHub-hosted `ubuntu-latest` is the conservative target for this workflow. No deploy steps, secrets, or application logic were added.

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
NODE20_WARNING_STATUS: ACTIONS_V6_UPDATE_PENDING_CI_OBSERVATION
PUBLIC_RELEASE: BLOCKED
```
