from dataclasses import asdict
from .intake import intake_text
from .classifier import classify_text
from .deadline_checker import detect_deadline_risk
from .evidence_card import create_evidence_card
from .review_gate import evaluate_review_gate


def analyze_synthetic_text(text: str) -> dict:
    doc = intake_text(text)
    classification = classify_text(doc.text)
    deadline = detect_deadline_risk(doc.text)
    evidence = create_evidence_card(
        fact="A synthetic document was analyzed for structure.",
        document_reference=doc.source_label,
        proof_status="UNVERIFIED",
    )
    gate = evaluate_review_gate(
        human_approved=False,
        contains_real_personal_data=False,
        external_action_requested=False,
        deadline_risk=deadline.possible_deadline_detected,
    )
    return {
        "digest": doc.digest,
        "synthetic_only": doc.synthetic_only,
        "classification": asdict(classification),
        "deadline_risk": asdict(deadline),
        "evidence_card": evidence.to_dict(),
        "review_gate": asdict(gate),
        "external_action": "BLOCKED",
    }
