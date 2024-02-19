import sqlite3

DB_FILE = "contacts.db"
contacts = []


def create_table():
    db = sqlite3.connect(DB_FILE)
    cursor = db.cursor()

    cursor.execute("CREATE TABLE IF NOT EXISTS contacts "
                   "(id INTEGER PRIMARY KEY,"
                   "name varchar(50) NOT NULL UNIQUE,"
                   "email varchar(50) NOT NULL,"
                   "phone varchar(50) NOT NULL)")

    db.commit()
    db.close()


def add_contact():
    name = input("Please enter your\nname: ").lower()
    email = input("email: ")
    phone = input("phone: ")

    if not name or not email or not phone:
        print("Invalid input. Please provide values for all three parameters.")
        return

    new_contact = {
        "name": name,
        "email": email,
        "phone": phone
    }
    contacts.append(new_contact)
    print("Contact added:", new_contact)


def update_contact():
    name = input("Please enter the name of the contact you want to update: ").lower()
    if not name:
        print("Invalid name. Please provide a valid name.")
        return

    contact_found = False

    for contact in contacts:
        if contact["name"] == name:
            contact_found = True
            print("Contact found. What do you want to update?")
            print("1. Email")
            print("2. Phone")
            print("3. Cancel")

            choice = input("Enter your choice (1/2/3): ")

            if choice == "1":
                new_email = input("Enter new email: ")
                contact["email"] = new_email
                print("Email updated successfully.")

            elif choice == "2":
                new_phone = input("Enter new phone: ")
                contact["phone"] = new_phone
                print("Phone updated successfully.")

            elif choice == "3":
                print("Operation canceled.")
                return
            else:
                print("Invalid choice. Please enter 1, 2, or 3")
                return

    if not contact_found:
        print("Contact not found. Add the contact first.")


def print_contact_details(contact):
    print(f"Name: {contact['name']}")
    print(f"Email: {contact['email']}")
    print(f"Phone: {contact['phone']}")
    print()


def view_all_contacts():
    if not contacts:
        print("No contacts available.")
    else:
        for contact in contacts:
            print_contact_details(contact)


def view_contact_by_name():
    name = input("Please enter the name of the contact you want to view: ").lower()
    contact_found = False

    for contact in contacts:
        if contact["name"] == name:
            print_contact_details(contact)
            contact_found = True
            break
    if not contact_found:
        print("Contact not found.")


def view_contacts():
    print("Choose an option to view contacts?")
    print("1. View all contacts")
    print("2. Search for a contact by name")
    choice = input("Enter your choice (1/2): ")

    if choice == "1":
        view_all_contacts()
    elif choice == "2":
        view_contact_by_name()
    else:
        print("Invalid choice. Please enter 1 or 2.")


def delete_contact_by_name():
    if not contacts:
        print("No contacts available.")
    else:
        name = input("Please enter the name of the contact you want to delete: ").lower()
        for contact in contacts:
            if contact["name"] == name:
                contacts.remove(contact)
                print(f"Contact '{name}' deleted successfully.")
                return
        print(f"Contact '{name}' not found")


def display_menu():
    print("\nCLI Menu for collecting information.")
    print("Options:")
    print("1. Add Contact")
    print("2. Update Contact")
    print("3. View Contacts")
    print("4. Delete Contact")
    print("5. Exit")


while True:
    display_menu()
    choice = input("Enter your choice (1/2/3/4/5): ")

    if choice == '1':
        add_contact()
        print(contacts)

    elif choice == '2':
        update_contact()
        print(contacts)

    elif choice == '3':
        view_contacts()

    elif choice == '4':
        delete_contact_by_name()
        print(contacts)

    elif choice == '5':
        print("Exiting the program.")
        break

    else:
        print("Invalid choice. Please enter 1, 2, 3, 4 or 5.")
