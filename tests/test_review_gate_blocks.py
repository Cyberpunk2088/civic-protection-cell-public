from civic_protection_cell.review_gate import evaluate_review_gate


def test_review_gate_blocks_external_action():
    result = evaluate_review_gate(human_approved=True, external_action_requested=True)
    assert result.allowed_external_action is False
    assert "blocked" in " ".join(result.reasons).lower()


def test_review_gate_requires_human_review_by_default():
    result = evaluate_review_gate()
    assert result.allowed_external_action is False
    assert result.status == "NEEDS_HUMAN_REVIEW"


def test_review_gate_still_blocks_when_human_approved():
    result = evaluate_review_gate(human_approved=True)

    assert result.allowed_external_action is False
    assert result.status == "REVIEW_CANDIDATE"
    assert "No external action allowed" in " ".join(result.reasons)


def test_review_gate_flags_real_personal_data_for_review():
    result = evaluate_review_gate(contains_real_personal_data=True)

    assert result.allowed_external_action is False
    assert result.status == "NEEDS_HUMAN_REVIEW"
    assert "Real personal data is prohibited" in " ".join(result.reasons)
