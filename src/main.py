from model.person import Person
from model.addressbook import AddressBook

print(" Welcome to Address Book ._. 📖 ")

address_book = AddressBook()

while True:

    first_name = input("\nEnter First Name : ")
    last_name = input("Enter Last Name  : ")
    address = input("Enter Address    : ")
    city = input("Enter City       : ")
    state = input("Enter State      : ")
    zip_code = input("Enter Zip Code   : ")
    phone = input("Enter Phone      : ")
    email = input("Enter Email      : ")

    person = Person(
        first_name,
        last_name,
        address,
        city,
        state,
        zip_code,
        phone,
        email
    )

    address_book.add_contact(person)

    choice = input("\nDo you want to add another contact? (yes/no): ")

    if choice.lower() != "yes":
        break

print("\nAll Contacts:")
address_book.display_contact()

choice = input("\nDo you want to edit a contact? (yes/no): ")

if choice.lower() == "yes":

    first_name = input("Enter First Name to Edit: ")
    address_book.edit_contact(first_name)

    print("\nUpdated Contact List:")
    address_book.display_contact()

choice = input("\nDo you want to delete a contact? (yes/no): ")

if choice.lower() == "yes":

    first_name = input("Enter First Name to Delete: ")
    address_book.delete_contact(first_name)

    print("\nUpdated Contact List:")
    address_book.display_contact()