import random
import sys

def nump():
    while True:
        try:
            x = int(input("Level: "))
            if x > 0:
                break
        except ValueError:
            continue
    return x

def rd():
    while True:
        try:
            z = int(input("Guess: "))
            if z > 0:
                break
        except ValueError:
            continue
    return z

def main():
    x = nump()
    y = random.randint(1, x)
    while True:
        z = rd()
        if z < y:
            print("Too small!")
            continue
        elif z > y:
            print("Too large!")
            continue
        else:
            print("Just right!")
            sys.exit()

main()
