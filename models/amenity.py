#!/usr/bin/env python3
"""Defines the Amenity class.
from models.base_model import Base, BaseModel
from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy.orm import relationship


class Amenity(BaseModel, Base):
    ""Represents an Amenity for a MySQL database.

    Inherits from SQLAlchemy Base and links to the MySQL table `amenities`.

    Attributes:
        __tablename__ (str): The name of the MySQL table to store Amenities.
        name (sqlalchemy String): The amenity name.
        place_amenities (sqlalchemy relationship): Place-Amenity relationship.
    ""replace comment quotes
    __tablename__ = "amenities"
    name = Column(String(128), nullable=False)
    place_amenities = relationship("Place", secondary="place_amenity",
                                   viewonly=False)"""
# models/amenity.py
from engines.file_storage import FileStorage
from models.base_model import BaseModel

class Amenity(BaseModel):
    name = ""

    def __init__(self, *args, **kwargs):
        if kwargs:
            for key, value in kwargs.items():
                if key == "name":
                    self.name = value
        else:
            super().__init__()
            self.name = ""

    def to_dict(self):
        dict_amenity = {}
        dict_amenity["name"] = self.name
        dict_amenity["created_at"] = self.created_at.isoformat()
        dict_amenity["updated_at"] = self.updated_at.isoformat()
        dict_amenity["id"] = self.id
        return dict_amenity

    def save(self):
        FileStorage.new(self)
        FileStorage.save()

    def __str__(self):
        return "[Amenity] ({}) {}".format(self.id, self.__dict__)

