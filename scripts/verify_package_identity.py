#!/usr/bin/env python3
"""Fail fast if contracts/__init__ were swapped with another engine (upload mix-up)."""
from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))


def main() -> int:
    try:
        from antimatter_phenomenology import contracts as c
    except ImportError as e:
        print("verify_package_identity: cannot import antimatter_phenomenology.contracts:", e, file=sys.stderr)
        return 2

    required = (
        "AntimatterDomain",
        "AntimatterInventory",
        "AntimatterConfinementContext",
        "AntimatterAsymmetryContext",
        "AntimatterFoundationReport",
    )
    missing = [n for n in required if not hasattr(c, n)]
    if missing:
        print("verify_package_identity: contracts missing:", missing, file=sys.stderr)
        return 1

    import inspect

    src = inspect.getsource(c)
    if "class AntimatterInventory" not in src or "class AntimatterFoundationReport" not in src:
        print("verify_package_identity: contracts.py does not look like antimatter contracts.", file=sys.stderr)
        return 1

    import antimatter_phenomenology as ap

    if not hasattr(ap, "assess_antimatter_foundation"):
        print("verify_package_identity: root package missing assess_antimatter_foundation.", file=sys.stderr)
        return 1

    print("verify_package_identity: OK (antimatter_phenomenology contracts + public API)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
