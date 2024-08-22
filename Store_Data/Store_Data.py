# This function store the personal user's data in a file.
# The path of the file will be inside the project's directory.
from pathlib import Path


def Store_Data_In_A_File(user):
    storage_file = None

    # Creating an PATH object to get the current directory of the script.
    # This module is usable only with Python 3.4+, else you must use the OS module.
    # The ".parent" module, moves up one level in the directory tree, effectively going back one directory
    current_directory = Path(__file__)

    # Going back 2 level directory with the index level "PARENTS"
    # 0 -> 1 level
    # 1 -> 2 level
    storage_path = current_directory.parents[1]
    name_folder_storage = "Storage"
    try:
        print("CIAO")
        storage_file = open(storage_path / name_folder_storage / "Storage.txt", 'a')
        storage_file.write("Name: " + str(user.get_name()) + "\n")
        storage_file.write("Username: " + user.get_name() + "\n")
        storage_file.write("Address: " + user.get_address() + "\n")
        storage_file.write("Phone Number: " + user.get_phone_number() + "\n\n")
        storage_file.close()
    except FileNotFoundError:
        print("The file does not exist.")
    except PermissionError:
        print("You do not have permission to access this file.")
    except IOError:
        print("An I/O error occurred while writing the file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    except:
        storage_file = open(storage_path / name_folder_storage / "Storage.txt", 'w')
        storage_file.write("Name: " + str(user.get_name()) + "\n")
        storage_file.write("Username: " + user.get_name() + "\n")
        storage_file.write("Address: " + user.get_address() + "\n")
        storage_file.write("Phone Number: " + user.get_phone_number() + "\n\n")
        storage_file.close()
    finally:
        storage_file.close()
