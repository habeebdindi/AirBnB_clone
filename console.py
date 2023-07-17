#!/usr/bin/python3
"""
A shell to manage operations. There is minimum documentation here.
May be updated later, or feel free to edit and make a pull req.
"""
import sys
import cmd
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models import storage


class HBNBCommand(cmd.Cmd):
    """
    class sub-classing the cmd module for usage
    """
    prompt = "(hbnb) "
    classes = ["BaseModel", "User", "Place", "State", "City",
               "Amenity", "Review"]

    def do_quit(self, line):
        """Quit command to exit the program
        """
        sys.exit()

    def do_EOF(self, line):
        """handles CTRL+D, quits from shell
        """
        return True

    def do_create(self, line):
        """Creates a new instance of a class and saves it's json to file
        """
        parseline = line.split(' ')
        if not parseline[0]:
            print("** class name missing **")
        elif parseline[0] not in self.classes:
            print("** class doesn't exist **")
        else:
            instance = eval(parseline[0])()
            instance.save()
            print(instance.id)

    def do_show(self, line):
        """Shows an instance of a class
        """
        parseline = line.split(' ')
        if not parseline[0]:
            print("** class name missing **")
        elif parseline[0] not in self.classes:
            print("** class doesn't exist **")
        elif len(parseline) == 1:
            print("** instance id missing **")
        else:
            all_objs = storage.all()
            for obj_key in all_objs.keys():
                if str(obj_key) == "{}.{}".format(parseline[0], parseline[1]):
                    obj = all_objs[obj_key]
                    print(obj)
                    break
            else:
                print("** no instance found **")

    def do_destroy(self, line):
        """Destroys an instance of a class and saves the change
        """
        parseline = line.split(' ')
        if not parseline[0]:
            print("** class name missing **")
        elif parseline[0] not in self.classes:
            print("** class doesn't exist **")
        elif len(parseline) == 1:
            print("** instance id missing **")
        else:
            all_objs = storage.all()
            for obj_key in all_objs.keys():
                if str(obj_key) == "{}.{}".format(parseline[0], parseline[1]):
                    del all_objs[obj_key]
                    storage.save()
                    break
            else:
                print("** no instance found **")

    def do_all(self, line):
        """Displays all instances in a list
        """
        parseline = line.split(' ')
        if not parseline[0] or parseline[0] in self.classes:
            all_objs = storage.all()
            obj_list = []
            for obj_v in all_objs.values():
                obj_list.append(str(obj_v))
            print(obj_list)
        else:
            print("** class doesn't exist **")

    def do_update(self, line):
        """Updates an instance attribute or adds a new attribute
        """
        parseline = line.split(' ')
        if not parseline[0]:
            print("** class name missing **")
        elif parseline[0] not in self.classes:
            print("** class doesn't exist **")
        elif len(parseline) == 1:
            print("** instance id missing **")
        elif len(parseline) == 2:
            print("** attribute name missing **")
        elif len(parseline) == 3:
            print("** value missing **")
        else:
            all_objs = storage.all()
            for obj_key in all_objs.keys():
                if str(obj_key) == "{}.{}".format(parseline[0], parseline[1]):
                    attr_val = type(parseline[2])(parseline[3].strip('"'))
                    setattr(all_objs[obj_key], parseline[2], attr_val)
                    storage.save()
                    break
            else:
                print("** no instance found **")

    def precmd(self, line):
        """Retrieve all instances of a class
        """
        all_objs = storage.all()

        for cl_name in self.classes:
            if line == "{}.all()".format(cl_name):
                obj_list = [str(all_objs[k]) for k in all_objs.keys()
                            if k.split('.')[0] == cl_name]
                print(obj_list)
                return ''
            elif line == "{}.count()".format(cl_name):
                obj_list = [str(all_objs[k]) for k in all_objs.keys()
                            if k.split('.')[0] == cl_name]
                print(len(obj_list))
                return ''
            elif line.split('.')[0] == cl_name:
                for ob in all_objs.keys():
                    if line == "{}.show(\"{}\")".format(cl_name,
                                                        str(ob.split('.')[1])):
                        new_line = cl_name + " " + str(ob.split('.')[1])
                        self.do_show(new_line)
                        return ''
        else:
            return line

    def emptyline(self):
        """Here goes nothing
        """
        pass

    def postloop(self):
        """If you delete this overriden method, your shell will be messy
        when you type CRTL+D or use it non-interactively
        """
        print()


if __name__ == "__main__":
    HBNBCommand().cmdloop()
