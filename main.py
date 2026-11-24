#!/usr/bin/env python3
"""news-image-20261124: write one image summing up 24 November 2026's world news.

Deterministic and offline: copies the image shipped in assets/entry.png to
/output/entry.png. No network, no randomness, no timestamps in the output,
so two runs write byte-identical files.
"""

import hashlib
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
SOURCE = HERE / "assets" / "entry.png"
DEST = Path("/output") / "entry.png"


def sha256_of(path: Path) -> str:
    """Return the hex SHA-256 digest of a file's bytes."""
    digest = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 20), b""):
            digest.update(chunk)
    return digest.hexdigest()


def verify_copy(source: Path, dest: Path) -> str:
    """Check the written copy matches the shipped asset byte-for-byte.

    Returns the matching SHA-256 hex digest; raises SystemExit if the
    written file differs from the asset.
    """
    expected = sha256_of(source)
    actual = sha256_of(dest)
    if actual != expected:
        raise SystemExit(f"self-check failed: {dest} hash {actual} != asset hash {expected}")
    return actual


def main() -> None:
    DEST.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(SOURCE, DEST)
    digest = verify_copy(SOURCE, DEST)
    print(f"wrote {DEST} ({DEST.stat().st_size} bytes) sha256={digest}")


if __name__ == "__main__":
    main()
