#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""Unit test for place.py"""
from models.base_model import BaseModel
from unittest import TestCase
from datetime import datetime
import uuid
import inspect
import pep8

class TestState(TestCase):
    """Test cases for Place class."""

    def setUp(self):
        """Setup for Place tests."""
        self.base_1 = Place()

    def test_instance(self):
        """Test for correct instancing of Place object."""
        self.assertIsInstance(self.base_1, Place)

    def test_empty_string(self):
        """Test for a empty string in the name instance."""
        name_empty = ""
        self.assertEqual(self.base_1.city_id, name_empty)
        self.assertEqual(self.base_1.user_id, name_empty)
        self.assertEqual(self.base_1.name, name_empty)
        self.assertEqual(self.base_1.description, name_empty)

    def test_int_value(self):
        """Test for a integrer value in the name instance."""
        int_test = 0
        self.assertEqual(self.base_1.number_rooms, int_test)
        self.assertEqual(self.base_1.number_bathrooms, int_test)
        self.assertEqual(self.base_1.max_guest, int_test)
        self.assertEqual(self.base_1.price_by_night, int_test)

    def test_int_value(self):
        """Test for a float value in the name instance."""
        float_test = 0.0
        self.assertEqual(self.base_1.latitude, float_test)
        self.assertEqual(self.base_1.longitude, float_test)
class TestBaseModelDoc(TestCase):
    "Tests documentation and pep8 for Place class."

    @classmethod
    def setUpClass(cls):
        """Sets the whole functions of the class Place to be inspected for
        correct documentation."""
        cls.functions = inspect.getmembers(Place,
                                           inspect.isfunction(Place))

    def test_doc_module(self):
        """Tests for docstring presence in the module and the class."""
        from models import base_model

        self.assertTrue(len(base_model.__doc__) > 0)
        self.assertTrue(len(base_model.Place.__doc__) > 0)

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