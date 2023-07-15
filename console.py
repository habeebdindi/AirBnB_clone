#!/usr/bin/python3
"""
"""
import cmd
from models.base_model import BaseModel

class HBNBCommand(cmd.Cmd):
    """
    """
    prompt = "(hbnb) "
    classes = ["BaseModel"]

    def do_quit(self, line):
        """Quit command to exit the program
        """
        return self.do_EOF(line)

    def do_EOF(self, line):
        """
        """
        return True

    def do_create(self, line):
        """
        """
        if not line:
            print("** class name missing **")
        if line not in classes:
            print("** class doesn't exist **")
        for 

    def emptyline(self, line):
        """
        """
        pass

    def postloop(self):
        """
        """
        print("")

if __name__ == "__main__":
    HBNBCommand().cmdloop()
