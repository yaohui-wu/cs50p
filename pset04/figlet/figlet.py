import sys
from random import choice

from pyfiglet import Figlet


def main():
    figlet = Figlet()
    fonts = figlet.getFonts()
    error = "Invalid usage"
    num_arg = len(sys.argv)
    if num_arg == 1:
        font = choice(fonts)
    elif num_arg == 3:
        font_flag = sys.argv[1]
        if font_flag != "-f" and font_flag != "--font":
            sys.exit(error)
        font = sys.argv[2]
        if font not in fonts:
            sys.exit(error)
    else:
        sys.exit(error)
    figlet.setFont(font=font)
    text = input("Input: ")
    output = figlet.renderText(text)
    print("Output:")
    print(output)


if __name__ == "__main__":
    main()
