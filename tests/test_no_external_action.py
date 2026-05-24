from pathlib import Path


def test_no_sending_or_submission_modules_present():
    repo_root = Path(__file__).resolve().parents[1]
    suspicious = []
    for path in (repo_root / "src").rglob("*.py"):
        name = path.name.lower()
        text = path.read_text(encoding="utf-8").lower()
        if any(token in name for token in ["send", "submit", "mail", "smtp", "crawl", "browser"]):
            suspicious.append(str(path))
        if any(
            token in text
            for token in [
                "smtplib",
                "requests.",
                "urllib.request",
                "http.client",
                "socket.",
                "httpx",
                "aiohttp",
                "selenium",
                "playwright",
                "crawl",
                "browser automation",
            ]
        ):
            suspicious.append(str(path))
    assert suspicious == []


def test_human_approval_file_absent_or_guarded():
    repo_root = Path(__file__).resolve().parents[1]
    approval_file = repo_root / "HUMAN_APPROVAL.md"

    if not approval_file.exists():
        return

    text = approval_file.read_text(encoding="utf-8")
    required_markers = [
        "OWNER_APPROVAL: GIVEN",
        "REPOSITORY_SCOPE: Public-safe repository layer only",
        "LEGAL_REVIEW_STATUS: NOT_REPLACED_BY_THIS_RECORD",
        "REPOSITORY_VISIBILITY_CHANGE: MANUAL_GITHUB_ACTION_REQUIRED",
        "REAL_DATA: PROHIBITED",
        "SYNTHETIC_DATA: ONLY",
        "EXTERNAL_ACTION: BLOCKED",
        "LEGAL_ADVICE: NOT_PROVIDED",
        "FINAL_DEADLINE_CALCULATION: NOT_PROVIDED",
        "HUMAN_REVIEW: REQUIRED",
        "PROTECTED_CORE: EXCLUDED",
        "TAX_NUMBER_PUBLICATION: NO",
        "BANK_DATA_PUBLICATION: NO",
        "No automated repository visibility change is performed by this file.",
    ]

    for marker in required_markers:
        assert marker in text
