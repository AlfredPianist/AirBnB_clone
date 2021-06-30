#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""console module.
- Class HBNBCommand - A class inheriting from cmd.Cmd acting as a shell
                      for testing the storage engine of the HBnB project.
- Instance Attributes (public):
      - prompt: The prompt to be shown.
      - class_list: The list of available classes to operate.
- Methods (public):
      - do_quit: Exits the shell.
      - do_EOF: Exits the shell.
      - do_create: Creates a new instance of an object and prints its id.
      - do_show: Shows the string representation of an object given its class
                 name and id.
      - do_destroy: Destroys an object given its class name and id.
      - do_all: Shows the string representation of all objects of a given class
                or all objects created of all classes.
      - do_update: Updates the attributes of an object given its class
                 name and id with an attribute and its value. It supports
                 also its dictionary representation.
      - do_count: Counts the number of instances of a given class.
      - default: Parses the dot versions of commands show, destroy, all,
                 update and count.
"""
import cmd
import sys
import shlex
import json

from models import storage
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State


class HBNBCommand(cmd.Cmd):
    """The shell for the HBnB project.
    Attributes:
        prompt (str): The shell prompt.
        class_list (tuple of str): The list of available classes to operate.
    """
    prompt = "(hbnb) "
    class_list = ("BaseModel", "User", "Amenity", "City",
                  "Place", "Review", "State")

    def do_quit(self, arg):
        """\
        Quit command. Exits hbnb shell.\
        """
        return True

    def do_EOF(self, arg):
        """\
        EOF command. Exits hbnb shell.\
        """
        return True

    def emptyline(self):
        """\
        Empty line function. Does nothing.\
        """
        return

    def do_create(self, arg):
        """\
        Creates a new instance of type TYPE, saves it as JSON and prints
        its id.
            Usage: create TYPE
            Example: create BaseModel\
        """
        if not arg:
            print("** class name missing **")
            return
        if arg not in HBNBCommand.class_list:
            print("** class doesn't exist **")
            return
        obj = eval(arg + "()")
        obj.save()
        print(obj.id)

    def do_show(self, arg):
        """\
        Prints a string representation of an instance type TYPE with id ID.
            Usage: show TYPE ID | TYPE.show(ID)
            Examples: show BaseModel 1234-1234-1234
                      BaseModel.show(1234-1234-1234)\
        """
        arg_list = arg.split(" ") if type(arg) == str else arg
        if not arg:
            print("** class name missing **")
            return
        if arg_list[0] not in HBNBCommand.class_list:
            print("** class doesn't exist **")
            return
        if len(arg_list) < 2:
            print("** instance id missing **")
            return
        key = arg_list[0] + "." + arg_list[1]
        if key not in storage.all():
            print("** no instance found **")
            return
        print(storage.all()[key])

    def do_destroy(self, arg):
        """\
        Deletes an instance type TYPE with id ID and saves the changes
        in a JSON file.
            Usage: destroy TYPE ID | TYPE.destroy(ID)
            Example: destroy BaseModel 1234-1234-1234
                     BaseModel.destroy(1234-1234-1234)\
        """
        arg_list = arg.split(" ") if type(arg) == str else arg
        if not arg:
            print("** class name missing **")
            return
        if arg_list[0] not in HBNBCommand.class_list:
            print("** class doesn't exist **")
            return
        if len(arg_list) < 2:
            print("** instance id missing **")
            return
        key = arg_list[0] + "." + arg_list[1]
        if key in storage.all():
            del storage.all()[key]
            storage.save()
            return
        print("** no instance found **")

    def do_all(self, arg):
        """\
        Prints a string representation of type TYPE or all types.
            Usage: all [TYPE] | TYPE.all()
            Examples: all
                      all BaseModel
                      BaseModel.all()\
        """
        arg_list = arg.split(" ") if type(arg) == str else arg
        if arg:
            if arg_list[0] not in HBNBCommand.class_list:
                print("** class doesn't exist **")
                return
            obj_list = []
            for key, val in storage.all().items():
                if key.split(".")[0] == arg_list[0]:
                    obj_list.append(str(val))
            print(obj_list)
            return
        obj_list = [str(val) for val in storage.all().values()]
        print(obj_list)

    def do_update(self, arg):
        """\
        Updates an instance of type TYPE and id ID with ATTRIBUTE_NAME
        and ATTRIBUTE_VALUE and saves it to a JSON file.
        It also supports updating using a dictionary representation
        of ATTRIBUTE_NAME: ATTRIBUTE_VALUE pairs.
            Usage: update TYPE ID ATTRIBUTE_NAME ATTRIBUTE_VALUE |
                   TYPE.update(ID, ATTRIBUTE_NAME, ATTRIBUTE_VALUE) |
                   TYPE.update(ID, {ATTRIBUTE_NAME: ATTRIBUTE_VALUE[, ...]})
            Examples: update BaseModel 1234-1234-1234 email "hbnb@hlbrtn.com"
                      BaseModel.update(1234-1234-1234, email,
                                       "hbnb@hlbrtn.com")
                      BaseModel.update(1234-1234-1234,
                                       {"email": "hbnb@hlbrtn.com"})\
        """
        if type(arg) == str:
            arg_list = shlex.shlex(arg)
            arg_list.wordchars += "-"
            arg_list = list(arg_list)
            try:
                idx_start = arg_list.index("[")
                idx_end = arg_list.index("]")
                list_str = "".join(arg_list[idx_start:idx_end + 1])
                list_str = eval(list_str)
                list_start = arg_list[:idx_start]
                list_end = arg_list[idx_end + 1:]
                arg_list = list_start
                arg_list.append(list_str)
                arg_list.extend(list_end)
            except ValueError:
                pass
        else:
            arg_list = arg
        if not arg:
            print("** class name missing **")
            return
        if arg_list[0] not in HBNBCommand.class_list:
            print("** class doesn't exist **")
            return
        if len(arg_list) < 2:
            print("** instance id missing **")
            return
        key = arg_list[0] + "." + arg_list[1]
        if key not in storage.all():
            print("** no instance found **")
            return
        if len(arg_list) == 3 and type(arg_list[2]) == dict:
            obj = storage.all()[key]
            for key, val in arg_list[2].items():
                setattr(obj, key, val)
                obj.save()
            return
        if len(arg_list) < 3:
            print("** attribute name missing **")
            return
        if len(arg_list) < 4:
            print("** value missing **")
            return
        obj = storage.all()[key]
        if type(arg_list[3]) != list:
            arg_list[3].replace('"', "").replace("'", "")
        setattr(obj, arg_list[2].replace('"', "").replace("'", ""),
                arg_list[3])
        obj.save()

    def do_count(self, arg):
        """\
        Prints the number of instances of type TYPE.
            Usage: count TYPE
            Examples: count BaseModel
                      BaseModel.count()\
        """
        arg_list = arg.split(" ") if type(arg) == str else arg
        if not arg:
            print("** class name missing **")
            return
        if arg_list[0] not in HBNBCommand.class_list:
            print("** class doesn't exist **")
            return
        objs = [key for key in map(lambda x: x.split(".")[0],
                                   storage.all().keys())]
        print(objs.count(arg_list[0]))

    def default(self, line):
        """\
        Parses when command is of type TYPE.COMMAND(ARGS).
            Example: BaseModel.all()\
        """
        lexer = shlex.shlex(line)
        lexer.wordchars += "-"
        lexer = list(lexer)
        arg = []
        func_name = ""
        idx = 0
        in_paren = False

        while idx < len(lexer):
            if lexer[idx][0].islower() is True and func_name == "":
                func_name = lexer[idx]
            elif in_paren is True:
                if lexer[idx] == "[":
                    idx_start = lexer.index("[")
                    idx_end = lexer.index("]")
                    list_str = "".join(lexer[idx_start:idx_end + 1])
                    arg.append(eval(list_str))
                    idx = idx_end
                if lexer[idx] == "{":
                    dict_str = "".join(lexer[idx:-1])
                    dict_str = dict_str.replace("'", '"')
                    arg.append(json.loads(dict_str))
                    idx = len(lexer) - 1
                if lexer[idx] not in ",)":
                    arg.append(lexer[idx].replace('"', "").replace("'", ""))
            elif lexer[idx] == "(":
                in_paren = True
            elif lexer[idx] != ".":
                arg.append(lexer[idx].replace('"', "").replace("'", ""))
            idx += 1

        cmd_list = ("all", "count", "show", "destroy", "update")
        if func_name in cmd_list:
            eval("self.do_" + func_name + "(arg)")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
