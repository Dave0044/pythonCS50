import sys
import tabulate
import csv

if len(sys.argv) == 2:
    if not ".csv" in sys.argv[1]:
        sys.exit("Not a csv file")

    try:
        with open(sys.argv[1]) as file:
            reader = csv.DictReader(file)
            reader = list(reader)
            print(tabulate.tabulate(reader, headers="keys", tablefmt="grid"))

    except FileNotFoundError:
        sys.exit("File does not exist")

elif len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")

else:
    sys.exit("Too many command-line arguments")
