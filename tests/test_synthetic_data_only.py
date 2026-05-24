from pathlib import Path
import re


def test_examples_are_marked_synthetic():
    repo_root = Path(__file__).resolve().parents[1]
    files = [p for p in (repo_root / "examples").rglob("*") if p.is_file()]
    assert files, "expected synthetic example files"
    for path in files:
        text = path.read_text(encoding="utf-8").lower()
        assert "synthetisch" in text or "synthetic" in text
        assert "kein echter fall" in text or "not a real case" in text or "synthetic" in text


def test_tests_and_examples_do_not_contain_private_data_patterns():
    repo_root = Path(__file__).resolve().parents[1]
    checked_roots = [repo_root / "tests", repo_root / "examples"]
    private_patterns = [
        re.compile(r"\b\S+" + "@" + r"\S+\.\S+\b"),
        re.compile(r"\b\d{5}\s+[A-ZÄÖÜ][A-Za-zÄÖÜäöüß-]+\b"),
        re.compile(r"\b[A-Z]{1,3}\s?\d{1,4}/\d{2,4}\b"),
    ]
    hits = []

    for root in checked_roots:
        for path in root.rglob("*"):
            if path.is_file() and path.suffix in {".py", ".txt", ".md"}:
                text = path.read_text(encoding="utf-8")
                for pattern in private_patterns:
                    if pattern.search(text):
                        hits.append(str(path))

    assert hits == []
