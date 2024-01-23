def main():
    x = input("camelCase: ")
    x = snake(x)
    print(x)

def snake(n):
    res = ""
    for i in n:
        if i.isupper():
            res = res + "_" + i
        else:
            res = res + i
    return res.lower()

if __name__ == "__main__":
    main()
