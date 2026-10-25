"""
CS50P Problem Set 7: Watch on YouTube

Extract a YouTube embed URL from an iframe's src attribute
and convert it to a shortened YouTube URL.
"""

import re


def main():
    print(parse(input("HTML: ")))


def parse(s):
    # Match a YouTube embed URL
    url = r"https?://(?:www\.)?youtube\.com/embed"
    # Match an iframe containing a YouTube embed URL
    pattern = rf'^<iframe\s.*?src="{url}/([A-Za-z0-9]+)".*?></iframe>$'
    if match := re.search(pattern, s):
        # Extract the video ID in the YouTube embed URL
        video_id = match.group(1)
        # Return a shortened YouTube URL for the video
        return f"https://youtu.be/{video_id}"
    return None


if __name__ == "__main__":
    main()
