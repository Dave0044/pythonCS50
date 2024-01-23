from datetime import date
import sys
import inflect
import re

p=inflect.engine()

def main():
    birthday = input("Date of Birth: ")
    try:
        year, month, day = check_birthday(birthday)
    except:
        sys.exit("Invalid date")

    date_of_birth = date(int(year), int(month), int(day))
    today = date.today()
    diff = today - date_of_birth
    total_min = diff.days * 24 * 60


    letras = p.number_to_words(int(total_min), andword="")
    print(letras.capitalize() + " minutes")

def check_birthday(birthday):
    if re.search(r"^[0-9]{4}-[0-9]{2}-[0-9]{2}$", birthday):
        year, month, day = birthday.split("-")
        return year, month, day



if __name__ == "__main__":
    main()
