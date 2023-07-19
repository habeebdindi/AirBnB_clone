#!/usr/bin/python3
"""
This module tests the City module
"""

import unittest
from models.city import City
from models.base_model import BaseModel


class TestCity(unittest.TestCase):
    """
    Testing the City class
    """
    def test_inheritance(self):
        """
        Testing if City is a subclass of BaseModel
        """
        self.assertTrue(issubclass(City, BaseModel))

    def test_attributes(self):
        """
        Testing for City() instance values
        """
        city = City()
        self.assertEqual(city.name, "")
        self.assertEqual(city.state_id, "")

    def test_attribute_types(self):
        """
        Testing for instance type
        """
        city = City()
        self.assertIsInstance(city.name, str)
        self.assertIsInstance(city.state_id, str)

    def test_str_representation(self):
        """
        Testing __str__ representation for
        City() class instance
        """
        city = City()
        expected_str = "[City] ({}) {}".format(city.id, city.__dict__)
        self.assertEqual(str(city), expected_str)


if __name__ == '__main__':
    unittest.main()
