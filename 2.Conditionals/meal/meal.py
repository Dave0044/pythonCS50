def main():
    x = input("What time is it? ")
    x = convert(x)

    if 7.00 <= x <= 8.00:
        print("breakfast time")
    elif 12.00 <= x <= 13.00:
        print("lunch time")
    elif 18.00 <= x <= 19.00:
        print("dinner time")


def convert(time):
    hours, minutes = time.split(":")
    hours = int(hours)
    minutes = int(minutes)
    time = hours + minutes/60
    return float(time)



if __name__ == "__main__":
    main()
