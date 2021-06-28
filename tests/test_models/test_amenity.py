#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""Unit test for amenity.py"""
from models.amenity import Amenity
from models.base_model import BaseModel
from models import storage

from unittest import TestCase
from datetime import datetime
import os
import uuid
import inspect
import pep8


class TestAmenity(TestCase):
    """Test cases for Amenity class."""

    def setUp(self):
        """Setup for Amenity tests."""
        self.amenity_1 = Amenity()

    def tearDown(self):
        """Clean test files."""
        if os.path.exists(storage._FileStorage__file_path):
            os.remove(storage._FileStorage__file_path)

    def test_instance(self):
        """Test for correct instancing of Amenity object."""
        self.assertIsInstance(self.amenity_1, Amenity)

    def test_inheritance(self):
        """Test for correct inheritance of Amenity object."""
        self.assertTrue(issubclass(type(self.amenity_1), BaseModel))

    def test_attribute_types(self):
        """Test for correct attribute types of Amenity object."""
        self.assertIsInstance(self.amenity_1.name, str)

    def test_empty_string(self):
        """Test for empty string in Amenity instance."""
        self.assertEqual(self.amenity_1.name, "")

    def test_id_creation(self):
        """Test for correct id creation and type."""
        amenity_1_id = eval("uuid.UUID('" + self.amenity_1.id + "')")
        self.assertIsInstance(amenity_1_id, uuid.UUID)

    def test_id_uniqueness(self):
        """Test for id uniqueness."""
        amenity_2 = Amenity()
        self.assertNotEqual(self.amenity_1.id, amenity_2.id)

    def test_datetime_creation(self):
        """Test for correct datetime creation and type."""
        self.assertIsInstance(self.amenity_1.created_at, datetime)
        self.assertIsInstance(self.amenity_1.updated_at, datetime)
        self.assertEqual(self.amenity_1.created_at, self.amenity_1.updated_at)

    def test_str_magic_method(self):
        """Test for correct __str__ output"""
        correct_output = "[Amenity] ({}) {}".format(
            self.amenity_1.id, self.amenity_1.__dict__)

        self.assertEqual(correct_output, self.amenity_1.__str__())

    def test_save(self):
        """Test for correct update of attribute updated_at"""
        old_updated_at = self.amenity_1.updated_at
        self.amenity_1.save()

        self.assertNotEqual(self.amenity_1.created_at,
                            self.amenity_1.updated_at)
        self.assertNotEqual(self.amenity_1.updated_at, old_updated_at)

    def test_to_dict(self):
        """Test for correct dictionary type and output of to_dict method."""
        self.amenity_1.name = "Test"
        self.amenity_1.num = 1
        amenity_1_dict = self.amenity_1.to_dict()

        self.assertIsInstance(amenity_1_dict, dict)

        amenity_1_class = type(self.amenity_1).__name__
        self.assertIn(("__class__", amenity_1_class),
                      amenity_1_dict.items())
        self.assertNotIn(("__class__", amenity_1_class),
                         self.amenity_1.__dict__)

        amenity_1_created_at = self.amenity_1.created_at.isoformat()
        amenity_1_updated_at = self.amenity_1.updated_at.isoformat()
        self.assertIn(("created_at", amenity_1_created_at),
                      amenity_1_dict.items())
        self.assertIn(("updated_at", amenity_1_updated_at),
                      amenity_1_dict.items())

        isoformat = '%Y-%m-%dT%H:%M:%S.%f'
        amenity_1_created_at = datetime.strptime(amenity_1_dict["created_at"],
                                                 isoformat)
        amenity_1_updated_at = datetime.strptime(amenity_1_dict["updated_at"],
                                                 isoformat)
        self.assertEqual(amenity_1_created_at, self.amenity_1.created_at)
        self.assertEqual(amenity_1_updated_at, self.amenity_1.updated_at)

    def test_kwargs(self):
        """Test for correct instance creation from kwargs (dictionary)."""
        amenity_1_dict = self.amenity_1.to_dict()
        amenity_2 = Amenity(**amenity_1_dict)

        self.assertIsInstance(amenity_2, Amenity)
        self.assertIsNot(self.amenity_1, amenity_2)
        self.assertEqual(self.amenity_1.__dict__, amenity_2.__dict__)


class TestAmenityDoc(TestCase):
    "Tests documentation and pep8 for Amenity class."

    @classmethod
    def setUpClass(cls):
        """Sets the whole functions of the class Amenity to be inspected for
        correct documentation."""
        cls.functions = inspect.getmembers(Amenity,
                                           inspect.isfunction(Amenity))

    def test_doc_module(self):
        """Tests for docstring presence in the module and the class."""
        from models import amenity

        self.assertTrue(len(amenity.__doc__) > 0)
        self.assertTrue(len(amenity.Amenity.__doc__) > 0)

    def test_doc_fun(self):
        """Tests for docstring presence in all functions of class."""
        for fun in self.functions:
            self.assertTrue(len(fun.__doc__) > 0)

    def test_pep8(self):
        """Tests pep8 style compliance of module and test files."""
        p8 = pep8.StyleGuide(quiet=False)

        res = p8.check_files(['models/amenity.py'])
        self.assertEqual(res.total_errors, 0,
                         "Found code style errors (and warnings).")
        res = p8.check_files(['tests/test_models/test_amenity.py'])
        self.assertEqual(res.total_errors, 0,
                         "Found code style errors (and warnings).")
