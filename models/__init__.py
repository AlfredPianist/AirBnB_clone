#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""Initialization file reloading all persistent instances for all model
modules
"""
from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
