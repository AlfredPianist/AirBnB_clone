#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""Unit test for city.py"""
from models.city import City
from models.base_model import BaseModel
from models import storage

from unittest import TestCase
from datetime import datetime
import time
import os
import uuid
import inspect
import pep8


class TestCity(TestCase):
    """Test cases for City class."""

    def setUp(self):
        """Setup for City tests."""
        self.city_1 = City()

    def tearDown(self):
        """Clean test files."""
        if os.path.exists(storage._FileStorage__file_path):
            os.remove(storage._FileStorage__file_path)

    def test_instance(self):
        """Test for correct instancing of City object."""
        self.assertIsInstance(self.city_1, City)

    def test_inheritance(self):
        """Test for correct inheritance of City object."""
        self.assertTrue(issubclass(type(self.city_1), BaseModel))

    def test_attribute_types(self):
        """Test for correct attribute types of City object."""
        self.assertIsInstance(self.city_1.name, str)

    def test_empty_string(self):
        """Test for empty string in City instance."""
        self.assertEqual(self.city_1.city_id, "")
        self.assertEqual(self.city_1.name, "")

    def test_id_creation(self):
        """Test for correct id creation and type."""
        city_1_id = eval("uuid.UUID('" + self.city_1.id + "')")
        self.assertIsInstance(city_1_id, uuid.UUID)

    def test_id_uniqueness(self):
        """Test for id uniqueness."""
        city_2 = City()
        self.assertNotEqual(self.city_1.id, city_2.id)

    def test_datetime_creation(self):
        """Test for correct datetime creation and type."""
        self.assertIsInstance(self.city_1.created_at, datetime)
        self.assertIsInstance(self.city_1.updated_at, datetime)
        self.assertEqual(self.city_1.created_at, self.city_1.updated_at)

    def test_str_magic_method(self):
        """Test for correct __str__ output"""
        correct_output = "[City] ({}) {}".format(
            self.city_1.id, self.city_1.__dict__)

        self.assertEqual(correct_output, self.city_1.__str__())

    def test_save(self):
        """Test for correct update of attribute updated_at"""
        old_updated_at = self.city_1.updated_at
        time.sleep(0.5)
        self.city_1.save()

        self.assertNotEqual(self.city_1.created_at, self.city_1.updated_at)
        self.assertNotEqual(self.city_1.updated_at, old_updated_at)

    def test_to_dict(self):
        """Test for correct dictionary type and output of to_dict method."""
        self.city_1.name = "Test"
        self.city_1.num = 1
        city_1_dict = self.city_1.to_dict()

        self.assertIsInstance(city_1_dict, dict)

        city_1_class = type(self.city_1).__name__
        self.assertIn(("__class__", city_1_class),
                      city_1_dict.items())
        self.assertNotIn(("__class__", city_1_class),
                         self.city_1.__dict__)

        city_1_created_at = self.city_1.created_at.isoformat()
        city_1_updated_at = self.city_1.updated_at.isoformat()
        self.assertIn(("created_at", city_1_created_at),
                      city_1_dict.items())
        self.assertIn(("updated_at", city_1_updated_at),
                      city_1_dict.items())

        isoformat = '%Y-%m-%dT%H:%M:%S.%f'
        city_1_created_at = datetime.strptime(city_1_dict["created_at"],
                                              isoformat)
        city_1_updated_at = datetime.strptime(city_1_dict["updated_at"],
                                              isoformat)
        self.assertEqual(city_1_created_at, self.city_1.created_at)
        self.assertEqual(city_1_updated_at, self.city_1.updated_at)

    def test_kwargs(self):
        """Test for correct instance creation from kwargs (dictionary)."""
        city_1_dict = self.city_1.to_dict()
        city_2 = City(**city_1_dict)

        self.assertIsInstance(city_2, City)
        self.assertIsNot(self.city_1, city_2)
        self.assertEqual(self.city_1.__dict__, city_2.__dict__)


class TestCityDoc(TestCase):
    "Tests documentation and pep8 for City class."

    @classmethod
    def setUpClass(cls):
        """Sets the whole functions of the class City to be inspected for
        correct documentation."""
        cls.functions = inspect.getmembers(City,
                                           inspect.isfunction(City))

    def test_doc_module(self):
        """Tests for docstring presence in the module and the class."""
        from models import city

        self.assertTrue(len(city.__doc__) > 0)
        self.assertTrue(len(city.City.__doc__) > 0)

    def test_doc_fun(self):
        """Tests for docstring presence in all functions of class."""
        for fun in self.functions:
            self.assertTrue(len(fun.__doc__) > 0)

    def test_pep8(self):
        """Tests pep8 style compliance of module and test files."""
        p8 = pep8.StyleGuide(quiet=False)

        res = p8.check_files(['models/city.py'])
        self.assertEqual(res.total_errors, 0,
                         "Found code style errors (and warnings).")
        res = p8.check_files(['tests/test_models/test_city.py'])
        self.assertEqual(res.total_errors, 0,
                         "Found code style errors (and warnings).")
