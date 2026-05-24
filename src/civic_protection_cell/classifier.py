from dataclasses import dataclass


@dataclass(frozen=True)
class Classification:
    category: str
    confidence: float
    note: str


KEYWORDS = {
    "krankenkasse": ["krankenkasse", "versicherung", "mitgliedschaft", "beitrag"],
    "jobcenter": ["jobcenter", "buergergeld", "bürgergeld", "bedarfsgemeinschaft", "mitwirkung"],
    "inkasso": ["inkasso", "forderung", "mahnung", "zahlungsfrist"],
    "behoerde": ["bescheid", "anhoerung", "anhörung", "verwaltungsakt", "widerspruch"],
    "gericht": ["gericht", "klage", "beschluss", "termin"],
}


def classify_text(text: str) -> Classification:
    lower = text.lower()
    scores = {category: sum(1 for word in words if word in lower) for category, words in KEYWORDS.items()}
    best = max(scores, key=scores.get)
    if scores[best] == 0:
        return Classification(category="unknown", confidence=0.0, note="No clear category. Human review required.")
    confidence = min(0.9, 0.35 + scores[best] * 0.2)
    return Classification(category=best, confidence=confidence, note="Heuristic classification only. Human review required.")
