from model.person import Person
from model.addressbook import AddressBook
from model.addressbooksystem import AddressBookSystem

print(" Welcome to Address Book ._. 📖 ")

system = AddressBookSystem()

book_name = input("Enter Address Book Name : ")

system.create_address_book(book_name)

address_book = system.get_address_book(book_name)



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



choice = input("\nDo you want to search contacts by City? (yes/no): ")

if choice.lower() == "yes":

    city = input("Enter City: ")

    print("\nContacts Found:\n")

    address_book.search_by_city(city)



choice = input("\nDo you want to search contacts by State? (yes/no): ")

if choice.lower() == "yes":

    state = input("Enter State: ")

    print("\nContacts Found:\n")

    address_book.search_by_state(state)

choice = input("\nDo you want to view contacts by City? (yes/no): ")

if choice.lower() == "yes":

    print("\nContacts Grouped By City")

    address_book.view_by_city()

choice = input("\nDo you want to view contacts by State? (yes/no): ")

if choice.lower() == "yes":

    print("\nContacts Grouped By State")

    address_book.view_by_state()