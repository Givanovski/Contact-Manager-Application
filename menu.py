import sqlite3


def display_menu():
    print("\nCLI Menu for collecting information.")
    print("Options:")
    print("1. Add Contact")
    print("2. Update Contact")
    print("3. View Contacts")
    print("4. Delete Contact")
    print("5. Exit")


def handle_menu_choice(choice, operations_manager, db_connector):
    if choice == '1':
        add_contact(operations_manager)
    elif choice == '2':
        update_contact(operations_manager, db_connector)
    elif choice == '3':
        view_contacts(operations_manager)
    elif choice == '4':
        delete_contact_by_name(operations_manager)
    elif choice == '5':
        print("Exiting the program.")
        return False
    else:
        print("Invalid choice. Please enter 1, 2, 3, 4 or 5.")
    return True


def add_contact(operations_manager):
    name = input("Please enter your\nname: ").lower()
    email = input("email: ")
    phone = input("phone: ")
    if not name or not email or not phone:
        print("Invalid input. Please provide values for all three parameters.")
        return
    operations_manager.add_contact_to_db(name, email, phone)


def update_contact(operations_manager, db_connector):
    name = input("Please enter the name of the contact you want to update: ").lower()
    if not name:
        print("Invalid name. Please provide a valid name.")
        return
    try:
        _, cursor = db_connector.connect()
        cursor.execute("SELECT * FROM contacts WHERE name = ?", (name,))
        result = cursor.fetchone()
        if result:
            print("Contact found. What do you want to update?")
            print("1. Email")
            print("2. Phone")
            print("3. Cancel")
            choice = input("Enter your choice (1/2/3): ")
            if choice == "1":
                new_email = input("Enter new email: ")
                operations_manager.update_contact_in_db(name, "email", new_email)
            elif choice == "2":
                new_phone = input("Enter new phone: ")
                operations_manager.update_contact_in_db(name, "phone", new_phone)
            elif choice == "3":
                print("Operation canceled.")
                return
            else:
                print("Invalid choice. Please enter 1, 2, or 3")
                return
        else:
            print("Contact not found. Add the contact first.")
    except sqlite3.Error as e:
        print(f"Error updating contact: {e}")
    finally:
        db_connector.close()


def view_contacts(operations_manager):
    print("Choose an option to view contacts?")
    print("1. View all contacts")
    print("2. Search for a contact by name")
    choice = input("Enter your choice (1/2): ")
    if choice == "1":
        operations_manager.view_all_contacts()
    elif choice == "2":
        operations_manager.view_contact_by_name()
    else:
        print("Invalid choice. Please enter 1 or 2.")


def delete_contact_by_name(operations_manager):
    name = input("Please enter the name of the contact you want to delete: ").lower()
    operations_manager.delete_contact_from_db(name)
