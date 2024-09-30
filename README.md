# Contact Management API

This project defines a Flask Blueprint for managing contact-related routes, allowing for operations such as retrieving, adding, updating, and deleting contacts. The API communicates with a SQLite database to perform these operations.

## API Endpoints

The following endpoints are available for managing contacts:

### 1. Get All Contacts
- **Method**: `GET`
- **URL**: `http://127.0.0.1:5000/`
- **Description**: Retrieves all contacts from the database.

### 2. Get Contact By ID
- **Method**: `GET`
- **URL**: `http://127.0.0.1:5000/contacts/<contact_id>`
- **Example**: `http://127.0.0.1:5000/contacts/1`
- **Description**: Fetches the details of a contact by their ID.

### 3. Search Contact By Name
- **Method**: `GET`
- **URL**: `http://127.0.0.1:5000/search`
- **Query Parameters**: 
  - `name` (string): The name of the contact to search for.
- **Example**: `http://127.0.0.1:5000/search?name=goran`
- **Description**: Searches for contacts matching the provided name.

### 4. Add New Contact
- **Method**: `POST`
- **URL**: `http://127.0.0.1:5000/add`
- **Body** (application/x-www-form-urlencoded):
  - `name` (string): The name of the new contact.
  - `email` (string): The email address of the new contact.
  - `phone` (string): The phone number of the new contact.
- **Example Request**: You can add a new contact using the following `curl` command:
  ```bash
  curl -X POST http://127.0.0.1:5000/add -d "name=petar&email=petar@example.com&phone=075222111"
- **Description**: Adds a new contact to the database.

### 5. Update Phone Number
- **Method**: `PATCH`
- **URL**: `http://127.0.0.1:5000/update-phone/<contact_name>`
- **Query Parameters**:
  - `phone` (string): The new phone number for the contact.
- **Example**: `http://127.0.0.1:5000/update-phone/joana?phone=075444333`
- **Description**: Updates the phone number for the specified contact.

### 6. Delete Contact
- **Method**: `DELETE`
- **URL**: `http://127.0.0.1:5000/delete/<contact_name>`
- **Example**: `http://127.0.0.1:5000/delete/petar`
- **Description**: Deletes the specified contact from the database.

## Installation
1. Clone the repository:
   ``` bash
   git clone https://github.com/Givanovski/Morse-Code-Converter.git
2. Navigate into the project directory:
   ``` bash
   cd Morse-Code-Converter
3. Install dependencies:
   ``` bash
   pip install -r requirements.txt
4. Run the application:
   ``` bash
   python run.py
