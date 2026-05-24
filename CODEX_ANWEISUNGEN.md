# ###CodexAnweisungen

## Ziel

Dieses Repository ist die public-safe, local-first Civic Protection Cell.

Arbeitsziel:

```text
PUBLIC_SAFE_LAYER_READY
PUBLIC_RELEASE_PREP_OWNER_APPROVED
PUBLIC_VISIBILITY_MANUAL_GITHUB_ACTION_REQUIRED
```

Das System soll helfen bei:

- Dokumentenstruktur
- Fristen-Risiko-Hinweisen
- Evidence Cards
- Human Review Gate
- synthetischen Beispielen
- lokaler Analyse ohne externe Wirkung

## Grundregeln

Codex arbeitet konservativ, testgetrieben und public-safe.

```text
Real Data: prohibited
Synthetic Data: only
Human Review: required
External Effect: blocked
Protected Core: private
Repository Visibility: manual owner action only
```

Codex darf keine Funktion einbauen, die ohne menschliche Freigabe nach außen wirkt.

## Safety-Invariants

Immer erhalten:

- keine echten Fallbeispiele
- keine privaten Identitätsdaten
- keine Zugangsdaten
- keine automatische Außenwirkung
- keine verbindlichen Hochrisiko-Endentscheidungen
- keine produktive Operator-Logik
- keine geschützte kommerzielle Kernlogik im Public Layer
- Human Review bleibt Pflicht
- keine Veröffentlichung persönlicher Steuer- oder Bankdaten

Bei Verstoß:

```text
STATUS: BLOCKED
ACTION: stop, document, propose safer path
```

## Repo-Hinweis

Aktuelles Ziel-Repo:

```text
Cyberpunk2088/civic-protection-cell-public
```

Repo-Namensprüfung:

```text
REPO_NAME_PUBLIC_REVIEW: RESOLVED
REPOSITORY_NAME: civic-protection-cell-public
REPOSITORY_FULL_NAME: Cyberpunk2088/civic-protection-cell-public
PUBLIC_RELEASE_PREP: OWNER_APPROVED
PUBLIC_VISIBILITY: PRIVATE_UNTIL_MANUAL_GITHUB_ACTION
HUMAN_APPROVAL: GIVEN
HUMAN_APPROVAL_FILE: PRESENT_GUARDED
CI_STATUS: PASSED_OBSERVED_AFTER_HUMAN_APPROVAL_TEST_FIX
PROTECTED_CORE: CONFIRMED_EXCLUDED
TAX_NUMBER_PUBLICATION: NO
BANK_DATA_PUBLICATION: NO
```

## Roadmap

### Phase 0 — Baseline prüfen

Erstelle oder aktualisiere:

```text
AUDIT_BASELINE.md
```

Prüfen:

- README vorhanden
- pyproject vorhanden
- src-Paket vorhanden
- Tests vorhanden
- synthetische Beispiele vorhanden
- Security-Dokumente vorhanden
- CI-Workflow vorhanden

### Phase 1 — Core erhalten

Erforderliche Module:

```text
src/civic_protection_cell/__init__.py
src/civic_protection_cell/status.py
src/civic_protection_cell/intake.py
src/civic_protection_cell/classifier.py
src/civic_protection_cell/deadline_checker.py
src/civic_protection_cell/evidence_card.py
src/civic_protection_cell/review_gate.py
src/civic_protection_cell/output.py
src/civic_protection_cell/demo.py
```

Anforderungen:

- lokale Verarbeitung
- synthetische Daten
- Review Gate aktiv
- Output enthält `external_action = BLOCKED`
- Fristenmodul liefert nur Risiko-Hinweis
- Klassifikation bleibt heuristisch

### Phase 2 — Tests erhalten

Erforderliche Tests:

```text
tests/test_review_gate_blocks.py
tests/test_output.py
tests/test_no_external_action.py
tests/test_synthetic_data_only.py
tests/test_no_secrets.py
tests/test_deadline_checker.py
tests/test_classifier.py
tests/test_evidence_card.py
tests/test_demo.py
```

Testbefehl:

```bash
python -m pip install --upgrade pip
pip install -e ".[test]"
python -m pytest -q
```

Erwartung:

```text
all tests passed
```

### Phase 3 — CI erhalten

Erforderlich:

```text
.github/workflows/tests.yml
```

Workflow:

- Python 3.12
- Installation mit `pip install -e ".[test]"`
- Testlauf mit `python -m pytest -q`
- nur minimale Rechte
- kein Deployment

### Phase 4 — Governance-Dateien erhalten

Erforderliche Dateien:

```text
SECURITY.md
DISCLAIMER.md
ABUSE_PREVENTION.md
VALUE_AND_SURVIVAL.md
SPONSORSHIP_AND_SUPPORT.md
NAME_AND_IDENTITY_PROTECTION.md
PUBLICATION_POLICY.md
THREAT_MODEL.md
LICENSE.md
CHANGELOG.md
ROADMAP.md
LEGAL_RELEASE_BLOCKERS.md
PUBLIC_GO_LIVE_PACKET.md
HUMAN_APPROVAL.md
```

