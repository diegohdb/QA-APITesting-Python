import json
from os.path import join, dirname
import time


def load_json_file(filename):
    absolute_path = join(dirname(__file__), filename)

    with open(absolute_path) as read_file:
        return json.loads(read_file.read())


def update_json_file(filename, newinfo):
    absolute_path = join(dirname(__file__), filename)

    with open(absolute_path, 'w') as write_file:
        json.dump(newinfo, write_file, indent=2)
