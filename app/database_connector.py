"""
Module for managing the database connection and table creation.
"""
import sqlite3


class CreateTableManager:
    """
    Manager for creating tables in the database.
    """
    def __init__(self, db_connector):
        self.db_connector = db_connector

    def create_table(self):
        """
        Create the 'contacts' table in the database if it does not exist.
        """
        _, cursor = self.db_connector.connect()
        cursor.execute("CREATE TABLE IF NOT EXISTS contacts "
                       "(id INTEGER PRIMARY KEY,"
                       "name varchar(50) NOT NULL UNIQUE,"
                       "email varchar(50) NOT NULL,"
                       "phone varchar(50) NOT NULL)")


class DatabaseConnector:
    """
    Class for handling the SQLite database connection.
    """
    def __init__(self, db_file):
        self.db_file = db_file
        self.connection = None
        self.cursor = None

    def connect(self):
        """
        Connect to the SQLite database and return the connection and cursor.
        """
        self.connection = sqlite3.connect(self.db_file)
        self.cursor = self.connection.cursor()
        return self.connection, self.cursor

    def close(self):
        """
        Close the SQLite database connection.
        """
        if self.connection:
            self.connection.close()

    def commit(self):
        """
        Commit changes to the SQLite database.
        """
        if self.connection:
            self.connection.commit()


