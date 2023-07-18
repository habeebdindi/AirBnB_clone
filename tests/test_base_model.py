#!/usr/bin/python3
"""
This module tests the BaseModel module
"""

import unittest
from models.base_model import BaseModel
import uuid
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    """
    The TestBaseModel class
    """
    def test_init_with_kwargs(self):
        """
        Testing for the __init__ call
        with **kwargs
        """
        data = {
                'id': '1234',
                'created_at': '2023-07-18T12:34:56.789',
                'updated_at': '2023-07-18T12:34:56.789',
                'name': 'My Test Model'
                }
        obj = BaseModel(**data)
        self.assertEqual(obj.id, '1234')
        self.assertEqual(obj.name, 'My Test Model')
        self.assertEqual(obj.created_at, datetime(2023, 7, 18, 12, 34, 56, 789000))
        self.assertEqual(obj.updated_at, datetime(2023, 7, 18, 12, 34, 56, 789000))

    def test_init_without_kwargs(self):
        """
        Testing for the __init__ call
        without **kwargs
        """
        obj = BaseModel()
        self.assertIsInstance(obj.id, str)    # Testing if obj.id is of type str
        self.assertIsInstance(obj.created_at, datetime)    # Test if obj.created_at is of datetime instance
        self.assertIsInstance(obj.updated_at, datetime)    # Test if obj.updated_at is of datetime instance
        self.assertLessEqual(obj.created_at, datetime.now())
        self.assertLessEqual(obj.updated_at, datetime.now())

    def test_str_representation(self):
        """
        Testing the __str__ representation of
        the BaseModel class
        """
        obj = BaseModel(id='abcd')
        expected_str = "[BaseModel] (abcd) {'id': 'abcd', 'created_at': datetime, 'updated_at': datetime}"
        self.assertEqual(str(obj), expected_str)

    def test_to_dict(self):
        """
        Testing tht to_dict() method of
        the BaseModel class
        """
        obj = BaseModel(id='xyz', created_at=datetime(2023, 7, 18, 12, 34, 56, 789000))
        obj_dict = obj.to_dict()
        self.assertEqual(obj_dict['__class__'], 'BaseModel')
        self.assertEqual(obj_dict['id'], 'xyz')
        self.assertEqual(obj_dict['created_at'], '2023-07-18T12:34:56.789000')
        self.assertIn('updated_at', obj_dict)
        self.assertIn('save', obj_dict)
        self.assertIn('to_dict', obj_dict)


# Running the unittest on the BaseModel class
if __name__ == '__main__':
    unittest.main()
