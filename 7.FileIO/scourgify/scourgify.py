import sys
import csv

if len(sys.argv) == 3:
    if not (sys.argv[1][-4:] == ".csv" and sys.argv[2][-4:] == ".csv"):
        sys.exit("Not a csv file")
    try:
        with open(sys.argv[1]) as file:
            reader = csv.DictReader(file)

            with open(sys.argv[2], "w") as file1:
                writer = csv.DictWriter(file1, fieldnames=["first", "last", "house"])
                writer.writeheader()
                for row in reader:
                    row["first"] = row.pop("name")
                    last_name, first_name = row["first"].split(", ")
                    row["first"] = first_name
                    row["last"] = last_name
                    writer.writerow(row)

    except FileNotFoundError:
        sys.exit("File does not exist")

elif len(sys.argv) <3:
    sys.exit("Too few command-line arguments ")

else:
    sys.exit("Too many command-line arguments")

