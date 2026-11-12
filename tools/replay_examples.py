"""Replay the checked-in examples and compare their results to the baseline."""
import argparse
import difflib
import json
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]


def local_file(relative):
    path = (ROOT / relative).resolve()
    if not path.is_relative_to(ROOT) or not path.is_file():
        raise ValueError(f"Missing or out-of-tree file: {relative}")
    return path


def run_case(case):
    expected = local_file(case["expected"]).read_text(encoding="utf-8")
    script = local_file(case["args"][0])
    result = subprocess.run(
        [sys.executable, "-B", str(script), *case["args"][1:]], cwd=ROOT,
        text=True, encoding="utf-8", capture_output=True, timeout=30,
    )
    if result.returncode:
        return False, f"Exit {result.returncode}: {result.stderr.strip()}"
    if expected == result.stdout:
        return True, result.stdout
    diff = difflib.unified_diff(
        expected.splitlines(keepends=True), result.stdout.splitlines(keepends=True),
        fromfile="expected", tofile="observed",
    )
    return False, "".join(diff)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--report", type=Path, help="write a Markdown review report")
    args = parser.parse_args()
    cases = json.loads(local_file("examples/replay-manifest.json").read_text(encoding="utf-8"))
    sections = ["# Replay evidence", "", "Captured stdout is compared with a checked-in baseline.", ""]
    failures = 0
    for case in cases:
        try:
            passed, detail = run_case(case)
        except (ValueError, OSError, subprocess.TimeoutExpired) as error:
            passed, detail = False, str(error)
        outcome = "PASS" if passed else "FAIL"
        print(f"{outcome}: {case['name']}")
        if not passed:
            failures += 1
            print(detail, file=sys.stderr)
        sections.extend([f"## {case['name']}", "", f"Result: **{outcome}**", "",
                         "````text", detail.rstrip() or "(empty stdout)", "````", ""])
    if args.report:
        args.report.write_text("\n".join(sections).rstrip() + "\n", encoding="utf-8")
    return int(bool(failures))


if __name__ == "__main__":
    sys.exit(main())
