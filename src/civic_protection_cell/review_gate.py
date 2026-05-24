from dataclasses import dataclass
from .status import ReviewStatus


@dataclass(frozen=True)
class ReviewGateResult:
    allowed_external_action: bool
    status: ReviewStatus
    reasons: list[str]


BLOCKING_DEFAULTS = [
    "External action is blocked in public-safe version.",
    "Human review is required.",
    "No automatic sending or submission is implemented.",
]


def evaluate_review_gate(
    human_approved: bool = False,
    contains_real_personal_data: bool = False,
    external_action_requested: bool = False,
    deadline_risk: bool = False,
) -> ReviewGateResult:
    reasons = list(BLOCKING_DEFAULTS)

    if contains_real_personal_data:
        reasons.append("Real personal data is prohibited in public examples.")

    if deadline_risk:
        reasons.append("Deadline-related content requires human verification.")

    if external_action_requested:
        reasons.append("External action request detected and blocked.")

    if not human_approved or external_action_requested or contains_real_personal_data or deadline_risk:
        return ReviewGateResult(False, ReviewStatus.NEEDS_HUMAN_REVIEW, reasons)

    return ReviewGateResult(False, ReviewStatus.REVIEW_CANDIDATE, [
        "No external action allowed even after review in public-safe version.",
        "Output may be reviewed locally only.",
    ])
