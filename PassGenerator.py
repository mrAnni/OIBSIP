import random

lowercase_letters = "abcdefghijklmnopqrstuvwxyz"
uppercase_letters = lowercase_letters.upper()
digits = "0123456789"
symbols = "!@#$%^&*()"

character_sets = {
    "lowercase": lowercase_letters,
    "uppercase": uppercase_letters,
    "digits": digits,
    "symbols": symbols,
}


def generate_password(length=12, include_uppercase=True, include_digits=True, include_symbols=True):

    # Validate user input
    if length < 1:
        raise ValueError("Password length must be at least 1 character.")

    all_chars = ""
    if include_uppercase:
        all_chars += character_sets["uppercase"]
    if include_digits:
        all_chars += character_sets["digits"]
    if include_symbols:
        all_chars += character_sets["symbols"]
    all_chars += lowercase_letters

    if not all_chars:
        raise ValueError("At least one character set must be included.")

    # Generate random password
    password = "".join(random.sample(all_chars, length))
    return password


def main():

    while True:
        try:
            length = int(input("Enter desired password length (minimum 1): "))
            if length < 1:
                raise ValueError

            include_uppercase = input("Include uppercase letters (y/n)? ").lower() == "y"
            include_digits = input("Include digits (y/n)? ").lower() == "y"
            include_symbols = input("Include symbols (y/n)? ").lower() == "y"

            password = generate_password(length, include_uppercase, include_digits, include_symbols)
            print(f"Your random password is: {password}")
            break

        except ValueError:
            print("Invalid input. Please enter a positive integer for password length.")


if __name__ == "__main__":
    main()
