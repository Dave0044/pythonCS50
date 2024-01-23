def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if len(s) < 2 or len(s) > 6:
        return False

    if not s.isalnum():
        return False

    if not s[:2].isalpha():
        return False

    letter = False
    for i in s[::-1]:
        if i.isalpha():
            letter = True
        elif letter and i.isdigit():
            return False

    first_number = None
    for i in s:
        if i.isdigit():
            if first_number is None:
                first_number = int(i)
            if first_number == 0:
                return False

    return True


if __name__ == "__main__":
    main()
