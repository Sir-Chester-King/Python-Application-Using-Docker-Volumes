from pathlib import Path

import Main_Code.main


def list_users():
    storage_file = None
    content = None

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
        storage_file = open(storage_path / name_folder_storage / "Storage.txt", 'r')
        content = storage_file.read()
        storage_file.close()
    except FileNotFoundError:
        print("The file does not exist.")
    except PermissionError:
        print("You do not have permission to access this file.")
    except IOError:
        print("An I/O error occurred while writing the file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

    Main_Code.main.clean_console()
    print("Here the data gathered from the file: ", storage_path / name_folder_storage / "Storage.txt", end="\n")
    print("Content: \n")
    print(content)
