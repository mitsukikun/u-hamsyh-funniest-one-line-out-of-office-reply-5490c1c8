"""Write the funniest one-line out-of-office reply to /output/entry.txt.

Deterministic, no network, no randomness. Writes only to /output/entry.txt.
"""

LINE = "I'm away until Monday \u2014 my cover is also me, but on holiday and far less helpful."


def main():
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
