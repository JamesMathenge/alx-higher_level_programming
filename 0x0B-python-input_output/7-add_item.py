#!/usr/bin/python3
"""This module adds all arguments to a Python list and save them to a file."""


import sys
from os.path import exists
from json import dump, load


def save_to_json_file(my_obj, filename):
    """
    Save an object to a JSON file.

    Args:
        my_obj: The object to be saved.
        filename (str): The name of the file.

    Returns:
        None
    """
    with open(filename, 'w') as file:
        dump(my_obj, file)


def load_from_json_file(filename):
    """
    Load an object from a JSON file.

    Args:
        filename (str): The name of the file.

    Returns:
        The loaded object.
    """
    with open(filename, 'r') as file:
        return load(file)


if __name__ == '__main__':
    filename = 'add_item.json'

    if exists(filename):
        my_list = load_from_json_file(filename)
    else:
        my_list = []

    my_list.extend(sys.argv[1:])
    save_to_json_file(my_list, filename)
