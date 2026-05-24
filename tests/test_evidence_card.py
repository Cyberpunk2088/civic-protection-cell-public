import pytest

from civic_protection_cell.evidence_card import create_evidence_card


def test_evidence_card_defaults_to_unverified():
    card = create_evidence_card("Synthetischer Fakt zur Strukturpruefung.")

    assert card.proof_status == "UNVERIFIED"
    assert card.gap == "Original and source not verified."
    assert card.next_step == "Human review required."


def test_evidence_card_rejects_empty_fact():
    with pytest.raises(ValueError):
        create_evidence_card("   ")


def test_evidence_card_dict_preserves_conservative_defaults():
    card = create_evidence_card("Synthetischer Fakt zur lokalen Evidence Card.")
    payload = card.to_dict()

    assert payload["proof_status"] == "UNVERIFIED"
    assert payload["gap"] == "Original and source not verified."
    assert payload["next_step"] == "Human review required."
