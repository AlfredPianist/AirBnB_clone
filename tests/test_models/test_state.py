#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""Unit test for state.py"""
from models.state import State
from models.base_model import BaseModel
from models import storage

from unittest import TestCase
from datetime import datetime
import time
import os
import uuid
import inspect
import pep8


class TestState(TestCase):
    """Test cases for State class."""

    def setUp(self):
        """Setup for State tests."""
        self.state_1 = State()

    def tearDown(self):
        """Clean test files."""
        if os.path.exists(storage._FileStorage__file_path):
            os.remove(storage._FileStorage__file_path)

    def test_instance(self):
        """Test for correct instancing of State object."""
        self.assertIsInstance(self.state_1, State)

    def test_inheritance(self):
        """Test for correct inheritance of State object."""
        self.assertTrue(issubclass(type(self.state_1), BaseModel))

    def test_attribute_types(self):
        """Test for correct attribute types of State object."""
        self.assertIsInstance(self.state_1.name, str)

    def test_empty_string(self):
        """Test for empty string in State instance."""
        self.assertEqual(self.state_1.name, "")

    def test_id_creation(self):
        """Test for correct id creation and type."""
        state_1_id = eval("uuid.UUID('" + self.state_1.id + "')")
        self.assertIsInstance(state_1_id, uuid.UUID)

    def test_id_uniqueness(self):
        """Test for id uniqueness."""
        state_2 = State()
        self.assertNotEqual(self.state_1.id, state_2.id)

    def test_datetime_creation(self):
        """Test for correct datetime creation and type."""
        self.assertIsInstance(self.state_1.created_at, datetime)
        self.assertIsInstance(self.state_1.updated_at, datetime)
        self.assertEqual(self.state_1.created_at, self.state_1.updated_at)

    def test_str_magic_method(self):
        """Test for correct __str__ output"""
        correct_output = "[State] ({}) {}".format(
            self.state_1.id, self.state_1.__dict__)

        self.assertEqual(correct_output, self.state_1.__str__())

    def test_save(self):
        """Test for correct update of attribute updated_at"""
        old_updated_at = self.state_1.updated_at
        time.sleep(0.5)
        self.state_1.save()

        self.assertNotEqual(self.state_1.created_at, self.state_1.updated_at)
        self.assertNotEqual(self.state_1.updated_at, old_updated_at)

    def test_to_dict(self):
        """Test for correct dictionary type and output of to_dict method."""
        self.state_1.name = "Test"
        self.state_1.num = 1
        state_1_dict = self.state_1.to_dict()

        self.assertIsInstance(state_1_dict, dict)

        state_1_class = type(self.state_1).__name__
        self.assertIn(("__class__", state_1_class),
                      state_1_dict.items())
        self.assertNotIn(("__class__", state_1_class),
                         self.state_1.__dict__)

        state_1_created_at = self.state_1.created_at.isoformat()
        state_1_updated_at = self.state_1.updated_at.isoformat()
        self.assertIn(("created_at", state_1_created_at),
                      state_1_dict.items())
        self.assertIn(("updated_at", state_1_updated_at),
                      state_1_dict.items())

        isoformat = '%Y-%m-%dT%H:%M:%S.%f'
        state_1_created_at = datetime.strptime(state_1_dict["created_at"],
                                               isoformat)
        state_1_updated_at = datetime.strptime(state_1_dict["updated_at"],
                                               isoformat)
        self.assertEqual(state_1_created_at, self.state_1.created_at)
        self.assertEqual(state_1_updated_at, self.state_1.updated_at)

    def test_kwargs(self):
        """Test for correct instance creation from kwargs (dictionary)."""
        state_1_dict = self.state_1.to_dict()
        state_2 = State(**state_1_dict)

        self.assertIsInstance(state_2, State)
        self.assertIsNot(self.state_1, state_2)
        self.assertEqual(self.state_1.__dict__, state_2.__dict__)


class TestStateDoc(TestCase):
    "Tests documentation and pep8 for State class."

    @classmethod
    def setUpClass(cls):
        """Sets the whole functions of the class State to be inspected for
        correct documentation."""
        cls.functions = inspect.getmembers(State,
                                           inspect.isfunction(State))

    def test_doc_module(self):
        """Tests for docstring presence in the module and the class."""
        from models import state

        self.assertTrue(len(state.__doc__) > 0)
        self.assertTrue(len(state.State.__doc__) > 0)

    def test_doc_fun(self):
        """Tests for docstring presence in all functions of class."""
        for fun in self.functions:
            self.assertTrue(len(fun.__doc__) > 0)

    def test_pep8(self):
        """Tests pep8 style compliance of module and test files."""
        p8 = pep8.StyleGuide(quiet=False)

        res = p8.check_files(['models/state.py'])
        self.assertEqual(res.total_errors, 0,
                         "Found code style errors (and warnings).")
        res = p8.check_files(['tests/test_models/test_state.py'])
        self.assertEqual(res.total_errors, 0,
                         "Found code style errors (and warnings).")
