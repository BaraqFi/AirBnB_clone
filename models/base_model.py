import json
import os
from datetime import datetime
from uuid import uuid4

from engines.file_storage import FileStorage

# create a FileStorage instance to handle file operations
storage = FileStorage()

class BaseModel:
    """Base class for all models"""

    def __init__(self, *args, **kwargs):
        """Initialize a new BaseModel instance"""
        if not kwargs:
            # if no kwargs are given, create a new instance with default values
            self.id = str(uuid4()) # generate a unique ID for the instance
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self) # add new instance to the file storage database
        else:
            # if kwargs are given, initialize the instance from the provided data
            self.__dict__.update(kwargs)
            self.created_at = datetime.strptime(self.created_at, '%Y-%m-%d %H:%M:%S.%f')
            self.updated_at = datetime.strptime(self.updated_at, '%Y-%m-%d %H:%M:%S.%f')

    def __str__(self):
        """Return a string representation of the instance"""
        return "[{}] ({}) {}".format(type(self).__name__, self.id, self.__dict__)

    def save(self):
        """Update the instance and save changes to the file storage database"""
        self.updated_at = datetime.now()
        storage.save(self)

    def delete(self):
        """Delete the instance from the file storage database"""
        storage.delete(self)

    def to_dict(self):
        """Return a dictionary representation of the instance"""
        result = self.__dict__.copy()
        result['created_at'] = self.created_at.isoformat()
        result['updated_at'] = self.updated_at.isoformat()
        result['__class__'] = type(self).__name__
        return result
