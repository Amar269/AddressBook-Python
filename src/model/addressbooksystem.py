from model.addressbook import AddressBook

class AddressBookSystem:

    def __init__(self):
        self.address_books = {}

    def create_address_book(self, name):

        if name in self.address_books:
            print("Address Book already exists.")
            return

        self.address_books[name] = AddressBook()

        print(f"Address Book '{name}' created successfully.")

    def get_address_book(self, name):

        if name in self.address_books:
            return self.address_books[name]

        print("Address Book not found.")
        return None

    def display_address_books(self):

        if len(self.address_books) == 0:
            print("No Address Books Found.")
            return

        print("\nAvailable Address Books:")

        for name in self.address_books:
            print(name)