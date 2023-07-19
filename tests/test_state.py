#!/usr/bin/python3
"""
Test module for State module
"""

import unittest
from models.state import State
from models.base_model import BaseModel


class TestState(unittest.TestCase):
    """
    Testing the State module
    """
    def test_inheritance(self):
        """
        Test if State is a subclass of BaseModel
        """
        self.assertTrue(issubclass(State, BaseModel))

    def test_default_attribute(self):
        """
        Test default value for State instance
        """
        state = State()
        self.assertEqual(state.name, "")


if __name__ == '__main__':
    unittest.main()
