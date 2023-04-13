#!/usr/bin/python3
"""saves object as json string in a file"""
import json


def save_to_json_file(my_obj, filename):
    """ a script adding arguments to a Python list,saves them to a file"""
    with open(filename, mode='w', encoding='utf-8') as f:
        f.write(json.dumps(my_obj))
