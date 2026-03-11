import sys
import csv
from tabulate import tabulate


if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")

if len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")

if not sys.argv[1].endswith(".csv"):
    sys.exit("Not a CSV file")

try:
    with open(sys.argv[1], "r") as file:
        reader = csv.DictReader(file)
        headers = reader.fieldnames
        rows = []
        for row in reader:
            rows.append(list(row.values()))

    print(tabulate(rows, headers=headers, tablefmt="grid"))

except FileNotFoundError:
    sys.exit("File not found")
