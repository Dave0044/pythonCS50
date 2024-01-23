def main():
    x = input("camelCase: ")
    x = snake(x)
    print(f"Snake case: {x}")

def snake(n):
    res = ""
    for i in n:
        if i.isupper():
            res += "_" + i
        else:
            res += i
    return res.lower()

if __name__ == "__main__":
    main()
