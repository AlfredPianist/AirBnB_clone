#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""Unit test for review.py"""
from models.review import Review
from models.base_model import BaseModel
from models import storage

from unittest import TestCase
from datetime import datetime
import time
import os
import uuid
import inspect
import pep8


class TestReview(TestCase):
    """Test cases for Review class."""

    def setUp(self):
        """Setup for Review tests."""
        self.review_1 = Review()

    def tearDown(self):
        """Clean test files."""
        if os.path.exists(storage._FileStorage__file_path):
            os.remove(storage._FileStorage__file_path)

    def test_instance(self):
        """Test for correct instancing of Review object."""
        self.assertIsInstance(self.review_1, Review)

    def test_inheritance(self):
        """Test for correct inheritance of Review object."""
        self.assertTrue(issubclass(type(self.review_1), BaseModel))

    def test_attribute_types(self):
        """Test for correct attribute types of Review object."""
        self.assertIsInstance(self.review_1.place_id, str)
        self.assertIsInstance(self.review_1.user_id, str)
        self.assertIsInstance(self.review_1.text, str)

    def test_empty_string(self):
        """Test for empty string in Review instance."""
        self.assertEqual(self.review_1.place_id, "")
        self.assertEqual(self.review_1.user_id, "")
        self.assertEqual(self.review_1.text, "")

    def test_id_creation(self):
        """Test for correct id creation and type."""
        review_1_id = eval("uuid.UUID('" + self.review_1.id + "')")
        self.assertIsInstance(review_1_id, uuid.UUID)

    def test_id_uniqueness(self):
        """Test for id uniqueness."""
        review_2 = Review()
        self.assertNotEqual(self.review_1.id, review_2.id)

    def test_datetime_creation(self):
        """Test for correct datetime creation and type."""
        self.assertIsInstance(self.review_1.created_at, datetime)
        self.assertIsInstance(self.review_1.updated_at, datetime)

    def test_str_magic_method(self):
        """Test for correct __str__ output"""
        correct_output = "[Review] ({}) {}".format(
            self.review_1.id, self.review_1.__dict__)

        self.assertEqual(correct_output, self.review_1.__str__())

    def test_save(self):
        """Test for correct update of attribute updated_at"""
        old_updated_at = self.review_1.updated_at
        time.sleep(0.5)
        self.review_1.save()

        self.assertNotEqual(self.review_1.created_at, self.review_1.updated_at)
        self.assertNotEqual(self.review_1.updated_at, old_updated_at)

    def test_to_dict(self):
        """Test for correct dictionary type and output of to_dict method."""
        self.review_1.name = "Test"
        self.review_1.num = 1
        review_1_dict = self.review_1.to_dict()

        self.assertIsInstance(review_1_dict, dict)

        review_1_class = type(self.review_1).__name__
        self.assertIn(("__class__", review_1_class),
                      review_1_dict.items())
        self.assertNotIn(("__class__", review_1_class),
                         self.review_1.__dict__)

        review_1_created_at = self.review_1.created_at.isoformat()
        review_1_updated_at = self.review_1.updated_at.isoformat()
        self.assertIn(("created_at", review_1_created_at),
                      review_1_dict.items())
        self.assertIn(("updated_at", review_1_updated_at),
                      review_1_dict.items())

        isoformat = '%Y-%m-%dT%H:%M:%S.%f'
        review_1_created_at = datetime.strptime(review_1_dict["created_at"],
                                                isoformat)
        review_1_updated_at = datetime.strptime(review_1_dict["updated_at"],
                                                isoformat)
        self.assertEqual(review_1_created_at, self.review_1.created_at)
        self.assertEqual(review_1_updated_at, self.review_1.updated_at)

    def test_kwargs(self):
        """Test for correct instance creation from kwargs (dictionary)."""
        review_1_dict = self.review_1.to_dict()
        review_2 = Review(**review_1_dict)

        self.assertIsInstance(review_2, Review)
        self.assertIsNot(self.review_1, review_2)
        self.assertEqual(self.review_1.__dict__, review_2.__dict__)


class TestReviewDoc(TestCase):
    "Tests documentation and pep8 for Review class."

    @classmethod
    def setUpClass(cls):
        """Sets the whole functions of the class Review to be inspected for
        correct documentation."""
        cls.functions = inspect.getmembers(Review,
                                           inspect.isfunction(Review))

    def test_doc_module(self):
        """Tests for docstring presence in the module and the class."""
        from models import review

        self.assertTrue(len(review.__doc__) > 0)
        self.assertTrue(len(review.Review.__doc__) > 0)

    def test_doc_fun(self):
        """Tests for docstring presence in all functions of class."""
        for fun in self.functions:
            self.assertTrue(len(fun.__doc__) > 0)

    def test_pep8(self):
        """Tests pep8 style compliance of module and test files."""
        p8 = pep8.StyleGuide(quiet=False)

        res = p8.check_files(['models/review.py'])
        self.assertEqual(res.total_errors, 0,
                         "Found code style errors (and warnings).")
        res = p8.check_files(['tests/test_models/test_review.py'])
        self.assertEqual(res.total_errors, 0,
                         "Found code style errors (and warnings).")
