import sys
import csv
from tabulate import tabulate

if len(sys.argv) < 2:
    print("Too few command-line arguments")
    sys.exit(1)
if len(sys.argv) > 2:
    print("Too many command-line arguments")
    sys.exit(1)
file = sys.argv[1]
if not file.endswith(".csv"):
    print("Not a CSV file")
    sys.exit(1)
try:
    # with open("sicilian.csv", newline="") as csvfile:
    with open(file, newline="") as csvfile:
        reader = csv.reader(csvfile)
        print(tabulate(reader, headers="firstrow", tablefmt="grid"))
except FileNotFoundError:
    print("File does not exist")
    sys.exit(1)