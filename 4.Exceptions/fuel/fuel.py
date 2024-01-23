while True:
    try:
        expression = input("Fraction: ")
        z= expression.split("/")
        x = int(z[0])
        y = int(z[1])
        porcent = round(x / y * 100)
        if x > y:
            continue
        elif porcent <= 1:
            print("E")
        elif porcent >= 99:
            print("F")
        else:
            print(f"{porcent}%")
    except (ValueError, ZeroDivisionError):
        pass
    else:
        break







"""
def get_int():
    while True:
        try:
            x = int(input("What is x? "))
        except ValueError:
            print("x is not a integer")
        else:
            break
    return x

def main():
    x = get_int()
    print(f"x is {x}")

main()
"""
