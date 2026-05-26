"""
Run the daily CSE dataset update pipeline.

Default mode performs remote incremental fetches. Use --offline to rebuild derived
artifacts from cached/committed inputs without touching remote sources.
"""

from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


REMOTE_STEPS = [
    ["scripts/02_collect_prices.py", "--mode", "incremental"],
    ["scripts/05_collect_macro.py"],
    ["scripts/04a_scrape_lbo.py"],
    ["scripts/04b_scrape_cse_news.py"],
]

DERIVED_STEPS = [
    ["scripts/02b_merge_data.py"],
    ["scripts/06_clean_prices.py"],
    ["scripts/07_engineer_features.py"],
    ["scripts/04c_sentiment_analysis.py"],
    ["scripts/08_build_unified.py"],
    ["scripts/validate_dataset.py"],
]


def run_step(args: list[str]) -> None:
    cmd = [sys.executable, *args]
    print(f"\n==> {' '.join(cmd)}", flush=True)
    subprocess.run(cmd, cwd=ROOT, check=True)


def main() -> None:
    parser = argparse.ArgumentParser(description="Run the daily CSE dataset update")
    parser.add_argument(
        "--offline",
        action="store_true",
        help="Skip remote fetches and rebuild derived artifacts from existing files",
    )
    parser.add_argument(
        "--allow-stale",
        action="store_true",
        help="Allow stale max-date validation; useful for local offline smoke runs",
    )
    args = parser.parse_args()

    steps = [] if args.offline else REMOTE_STEPS
    steps = [*steps, *DERIVED_STEPS]

    for step in steps:
        if step == ["scripts/validate_dataset.py"] and args.allow_stale:
            step = [*step, "--allow-stale"]
        run_step(step)


if __name__ == "__main__":
    main()
