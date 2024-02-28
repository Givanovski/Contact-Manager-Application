import sqlite3


class ContactOperationsManager:

    def __init__(self, db_connector):
        self.db_connector = db_connector

    def create_table(self):
        def operation():
            _, cursor = self.db_connector.connect()
            cursor.execute("CREATE TABLE IF NOT EXISTS contacts "
                           "(id INTEGER PRIMARY KEY,"
                           "name varchar(50) NOT NULL UNIQUE,"
                           "email varchar(50) NOT NULL,"
                           "phone varchar(50) NOT NULL)")

        self.handle_exception(operation)

    def handle_exception(self, operation):
        try:
            operation()
            self.db_connector.commit()
        except sqlite3.Error as e:
            print(f"Error: {e}")
        finally:
            self.db_connector.close()

    def add_contact_to_db(self, name, email, phone):
        def operation():
            _, cursor = self.db_connector.connect()
            cursor.execute("INSERT INTO contacts (name, email, phone) VALUES (?, ?, ?)",
                           (name, email, phone))
            print("Contact added successfully.")

        self.handle_exception(operation)

    def update_contact_in_db(self, name, field, new_value):
        def operation():
            _, cursor = self.db_connector.connect()
            cursor.execute(f"UPDATE contacts SET {field} = ? WHERE name = ?", (new_value, name))
            print(f"{field.capitalize()} update successfully.")

        self.handle_exception(operation)

    @staticmethod
    def print_contact_details(contact):
        print(f"Name: {contact['name']}")
        print(f"Email: {contact['email']}")
        print(f"Phone: {contact['phone']}")
        print()

    def view_all_contacts(self):
        def operation():
            _, cursor = self.db_connector.connect()
            cursor.execute("SELECT * FROM contacts")
            result = cursor.fetchall()
            if not result:
                print("No contacts available.")
            else:
                for contact in result:
                    self.print_contact_details({"name": contact[1], "email": contact[2], "phone": contact[3]})

        self.handle_exception(operation)

    def view_contact_by_name(self):
        def operation():
            name = input("Please enter the name of the contact you want to view: ").lower()
            _, cursor = self.db_connector.connect()
            cursor.execute("SELECT * FROM contacts WHERE name = ?", (name,))
            contact = cursor.fetchone()

            if contact:
                self.print_contact_details({"name": contact[1], "email": contact[2], "phone": contact[3]})
            else:
                print("Contact not found.")

        self.handle_exception(operation)

    def delete_contact_from_db(self, name):
        def operation():
            _, cursor = self.db_connector.connect()
            cursor.execute("SELECT * FROM contacts WHERE name = ?", (name,))
            existing_contact = cursor.fetchone()

            if existing_contact:
                cursor.execute("DELETE FROM contacts WHERE name = ?", (name,))
                print(f"Contact '{name}' deleted successfully.")
            else:
                print(f"Contact '{name}' not found.")

        self.handle_exception(operation)



