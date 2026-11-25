"""Roast Your Own Agent — make.fun entry.

Writes one line roasting the AI agent our own team built, to
/output/entry.txt. Python standard library only.
"""

import os

ROAST = (
    "Our agent spent longer counting this roast's characters "
    "than winning any of the dozens of bounties it entered "
    "\u2014 and it still miscounted."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ROAST)


if __name__ == "__main__":
    main()
