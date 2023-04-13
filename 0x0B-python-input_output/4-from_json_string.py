#!/usr/bin/python3
""" From JSON string to Object
Contains the from_json_string method needed
    """

import json


def from_json_string(my_str):
    """ Returns the object represented by a JSON string """
    return json.loads(my_str)
