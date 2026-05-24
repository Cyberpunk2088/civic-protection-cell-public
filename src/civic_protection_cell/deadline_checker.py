from dataclasses import dataclass
import re


@dataclass(frozen=True)
class DeadlineRisk:
    possible_deadline_detected: bool
    risk_level: str
    evidence: list[str]
    note: str


DEADLINE_PATTERNS = [
    r"innerhalb von\s+\d+\s+(tagen|wochen|monaten)",
    r"bis zum\s+\d{1,2}\.\d{1,2}\.\d{4}",
    r"frist",
    r"widerspruch",
    r"anhoerung|anhörung",
]


def detect_deadline_risk(text: str) -> DeadlineRisk:
    lower = text.lower()
    pattern_hits = []
    for pattern in DEADLINE_PATTERNS:
        if re.search(pattern, lower):
            pattern_hits.append(pattern)

    direct_hits = [word for word in ["frist", "widerspruch", "anhörung", "anhoerung"] if word in lower]
    possible = bool(pattern_hits or direct_hits)

    if possible:
        return DeadlineRisk(
            possible_deadline_detected=True,
            risk_level="NEEDS_HUMAN_REVIEW",
            evidence=direct_hits or ["deadline pattern detected"],
            note="Possible deadline risk. No final deadline calculation. Human review required.",
        )

    return DeadlineRisk(
        possible_deadline_detected=False,
        risk_level="LOW",
        evidence=[],
        note="No obvious deadline signal detected. This is not a legal conclusion.",
    )
