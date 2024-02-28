import sqlite3
from contact_operations_manager import ContactOperationsManager
from database_connector import DatabaseConnector
from menu import display_menu, handle_menu_choice


def main():
    DB_FILE = "contacts.db"
    db_connector = DatabaseConnector(DB_FILE)
    operations_manager = ContactOperationsManager(db_connector)
    operations_manager.create_table()

    while True:
        display_menu()
        choice = input("Enter your choice (1/2/3/4/5): ")
        if not handle_menu_choice(choice, operations_manager, db_connector):
            break


if __name__ == "__main__":
    main()
