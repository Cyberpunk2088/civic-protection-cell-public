# Legal Release Blockers

This file records the hard blockers that must remain open until a separate qualified human review or owner decision documents them.

It is not legal clearance. It does not authorize publication, payment processing, public offers, real-case handling, external action or production use.

## Current Status

```text
LEGAL_RELEASE_BLOCKERS: ACTIVE
PUBLIC_RELEASE: BLOCKED
HUMAN_APPROVAL: NOT_GIVEN
HUMAN_APPROVAL.md: ABSENT
REPOSITORY_VISIBILITY: PRIVATE
LEGAL_CLEARANCE: NOT_GIVEN
PAYMENT_LINKS: REFERENCED_FOR_REVIEW
REAL_DATA: PROHIBITED
EXTERNAL_ACTION: BLOCKED
PROTECTED_CORE: CONFIRMED_EXCLUDED
```

## Hard Blockers Before Public Release

Public release must remain blocked until the following items are reviewed and explicitly resolved:

- Provider identification / imprint: actual provider identity, contact route, responsible party and required provider information must be reviewed before any public release or linked public offer.
- Privacy notice: any public operation, contact flow, support flow or payment-related flow must have reviewed controller identity, purposes, legal bases, recipients, storage periods, data subject rights, complaint route and processor / third-country posture.
- Legal-services boundary: the public layer must not handle concrete foreign legal matters requiring individual legal assessment. It must not offer final legal advice, final deadline calculation, pleading generation, claim filing, authority contact, court contact or real-case decision-making.
- Consumer and distance-selling information: any B2C paid templates, setup, consulting or support sold remotely must have reviewed price, tax, scope, payment, refund, cancellation / withdrawal and confirmation wording.
- Tax and invoice process: any paid-work flow must have reviewed invoice, VAT / tax and bookkeeping handling.
- Payment-link posture: PayPal, support or unrestricted payment links remain references for review only. They do not create a completed public offer, legal-service duty, emergency support, commercial license, production readiness or release approval.
- Security contact: before public release, a reviewed private vulnerability and sensitive-reporting channel must exist.
- Data posture: the public layer remains synthetic-data-only. No real personal data, real case files, credentials, secrets, private letters, government documents, medical documents or protected-core material may be used.
- External action: no sending, filing, submission, authority contact, court contact, productive write action, deployment or publication automation is authorized.

## Permitted Current State

The following remains permitted while the blockers are open:

- private repository work
- documentation-only hardening
- synthetic examples
- local tests
- non-production review-gate logic
- payment-channel references for review
- legal-review preparation without legal clearance

## Non-Closure Decision

The following gates remain open by design:

- Issue #1: Legal Review Gate
- Issue #2: Human Approval Gate
- Issue #3: Freeze Control

```text
PUBLIC_RELEASE: BLOCKED_UNTIL_SEPARATE_HUMAN_APPROVAL
LEGAL_REVIEW: OPEN
NO_HUMAN_APPROVAL_FILE
NO_PUBLIC_VISIBILITY_CHANGE
NO_PAYMENT_PROCESSOR_INTEGRATION
NO_REAL_CASE_PROCESSING
NO_EXTERNAL_ACTION
```

## Release Rule

Resolving any item in this file does not itself approve release.

Public release requires a separate Human Approval process and an intentionally reviewed `HUMAN_APPROVAL.md` file. Until then, this repository remains private and blocked for public release.
