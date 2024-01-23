def main():
    x = input("Input: ")
    result = shorten(x)
    print(f"Output: {result}")
    return result

def shorten(word):
    char = ""
    for i in word:
        if i in "aeiou":
            continue
        else:
            char += i
    return char

if __name__ == "__main__":
    main()
