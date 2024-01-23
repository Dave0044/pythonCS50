def main():
    x = input("Greeting: ")
    x = x.lower().strip()
    x = value(x)
    print(f"Output: {x}")

def value(greeting):
    if greeting.startswith("hello"):
        return 0
    elif greeting.startswith("h") and not greeting.startswith("hello"):
        return 20
    else:
        return 100

if __name__ == "__main__":
    main()
