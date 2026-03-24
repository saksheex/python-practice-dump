
from fpdf import FPDF

name = input("Name: ")

pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.set_auto_page_break(auto=False)
pdf.add_page()

# Title
pdf.set_font("Helvetica", "B", 36)
pdf.set_text_color(0, 0, 0)
pdf.set_y(20)
pdf.cell(210, 20, "CS50 Shirtificate", align="C")

# Shirt image centered horizontally
image_width = 190
image_x = (210 - image_width) / 2
pdf.image("shirtificate.png", x=image_x, y=50, w=image_width)

# User's name on top of shirt in white
pdf.set_font("Helvetica", "B", 26)
pdf.set_text_color(255, 255, 255)
pdf.set_xy(0, 130)
pdf.cell(210, 10,f"{name} took CS50", align="C")

pdf.output("shirtificate.pdf")

