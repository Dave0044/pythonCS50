"""
x = input("Input: ")
char = ""
for i in x:
    if i.lower() in "aeiou":
        char = char.replace(i, "")
    else:
        char = char + i
print(f"Output: {char}")
"""

def main():
    x = input("Input: ")
    x = print(f"Output: {cons(x)}")

def cons(n):
    char = ""
    for i in n:
        if i.lower() in "aeiou":
            continue
        else:
            char += i
    return char

main()