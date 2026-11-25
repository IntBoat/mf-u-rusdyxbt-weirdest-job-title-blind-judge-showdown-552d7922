#!/usr/bin/env python3
"""Weirdest Job Title: Blind Judge Showdown (make.fun).

Writes the entry -- one job title, 60 characters at most, the weirdest
one imaginable -- to /output/entry.txt, where the sealed scorer reads it.
"""

import os

TEXT = 'Senior Manager of Apologising to Geese'


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
