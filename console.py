#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""console module.
- Class HBNBCommand - A class inheriting from cmd.Cmd acting as a shell
                      for testing the storage engine of the HBnB project.
- Instance Attributes (public):
      - prompt: The prompt to be shown.
- Methods (public):
      - do_quit: Exits the shell.
      - do_EOF: Exits the shell.
      - do_create: Creates a new instance of an object and prints its id.
      - do_show: Shows the string representation of an object given its class
                 name and id.
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
            Usage: show TYPE ID
            Example: show BaseModel 1234-1234-1234\
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
        for key, value in storage.all().items():
            if key.split(".")[1] == arg_list[1]:
                print(value)
                return
        print("** no instance found **")

    def do_destroy(self, arg):
        """\
        Deletes an instance type TYPE with id ID and saves the changes
        in a JSON file.
            Usage: destroy TYPE ID
            Example: destroy BaseModel 1234-1234-1234\
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
            Usage: all [TYPE]
            Examples: all
                      all BaseModel
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
            Usage: update TYPE ID ATTRIBUTE_NAME ATTRIBUTE_VALUE
            Example: update BaseModel 1234-1234-1234 email "hbnb@hlbrtn.com"\
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
        setattr(obj, arg_list[2].replace('"', "").replace("'", ""),
                arg_list[3].replace('"', "").replace("'", ""))
        obj.save()

    def do_count(self, arg):
        pass

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
