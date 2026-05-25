# Contributing

Thank you for considering a contribution.

This repository is public-safe by design. Contributions are welcome only when they preserve the safety boundary.

## Allowed Contributions

Contributions may improve:

- documentation clarity
- synthetic examples
- tests
- local-only workflow output
- evidence-card structure
- deadline-risk awareness labels
- human-review gate clarity
- safety documentation

## Not Allowed

Do not contribute:

- real personal data
- real case files
- legal advice
- final deadline calculations
- automatic submission or filing logic
- authority, court or third-party contact automation
- network, crawler or browser automation logic
- credential handling
- payment processor integration
- protected-core material
- tax numbers, bank data or private identifiers

## Required Posture

Every change must preserve:

```text
REAL_DATA: PROHIBITED
SYNTHETIC_DATA: ONLY
EXTERNAL_ACTION: BLOCKED
HUMAN_REVIEW: REQUIRED
LEGAL_ADVICE: NOT_PROVIDED
PROTECTED_CORE: EXCLUDED
```

## Pull Request Checklist

Before opening a pull request, check:

- [ ] The change is small and reviewable.
- [ ] No real data is included.
- [ ] No secrets or credentials are included.
- [ ] No external-action logic is added.
- [ ] No legal advice is added.
- [ ] Tests pass locally where applicable.
- [ ] Documentation is updated if user-facing behavior changes.

## Human Review

Any real-world use, commercial deployment, legal workflow, deadline-dependent use or external communication requires qualified human review outside this repository.
