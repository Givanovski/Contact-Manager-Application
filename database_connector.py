import sqlite3


class DatabaseConnector:
    def __init__(self, db_file):
        self.db_file = db_file
        self.connection = None
        self.cursor = None

    def connect(self):
        self.connection = sqlite3.connect(self.db_file)
        self.cursor = self.connection.cursor()
        return self.connection, self.cursor

    def close(self):
        if self.connection:
            self.connection.close()

    def commit(self):
        if self.connection:
            self.connection.commit()
