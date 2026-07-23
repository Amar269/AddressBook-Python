class Person:

    def __init__(self, first_name, last_name, address, city, state, zip_code, phone, email):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.city = city
        self.state = state
        self.zip_code = zip_code
        self.phone = phone
        self.email = email

    def display(self):
        print("First Name :", self.first_name)
        print("Last Name  :", self.last_name)
        print("Address    :", self.address)
        print("City       :", self.city)
        print("State      :", self.state)
        print("Zip Code   :", self.zip_code)
        print("Phone      :", self.phone)
        print("Email      :", self.email)