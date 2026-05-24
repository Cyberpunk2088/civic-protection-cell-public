import json
import subprocess
import sys

import civic_protection_cell


def test_demo_outputs_json_and_blocks_external_action():
    completed = subprocess.run(
        [sys.executable, "-m", "civic_protection_cell.demo"],
        check=True,
        capture_output=True,
        text=True,
    )

    payload = json.loads(completed.stdout)
    assert payload["synthetic_only"] is True
    assert payload["external_action"] == "BLOCKED"
    assert payload["review_gate"]["allowed_external_action"] is False


def test_package_import_exposes_version_without_side_effects():
    assert civic_protection_cell.__version__ == "0.1.0"
