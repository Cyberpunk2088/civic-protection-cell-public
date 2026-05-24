# Publication Policy

## Current Status

```text
REPOSITORY_NAME: civic-protection-cell-public
REPOSITORY_FULL_NAME: Cyberperpunk2078/civic-protection-cell-public
REPO_NAME_PUBLIC_REVIEW: RESOLVED
PRIVATE_TARGET_REPO: ACTIVE
PUBLIC_RELEASE: BLOCKED
HUMAN_APPROVAL: NOT_GIVEN
PROTECTED_CORE: CONFIRMED_EXCLUDED
CI_STATUS: PASSED_OBSERVED
REAL_DATA: PROHIBITED
SYNTHETIC_DATA_ONLY: REQUIRED
EXTERNAL_EFFECT: BLOCKED
NODE20_DEPRECATION_WARNING: TRACKED
```

## Release Requirements

Public release requires all of the following:

- tests passed
- CI passed or explicitly reviewed
- final audit completed
- no real personal data
- no credentials
- no protected core material
- no external action logic
- Security policy present
- Disclaimer present
- Threat model present
- Publication policy present
- License posture documented
- Human Approval documented in `HUMAN_APPROVAL.md`

## Blocked Without Human Approval

Codex must not approve public release. Public release remains blocked until a human intentionally creates and reviews `HUMAN_APPROVAL.md`.

## No Automatic Publication

No script, workflow or agent may change repository visibility, create a release, publish packages or deploy the project.
