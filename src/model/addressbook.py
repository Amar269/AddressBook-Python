class AddressBook:

    def __init__(self):
        self.contacts = []

    def add_contact(self, person):
        for contact in self.contacts:
            if (contact.first_name == person.first_name and
                contact.last_name == person.last_name):
                print("Duplicate Contact Found. Contact Not Added.")
            return
        self.contacts.append(person)
    print("\nContact Added Successfully!")
    def display_contact(self):

        if len(self.contacts) == 0:
            print("No Contact Found.")
            return

        print("\n Contact List ")

        for person in self.contacts:
            person.display()
            print("--------------------------")

    def edit_contact(self, first_name):

        if len(self.contacts) == 0:
            print("No Contact Found.")
            return

        for person in self.contacts:

            if person.first_name == first_name:

                person.last_name = input("Enter New Last Name: ")
                person.address = input("Enter New Address: ")
                person.city = input("Enter New City: ")
                person.state = input("Enter New State: ")
                person.zip_code = input("Enter New Zip Code: ")
                person.phone = input("Enter New Phone: ")
                person.email = input("Enter New Email: ")

                print("\nContact Updated Successfully!")
                return

        print("Contact Not Found.")

    def delete_contact(self, first_name):

        if len(self.contacts) == 0:
            print("No Contact Found.")
            return

        for person in self.contacts:

            if person.first_name == first_name:

                self.contacts.remove(person)

                print("\nContact Deleted Successfully!")
                return

        print("Contact Not Found.")