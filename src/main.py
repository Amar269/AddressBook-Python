from model.person import Person
from model.addressbook import AddressBook


print(" Welcome to Address Book ._. 📖 ")


first_name = input("Enter First Name : ")
last_name = input("Enter Last Name  : ")
address = input("Enter Address    : ")
city = input("Enter City       : ")
state = input("Enter State      : ")
zip_code = input("Enter Zip Code   : ")
phone = input("Enter Phone      : ")
email = input("Enter Email      : ")

person1 = Person(
    first_name,
    last_name,
    address,
    city,
    state,
    zip_code,
    phone,
    email
)

address_book = AddressBook()

address_book.add_contact(person1)

print("\nContact Added Successfully!\n")

address_book.display_contact()

choice = input("\nDo you want to edit the contact? (yes/no): ")

if choice.lower() == "yes":
    first_name = input("Enter First Name of the Contact to Edit: ")
    address_book.edit_contact(first_name)

    print("\nUpdated Contact Details:\n")
    address_book.display_contact()


choice = input("\nDo you want to delete the contact? (yes/no): ")

if choice.lower() == "yes":
    first_name = input("Enter First Name of the Contact to Delete: ")

    address_book.delete_contact(first_name)

    print("\nCurrent Address Book:\n")
    address_book.display_contact()
