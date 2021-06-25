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
"""
import cmd
import sys


class HBNBCommand(cmd.Cmd):
    """The shell for the HBnB project.
    Attributes:
        prompt (str): The shell prompt.
    """
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit command. Exits hbnb shell."""
        return True

    def do_EOF(self, arg):
        """EOF command. Exits hbnb shell."""
        return True

    def empty_line(self):
        """Empty line function. Does nothing."""
        return


if __name__ == '__main__':
    HBNBCommand().cmdloop()
