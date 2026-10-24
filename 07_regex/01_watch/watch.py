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
    # Pattern for standard YouTube URLs
    long_prefix = r"https?://(www.)?youtube.com/embed"
    pattern = long_prefix + r"/[A-Za-z0-9]+"
    if match := re.search(pattern, s):
        short_prefix = r"https://youtu.be"
        url = re.sub(long_prefix, short_prefix, match.group(0))
        return url
    return None


if __name__ == "__main__":
    main()
