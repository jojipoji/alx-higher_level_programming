#!/usr/bin/python3
"""To JSON string
Contains the to_json_string method needed
    """

import json


def to_json_string(my_obj):
    """ Returns JSON representation of an str object """
    return json.dumps(my_obj)
