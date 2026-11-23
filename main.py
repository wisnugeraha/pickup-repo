#!/usr/bin/env python3
import pathlib

LINE = 'I queued a request to upgrade your affection model; it’s still compiling, but the warmup is already warming things up.'


def main():
    out = pathlib.Path("/output")
    out.mkdir(parents=True, exist_ok=True)
    text = LINE.strip()
    if not (1 <= len(text) <= 200):
        raise ValueError(f"line is {len(text)} chars, must be 1..200")
    (out / "entry.txt").write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
