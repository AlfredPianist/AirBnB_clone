#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""Unit test for file_storage.py"""
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.user import User

from unittest import TestCase
import copy
import os
import inspect
import pep8


class TestFileStorage(TestCase):
    """Test cases for FileStorage class."""

    def setUp(self):
        """Setup for FileStorage tests."""
        self.engine = FileStorage()
        FileStorage._FileStorage__objects.clear()

    def tearDown(self):
        """Clean test files."""
        if os.path.exists(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_instance(self):
        """Test for correct instancing of FileStorage object."""
        self.assertIsInstance(self.engine, FileStorage)

    def test_attribute_types(self):
        """Test for correct attribute type of FileStorage file_path."""
        self.assertIsInstance(self.engine._FileStorage__file_path, str)

    def test_all_method_type(self):
        """Test correct type return of the all method."""
        self.assertIsInstance(self.engine.all(), dict)

    def test_methods_base(self):
        """Test all FileStorage methods on a BaseModel instance."""
        # Testing engine.new() and engine.all()
        base_1 = BaseModel()
        base_2 = BaseModel()
        key_1 = "{}.{}".format(type(base_1).__name__, base_1.id)
        key_2 = "{}.{}".format(type(base_2).__name__, base_2.id)

        self.assertIn((key_1, base_1),
                      self.engine.all().items())
        self.assertIn((key_2, base_2),
                      self.engine.all().items())

        # Testing engine.save() and engine.reload()
        self.engine.save()
        old_objects = copy.deepcopy(FileStorage._FileStorage__objects)
        old_objects = {key: str(val) for key, val in old_objects.items()}

        FileStorage._FileStorage__objects.clear()
        self.engine.reload()
        new_objects = copy.deepcopy(FileStorage._FileStorage__objects)
        new_objects = {key: str(val) for key, val in new_objects.items()}

        self.assertEqual(old_objects, new_objects)

    def test_methods_user(self):
        """Test all FileStorage methods on an User instance."""
        # Testing engine.new() and engine.all()
        user_1 = User()
        user_2 = User()
        key_1 = "{}.{}".format(type(user_1).__name__, user_1.id)
        key_2 = "{}.{}".format(type(user_2).__name__, user_2.id)

        self.assertIn((key_1, user_1),
                      self.engine.all().items())
        self.assertIn((key_2, user_2),
                      self.engine.all().items())

        # Testing engine.save() and engine.reload()
        self.engine.save()
        old_objects = copy.deepcopy(FileStorage._FileStorage__objects)
        old_objects = {key: str(val) for key, val in old_objects.items()}

        FileStorage._FileStorage__objects.clear()
        self.engine.reload()
        new_objects = copy.deepcopy(FileStorage._FileStorage__objects)
        new_objects = {key: str(val) for key, val in new_objects.items()}

        self.assertEqual(old_objects, new_objects)


class TestFileStorageDoc(TestCase):
    "Tests documentation and pep8 for FileStorage class."

    @classmethod
    def setUpClass(cls):
        """Sets the whole functions of the class FileStorage to be inspected for
        correct documentation."""
        cls.functions = inspect.getmembers(FileStorage,
                                           inspect.isfunction(FileStorage))

    def test_doc_module(self):
        """Tests for docstring presence in the module and the class."""
        from models.engine import file_storage

        self.assertTrue(len(file_storage.__doc__) > 0)
        self.assertTrue(len(file_storage.FileStorage.__doc__) > 0)

    def test_doc_fun(self):
        """Tests for docstring presence in all functions of class."""
        for fun in self.functions:
            self.assertTrue(len(fun.__doc__) > 0)

    def test_pep8(self):
        """Tests pep8 style compliance of module and test files."""
        p8 = pep8.StyleGuide(quiet=False)

        res = p8.check_files(['models/engine/file_storage.py'])
        self.assertEqual(res.total_errors, 0,
                         "Found code style errors (and warnings).")
        res = p8.check_files(
            ['tests/test_models/test_engine/test_file_storage.py'])
        self.assertEqual(res.total_errors, 0,
                         "Found code style errors (and warnings).")
