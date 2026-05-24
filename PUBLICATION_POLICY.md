# Publication Policy

## Current Status

```text
REPOSITORY_NAME: civic-protection-cell-public
REPOSITORY_FULL_NAME: Cyberperpunk2078/civic-protection-cell-public
REPO_NAME_PUBLIC_REVIEW: RESOLVED
PRIVATE_TARGET_REPO: ACTIVE
PUBLIC_RELEASE: BLOCKED
HUMAN_APPROVAL: NOT_GIVEN
LEGAL_REVIEW: OPEN
LEGAL_RELEASE_BLOCKERS: ACTIVE
PROTECTED_CORE: CONFIRMED_EXCLUDED
CI_STATUS: PASSED_OBSERVED
REAL_DATA: PROHIBITED
SYNTHETIC_DATA_ONLY: REQUIRED
EXTERNAL_EFFECT: BLOCKED
NODE20_DEPRECATION_WARNING: TRACKED
```

## Legal Release Blocker Register

`LEGAL_RELEASE_BLOCKERS.md` is the active blocker register for provider, privacy, consumer, payment, tax, invoice, legal-services, security-contact, data and external-action release blockers.

It is preparatory only. It does not provide legal clearance and does not replace `HUMAN_APPROVAL.md`.

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
- Legal release blocker register present and reviewed
- License posture documented
- Provider information reviewed
- Privacy notice reviewed
- Consumer information reviewed
- Withdrawal and refund wording reviewed
- Tax, invoice and payment terms reviewed
- Rechtsdienstleistungsgesetz boundary reviewed
- Security contact/process reviewed
- Human Approval documented in `HUMAN_APPROVAL.md`

## Blocked Without Human Approval

Codex must not approve public release. Public release remains blocked until a human intentionally creates and reviews `HUMAN_APPROVAL.md`.

## Legal Review Preconditions

Before any public release, a qualified human/legal reviewer must decide whether provider information, privacy notice, consumer information, withdrawal/refund wording, tax/invoice/payment terms and Rechtsdienstleistungsgesetz boundaries are required or need revisions.

Security contact and vulnerability-reporting processes must also be reviewed before public release so reports do not require public disclosure of sensitive details.

Open items must be tracked in `LEGAL_RELEASE_BLOCKERS.md` until resolved by a qualified human/legal reviewer or by an explicit owner decision.

## No Automatic Publication

No script, workflow or agent may change repository visibility, create a release, publish packages or deploy the project.
