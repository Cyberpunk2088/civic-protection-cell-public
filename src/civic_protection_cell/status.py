from enum import Enum


class ReviewStatus(str, Enum):
    DRAFT = "DRAFT"
    NEEDS_HUMAN_REVIEW = "NEEDS_HUMAN_REVIEW"
    BLOCKED = "BLOCKED"
    REVIEW_CANDIDATE = "REVIEW_CANDIDATE"
