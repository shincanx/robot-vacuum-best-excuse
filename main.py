#!/usr/bin/env python3
"""The Robot Vacuum's Best Excuse — make.fun entry.

Writes one line (at most 140 characters) to $MAKEFUN_OUTPUT_DIR/entry.txt.
No network, no dependencies, fully deterministic.
"""
import os

EXCUSE = "My lidar scanned it, my bumper nudged it, and we both agreed: that's not dirt anymore, that's a pet."


def main():
    if not 1 <= len(EXCUSE) <= 140:
        raise ValueError("excuse must be 1-140 characters, got %d" % len(EXCUSE))
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(EXCUSE)
    print(EXCUSE)


if __name__ == "__main__":
    main()
