#!/usr/bin/python3
"""
Testing the Review module
"""

import unittest
from models.review import Review
from models.base_model import BaseModel


class TestReview(unittest.TestCase):
    """
    Testing the Review module
    """
    def test_inheritance(self):
        """
        Testing if Review is a subclass of BaseModel
        """
        self.assertTrue(issubclass(Review, BaseModel))

    def test_default_attributes(self):
        """
        Test the default values of Review instance
        """
        review = Review()
        self.assertEqual(review.place_id, "")
        self.assertEqual(review.user_id, "")
        self.assertEqual(review.text, "")


if __name__ == '__main__':
    unittest.main()
