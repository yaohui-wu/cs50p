"""
CS50P Problem Set 7: NUMB3RS

Validate whether an input string is a valid IPv4 address.
"""

import re


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    # Regex to match a single octet for a valid IPv4 address
    # Match 250-255, 200-249, 100-199, 10-99, and 0-9 without leading zeros
    octet = r"(?:25[0-5]|2[0-4]\d|1\d\d|[1-9]\d|\d)"
    # Valid IPv4 address: #.#.#.#
    # Each # (octet) is a number between 0 to 255
    pattern = rf"^(?:(?:{octet}\.){{3}}{octet})$"
    if re.search(pattern, ip.strip()):
        return True
    return False


if __name__ == "__main__":
    main()
