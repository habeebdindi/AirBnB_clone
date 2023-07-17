#!/usr/bin/python3
"""Defines a User class
"""
from .base_model import BaseModel


class User(BaseModel):
    """User class, defines class-specific attributes
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
