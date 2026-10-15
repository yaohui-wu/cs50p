import random
import sys

from pyfiglet import Figlet


def main():
    figlet = Figlet()
    fonts = figlet.getFonts()
    f = choose_font(fonts, sys.argv[1:])
    figlet.setFont(font=f)
    text = input("Input: ")
    output = figlet.renderText(text)
    print("Output: ")
    print(output)


def choose_font(fonts, args):
    num_arg = len(args)
    if num_arg == 0:
        font = random.choice(fonts)
        return font
    elif num_arg == 2:
        font_flag = args[0]
        if font_flag == "-f" or font_flag == "--font":
            font = args[1]
            if font in fonts:
                return font
    sys.exit("Invalid usage")


if __name__ == "__main__":
    main()
