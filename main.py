#!/usr/bin/env python3
"""A Day of One-Line Pitches entry.

Writes a single original one-sentence pitch (at most 240 characters)
to /output/entry.txt, aimed at convincing a friend who has never coded
to let an AI agent build their first app idea on make.fun.
"""

import os

LINE = "You've been sitting on that app idea for years, so describe it in plain words on make.fun and an AI agent will build your first version — no coding, nothing to install, and you'll finally have something real to show your friends."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
