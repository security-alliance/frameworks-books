#!/usr/bin/env python3
"""Structural checks for the pocket-guide PDF."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from pypdf import PdfReader


MM_PER_PT = 25.4 / 72.0


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("pdf", type=Path)
    args = parser.parse_args()

    reader = PdfReader(str(args.pdf))
    if len(reader.pages) < 40:
        raise SystemExit(f"Unexpectedly short book: {len(reader.pages)} pages")

    sizes = []
    blank_pages = []
    for number, page in enumerate(reader.pages, start=1):
        width = float(page.mediabox.width) * MM_PER_PT
        height = float(page.mediabox.height) * MM_PER_PT
        sizes.append((round(width, 2), round(height, 2)))
        if not (page.extract_text() or "").strip():
            blank_pages.append(number)

    expected = (70.0, 110.0)
    bad_sizes = sorted({size for size in sizes if abs(size[0] - expected[0]) > 0.2 or abs(size[1] - expected[1]) > 0.2})
    if bad_sizes:
        raise SystemExit(f"Unexpected page sizes: {bad_sizes}")

    text = "\n".join((page.extract_text() or "") for page in reader.pages)
    required = [
        "SECURITY FRAMEWORKS",
        "Never sign blindly",
        "Safe Harbor",
        "Attribution-ShareAlike",
    ]
    missing = [item for item in required if item not in text]
    if missing:
        raise SystemExit(f"Missing expected text: {missing}")

    report = {
        "file": str(args.pdf),
        "pages": len(reader.pages),
        "page_size_mm": list(expected),
        "textless_pages": blank_pages,
        "status": "passed",
    }
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
