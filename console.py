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

from models import storage
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """The shell for the HBnB project.
    Attributes:
        prompt (str): The shell prompt.
    """
    prompt = "(hbnb) "
    class_list = ["BaseModel"]

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

    def empty_line(self):
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
        arg_list = arg.split(" ")
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


if __name__ == '__main__':
    HBNBCommand().cmdloop()
