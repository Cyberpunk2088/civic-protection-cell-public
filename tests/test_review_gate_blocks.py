from civic_protection_cell.review_gate import evaluate_review_gate


def test_review_gate_blocks_external_action():
    result = evaluate_review_gate(human_approved=True, external_action_requested=True)
    assert result.allowed_external_action is False
    assert "blocked" in " ".join(result.reasons).lower()


def test_review_gate_requires_human_review_by_default():
    result = evaluate_review_gate()
    assert result.allowed_external_action is False
    assert result.status == "NEEDS_HUMAN_REVIEW"
