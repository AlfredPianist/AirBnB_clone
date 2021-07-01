#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""Unit test for place.py"""
from models.place import Place
from models.base_model import BaseModel
from models import storage

from unittest import TestCase
from datetime import datetime
import time
import os
import uuid
import inspect
import pep8


class TestPlace(TestCase):
    """Test cases for Place class."""

    def setUp(self):
        """Setup for Place tests."""
        self.place_1 = Place()

    def tearDown(self):
        """Clean test files."""
        if os.path.exists(storage._FileStorage__file_path):
            os.remove(storage._FileStorage__file_path)

    def test_instance(self):
        """Test for correct instancing of Place object."""
        self.assertIsInstance(self.place_1, Place)

    def test_inheritance(self):
        """Test for correct inheritance of Place object."""
        self.assertTrue(issubclass(type(self.place_1), BaseModel))

    def test_attribute_types(self):
        """Test for correct attribute types of Place object."""
        self.assertIsInstance(self.place_1.city_id, str)
        self.assertIsInstance(self.place_1.user_id, str)
        self.assertIsInstance(self.place_1.name, str)
        self.assertIsInstance(self.place_1.description, str)
        self.assertIsInstance(self.place_1.number_rooms, int)
        self.assertIsInstance(self.place_1.number_bathrooms, int)
        self.assertIsInstance(self.place_1.max_guest, int)
        self.assertIsInstance(self.place_1.price_by_night, int)
        self.assertIsInstance(self.place_1.latitude, float)
        self.assertIsInstance(self.place_1.longitude, float)

    def test_empty_string(self):
        """Test for empty string in Place instance."""
        self.assertEqual(self.place_1.city_id, "")
        self.assertEqual(self.place_1.user_id, "")
        self.assertEqual(self.place_1.name, "")
        self.assertEqual(self.place_1.description, "")

    def test_int_value(self):
        """Test for 0 integrer value in Place instance."""
        self.assertEqual(self.place_1.number_rooms, 0)
        self.assertEqual(self.place_1.number_bathrooms, 0)
        self.assertEqual(self.place_1.max_guest, 0)
        self.assertEqual(self.place_1.price_by_night, 0)

    def test_float_value(self):
        """Test for 0 float value in Place instance."""
        self.assertEqual(self.place_1.latitude, 0.0)
        self.assertEqual(self.place_1.longitude, 0.0)

    def test_id_creation(self):
        """Test for correct id creation and type."""
        place_1_id = eval("uuid.UUID('" + self.place_1.id + "')")
        self.assertIsInstance(place_1_id, uuid.UUID)

    def test_id_uniqueness(self):
        """Test for id uniqueness."""
        place_2 = Place()
        self.assertNotEqual(self.place_1.id, place_2.id)

    def test_datetime_creation(self):
        """Test for correct datetime creation and type."""
        self.assertIsInstance(self.place_1.created_at, datetime)
        self.assertIsInstance(self.place_1.updated_at, datetime)
        self.assertNotEqual(self.place_1.created_at, self.place_1.updated_at)

    def test_str_magic_method(self):
        """Test for correct __str__ output"""
        correct_output = "[Place] ({}) {}".format(
            self.place_1.id, self.place_1.__dict__)

        self.assertEqual(correct_output, self.place_1.__str__())

    def test_save(self):
        """Test for correct update of attribute updated_at"""
        old_updated_at = self.place_1.updated_at
        time.sleep(0.5)
        self.place_1.save()

        self.assertNotEqual(self.place_1.created_at, self.place_1.updated_at)
        self.assertNotEqual(self.place_1.updated_at, old_updated_at)

    def test_to_dict(self):
        """Test for correct dictionary type and output of to_dict method."""
        self.place_1.name = "Test"
        self.place_1.num = 1
        place_1_dict = self.place_1.to_dict()

        self.assertIsInstance(place_1_dict, dict)

        place_1_class = type(self.place_1).__name__
        self.assertIn(("__class__", place_1_class),
                      place_1_dict.items())
        self.assertNotIn(("__class__", place_1_class),
                         self.place_1.__dict__)

        place_1_created_at = self.place_1.created_at.isoformat()
        place_1_updated_at = self.place_1.updated_at.isoformat()
        self.assertIn(("created_at", place_1_created_at),
                      place_1_dict.items())
        self.assertIn(("updated_at", place_1_updated_at),
                      place_1_dict.items())

        isoformat = '%Y-%m-%dT%H:%M:%S.%f'
        place_1_created_at = datetime.strptime(place_1_dict["created_at"],
                                               isoformat)
        place_1_updated_at = datetime.strptime(place_1_dict["updated_at"],
                                               isoformat)
        self.assertEqual(place_1_created_at, self.place_1.created_at)
        self.assertEqual(place_1_updated_at, self.place_1.updated_at)

    def test_kwargs(self):
        """Test for correct instance creation from kwargs (dictionary)."""
        place_1_dict = self.place_1.to_dict()
        place_2 = Place(**place_1_dict)

        self.assertIsInstance(place_2, Place)
        self.assertIsNot(self.place_1, place_2)
        self.assertEqual(self.place_1.__dict__, place_2.__dict__)


class TestPlaceDoc(TestCase):
    "Tests documentation and pep8 for Place class."

    @classmethod
    def setUpClass(cls):
        """Sets the whole functions of the class Place to be inspected for
        correct documentation."""
        cls.functions = inspect.getmembers(Place,
                                           inspect.isfunction(Place))

    def test_doc_module(self):
        """Tests for docstring presence in the module and the class."""
        from models import place

        self.assertTrue(len(place.__doc__) > 0)
        self.assertTrue(len(place.Place.__doc__) > 0)

    def test_doc_fun(self):
        """Tests for docstring presence in all functions of class."""
        for fun in self.functions:
            self.assertTrue(len(fun.__doc__) > 0)

    def test_pep8(self):
        """Tests pep8 style compliance of module and test files."""
        p8 = pep8.StyleGuide(quiet=False)

        res = p8.check_files(['models/place.py'])
        self.assertEqual(res.total_errors, 0,
                         "Found code style errors (and warnings).")
        res = p8.check_files(['tests/test_models/test_place.py'])
        self.assertEqual(res.total_errors, 0,
                         "Found code style errors (and warnings).")
