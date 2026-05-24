# Audit Baseline

Date: 2026-05-24
Repository: `Cyberpunk2088/civic-protection-cell-public`
Project name: `civic-protection-cell-public`
Phase: `0`

## Status

```text
BASELINE_STATUS: CHECKED
REPOSITORY_NAME: civic-protection-cell-public
REPOSITORY_FULL_NAME: Cyberpunk2088/civic-protection-cell-public
PRIVATE_TARGET_REPO: ACTIVE
PUBLIC_RELEASE_PREP: OWNER_APPROVED
PUBLIC_VISIBILITY: PRIVATE_UNTIL_MANUAL_GITHUB_ACTION
HUMAN_APPROVAL: GIVEN
HUMAN_APPROVAL_FILE: PRESENT_GUARDED
CI_STATUS: PASSED_OBSERVED_AFTER_HUMAN_APPROVAL_TEST_FIX
REAL_DATA: PROHIBITED
SYNTHETIC_DATA_ONLY: REQUIRED
EXTERNAL_EFFECT: BLOCKED
HUMAN_REVIEW: REQUIRED
PROTECTED_CORE: CONFIRMED_EXCLUDED
TAX_NUMBER_PUBLICATION: NO
BANK_DATA_PUBLICATION: NO
PAYMENT_ROUTE: PAYPAL_ONLY
NEXT_PHASE: MANUAL_OWNER_VISIBILITY_DECISION
```

## Baseline Inventory

| Path | Status | Note |
| --- | --- | --- |
| `README.md` | PRESENT | Public-safe status documented. |
| `CODEX_ANWEISUNGEN.md` | PRESENT | Codex operating rules documented. |
| `pyproject.toml` | PRESENT | Local package and pytest config present. |
| `src/civic_protection_cell/` | PRESENT | Core package present. |
| `src/civic_protection_cell/__init__.py` | PRESENT | Version only. |
| `src/civic_protection_cell/status.py` | PRESENT | Review statuses present. |
| `src/civic_protection_cell/intake.py` | PRESENT | Synthetic-only intake present. |
| `src/civic_protection_cell/classifier.py` | PRESENT | Heuristic classifier present. |
| `src/civic_protection_cell/deadline_checker.py` | PRESENT | Deadline-risk detector present. |
| `src/civic_protection_cell/evidence_card.py` | PRESENT | Evidence card model present. |
| `src/civic_protection_cell/review_gate.py` | PRESENT | External action blocked. |
| `src/civic_protection_cell/output.py` | PRESENT | Structured local output present. |
| `src/civic_protection_cell/demo.py` | PRESENT | Synthetic local demo present. |
| `tests/` | PRESENT | Tests present. |
| `examples/synthetic_only/` | PRESENT | Synthetic example present. |
| `SECURITY.md` | PRESENT | Public-safe reporting rules documented. |
| `DISCLAIMER.md` | PRESENT | No-final-advice boundary documented. |
| `ABUSE_PREVENTION.md` | PRESENT | External-effect block documented. |
| `VALUE_AND_SURVIVAL.md` | PRESENT | Public/protected layer split documented. |
| `SPONSORSHIP_AND_SUPPORT.md` | PRESENT | Support and pay-for-work boundaries documented. |
| `NAME_AND_IDENTITY_PROTECTION.md` | PRESENT | Identity protection guidance documented. |
| `PUBLICATION_POLICY.md` | PRESENT | Publication gates documented. |
| `THREAT_MODEL.md` | PRESENT | Threat model documented. |
| `LICENSE.md` | PRESENT | Conservative source-available working draft present. |
| `CHANGELOG.md` | PRESENT | Changelog present. |
| `ROADMAP.md` | PRESENT | Roadmap present. |
| `.github/FUNDING.yml` | PRESENT | Funding links present. |
| `.github/workflows/tests.yml` | PRESENT | Local test workflow present. |
| `PROTECTED_CORE_AUDIT.md` | PRESENT | Protected-core exclusion documented. |
| `FINAL_AUDIT_REPORT.md` | PRESENT | Final audit report present. |
| `HUMAN_APPROVAL.md` | PRESENT_GUARDED | Owner approval exists with safety guards. |

## Baseline Decision

```text
PUBLIC_RELEASE_PREP: OWNER_APPROVED
PUBLIC_VISIBILITY_CHANGE: MANUAL_GITHUB_OWNER_ACTION_REQUIRED
HUMAN_APPROVAL_REQUIRED: SATISFIED_FOR_PUBLIC_SAFE_LAYER
LEGAL_TAX_PROVIDER_REVIEW: RECOMMENDED_BEFORE_PUBLIC_PROMOTION_OR_COMMERCIAL_USE
```

No automated repository visibility change is approved by this baseline.
