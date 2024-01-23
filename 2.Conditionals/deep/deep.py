def deep(n):
    n = n.lower().replace(" ", "")

    if n == "42":
        print("Yes")

    elif n == "forty-two" or n == "fortytwo":
        print("Yes")

    else:
        print("No")

def main():
    x = input("What is de answer  to the Great Question of Life, the Universe and? ")
    x = deep(x)

main()
