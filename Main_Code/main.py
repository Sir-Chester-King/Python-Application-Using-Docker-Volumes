# Main function of program.
# The purpose of this application is to create objects "user" and store their info's in a file.
import os

import Create_Users.Create_users
import Modify_Users.Modify_users
import View_Users.View_users


def clean_console():
    # For Windows environment
    if os.name == 'nt':
        os.system('cls')
    # For Linux/Unix environment
    else:
        os.system("clear")


def main():
    clean_console()
    menu_app = {
        "1": "Create new user",
        "2": "View list users",
        "3": "Modify user's info"
    }
    options_available = list(menu_app.keys())

    # Print the menu app.
    print("{:<10} {:<15}".format('Option', 'Action'))
    for key, value in menu_app.items():
        print("{:<10} {:<15}".format(key, value))
    print("Please, insert only the available value from the menu.")

    # Loop state in case of wrong input option insert
    option_chosen = str(input("Insert option: "))
    while option_chosen not in options_available:
        option_chosen = str(input("Insert option: "))

    clean_console()

    # Call the property function based on the user's chosen option.
    match option_chosen:
        case "1":
            Create_Users.Create_users.new_user()
        case "2":
            View_Users.View_users.list_users()
        case "3":
            Modify_Users.Modify_users.modify_user()
        case _:
            return 0


# Using the special variable __name__
if __name__ == "__main__":
    main()
