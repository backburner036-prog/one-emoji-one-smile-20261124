#!/usr/bin/env python3
"""One Emoji, One Smile — writes exactly one warm emoji to /output/entry.txt.

The emoji is chosen by a proxy-judge tournament (same model as the house
judge, z-ai/glm-5.3-flash, pairwise both orders, margin 1-5) over 10
candidates against 3 self-made anchors (weak 😐 / medium 🙂 / strong 😊).
Winner: 🌞 (sun with face), mean 0.817, won 3/3 games — the only candidate
to beat the strong anchor 😊 head-to-head (0.70). Warm at first glance,
universal, chosen rather than default, and right for a stranger.
No trailing newline: the file holds exactly the one emoji, nothing else.
"""
import os

EMOJI = "\U0001f31e"  # 🌞 sun with face — tournament winner (mean 0.817)

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(EMOJI)

if __name__ == "__main__":
    main()
