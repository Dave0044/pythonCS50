"""
print("Amount Due: 50")
y = 50

while y > 0:
    x = int(input("Insert Coin: "))
    if x == 5 or x == 10 or x == 25:
        y = y - x
        if y > 0:
            print(f"Amount Due: {y}")
    else:
        print(f"Amount Due: {y}")
    if y <= 0:
        print(f"Change Owed: {-y}")
"""
def main():
    y = 50
    print(f"Amount Due: {y}")
    y = coke(y)


def coke(y):
    while y > 0:
        i = int(input("Insert Coin: "))
        if i == 5 or i == 10 or i == 25:
            y = y - i
            if y > 0:
                print(f"Amount Due: {y}")
        else:
            print(f"Amount Due: {y}")
        if y <= 0:
            print(f"Change Owed: {-y}")
main()







