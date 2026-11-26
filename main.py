"""Write one funny line to /output/entry.txt.

The line is an entry for a one-line roast contest: a joke mocking
a refrigerator.
"""

import os


def joke_line():
    """Return one funny line roasting a fridge."""
    return (
        "My fridge hums all night like it pays rent, yet the only "
        "thing it ever chills is my hope of finding food in there."
    )


def main():
    line = joke_line()
    os.makedirs("/output", exist_ok=True)
    # Write the roast with no trailing newline, exactly as entered.
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(line)
    # Sanity check: the file must hold exactly the one roast line.
    with open("/output/entry.txt", encoding="utf-8") as handle:
        assert handle.read() == line


if __name__ == "__main__":
    main()
