# Threat Model

## Scope

This threat model covers the public-safe working draft of `civic-protection-cell-public`.

## Risks

| Risk | Impact | Mitigation | Status |
| --- | --- | --- | --- |
| Data leak | Real people, cases or private records could be exposed. | Synthetic examples only; no real data policy; tests scan for obvious secret patterns. | MITIGATED_BY_POLICY |
| False security | Users may overtrust prototype output. | Disclaimer, Human Review Gate, no final advice wording. | MITIGATED_BY_POLICY |
| False deadline interpretation | A deadline signal could be mistaken for final calculation. | Deadline checker only flags risk and requires human review. | MITIGATED_BY_CODE |
| Abuse through automation | Tool could be extended into sending or submission. | No external action layer; tests block sending/submission modules. | MITIGATED_BY_CODE |
| Confusion with legal advice | Output could be read as legal advice. | Disclaimer and output language require human review. | MITIGATED_BY_POLICY |
| Protected-core leak | Commercial or private workflows could be exposed. | Protected Core Audit and public/protected layer split. | MITIGATED_BY_AUDIT |
| Identity exposure | Git identity or examples could reveal private identity. | Name and Identity Protection policy. | NEEDS_MANUAL_REVIEW |
| Payment-link confusion | Payment may be mistaken for release or rights approval. | Sponsorship policy states payment does not change safety or license status. | MITIGATED_BY_POLICY |
| Repo accidentally public | Private repo could be made public prematurely. | Publication policy blocks release until Human Approval. | NEEDS_HUMAN_REVIEW |
| Missing Human Review | Users may bypass review. | Review gate defaults to `NEEDS_HUMAN_REVIEW`; external action blocked. | MITIGATED_BY_CODE |
| CI not observed | Tests may pass locally but fail in CI. | CI workflow added; final audit must state observed status honestly. | NOT_OBSERVED |
| False test status | Documentation could claim unobserved tests passed. | Final audit records observed test status only. | MITIGATED_BY_PROCESS |
| License misunderstanding | Users may assume OSI open source or free commercial use. | Conservative source-available working draft license. | MITIGATED_BY_LICENSE |

## Decision

```text
PUBLIC_RELEASE: BLOCKED
HUMAN_REVIEW: REQUIRED
EXTERNAL_EFFECT: BLOCKED
```
