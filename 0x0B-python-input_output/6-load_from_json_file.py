#!/usr/bin/python3
"""Creates an object from a JSON file and
Contains the load_from_json_file method.
    """

import json


def load_from_json_file(filename):
    """ Creates an object from a json file """
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)
