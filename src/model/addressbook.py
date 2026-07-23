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