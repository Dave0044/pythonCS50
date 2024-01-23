def convert(fraction):
    try:
        x, y = map(int, fraction.split('/'))
        if x > y or y == 0:
            raise ValueError("Invalid fraction: X must be less than or equal to Y, and Y must not be 0.")
        return round(x / y * 100)
    except (ValueError, ZeroDivisionError):
        raise ValueError("Invalid fraction format: Use X/Y where X and Y are integers.")

def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"

def main():
    while True:
        try:
            expression = input("Fraction: ")
            percentage = convert(expression)
            result = gauge(percentage)
            print(result)
        except ValueError as ve:
            print(ve)
            continue
        else:
            break

if __name__ == "__main__":
    main()
