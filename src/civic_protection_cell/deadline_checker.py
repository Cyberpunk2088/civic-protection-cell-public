from dataclasses import dataclass
import re


@dataclass(frozen=True)
class DeadlineRisk:
    possible_deadline_detected: bool
    risk_level: str
    evidence: list[str]
    note: str


DEADLINE_PATTERNS = [
    (
        "pattern: relative_duration",
        r"\binnerhalb von\s+\d+\s+(tagen|wochen|monaten)\b",
    ),
    ("pattern: calendar_date", r"\bbis zum\s+\d{1,2}\.\d{1,2}\.\d{4}\b"),
    ("keyword: frist", r"\b\w*frist\w*\b"),
    ("keyword: widerspruch", r"\b\w*widerspruch\w*\b"),
    ("keyword: anhoerung", r"\b\w*(anhoerung|anhörung)\w*\b"),
]


def detect_deadline_risk(text: str) -> DeadlineRisk:
    lower = text.lower()
    evidence = []
    for label, pattern in DEADLINE_PATTERNS:
        if re.search(pattern, lower):
            evidence.append(label)

    possible = bool(evidence)

    if possible:
        return DeadlineRisk(
            possible_deadline_detected=True,
            risk_level="NEEDS_HUMAN_REVIEW",
            evidence=evidence,
            note="Possible deadline risk. No final deadline calculation. Human review required.",
        )

    return DeadlineRisk(
        possible_deadline_detected=False,
        risk_level="LOW",
        evidence=[],
        note="No obvious deadline signal detected. This is not a legal conclusion.",
    )
