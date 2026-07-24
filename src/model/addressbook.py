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

        print("\nContact List")

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

    def search_by_city(self, city):

        found = False

        for person in self.contacts:

            if person.city.lower() == city.lower():

                person.display()
                found = True

        if not found:
            print("No Contact Found.")

    def search_by_state(self, state):

        found = False

        for person in self.contacts:

            if person.state.lower() == state.lower():

                person.display()
                found = True

        if not found:
            print("No Contact Found.")

    def view_by_city(self):

        if len(self.contacts) == 0:
            print("No Contact Found.")
            return

        cities = []

        for person in self.contacts:

            if person.city not in cities:
                cities.append(person.city)

        for city in cities:

            print(f"\nCity : {city}")

            for person in self.contacts:

                if person.city == city:
                    print(f"{person.first_name} {person.last_name}")

    def view_by_state(self):

        if len(self.contacts) == 0:
            print("No Contact Found.")
            return

        states = []

        for person in self.contacts:

            if person.state not in states:
                states.append(person.state)

        for state in states:

            print(f"\nState : {state}")

            for person in self.contacts:

                if person.state == state:
                    print(f"{person.first_name} {person.last_name}")