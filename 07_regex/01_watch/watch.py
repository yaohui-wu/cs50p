"""
CS50P Problem Set 7: Watch on YouTube

Extract a YouTube URL from an iframe's src attribute
and convert it to a shorter, shareable URL.
"""

import re


def main():
    print(parse((input("HTML: "))))


def parse(s):
    # TODO
    pattern = r"https?://(www.)youtube.com/embed/[A-Za-z0-9]+"
    if match := re.search(pattern, s):
        print(match.group(0))
        prefix = r"https://youtu.be/"
        return prefix
    return None


if __name__ == "__main__":
    main()
