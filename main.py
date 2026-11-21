"""Catalogue photo entry: the Ice-O-Matic toaster that toasts ice cubes.

Copies the bundled entry.png (a studio catalogue photograph of the
impossible gadget) into the make.fun output directory as entry.png.

The image shows a retro chrome toaster with two ice cubes popping from
its slots — one golden-brown — and a single glass of water beside it.
"""

import os
import shutil
import sys

SOURCE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")
OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def main():
    if not os.path.isfile(SOURCE):
        print(f"error: source image not found: {SOURCE}", file=sys.stderr)
        sys.exit(1)
    if os.path.getsize(SOURCE) == 0:
        print(f"error: source image is empty: {SOURCE}", file=sys.stderr)
        sys.exit(1)
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    dest = os.path.join(OUTPUT_DIR, "entry.png")
    shutil.copyfile(SOURCE, dest)
    written = os.path.getsize(dest)
    if written != os.path.getsize(SOURCE):
        print(
            f"error: output size {written} != source size "
            f"{os.path.getsize(SOURCE)}",
            file=sys.stderr,
        )
        sys.exit(1)
    print(f"wrote {dest} ({written} bytes)")


if __name__ == "__main__":
    main()
