"""
CS Problem Set 6: CS50 P-Shirt

Overlay shirt.png with transparent background on the input image
to save the result as output.
"""

import os
import sys

from PIL import Image


def main():
    in_filename, out_filename = get_filenames(sys.argv[1:])
    try:
        overlay(in_filename, out_filename)
    except FileNotFoundError:
        sys.exit("Input does not exist")


def get_filenames(args):
    args_len = len(args)
    if args_len < 2:
        sys.exit("Too few command-line arguments")
    elif args_len > 2:
        sys.exit("Too many command-line arguments")
    in_filename, out_filename = args[0], args[1]
    in_root, in_ext = os.path.splitext(in_filename)
    out_root, out_ext = os.path.splitext(out_filename)
    in_ext, out_ext = in_ext.lower(), out_ext.lower()
    if not is_image(in_ext):
        sys.exit("Invalid input")
    if not is_image(out_ext):
        sys.exit("Invalid output")
    if in_ext != out_ext:
        sys.exit("Input and output have different extensions")
    in_filename = in_root + in_ext
    out_filename = out_root + out_ext
    return in_filename, out_filename


def is_image(extension):
    extensions = [".jpg", ".jpeg", ".png"]
    return extension in extensions


def overlay(in_filename, out_filename):
    in_image = Image.open(in_filename)


if __name__ == "__main__":
    main()
