from validator_collection import validators, checkers

def main():
    email_address = input("Enter an email address: ")
    if is_valid_email(email_address):
        print("Valid")
    else:
        print("Invalid")

def is_valid_email(email):
    # Using the is_email function from the validators library
    return checkers.is_email(email)

if __name__ == "__main__":
    main()
