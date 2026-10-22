"""
CS Problem Set 6: CS50 P-Shirt

Overlay shirt.png with transparent background on the input image
to save the result as a new output image.
"""

import os
import sys

from PIL import Image, ImageOps

EXTENSIONS = {".jpg", ".jpeg", ".png"}
SHIRT_FILE = "shirt.png"


def main():
    in_filename, out_filename = get_filenames(sys.argv[1:])
    try:
        overlay_shirt(in_filename, out_filename)
    except FileNotFoundError:
        sys.exit("Input does not exist")


def get_filenames(args):
    args_len = len(args)
    if args_len < 2:
        sys.exit("Too few command-line arguments")
    elif args_len > 2:
        sys.exit("Too many command-line arguments")
    in_filename, out_filename = args[0], args[1]
    in_ext = os.path.splitext(in_filename)[1].lower()
    out_ext = os.path.splitext(out_filename)[1].lower()
    if in_ext not in EXTENSIONS:
        sys.exit("Invalid input")
    if out_ext not in EXTENSIONS:
        sys.exit("Invalid output")
    if in_ext != out_ext:
        sys.exit("Input and output have different extensions")
    return in_filename, out_filename


def overlay_shirt(in_filename, out_filename):
    with Image.open(SHIRT_FILE) as shirt:
        with Image.open(in_filename) as image:
            image = ImageOps.fit(image, shirt.size)
            image.paste(shirt, shirt)
            image.save(out_filename)


if __name__ == "__main__":
    main()
