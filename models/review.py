#!/usr/bin/python3
"""Defines a Review class
"""
from .base_model import BaseModel


class Review(BaseModel):
    """Defines class-specific attributes
    """
    place_id = ""
    user_id = ""
    text = ""
