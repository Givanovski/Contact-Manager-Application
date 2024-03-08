"""
Initialization file for the Flask application.
"""
from flask import Flask
from app.views import contacts_bp


app = Flask(__name__)
app.register_blueprint(contacts_bp, url_prefix="/")

