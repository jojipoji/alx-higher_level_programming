#!/usr/bin/python3
""" Load, add and save

Script adding arguments to a Python list, and then saves them to a file.
    """

import sys

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"

try:
        my_list = load_from_json_file(filename)
except FileNotFoundError:
        my_list = []
save_to_json_file(my_list + sys.argv[1:], filename)
