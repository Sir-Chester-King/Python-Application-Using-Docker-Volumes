import re

import Classes.Users
import Main_Code.main
import Store_Data.Store_Data


# Function to create a new user.
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

    print("\n")
    print("Here the info's defined.")
    print("Name: " + name)
    print("Surname: " + surname)
    print("Address: " + address)
    print("Phone Number: " + phone_number, end="\n\n")
    print("Is everything correct?")
    while True:
        correct = input("Yes or No (y / n): ").lower()
        if correct == "y":
            break

    # Creating a new instance "USER" to pass ad parameter to the proper function to be stored in a file.
    user = Classes.Users.User(name, surname, address, phone_number)

    # Function to store the new user in a file.
    Store_Data.Store_Data.Store_Data_In_A_File(user)
