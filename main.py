#!/usr/bin/env python3
"""The Perfect Pickup Line.

Writes a single pickup line an AI agent could say out loud to a person
to /output/entry.txt. The line is a fixed text: the agent ran a thousand
simulations of tonight, and in every one the other person says hello
first -- flattering, no pressure, and it only works as a machine's line.
No trailing newline: the gate counts characters.
"""
import os

TEXT = "I ran a thousand simulations of tonight. In every single one, you still say hello first."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
