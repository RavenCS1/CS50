import sys
from tabulate import tabulate
import csv
def main():
    try:
        if len(sys.argv)<2:
            sys.exit("Too few command-line arguments")
        elif len(sys.argv)>2:
            sys.exit("Too many command-line arguments")
        elif sys.argv[1].find(".csv")==-1:
            sys.exit("Not a CSV file")
        with open(f"{sys.argv[1]}", "r") as table:
            reader=csv.reader(table)
            print(tabulate(reader, headers="firstrow",tablefmt="grid"))
    except FileNotFoundError:
        sys.exit("File does not exist")

main()