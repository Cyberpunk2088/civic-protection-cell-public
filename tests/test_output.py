from civic_protection_cell.output import analyze_synthetic_text


def test_analyze_synthetic_text_blocks_external_action():
    result = analyze_synthetic_text("Synthetischer Bescheid mit Widerspruch und Frist.")
    assert result["synthetic_only"] is True
    assert result["external_action"] == "BLOCKED"
    assert result["review_gate"]["allowed_external_action"] is False
