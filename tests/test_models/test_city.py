#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""Unit test for city.py"""
from models.base_model import BaseModel
from models.city import City
from unittest import TestCase
from datetime import datetime
import uuid
import inspect
import pep8

class TestState(TestCase):
    """Test cases for City class."""

    def setUp(self):
        """Setup for City tests."""
        self.base_1 = City()

    def test_instance(self):
        """Test for correct instancing of City object."""
        self.assertIsInstance(self.base_1, City)

    def test_empty_string(self):
        """Test for a empty string in the name instance."""
        name_empty = ""
        self.assertEqual(self.base_1.state_id, name_empty)
        self.assertEqual(self.base_1.name, name_empty)
    
class TestBaseModelDoc(TestCase):
    "Tests documentation and pep8 for City class."

    @classmethod
    def setUpClass(cls):
        """Sets the whole functions of the class City to be inspected for
        correct documentation."""
        cls.functions = inspect.getmembers(City,
                                           inspect.isfunction(City))

    def test_doc_module(self):
        """Tests for docstring presence in the module and the class."""
        from models import base_model

        self.assertTrue(len(base_model.__doc__) > 0)
        self.assertTrue(len(base_model.City.__doc__) > 0)

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