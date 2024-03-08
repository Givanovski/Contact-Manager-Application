"""
Module defining the Flask Blueprint for handling contact-related routes.
"""
from flask import Blueprint, request, jsonify
from app.models import Contact
from app.db_setup import db_connector

contacts_bp = Blueprint("contacts", __name__)


@contacts_bp.route("/", methods=["GET"])
def get_all_contacts():
    """
    Get all contacts from the database.
    Returns:
    JSON response containing the list of contacts.
    """
    _, cursor = db_connector.connect()
    cursor.execute("SELECT * FROM contacts")
    result = cursor.fetchall()
    if not result:
        return jsonify(response={"Error": "No contacts available"}), 404

    contacts = []
    for row in result:
        contact = Contact(id=row[0], name=row[1], email=row[2], phone=row[3])
        contacts.append(contact.to_dict())
    return jsonify(contacts=contacts), 200


@contacts_bp.route("/contacts/<int:contact_id>", methods=["GET"])
def get_contact_by_id(contact_id):
    """
    Retrieve a contact by its ID.

    Parameters:
    - contact_id (int): The ID of the contact to retrieve.

    Returns:
    - JSON response with contact details if found.
    - JSON response with an error message and status code 404 if the contact is not found.
    """
    _, cursor = db_connector.connect()
    cursor.execute("SELECT * FROM contacts WHERE id = ?", (contact_id,))
    contact_data = cursor.fetchone()
    if not contact_data:
        return jsonify(response={"Error": "contact not found"}), 404
    contact = Contact(*contact_data)
    return jsonify(contact=contact.to_dict()), 200


@contacts_bp.route("/search", methods=["GET"])
def search_contact_by_name():
    """
    Search for a contact by name.

    Parameters:
    - name (str): The name of the contact to search for.

    Returns:
    - JSON response with contact details if found.
    - JSON response with an error message and status code 400 if the name parameter is missing.
    - JSON response with an error message and status code 404 if the contact is not found.
    """
    query_name = request.args.get("name")
    if not query_name:
        return jsonify(response={"Error": "Name parameter is missing"}), 400
    _, cursor = db_connector.connect()
    cursor.execute("SELECT * FROM contacts WHERE name = ?", (query_name,))
    contact_data = cursor.fetchone()
    if not contact_data:
        return jsonify(response={"Error": "contact not found"}), 404
    contact = Contact(*contact_data)
    return jsonify(contact=contact.to_dict()), 200


@contacts_bp.route("/add", methods=["GET", "POST"])
def add_new_contact():
    """
    Add a new contact.

    Parameters:
    - name (str): The name of the new contact.
    - email (str): The email of the new contact.
    - phone (str): The phone number of the new contact.

    Returns:
    - JSON response with success message and status code 201 if the contact is added successfully.
    - JSON response with an error message and status code 400 if missing required fields.
    - JSON response with an error message and status code 409 if a contact with the same name already exists.
    """
    name = request.form.get("name")
    email = request.form.get("email")
    phone = request.form.get("phone")
    if not name or not email or not phone:
        return jsonify(response={"error": "Missing required fields"}), 400
    _, cursor = db_connector.connect()
    cursor.execute("SELECT * FROM contacts WHERE name = ?", (name,))
    existing_contact = cursor.fetchone()
    if existing_contact:
        return jsonify(response={"error": "Contact with the same name already exists"}), 409
    cursor.execute("INSERT INTO contacts (name, email, phone) VALUES (?, ?, ?)",
                   (name, email, phone))
    db_connector.commit()
    db_connector.close()
    return jsonify(response={"Success": "Contact added successfully"}), 201


@contacts_bp.route("/update-phone/<string:contact_name>", methods=["GET", "PATCH"])
def update_phone(contact_name):
    """
    Update the phone number of a contact.

    Parameters:
    - contact_name (str): The name of the contact to update.
    - phone (str): The new phone number.

    Returns:
    - JSON response with success message and status code 200 if the contact is updated successfully.
    - JSON response with an error message and status code 400 if the phone parameter is missing.
    - JSON response with an error message and status code 404 if the contact is not found.
    """
    new_phone = request.args.get("phone")
    if not new_phone:
        return jsonify(response={"error": "Phone parameter must be provided for update"}), 400
    _, cursor = db_connector.connect()
    cursor.execute("SELECT * FROM contacts WHERE name = ?", (contact_name,))
    existing_contact = cursor.fetchone()
    if not existing_contact:
        return jsonify(response={"error": f"Contact '{contact_name}' not found"}), 404
    cursor.execute("UPDATE contacts SET phone = ? WHERE name= ?", (new_phone, contact_name))
    db_connector.commit()
    db_connector.close()
    return jsonify(response={"Success": f"Contact {contact_name} updated successfully."}), 200


@contacts_bp.route("/delete/<string:contact_name>", methods=["GET", "DELETE"])
def delete_contact(contact_name):
    """
    Delete a contact by name.

    Parameters:
    - contact_name (str): The name of the contact to delete.

    Returns:
    - JSON response with success message and status code 200 if the contact is deleted successfully.
    - JSON response with an error message and status code 404 if the contact is not found.
    """
    _, cursor = db_connector.connect()
    cursor.execute("SELECT * FROM contacts WHERE name = ?", (contact_name,))
    existing_contact = cursor.fetchone()

    if not existing_contact:
        return jsonify(response={"Error": f"Contact '{contact_name}' not found."}), 404
    cursor.execute("DELETE FROM contacts WHERE name = ?", (contact_name,))
    db_connector.commit()
    db_connector.close()
    return jsonify(response={"Success": f"Contact '{contact_name}' deleted successfully."}), 200



