# ###CodexAnweisungen

## Ziel

Dieses Repository wird zu einer public-safe, local-first Civic Protection Cell weiterentwickelt.

Arbeitsziel:

```text
PUBLIC_SAFE_RELEASE_CANDIDATE_READY
PUBLIC_RELEASE_BLOCKED_UNTIL_HUMAN_APPROVAL
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
Public Release: blocked until approval
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

Bei Verstoß:

```text
STATUS: BLOCKED
ACTION: stop, document, propose safer path
```

## Repo-Hinweis

Aktuelles Ziel-Repo:

```text
Cyberperpunk2078/civic-protection-cell-public
```

Repo-Namensprüfung:

```text
REPO_NAME_PUBLIC_REVIEW: RESOLVED
REPOSITORY_NAME: civic-protection-cell-public
REPOSITORY_FULL_NAME: Cyberperpunk2078/civic-protection-cell-public
PUBLIC_RELEASE: BLOCKED
HUMAN_APPROVAL: NOT_GIVEN
CI_STATUS: PASSED_OBSERVED
PROTECTED_CORE: CONFIRMED_EXCLUDED
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

### Phase 1 — Core vervollständigen

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

### Phase 2 — Tests vervollständigen

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

### Phase 3 — CI einrichten

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

### Phase 4 — Governance-Dateien ergänzen

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
```

Mindestinhalt:

- synthetische Beispiele
- keine echten Fälle
- Human Review Pflicht
- geschützter Kern bleibt privat
- kommerzielle Nutzung nur mit passender Erlaubnis oder Vereinbarung
- klare Grenzen der Nutzung

### Phase 5 — Supportpfade setzen

Dokumentiere in:

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

Erstelle:

```text
LICENSE.md
```

Lizenz muss klarstellen:

- Attribution bleibt erhalten
- keine Gewährleistung
- keine ungeprüfte Hochrisiko-Nutzung
- kommerzielle Nutzung nur mit Erlaubnis oder Vereinbarung
- Public-Safe-Grenzen bleiben bestehen

### Phase 7 — Protected Core prüfen

Erstelle:

```text
PROTECTED_CORE_AUDIT.md
```

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

Erstelle:

```text
FINAL_AUDIT_REPORT.md
```

Pflichtpunkte:

- Teststatus
- CI-Status
- Safety-Invariants
- Datenschutzstatus
- Protected-Core-Status
- Human-Review-Status
- Payment-/Support-Status
- License-/Rights-Status
- offene Blocker
- Release-Entscheidung

Erlaubter Status vor Approval:

```text
AUDIT_STATUS: PASSED_WITH_RELEASE_BLOCKERS
PUBLIC_RELEASE: BLOCKED
```

### Phase 9 — Release Candidate vorbereiten

Nur wenn erfüllt:

- Tests bestanden
- CI bestanden
- Audit erstellt
- Protected Core ausgeschlossen
- Supportpfade gesetzt
- Lizenzdatei vorhanden
- README vollständig
- keine echten Daten
- keine Zugangsdaten

Status:

```text
PUBLIC_SAFE_RELEASE_CANDIDATE_READY
PUBLIC_RELEASE: BLOCKED_UNTIL_HUMAN_APPROVAL
```

### Phase 10 — Human Approval

Codex darf Public Release nicht selbst freigeben.

Erforderliche Datei:

```text
HUMAN_APPROVAL.md
```

Ohne diese Datei bleibt:

```text
PUBLIC_RELEASE: BLOCKED
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

## Nächster Auftrag

```text
1. Complete missing docs and workflows.
2. Add missing tests for classifier, deadline checker, evidence card and demo.
3. Add funding configuration.
4. Add conservative LICENSE.md.
5. Add CHANGELOG.md and ROADMAP.md.
6. Run CI.
7. Create FINAL_AUDIT_REPORT.md.
8. Keep PUBLIC_RELEASE blocked until HUMAN_APPROVAL.md exists.
```

## Leitsatz

```text
Build useful civic protection.
Keep data synthetic.
Keep external effect blocked.
Keep human review mandatory.
Keep the protected core protected.
Release only with explicit human approval.
```
