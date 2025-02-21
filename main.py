import json
import hashlib
import os
import requests

HOME_DIR = os.path.expanduser("~")
SECRET_FILE = os.path.join(HOME_DIR, ".account.json")


def password_strength_checker(password):
    has_digit = False
    has_lowercase = False
    has_uppercase = False
    has_special = False

    # Checks if length of password is less than 8
    if len(password) < 8:
        return "Weak"

    # Loop through all characters in the password to check for types of characters
    for char in password:
        if char.isdigit():
            has_digit = True
        if char.islower():
            has_lowercase = True
        if char.isupper():
            has_uppercase = True
        if not char.isalnum():
            has_special = True

    # Check the strength of the password
    if is_password_pwned(password):
        print("[WARNING] This password has been found to be in a data breach!")
        return "Weak"
    elif has_digit and has_lowercase and has_uppercase and has_special:
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
        return "Moderate"


def is_password_pwned(password):
    sha1_password = hashlib.sha1(password.encode()).hexdigest().upper()

    # Gets first 5 characters
    password_prefix = sha1_password[:5]

    # Gets last 5 characters
    password_suffix = sha1_password[5:]

    # HIBP API calls
    url = f"https://api.pwnedpasswords.com/range/{password_prefix}"
    response = requests.get(url)

    return password_suffix in response.text


def signup():
    accounts = load_accounts()

    # Define username
    while True:
        username = input("Please define your username: ")
        if len(username) < 3:
            print("Username must be at least 3 characters.")
        elif " " in username:
            print("Username cannot have any spaces in it.")
        elif username in accounts:
            print("Username is already taken.")
        else:
            break

    # Define password
    while True:
        password = input("Please define your password: ")
        if len(password) < 6:
            print("Password must be at least 6 characters.")
        elif " " in password:
            print("Password cannot have any spaces in it.")
        else:
            break

    print("Your password strength is: " + password_strength_checker(password))

    # Hash the password
    hashed_password = hashlib.sha256(password.encode()).hexdigest()

    # Put account info into json
    account = {
        username: {
            "password": hashed_password
        }
    }

    # Save the account information to a file locally
    save_account(account)

    print("Your account has been created! Please terminate the program to sign out and try logging in with your new "
          "account.")


def login():
    print("Welcome!")

    accounts = load_accounts()

    # Check to make sure there are accounts that exist
    if not accounts:
        print("No accounts found. Please sign up first.")

    # Inputting login
    while True:
        username = input("Please input your username: ")
        password = input("Please input your password: ")

        if username not in accounts:
            print("Username not found. Please try again.")
        elif accounts[username]["password"] != hashlib.sha256(password.encode()).hexdigest():
            print("Password incorrect. Please try again.")
        else:
            print("Welcome " + username + "! You are now logged in. Please terminate the program to sign out.")
            break


def load_accounts():
    # Checks to make sure file exists
    if not os.path.exists(SECRET_FILE):
        return {}

    with open(SECRET_FILE, "r") as file:
        return json.load(file)


def save_account(account):
    with open(SECRET_FILE, "w") as file:
        json.dump(account, file, indent=4)


def debugging_checks():
    # Check if secrets file exists
    if not os.path.exists(SECRET_FILE):
        print("[WARNING] Account file is missing.")
    else:
        print("No warnings found.")


if __name__ == '__main__':
    while True:
        choice = input("Welcome! Please type 1 to login, type 2 to sign up, or 3 to run debugging checks: ")
        if choice == "1":
            login()
            break
        elif choice == "2":
            signup()
            break
        elif choice == "3":
            debugging_checks()
        else:
            print("Invalid input. Please try again.")
