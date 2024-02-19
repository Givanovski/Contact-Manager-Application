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


def add_contact_to_db(name, email, phone):
    try:
        db = sqlite3.connect(DB_FILE)
        cursor = db.cursor()

        cursor.execute("INSERT INTO contacts (name, email, phone) VALUES (?, ?, ?)",
                       (name, email, phone))
        db.commit()
        print("Contact added successfully.")
    except sqlite3.IntegrityError:
        print("Contact with the same name already exists. Please provide a unique name.")
    finally:
        db.close()


def add_contact():
    name = input("Please enter your\nname: ").lower()
    email = input("email: ")
    phone = input("phone: ")

    if not name or not email or not phone:
        print("Invalid input. Please provide values for all three parameters.")
        return

    add_contact_to_db(name, email, phone)


def update_contact_in_db(name, field, new_value):
    try:
        db = sqlite3.connect(DB_FILE)
        cursor = db.cursor()

        cursor.execute(f"UPDATE contacts SET {field} = ? WHERE name = ?", (new_value, name))
        db.commit()
        print(f"{field.capitalize()} update successfully.")
    except sqlite3.Error as e:
        print(f"Error updating contact: {e}")

    finally:
        db.close()


def update_contact():
    name = input("Please enter the name of the contact you want to update: ").lower()
    if not name:
        print("Invalid name. Please provide a valid name.")
        return

    try:
        db = sqlite3.connect(DB_FILE)
        cursor = db.cursor()

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
                update_contact_in_db(name, "email", new_email)

            elif choice == "2":
                new_phone = input("Enter new phone: ")
                update_contact_in_db(name, "phone", new_phone)

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
        db.close()


def print_contact_details(contact):
    print(f"Name: {contact['name']}")
    print(f"Email: {contact['email']}")
    print(f"Phone: {contact['phone']}")
    print()


def view_all_contacts():
    try:
        db = sqlite3.connect(DB_FILE)
        cursor = db.cursor()

        cursor.execute("SELECT * FROM contacts")
        result = cursor.fetchall()
        if not result:
            print("No contacts available.")
        else:
            for contact in result:
                print_contact_details({"name": contact[1], "email": contact[2], "phone": contact[3]})
    except sqlite3.Error as e:
        print(f"Error retrieving contacts: {e}")
    finally:
        db.close()


def view_contact_by_name():
    name = input("Please enter the name of the contact you want to view: ").lower()
    try:
        db = sqlite3.connect(DB_FILE)
        cursor = db.cursor()

        cursor.execute("SELECT * FROM contacts WHERE name = ?", (name,))
        contact = cursor.fetchone()

        if contact:
            print_contact_details({"name": contact[1], "email": contact[2], "phone": contact[3]})
        else:
            print("Contact not found.")
    except sqlite3.Error as e:
        print(f"Error retrieving contact: {e}")
    finally:
        db.close()


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


def delete_contact_from_db(name):
    try:
        db = sqlite3.connect(DB_FILE)
        cursor = db.cursor()

        cursor.execute("SELECT * FROM contacts WHERE name = ?", (name,))
        existing_contact = cursor.fetchone()

        if existing_contact:
            cursor.execute("DELETE FROM contacts WHERE name = ?", (name,))
            db.commit()
            print(f"Contact '{name}' deleted successfully.")
        else:
            print(f"Contact '{name}' not found.")
    except sqlite3.Error as e:
        print(f"Error deleting contact: {e}")
    finally:
        db.close()


def delete_contact_by_name():
    name = input("Please enter the name of the contact you want to delete: ").lower()
    delete_contact_from_db(name)


def display_menu():
    print("\nCLI Menu for collecting information.")
    print("Options:")
    print("1. Add Contact")
    print("2. Update Contact")
    print("3. View Contacts")
    print("4. Delete Contact")
    print("5. Exit")


if __name__ == "__main__":
    create_table()

    while True:
        display_menu()
        choice = input("Enter your choice (1/2/3/4/5): ")

        if choice == '1':
            add_contact()

        elif choice == '2':
            update_contact()

        elif choice == '3':
            view_contacts()

        elif choice == '4':
            delete_contact_by_name()

        elif choice == '5':
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please enter 1, 2, 3, 4 or 5.")
