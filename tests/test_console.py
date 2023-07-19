#!/usr/bin/python3
"""
Testing the console.py module
"""

import unittest
import sys
from io import StringIO
from unittest.mock import patch
from console import HBNBCommand


class TestHBNBCommand(unittest.TestCase):
    """
    Testing the HBNBCommand module
    """
    def setUp(self):
        self.cli = HBNBCommand()

    def tearDown(self):
        self.cli = None

    def test_help_message(self):
        """
        Testing the commands printed
        on call for help
        """
        commands = ['help', 'quit', 'EOF', 'create', 'show', 'destroy', 'all', 'update']
        with patch('sys.stdout', new=StringIO()) as output:
            for command in commands:
                self.cli.onecmd(command)
                output_str = output.getvalue()
                self.assertIn(command, output_str)

    def test_invalid_command(self):
        """
        Testing for invalid miscallenous commands
        """
        with patch('sys.stdout', new=StringIO()) as output:
            self.cli.onecmd('invalidcommand')
            output_str = output.getvalue()
            self.assertIn('*** Unknown syntax:', output_str)
            self.assertIn('invalidcommand', output_str)


if __name__ == '__main__':
    unittest.main()
