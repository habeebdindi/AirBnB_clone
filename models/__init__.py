#!/usr/bin/python3
"""
initialises this package any time it is imported, populates all
the object in its instance private attribute __objects.
"""
from .engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
