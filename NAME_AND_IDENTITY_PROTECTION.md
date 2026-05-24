# Name and Identity Protection

## Public Identity Rules

Do not publish:

- private full names
- private email addresses
- home addresses
- phone numbers
- case numbers
- account numbers
- real screenshots with private data
- real letters, files or records

Use synthetic examples and public handles intentionally.

## Pseudonymization

Public examples must be synthetic. If a future private workflow uses real material, it must stay outside this public-safe layer and be reviewed separately.

## GitHub Profile and Git Config

Before a public push or release, manually check local identity settings:

```bash
git config user.name
git config user.email
```

Recommended public-safe pattern:

```bash
git config user.name "Cyberpunk"
git config user.email "<github-noreply-email>"
```

## Release Gate

Identity exposure risk must be reviewed before any repository visibility change or public release.
