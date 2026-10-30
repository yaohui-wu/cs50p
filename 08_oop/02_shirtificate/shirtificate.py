"""
CS50P Problem Set 8: CS50 Shirtificate

Generate a customized CS50 shirtificate PDF with the user's name.
"""

import sys

from fpdf import FPDF, Align


def main() -> None:
    """
    Prompt for the user's name
    and save a customized CS50 shirtificate PDF.
    """
    # TODO
    name = input("Name: ").strip()
    if not name:  # Reject blank input
        sys.exit("Invalid name")
    name = name.title()
    # Initialize an A4 portrait PDF document
    pdf = FPDF(orientation="portrait", unit="mm", format="a4")
    pdf.add_page()
    # Set 1 in (25.4 mm) margins
    pdf.set_margins(left=25.4, top=25.4, right=25.4)
    # Scale and center the background image in the printable area
    pdf.image(
        name="shirtificate.png",
        x=Align.C,
        w=pdf.epw,
        h=pdf.eph,
        keep_aspect_ratio=True,
    )
    # Set the font for the PDF text
    pdf.set_font(family="Courier", style="", size=12)
    # Save the PDF document
    pdf.output("shirtificate.pdf")
    ...


if __name__ == "__main__":
    main()
