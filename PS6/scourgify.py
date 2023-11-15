import sys
import csv
from tabulate import tabulate

if len(sys.argv) < 3:
    print("Too few command-line arguments")
    sys.exit(1)
if len(sys.argv) > 4:
    print("Too many command-line arguments")
    sys.exit(1)
inputfile = sys.argv[1]
outputfile = sys.argv[2]
try:
    with open(inputfile, newline="") as csvfile:
        reader = csv.DictReader(csvfile)
        with open(outputfile, "w") as outfile:
            writer = csv.DictWriter(outfile, fieldnames=["first", "last", "house"])
        #   just writes the header
            writer.writeheader()
            for line in reader:
                last, first = line["name"].split(", ")
                row = {"first": first, "last": last, "house": line["house"]}
                writer.writerow(row)
except FileNotFoundError:
    print("File does not exist")
    sys.exit(1)