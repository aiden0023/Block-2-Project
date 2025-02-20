
def password_strength_checker(password):
    has_digit = False
    has_lowercase = False
    has_uppercase = False
    has_special = False

    # Checks if length of password is less than 8
    if len(password) < 8:
        return "Weak"

    for char in password:
        if char.isdigit():
            has_digit = True
        if char.islower():
            has_lowercase = True
        if char.isupper():
            has_uppercase = True
        if not char.isalnum():
            has_special = True

    if has_digit and has_lowercase and has_uppercase and has_special:
        return "Strong"
    elif has_digit and not has_lowercase and not has_uppercase and not has_special:
        return "Weak"
    elif not has_digit and has_lowercase and not has_uppercase and not has_special:
        return "Weak"
    elif not has_digit and has_uppercase and not has_lowercase and not has_special:
        return "Weak"
    elif not has_digit and not has_lowercase and not has_uppercase and has_special:
        return "Weak"
    else:
        return "Strong"


def signup():
    while True:
        username = input("Please define your username: ")
        if len(username) < 3:
            print("Username must be at least 3 characters.")
        elif " " in username:
            print("Username cannot have any spaces in it.")
        else:
            break

    while True:
        password = input("Please define your password: ")
        if len(password) < 6:
            print("Password must be at least 6 characters.")
        elif " " in password:
            print("Password cannot have any spaces in it.")
        else:
            break

    print("Your password strength is: " + password_strength_checker(password))

    # save account info logic

    print("Your account has been created! Please terminate the program to sign out and try logging in with your new "
          "account.")


def login():
    print("Welcome!")
    # login logic


if __name__ == '__main__':
    while True:
        choice = input("Welcome! Please type 1 to login, or type 2 to sign up: ")
        if choice == "1":
            login()
            break
        elif choice == "2":
            signup()
            break
        else:
            print("Invalid input. Please try again.")

