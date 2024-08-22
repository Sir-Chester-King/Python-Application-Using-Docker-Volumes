# Class for the User objects instances.
# The purpose of ths class is to set and get user's personal info.
class User(object):
    # Declare the constructor function.
    # It's the initialize function called when a new object instance in created
    def __init__(self, name, surname, address, phone_number):
        # Here declared the attributes of the instances
        # The keyword "self" indicate the object instance, the other are the parameters send via function "constructor"
        self.name = name
        self.surname = surname
        self.address = address
        self.phone_number = phone_number

    # Declaring the functions "SET" to manipulate the value of objects.
    def set_name(self, name):
        print("Setting name to this new one: ", name)
        self.name = name

    def set_surname(self, surname):
        print("Setting surname to this new one: ", surname)
        self.surname = surname

    def set_address(self, address):
        print("Setting address to this new one: ", address)
        self.address = address

    def set_phone_number(self, phone_number):
        print("Setting phone_number to this new one: ", phone_number)
        self.phone_number = phone_number

    # Declaring functions "GET" to return the value of tha objects.
    def get_name(self):
        print("Getting name...")
        return self.name

    def get_surname(self):
        print("Getting surname...")
        return self.surname

    def get_address(self):
        print("Getting address...")
        return self.address

    def get_phone_number(self):
        print("Getting phone_number...")
        return self.phone_number
