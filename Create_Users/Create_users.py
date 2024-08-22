import re

import Classes.Users
import Main_Code.main


def new_user():
    Main_Code.main.clean_console()
    print("Define here the new user.", end="\n")
    name = str(input("Name: "))
    surname = str(input("Surname: "))
    address = str(input("Address: "))
    while True:
        phone_number = str(input("Phone number: "))
        if re.match(r"^[-+]?\d{2,15}$", phone_number):  # This pattern is used to validate the phone number.
            break

    Main_Code.main.clean_console()

    print("Here the info's defined.", end="\n")

    print("Name: " + name)
    print("Surname: " + surname)
    print("Address: " + address)
    print("Phone Number: " + phone_number, end="\n")

    print("Is everything correct?")

    while True:
        correct = input("Yes or No (y / n): ").lower()
        if correct == "y":
            break

    user = Classes.Users.User(name, surname, address, phone_number)
