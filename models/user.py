from models.base_model import BaseModel
from engines.file_storage import FileStorage

class User(BaseModel):
    """User class"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """initialize User"""
        super().__init__(*args, **kwargs)

    def __str__(self):
        """return string representation of User"""
        return "[User] ({}) {}".format(self.id, self.__dict__)

    def save(self):
        """save User to file storage"""
        storage = FileStorage()
        storage.new(self)
        storage.save()

    def delete(self):
        """delete User from file storage"""
        storage = FileStorage()
        storage.delete(self)

    @classmethod
    def all(cls):
        """return a list of all User instances"""
        storage = FileStorage()
        users = storage.all(User)
        return users
