#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""
from os import getenv

storage_type = getenv("HBNB_TYPE_STORAGE")

if (storage_type == 'db'):
    from .engine import db_storage
    storage = db_storage.DBStorage()
else:
    from .engine import file_storage
    storage = file_storage.FileStorage()
storage.reload()
