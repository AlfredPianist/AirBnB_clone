#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""Unit test for base_model.py"""
from models.base_model import BaseModel

from unittest import TestCase
from datetime import datetime
import uuid
import inspect
import pep8


class TestBaseModel(TestCase):
    """Test cases for BaseModel class."""

    def setUp(self):
        """Setup for BaseModel tests."""
        self.base_1 = BaseModel()

    def test_instance(self):
        """Test for correct instancing of BaseModel object."""
        self.assertIsInstance(self.base_1, BaseModel)

    def test_id_creation(self):
        """Test for correct id creation and type."""
        base_1_id = eval("uuid.UUID('" + self.base_1.id + "')")
        self.assertIsInstance(base_1_id, uuid.UUID)

    def test_id_uniqueness(self):
        """Test for id uniqueness."""
        base_2 = BaseModel()
        self.assertNotEqual(self.base_1.id, base_2.id)

    def test_datetime_creation(self):
        """Test for correct datetime creation and type."""
        self.assertIsInstance(self.base_1.created_at, datetime)
        self.assertIsInstance(self.base_1.updated_at, datetime)
        self.assertEqual(self.base_1.created_at, self.base_1.updated_at)

    def test_str_magic_method(self):
        """Test for correct __str__ output"""
        correct_output = "[BaseModel] ({}) {}".format(
            self.base_1.id, self.base_1.__dict__)

        self.assertEqual(correct_output, self.base_1.__str__())

    def test_save(self):
        """Test for correct update of attribute updated_at"""
        old_updated_at = self.base_1.updated_at
        self.base_1.save()

        self.assertNotEqual(self.base_1.created_at, self.base_1.updated_at)
        self.assertNotEqual(self.base_1.updated_at, old_updated_at)

    def test_to_dict(self):
        """Test for correct dictionary type and output of to_dict method."""
        self.base_1.name = "Test"
        self.base_1.num = 1
        base_1_dict = self.base_1.to_dict()

        self.assertIsInstance(base_1_dict, dict)

        base_1_class = type(self.base_1).__name__
        self.assertIn(("__class__", base_1_class),
                      base_1_dict.items())
        self.assertNotIn(("__class__", base_1_class),
                         self.base_1.__dict__)

        base_1_created_at = self.base_1.created_at.isoformat()
        base_1_updated_at = self.base_1.updated_at.isoformat()
        self.assertIn(("created_at", base_1_created_at),
                      base_1_dict.items())
        self.assertIn(("updated_at", base_1_updated_at),
                      base_1_dict.items())

        isoformat = '%Y-%m-%dT%H:%M:%S.%f'
        base_1_created_at = datetime.strptime(base_1_dict["created_at"],
                                              isoformat)
        base_1_updated_at = datetime.strptime(base_1_dict["updated_at"],
                                              isoformat)
        self.assertEqual(base_1_created_at, self.base_1.created_at)
        self.assertEqual(base_1_updated_at, self.base_1.updated_at)

    def test_kwargs(self):
        """Test for correct instance creation from kwargs (dictionary)."""
        base_1_dict = self.base_1.to_dict()
        base_2 = BaseModel(**base_1_dict)

        self.assertIsInstance(base_2, BaseModel)
        self.assertIsNot(self.base_1, base_2)
        self.assertEqual(self.base_1.__dict__, base_2.__dict__)


class TestBaseModelDoc(TestCase):
    "Tests documentation and pep8 for BaseModel class."

    @classmethod
    def setUpClass(cls):
        """Sets the whole functions of the class BaseModel to be inspected for
        correct documentation."""
        cls.functions = inspect.getmembers(BaseModel,
                                           inspect.isfunction(BaseModel))

    def test_doc_module(self):
        """Tests for docstring presence in the module and the class."""
        from models import base_model

        self.assertTrue(len(base_model.__doc__) > 0)
        self.assertTrue(len(base_model.BaseModel.__doc__) > 0)

    def test_doc_fun(self):
        """Tests for docstring presence in all functions of class."""
        for fun in self.functions:
            self.assertTrue(len(fun.__doc__) > 0)

    def test_pep8(self):
        """Tests pep8 style compliance of module and test files."""
        p8 = pep8.StyleGuide(quiet=False)

        res = p8.check_files(['models/base_model.py'])
        self.assertEqual(res.total_errors, 0,
                         "Found code style errors (and warnings).")
        res = p8.check_files(['tests/test_models/test_base_model.py'])
        self.assertEqual(res.total_errors, 0,
                         "Found code style errors (and warnings).")
