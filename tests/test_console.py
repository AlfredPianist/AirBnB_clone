#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""Unit test for console.py"""
from console import HBNBCommand

from unittest import TestCase, mock
from io import StringIO
import cmd
import os
import uuid
import random
import inspect
import pep8

from models import storage


class TestHBNBCommand(TestCase):
    """Test cases for HBNBCommand class."""

    @classmethod
    def tearDownClass(self):
        """Clean test files."""
        if os.path.exists(storage._FileStorage__file_path):
            os.remove(storage._FileStorage__file_path)

    def test_instance(self):
        """Test for correct instancing of HBNBCommand object."""
        self.assertIsInstance(HBNBCommand(), HBNBCommand)
        self.assertIsInstance(HBNBCommand(), cmd.Cmd)

    def test_empty_line(self):
        """Test for correct empty line action (empty line + RETURN)."""
        with mock.patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("\n")
        self.assertEqual(f.getvalue(), "")

    def test_quit_eof(self):
        """Test for correct quit and eof command actions."""
        with mock.patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("quit")
        self.assertEqual(f.getvalue(), "")

        with mock.patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("EOF")
        self.assertEqual(f.getvalue(), "")

    def test_help(self):
        """Test for correct help command output."""
        msg = ("\nDocumented commands (type help <topic>):\n"
               "========================================\n"
               "EOF  create  help  quit  show\n\n")
        with mock.patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help")
        self.assertEqual(f.getvalue(), msg)

    def test_create(self):
        """Test for correct create command action."""
        # Correct message "** class name missing **"
        with mock.patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create")
        self.assertEqual(f.getvalue(), "** class name missing **\n")

        # Correct message "** class doesn't exist **"
        with mock.patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create MyModel")
        self.assertEqual(f.getvalue(), "** class doesn't exist **\n")

        # Correct creation of object
        for class_name in HBNBCommand().class_list:
            with mock.patch('sys.stdout', new=StringIO()) as f:
                HBNBCommand().onecmd("create " + class_name)
            self.assertIn(class_name + "." + f.getvalue()[:-1], storage.all())

    def test_show(self):
        """Test for correct show command action."""
        # Correct message "** class name missing **"
        with mock.patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show")
        self.assertEqual(f.getvalue(), "** class name missing **\n")

        # Correct message "** class doesn't exist **"
        with mock.patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show MyModel")
        self.assertEqual(f.getvalue(), "** class doesn't exist **\n")

        # Correct message "** instance id missing **"
        with mock.patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show BaseModel")
        self.assertEqual(f.getvalue(), "** instance id missing **\n")

        # Correct message "** no instance found **"
        rand_class = random.choice(HBNBCommand().class_list)
        rand_id = str(uuid.uuid4())
        with mock.patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show " + rand_class + " " + rand_id)
        self.assertEqual(f.getvalue(), "** no instance found **\n")

        # Correct search of object
        for class_name in HBNBCommand().class_list:
            with mock.patch('sys.stdout', new=StringIO()) as f:
                HBNBCommand().onecmd("create " + class_name)
        for key in storage.all():
            key = key.split(".")
            with mock.patch('sys.stdout', new=StringIO()) as f:
                HBNBCommand().onecmd("show " + key[0] + " " + key[1])
            f_class = f.getvalue().split(" ")[0][1:-1]
            f_id = f.getvalue().split(" ")[1][1:-1]
            self.assertIn(f_class + "." + f_id, storage.all())


class TestHBNBCommandDoc(TestCase):
    "Tests documentation and pep8 for HBNBCommand class."

    @classmethod
    def setUpClass(cls):
        """Sets the whole functions of the class HBNBCommand to be inspected for
        correct documentation."""
        cls.functions = inspect.getmembers(HBNBCommand,
                                           inspect.isfunction(HBNBCommand))

    def test_doc_module(self):
        """Tests for docstring presence in the module and the class."""
        import console

        self.assertTrue(len(console.__doc__) > 0)
        self.assertTrue(len(console.HBNBCommand.__doc__) > 0)

    def test_doc_fun(self):
        """Tests for docstring presence in all functions of class."""
        for fun in self.functions:
            self.assertTrue(len(fun.__doc__) > 0)

    def test_pep8(self):
        """Tests pep8 style compliance of module and test files."""
        p8 = pep8.StyleGuide(quiet=False)

        res = p8.check_files(['console.py'])
        self.assertEqual(res.total_errors, 0,
                         "Found code style errors (and warnings).")
        res = p8.check_files(['tests/test_console.py'])
        self.assertEqual(res.total_errors, 0,
                         "Found code style errors (and warnings).")
