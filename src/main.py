from model.person import Person
from model.addressbooksystem import AddressBookSystem

print("      Welcome to Address Book ._. 📖")
system = AddressBookSystem()

book_name = input("Enter Address Book Name : ")

system.create_address_book(book_name)

address_book = system.get_address_book(book_name)

while True:
    print("          ADDRESS BOOK MENU")
    print("-------------------------------------")
    print("1. Add Contact")
    print("2. Display Contacts")
    print("3. Edit Contact")
    print("4. Delete Contact")
    print("5. Search By City")
    print("6. Search By State")
    print("7. View Contacts By City")
    print("8. View Contacts By State")
    print("9. Exit")
    print("______________________________________")

    try:

        choice = int(input("Enter Your Choice : "))

        if choice == 1:

            first_name = input("Enter First Name : ")
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

        elif choice == 2:

            print("\nContact List")
            address_book.display_contact()

        elif choice == 3:

            first_name = input("Enter First Name to Edit : ")
            address_book.edit_contact(first_name)

        elif choice == 4:

            first_name = input("Enter First Name to Delete : ")
            address_book.delete_contact(first_name)

        elif choice == 5:

            city = input("Enter City : ")
            print("\nContacts Found")
            address_book.search_by_city(city)

        elif choice == 6:

            state = input("Enter State : ")
            print("\nContacts Found")
            address_book.search_by_state(state)

        elif choice == 7:

            print("\nContacts Grouped By City")
            address_book.view_by_city()

        elif choice == 8:

            print("\nContacts Grouped By State")
            address_book.view_by_state()

        elif choice == 9:

            print("\nThank You for Using Address Book 📖")
            break

        else:

            print("Invalid Choice. Please Try Again.")

    except ValueError:

        print("Invalid Input. Please Enter Numbers Only.")