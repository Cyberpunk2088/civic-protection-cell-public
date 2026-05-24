from pathlib import Path


def test_examples_are_marked_synthetic():
    repo_root = Path(__file__).resolve().parents[1]
    files = [p for p in (repo_root / "examples").rglob("*") if p.is_file()]
    assert files, "expected synthetic example files"
    for path in files:
        text = path.read_text(encoding="utf-8").lower()
        assert "synthetisch" in text or "synthetic" in text
        assert "kein echter fall" in text or "not a real case" in text or "synthetic" in text
