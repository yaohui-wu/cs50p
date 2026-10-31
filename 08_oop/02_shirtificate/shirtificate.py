"""
CS50P Problem Set 8: CS50 Shirtificate

Generate a customized CS50 shirtificate PDF with the user's name.
"""

import sys

from fpdf import FPDF
from fpdf.enums import Align


def main() -> None:
    """
    Prompt the user for the recipient's name
    and save a personalized CS50 shirtificate PDF.
    """
    # TODO
    name = input("Name: ").strip().title()
    if not name:  # Reject blank input
        sys.exit("Invalid name")
    # Create an A4 portrait PDF document
    pdf = FPDF(orientation="portrait", unit="mm", format="a4")
    pdf.add_page()
    # Set 1-inch margins
    pdf.set_margins(left=25.4, top=25.4, right=25.4)
    # Scale and center the shirt image
    pdf.image(
        name="shirtificate.png",
        x=Align.C,
        w=pdf.epw,
        h=pdf.eph,
        keep_aspect_ratio=True,
    )
    # Position the text over the shirt
    pdf.set_xy(pdf.epw / 2, pdf.eph / 2)
    # Configure typography and change text color to white
    pdf.set_font(family="Courier", style="B", size=20)
    pdf.set_text_color(r=255, g=255, b=255)
    # Customize the shirt with recipient's name
    pdf.cell(text=f"{name} took CS50", center=True)
    # Save the PDF file
    pdf.output("shirtificate.pdf")
    ...


if __name__ == "__main__":
    main()
