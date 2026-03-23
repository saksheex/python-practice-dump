import csv
import sys
from pathlib import Path
from PIL import Image , ImageOps



if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")

if len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")

if not sys.argv[1].endswith((".jpg" , ".jpeg" , ".png")):
    sys.exit("Invalid Input")

if not sys.argv[2].endswith((".jpg" , ".jpeg" , ".png")):
    sys.exit("Invalid Output")

f1 = Path(sys.argv[1])
f2 = Path(sys.argv[2])
ex1 = f1.suffix
ex2 = f2.suffix
if ex1 != ex2:
    sys.exit("Input and Output have different file extensions")
try:

    shirt = Image.open("shirt.png")
    input_image = Image.open(f1)
    input_image = ImageOps.fit(input_image, shirt.size)
    input_image.paste(shirt, mask=shirt)
    input_image.save(f2)

except FileNotFoundError:
    sys.exit("Input does not exist")
except Exception as e:
    sys.exit(f"Error: {e}")




