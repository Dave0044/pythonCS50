import sys
import csv
from PIL import Image, ImageOps

if len(sys.argv) == 3:
    for i in [1, 2]:
        if not sys.argv[i][-4:].lower() == ".jpg" and not sys.argv[i][-4:].lower() == ".jpeg" and not sys.argv[i][-4:].lower() == ".png":
            sys.exit("Invalid input")
    if sys.argv[1][-4:].lower() != sys.argv[2][-4:].lower():
        sys.exit("Input and output have different extensions")
    try:
        img = Image.open(sys.argv[1])
    except FileNotFoundError:
        sys.exit("File does not exist")

    shirt = Image.open("shirt.png")
    size = shirt.size
    img = ImageOps.fit(img, size)
    img.paste(shirt, shirt)
    img.save(sys.argv[2])

elif len(sys.argv) <3:
    sys.exit("Too few command-line arguments ")

else:
    sys.exit("Too many command-line arguments")

