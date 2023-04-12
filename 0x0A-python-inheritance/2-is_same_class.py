#!/usr/bin/python3
"""Defines the function is_same_class()"""
def is_same_class(obj, a_class):
    """Returns True if the object an exact instance of the,
    specified class ; otherwise False
    Args:
        obj (a_class): object checks type.
        a_class (type): type to check.
    Returns:
        boolean: True or False
    """
    return type(obj) == a_class
