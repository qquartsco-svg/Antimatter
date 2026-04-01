#!/usr/bin/env python3
from __future__ import annotations

import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def main() -> int:
    removed = 0
    for path in ROOT.rglob("*"):
        if path.name in {".pytest_cache", "__pycache__", ".DS_Store"}:
            if path.is_dir():
                shutil.rmtree(path, ignore_errors=True)
            else:
                path.unlink(missing_ok=True)
            removed += 1
    print(f"cleaned={removed}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
