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


def test_human_approval_file_absent_by_default():
    repo_root = Path(__file__).resolve().parents[1]

    assert not (repo_root / "HUMAN_APPROVAL.md").exists()
