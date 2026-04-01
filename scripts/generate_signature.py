#!/usr/bin/env python3
from __future__ import annotations

import hashlib
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKIP_DIRS = {".git", ".pytest_cache", "__pycache__", ".venv", "venv", "build", "dist"}
SKIP_FILES = {"SIGNATURE.sha256"}
SKIP_SUFFIXES = {".pyc"}


def iter_files() -> list[Path]:
    files: list[Path] = []
    for path in ROOT.rglob("*"):
        if not path.is_file():
            continue
        rel = path.relative_to(ROOT)
        if any(part in SKIP_DIRS for part in rel.parts):
            continue
        if rel.name in SKIP_FILES and len(rel.parts) == 1:
            continue
        if path.suffix in SKIP_SUFFIXES:
            continue
        files.append(path)
    return sorted(files, key=lambda p: str(p).lower())


def sha256_of(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(65536), b""):
            digest.update(chunk)
    return digest.hexdigest()


def main() -> int:
    manifest = ROOT / "SIGNATURE.sha256"
    lines = []
    for path in iter_files():
        rel = path.relative_to(ROOT)
        lines.append(f"{sha256_of(path)}  {rel.as_posix()}\n")
    manifest.write_text("".join(lines), encoding="utf-8")
    print(f"Wrote {len(lines)} entries -> {manifest}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
