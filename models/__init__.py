#!/usr/bin/python3
"""Initializes the package"""
from models.engine.filestorage import FileStorage
storage = FileStorage()
storage.reload()
