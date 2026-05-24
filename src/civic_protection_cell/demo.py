import json
from .output import analyze_synthetic_text


SYNTHETIC_TEXT = """
Synthetischer Behördenbrief.
Bitte reichen Sie die fehlenden Unterlagen innerhalb von 14 Tagen nach.
Dies ist kein echter Fall und enthält keine personenbezogenen Daten.
"""


def main() -> None:
    result = analyze_synthetic_text(SYNTHETIC_TEXT)
    print(json.dumps(result, indent=2, ensure_ascii=False, default=str))


if __name__ == "__main__":
    main()
