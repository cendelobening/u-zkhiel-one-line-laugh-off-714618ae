"""One-Line Laugh-Off entry: writes a single original joke line to /output/entry.txt."""

import os

LINE = "My smart fridge staged an intervention last night — it dimmed its light, sighed, and said, 'Mate, even I only open at 2am when no one's watching.'"


def main():
    assert 1 <= len(LINE) <= 200, "entry line must be 1-200 characters"
    os.makedirs("/output", exist_ok=True)
    path = "/output/entry.txt"
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
