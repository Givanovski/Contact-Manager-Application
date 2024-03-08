"""
Module defining the Contact class.
"""


class Contact:
    """
    Class representing a contact with id, name, email, and phone attributes.
    """
    def __init__(self, id, name, email, phone):
        self.id = id
        self.name = name
        self.email = email
        self.phone = phone

    def to_dict(self):
        """
        Convert the Contact object to a dictionary.
        """
        return {key: getattr(self, key) for key in self.__dict__.keys()}
