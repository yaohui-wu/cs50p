"""
CS50P Problem Set 8: CS50 Shirtificate

Generate a customized CS50 shirtificate PDF with the recipient's name.
"""

import sys

from fpdf import FPDF
from fpdf.enums import Align


class PDF(FPDF):
    def __init__(self, name: str) -> None:
        """
        Generate a customized CS50 shirtificate PDF
        with the recipient's name.
        """
        super().__init__(orientation="portrait", unit="mm", format="a4")
        self.shirtificate(name)

    def shirtificate(self, name: str) -> None:
        # TODO
        self.add_page()
        # Set 1-inch margins
        self.set_margins(left=25.4, top=25.4, right=25.4)
        # Scale and center the shirt image
        self.image(
            name="shirtificate.png",
            x=Align.C,
            w=self.epw,
            h=self.eph,
            keep_aspect_ratio=True,
        )
        # Position the text over the shirt
        self.set_xy(self.epw / 2, self.eph / 2)
        # Configure typography and change text color to white
        self.set_font(family="Courier", style="B", size=20)
        self.set_text_color(r=255, g=255, b=255)
        # Customize the shirt with recipient's name
        self.cell(text=f"{name} took CS50", center=True)
        ...


def main() -> None:
    """
    Prompt the user for the recipient's name
    and save a personalized CS50 shirtificate PDF.
    """
    # TODO
    name = input("Name: ").strip().title()
    if not name:  # Reject blank input
        sys.exit("Invalid name")
    pdf = PDF(name)
    # Save the PDF file
    pdf.output("shirtificate.pdf")
    ...


if __name__ == "__main__":
    main()
