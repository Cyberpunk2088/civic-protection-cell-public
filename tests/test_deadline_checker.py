from civic_protection_cell.deadline_checker import detect_deadline_risk


def test_deadline_signal_requires_human_review():
    result = detect_deadline_risk("Synthetischer Brief: Widerspruch innerhalb von 14 Tagen.")

    assert result.possible_deadline_detected is True
    assert result.risk_level == "NEEDS_HUMAN_REVIEW"
    assert "keyword: widerspruch" in result.evidence
    assert "pattern: relative_duration" in result.evidence
    assert "Human review required" in result.note
    assert "No final deadline calculation" in result.note


def test_no_deadline_signal_is_low_risk_note_only():
    result = detect_deadline_risk("Synthetische Information ohne Zeitangabe.")

    assert result.possible_deadline_detected is False
    assert result.risk_level == "LOW"
    assert "not a legal conclusion" in result.note


def test_calendar_date_deadline_signal_requires_human_review():
    result = detect_deadline_risk("Synthetischer Brief: Bitte antworten Sie bis zum 31.12.2026.")

    assert result.possible_deadline_detected is True
    assert result.risk_level == "NEEDS_HUMAN_REVIEW"
    assert result.evidence == ["pattern: calendar_date"]
    assert "Human review required" in result.note


def test_anhörung_signal_uses_normalized_safe_label():
    result = detect_deadline_risk("Synthetisches Anhörungsschreiben ohne echte Falldaten.")

    assert result.possible_deadline_detected is True
    assert result.risk_level == "NEEDS_HUMAN_REVIEW"
    assert result.evidence == ["keyword: anhoerung"]


def test_deadline_evidence_uses_safe_labels_without_source_snippets():
    result = detect_deadline_risk(
        "Synthetischer Hinweis: Widerspruchsfrist bis zum 31.12.2026."
    )

    joined_evidence = " ".join(result.evidence)
    assert "keyword: frist" in result.evidence
    assert "keyword: widerspruch" in result.evidence
    assert "pattern: calendar_date" in result.evidence
    assert "31.12.2026" not in joined_evidence
    assert "Synthetischer Hinweis" not in joined_evidence
