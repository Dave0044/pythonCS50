def main():
    x = input("Greeting: ")
    x = x.lower().strip()
    x = bank(x)


def bank(n):
    if n.startswith("hello"):
        print("$0")
    elif n.startswith("h") and not n.startswith("hello"):
        print("$20")
    else:
        print("$100")

main()
