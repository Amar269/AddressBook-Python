from model.person import Person


print(" Welcome to Address Book Program  ._. 📖 ")


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

print("\nContact Added Successfully!\n")

person1.display()
