# Civic Protection Cell Public

Public-safe, local-first prototype for civic document structure, deadline-risk awareness, evidence cards and human review gating.

## Status

```text
REPOSITORY_VISIBILITY: PRIVATE
PUBLIC_RELEASE: BLOCKED
TEST_STATUS: PASSED_LOCAL_PYTHON3
CI_STATUS: NOT_OBSERVED
EXTERNAL_ACTION: BLOCKED
REAL_DATA: PROHIBITED
SYNTHETIC_DATA: ONLY
HUMAN_REVIEW: REQUIRED
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

## Support

Donation/support and unrestricted payment links are listed in `SPONSORSHIP_AND_SUPPORT.md`.

## Release Note

This repository is private and public release remains blocked until explicit human approval is documented and CI is observed.
