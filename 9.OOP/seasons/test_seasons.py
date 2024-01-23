from seasons import check_birthday

def main():
    test_check_birthday()

def test_check_birthday():
    assert check_birthday("1994-04-04") == ("1994", "04", "04")
    assert check_birthday("1994-4-4") == None
    assert check_birthday("April 4, 1994") == None


if __name__ == "__main__":
    main()
