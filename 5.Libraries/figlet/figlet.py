import sys
from sys import argv
from sys import exit

import random
from random import choice

from pyfiglet import Figlet

object = Figlet()
list = object.getFonts()

if len(sys.argv) == 1:
    object.setFont(font = random.choice(list))
if len(sys.argv) == 3 and (sys.argv[1] == "-f" or sys.argv[1] == "-font") and sys.argv[2] in list:
    object.setFont(font = sys.argv[2])
else:
    sys.exit("Invalid usage")

x = input("Input: ")
print("Output: ", object.renderText(x))
