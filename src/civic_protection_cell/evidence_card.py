from dataclasses import dataclass, asdict
from typing import Literal


ProofStatus = Literal["UNVERIFIED", "PARTIAL", "SUPPORTED", "MISSING", "CONFLICTING"]


@dataclass(frozen=True)
class EvidenceCard:
    fact: str
    document_reference: str
    date_reference: str | None
    proof_status: ProofStatus
    gap: str | None
    next_step: str

    def to_dict(self) -> dict:
        return asdict(self)


def create_evidence_card(
    fact: str,
    document_reference: str = "synthetic-example",
    date_reference: str | None = None,
    proof_status: ProofStatus = "UNVERIFIED",
    gap: str | None = "Original and source not verified.",
    next_step: str = "Human review required.",
) -> EvidenceCard:
    if not fact.strip():
        raise ValueError("fact must not be empty")
    return EvidenceCard(
        fact=fact.strip(),
        document_reference=document_reference,
        date_reference=date_reference,
        proof_status=proof_status,
        gap=gap,
        next_step=next_step,
    )
