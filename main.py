#!/usr/bin/env python3
"""news-image-20261124: write one image summing up 24 November 2026's world news.

Deterministic and offline: copies the image shipped in assets/entry.png to
/output/entry.png. No network, no randomness, no timestamps in the output,
so two runs write byte-identical files.
"""

import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
SOURCE = HERE / "assets" / "entry.png"
DEST = Path("/output") / "entry.png"


def main() -> None:
    DEST.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(SOURCE, DEST)
    print(f"wrote {DEST} ({DEST.stat().st_size} bytes)")


if __name__ == "__main__":
    main()
