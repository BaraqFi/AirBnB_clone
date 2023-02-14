#!/usr/bin/python3
"""Instantiates a storage object.
--> Instantiates a file storage engine (FileStorage).
"""
from os import getenv


"""if getenv("ABNB_TYPE_STORAGE") == "db":
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
else:"""
    from models.engine.file_storage import FileStorage
    storage = FileStorage()
storage.reload()
