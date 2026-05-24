from civic_protection_cell.deadline_checker import detect_deadline_risk


def test_deadline_signal_requires_human_review():
    result = detect_deadline_risk("Synthetischer Brief: Widerspruch innerhalb von 14 Tagen.")

    assert result.possible_deadline_detected is True
    assert result.risk_level == "NEEDS_HUMAN_REVIEW"
    assert "Human review required" in result.note


def test_no_deadline_signal_is_low_risk_note_only():
    result = detect_deadline_risk("Synthetische Information ohne Zeitangabe.")

    assert result.possible_deadline_detected is False
    assert result.risk_level == "LOW"
    assert "not a legal conclusion" in result.note
