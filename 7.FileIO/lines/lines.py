import sys

if len(sys.argv) == 2:
    if not ".py" in sys.argv[1]:
        sys.exit("Not a Python file")
    try:
        nlines = 0
        with open(sys.argv[1]) as file:
            for i in file:
                i = i.lstrip()
                if i.startswith("#") or i == "":
                    nlines = nlines
                else:
                    nlines += 1
            print(nlines)
    except FileNotFoundError:
        sys.exit("File does not exist")

elif len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")

else:
    sys.exit("Too many command-line arguments")
