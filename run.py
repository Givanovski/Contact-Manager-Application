"""
This is the entry point for running the Flask application.
"""
from app import app
from app.db_setup import initialize_database

initialize_database()


if __name__ == '__main__':
    app.run(debug=True)

