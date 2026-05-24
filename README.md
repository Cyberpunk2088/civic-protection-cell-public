# Civic Protection Cell Public

Synthetic-data-only, local-first working draft for civic document structure, deadline-risk awareness, evidence cards and human review gating.

This repository is not a legal service, not legal advice, not an official authority or court system, and not suitable for real cases without separate qualified human review.

## Status

```text
REPOSITORY_NAME: civic-protection-cell-public
REPOSITORY_FULL_NAME: Cyberperpunk2078/civic-protection-cell-public
REPOSITORY_VISIBILITY: PRIVATE
PUBLIC_RELEASE: BLOCKED
HUMAN_APPROVAL: NOT_GIVEN
LEGAL_REVIEW: OPEN
TEST_STATUS: PASSED_LOCAL_PYTHON3
CI_STATUS: PASSED_OBSERVED
EXTERNAL_ACTION: BLOCKED
REAL_DATA: PROHIBITED
SYNTHETIC_DATA: ONLY
HUMAN_REVIEW: REQUIRED
PROTECTED_CORE: CONFIRMED_EXCLUDED
COMMERCIAL_CORE: PROTECTED
```

## Purpose

This repository helps structure civic or administrative documents without creating final legal conclusions or external actions.

It can:

- intake synthetic text
- classify broad document signals
- mark possible deadline risk
- create evidence cards
- enforce review gate status
- produce local structured output

It must not:

- process real case material
- process real public case files in examples
- send messages
- submit documents
- contact authorities
- calculate final legal deadlines
- produce final legal, medical, financial or administrative decisions

## Safe local commands

```bash
python -m pip install --upgrade pip
pip install -e ".[test]"
python -m pytest -q
python -m civic_protection_cell.demo
```

## Public-Safe Boundary

Public-safe means documentation, synthetic examples, non-production review-gate logic and tests.

Protected core remains private: production workflows, premium templates, real case data, operator notes, client-specific logic and commercial implementation methodology.

This public repository does not authorize any external action. Any future external-action implementation would require separate private/legal review and remains outside this public layer.

## Support

Donation/support and unrestricted payment links are listed in `SPONSORSHIP_AND_SUPPORT.md`.

Payments, donations, sponsorships, or support do not create legal-advice duties, emergency support, response-time guarantees, release approval, production readiness, or access to the Protected Core.

## Release Note

This repository is private and public release remains blocked until explicit human approval is documented.
