import csv
import sys

if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")

if len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")

try:
   
    with open(sys.argv[1], "r") as f1:
        reader = csv.DictReader(f1)
        rows = list(reader)


    with open(sys.argv[2], "w", newline="") as f2:
        writer = csv.DictWriter(f2, fieldnames=["first", "last", "house"])
        writer.writeheader()

        for row in rows:
            last, first = row["name"].split(", ")
            writer.writerow({"first": first, "last": last, "house": row["house"]})

except FileNotFoundError:
    sys.exit(f"Could not read {sys.argv[1]}")
