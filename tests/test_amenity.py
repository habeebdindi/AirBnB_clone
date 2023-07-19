#!/usr/bin/python3
"""
Testing the Amenity module
"""

import unittest
from models.amenity import Amenity
from models.base_model import BaseModel


class TestAmenity(unittest.TestCase):
    """
    Testing the Amenity class module
    """
    def test_inheritance(self):
        """
        Testing if Amenity is a subclass
        of the BaseModel class
        """
        self.assertTrue(issubclass(Amenity, BaseModel))

    def test_default_attribute(self):
        """
        Testing for the value of the
        Amenity instance
        """
        amenity = Amenity()
        self.assertEqual(amenity.name, "")


if __name__ == '__main__':
    unittest.main()
