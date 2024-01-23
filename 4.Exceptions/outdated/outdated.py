
months = [  "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]
while True:
    try:
        date = input("Date: ")
        if "/" in date:
            date = date.replace(" ", "")
            month, day, year = date.split("/")
            if 0 < int(month) > 12 or 0 < int(day) > 31:
                continue
            print(f"{int(year)}-{int(month):02}-{int(day):02}")
            break
        elif "," in date:
            date = date.strip()
            date = date.replace(",", "")
            month, day, year = date.split(" ")
            if 0 < int(day) > 31:
                continue
            if month not in months:
                continue
            if month in months:
                month = months.index(month) + 1
                print(f"{year}-{int(month):02}-{int(day):02}")
                break
    except ValueError:
        pass
