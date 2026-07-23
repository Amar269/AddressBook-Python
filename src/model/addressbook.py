class AddressBook:

    def __init__(self):
        self.contact = None

    def add_contact(self, person):
        self.contact = person

    def display_contact(self):
        if self.contact:
            self.contact.display()
        else:
            print("No Contact Found.")

def edit_contact(self, first_name):

    if self.contact is None:
        print("No Contact Found.")
        return

    if self.contact.first_name == first_name:

        self.contact.last_name = input("Enter New Last Name: ")
        self.contact.address = input("Enter New Address: ")
        self.contact.city = input("Enter New City: ")
        self.contact.state = input("Enter New State: ")
        self.contact.zip_code = input("Enter New Zip Code: ")
        self.contact.phone = input("Enter New Phone: ")
        self.contact.email = input("Enter New Email: ")

        print("\nContact Updated Successfully!")
        return

    print("Contact Not Found.")

def delete_contact(self, first_name):

    if self.contact is None:
        print("No Contact Found.")
        return

    if self.contact.first_name == first_name:
        self.contact = None
        print("\nContact Deleted Successfully!")
        return

    print("Contact Not Found.")
