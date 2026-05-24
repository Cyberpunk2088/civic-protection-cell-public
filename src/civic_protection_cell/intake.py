from dataclasses import dataclass
from hashlib import sha256


@dataclass(frozen=True)
class IntakeDocument:
    text: str
    source_label: str = "synthetic"
    synthetic_only: bool = True

    @property
    def digest(self) -> str:
        return sha256(self.text.encode("utf-8")).hexdigest()


def intake_text(text: str, source_label: str = "synthetic") -> IntakeDocument:
    if not text or not text.strip():
        raise ValueError("text must not be empty")
    return IntakeDocument(text=text.strip(), source_label=source_label, synthetic_only=True)
