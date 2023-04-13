#!/usr/bin/python3
"""Save Object to a file
Contains the save_to_json_file method required
    """

import json


def save_to_json_file(my_obj, filename):
    """ Returns JSON a representation of the str object """
    with open(filename, 'w', encoding='utf-8') as f:
        return json.dump(my_obj, f)
