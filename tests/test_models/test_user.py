#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""Unit test for user.py"""
from models.user import User
from models.base_model import BaseModel
from models import storage

from unittest import TestCase
from datetime import datetime
import time
import os
import uuid
import inspect
import pep8


class TestUser(TestCase):
    """Test cases for User class."""

    def setUp(self):
        """Setup for User tests."""
        self.user_1 = User()

    def tearDown(self):
        """Clean test files."""
        if os.path.exists(storage._FileStorage__file_path):
            os.remove(storage._FileStorage__file_path)

    def test_instance(self):
        """Test for correct instancing of User object."""
        self.assertIsInstance(self.user_1, User)

    def test_inheritance(self):
        """Test for correct inheritance of User object."""
        self.assertTrue(issubclass(type(self.user_1), BaseModel))

    def test_attribute_types(self):
        """Test for correct attribute types of User object."""
        self.assertIsInstance(self.user_1.email, str)
        self.assertIsInstance(self.user_1.password, str)
        self.assertIsInstance(self.user_1.first_name, str)
        self.assertIsInstance(self.user_1.last_name, str)

    def test_empty_string(self):
        """Test for empty string in User instance."""
        self.assertEqual(self.user_1.email, "")
        self.assertEqual(self.user_1.password, "")
        self.assertEqual(self.user_1.first_name, "")
        self.assertEqual(self.user_1.last_name, "")

    def test_id_creation(self):
        """Test for correct id creation and type."""
        user_1_id = eval("uuid.UUID('" + self.user_1.id + "')")
        self.assertIsInstance(user_1_id, uuid.UUID)

    def test_id_uniqueness(self):
        """Test for id uniqueness."""
        user_2 = User()
        self.assertNotEqual(self.user_1.id, user_2.id)

    def test_datetime_creation(self):
        """Test for correct datetime creation and type."""
        self.assertIsInstance(self.user_1.created_at, datetime)
        self.assertIsInstance(self.user_1.updated_at, datetime)
        self.assertNotEqual(self.user_1.created_at, self.user_1.updated_at)

    def test_str_magic_method(self):
        """Test for correct __str__ output"""
        correct_output = "[User] ({}) {}".format(
            self.user_1.id, self.user_1.__dict__)

        self.assertEqual(correct_output, self.user_1.__str__())

    def test_save(self):
        """Test for correct update of attribute updated_at"""
        old_updated_at = self.user_1.updated_at
        time.sleep(0.5)
        self.user_1.save()

        self.assertNotEqual(self.user_1.created_at, self.user_1.updated_at)
        self.assertNotEqual(self.user_1.updated_at, old_updated_at)

    def test_to_dict(self):
        """Test for correct dictionary type and output of to_dict method."""
        self.user_1.name = "Test"
        self.user_1.num = 1
        user_1_dict = self.user_1.to_dict()

        self.assertIsInstance(user_1_dict, dict)

        user_1_class = type(self.user_1).__name__
        self.assertIn(("__class__", user_1_class),
                      user_1_dict.items())
        self.assertNotIn(("__class__", user_1_class),
                         self.user_1.__dict__)

        user_1_created_at = self.user_1.created_at.isoformat()
        user_1_updated_at = self.user_1.updated_at.isoformat()
        self.assertIn(("created_at", user_1_created_at),
                      user_1_dict.items())
        self.assertIn(("updated_at", user_1_updated_at),
                      user_1_dict.items())

        isoformat = '%Y-%m-%dT%H:%M:%S.%f'
        user_1_created_at = datetime.strptime(user_1_dict["created_at"],
                                              isoformat)
        user_1_updated_at = datetime.strptime(user_1_dict["updated_at"],
                                              isoformat)
        self.assertEqual(user_1_created_at, self.user_1.created_at)
        self.assertEqual(user_1_updated_at, self.user_1.updated_at)

    def test_kwargs(self):
        """Test for correct instance creation from kwargs (dictionary)."""
        user_1_dict = self.user_1.to_dict()
        user_2 = User(**user_1_dict)

        self.assertIsInstance(user_2, User)
        self.assertIsNot(self.user_1, user_2)
        self.assertEqual(self.user_1.__dict__, user_2.__dict__)


class TestUserDoc(TestCase):
    "Tests documentation and pep8 for User class."

    @classmethod
    def setUpClass(cls):
        """Sets the whole functions of the class User to be inspected for
        correct documentation."""
        cls.functions = inspect.getmembers(User,
                                           inspect.isfunction(User))

    def test_doc_module(self):
        """Tests for docstring presence in the module and the class."""
        from models import user

        self.assertTrue(len(user.__doc__) > 0)
        self.assertTrue(len(user.User.__doc__) > 0)

    def test_doc_fun(self):
        """Tests for docstring presence in all functions of class."""
        for fun in self.functions:
            self.assertTrue(len(fun.__doc__) > 0)

    def test_pep8(self):
        """Tests pep8 style compliance of module and test files."""
        p8 = pep8.StyleGuide(quiet=False)

        res = p8.check_files(['models/user.py'])
        self.assertEqual(res.total_errors, 0,
                         "Found code style errors (and warnings).")
        res = p8.check_files(['tests/test_models/test_user.py'])
        self.assertEqual(res.total_errors, 0,
                         "Found code style errors (and warnings).")