Mindestinhalt:

- synthetische Beispiele
- keine echten Fälle
- Human Review Pflicht
- geschützter Kern bleibt privat
- kommerzielle Nutzung nur mit passender Erlaubnis oder Vereinbarung
- klare Grenzen der Nutzung

### Phase 5 — Supportpfade setzen

Dokumentiert in:

```text
SPONSORSHIP_AND_SUPPORT.md
.github/FUNDING.yml
```

Support / Donation:

```text
https://www.paypal.com/qrcodes/managed/dae42978-4f21-41cf-aa93-360c0662bd81?utm_source=consapp_download
```

Pay for Work:

```text
https://www.paypal.com/qrcodes/managed/8a5c5272-9b9d-46ac-95f5-b662af83f0ac?utm_source=consapp_download
```

### Phase 6 — Rechte und Lizenz

Arbeitsstand:

```text
Rights Holder: Cyberpunk Public-Safe Systems
License: Source-available public-safe working draft
Commercial use: requires permission or separate agreement
```

Lizenz muss klarstellen:

- Attribution bleibt erhalten
- keine Gewährleistung
- keine ungeprüfte Hochrisiko-Nutzung
- kommerzielle Nutzung nur mit Erlaubnis oder Vereinbarung
- Public-Safe-Grenzen bleiben bestehen

### Phase 7 — Protected Core prüfen

Nicht öffentlich aufnehmen:

- reale Dokumente
- private Identitätsdaten
- vertrauliche Arbeitsnotizen
- Produktiv-Workflows
- Premium-Templates
- kundenspezifische Logik
- Zugangsdaten
- geschützte kommerzielle Methodik

### Phase 8 — Final Audit

Pflichtpunkte:

- Teststatus
- CI-Status
- Safety-Invariants
- Datenschutzstatus
- Protected-Core-Status
- Human-Review-Status
- Payment-/Support-Status
- License-/Rights-Status
- offene manuelle Schritte
- Release-Entscheidung

Erlaubter Status nach Owner Approval:

```text
AUDIT_STATUS: PASSED_WITH_MANUAL_VISIBILITY_PENDING
PUBLIC_RELEASE_PREP: OWNER_APPROVED
PUBLIC_VISIBILITY: PRIVATE_UNTIL_MANUAL_GITHUB_ACTION
```

### Phase 9 — Release Candidate

Erfüllt, wenn:

- Tests bestanden
- CI bestanden
- Audit erstellt
- Protected Core ausgeschlossen
- Supportpfade gesetzt
- Lizenzdatei vorhanden
- README vollständig
- keine echten Daten
- keine Zugangsdaten
- Human Approval guarded vorhanden

Status:

```text
PUBLIC_SAFE_RELEASE_PREP_READY
PUBLIC_VISIBILITY: MANUAL_GITHUB_OWNER_ACTION_REQUIRED
```

### Phase 10 — Human Approval

`HUMAN_APPROVAL.md` ist vorhanden und guarded.

Codex darf trotzdem keine Repository-Sichtbarkeit ändern.

```text
HUMAN_APPROVAL: GIVEN
HUMAN_APPROVAL_FILE: PRESENT_GUARDED
REPOSITORY_VISIBILITY_CHANGE: MANUAL_GITHUB_ACTION_REQUIRED
```

## Codex-Arbeitsmodus

Bei jeder Änderung:

1. kleinste sichere Änderung
2. Tests aktualisieren
3. Safety-Invariants erhalten
4. keine unnötigen Dependencies
5. keine externe Wirkung einbauen
6. keine echten Daten einfügen
7. README bei Nutzerwirkung aktualisieren
8. CHANGELOG aktualisieren
9. Auditstatus ehrlich halten
10. bei Unsicherheit `NEEDS_HUMAN_REVIEW`

## Stop-Regeln

Stoppen, wenn:

- echte Daten auftauchen
- Zugangsdaten auftauchen
- externe Wirkung entsteht
- Human Review geschwächt wird
- Protected Core öffentlich wird
- Tests fehlschlagen
- Lizenzstatus unklar wird
- persönliche Steuer- oder Bankdaten veröffentlicht werden sollen

Dann dokumentieren:

```text
STATUS: BLOCKED
REASON: <reason>
NEXT_SAFE_PATH: <proposal>
```

## Definition of Done

Fertig erst wenn:

```text
pytest passes
CI passes
README updated
Safety docs present
Protected core excluded
No credentials found
No real data present
External effect blocked
Human review preserved
Changelog updated
Audit updated
Release status honest
```

## Leitsatz

```text
Build useful civic protection.
Keep data synthetic.
Keep external effect blocked.
Keep human review mandatory.
Keep the protected core protected.
Keep personal tax and bank data private.
Visibility changes stay manual.
```