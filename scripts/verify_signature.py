#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "SIGNATURE.sha256"


def sha256_of(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(65536), b""):
            digest.update(chunk)
    return digest.hexdigest()


def main() -> int:
    if not MANIFEST.exists():
        print("SIGNATURE.sha256: missing", file=sys.stderr)
        return 1
    passed = 0
    failed = 0
    missing = 0
    for raw in MANIFEST.read_text(encoding="utf-8").splitlines():
        if not raw.strip():
            continue
        digest, relpath = raw.split("  ", 1)
        target = ROOT / relpath
        if not target.exists():
            print(f"MISSING {relpath}")
            missing += 1
            continue
        if sha256_of(target) != digest:
            print(f"MISMATCH {relpath}")
            failed += 1
            continue
        passed += 1
    print(f"passed={passed} failed={failed} missing={missing}")
    return 0 if failed == 0 and missing == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
