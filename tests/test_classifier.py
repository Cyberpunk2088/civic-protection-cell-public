from civic_protection_cell.classifier import classify_text


def test_classifier_detects_jobcenter_heuristically():
    result = classify_text("Synthetischer Jobcenter-Bescheid zur Mitwirkung.")

    assert result.category == "jobcenter"
    assert 0 < result.confidence <= 0.9
    assert "Heuristic classification only" in result.note
    assert "Human review required" in result.note


def test_classifier_unknown_for_unclear_text():
    result = classify_text("Synthetische Notiz ohne klare Fachsignale.")

    assert result.category == "unknown"
    assert result.confidence == 0.0
    assert "Human review required" in result.note


def test_classifier_detects_court_signal_without_final_assessment():
    result = classify_text("Synthetischer Gerichtstermin mit Beschluss-Hinweis.")

    assert result.category == "gericht"
    assert 0 < result.confidence <= 0.9
    assert "Heuristic classification only" in result.note
    assert "Human review required" in result.note
