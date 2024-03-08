from app.database_connector import DatabaseConnector, CreateTableManager


DB_FILE = "contacts.db"
db_connector = DatabaseConnector(DB_FILE)


def initialize_database():
    table_creation_manager = CreateTableManager(db_connector)
    table_creation_manager.create_table()
