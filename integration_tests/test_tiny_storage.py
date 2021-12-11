import os
import sys
from pathlib import Path

import yaml

from tiny_storage import Storage
import unittest


def get_storage_path(name):
    if sys.platform.startswith('linux'):
        return os.getenv('HOME') / Path(f".{name}.yaml")

    if sys.platform.startswith('win'):
        return os.getenv('APPDATA') / Path(f"{name}/{name}.yaml")

    raise Exception(f"Platform {sys.platform} is not supported.")


class TinyStorageCase(unittest.TestCase):
    def setUp(self):
        self.storage = Storage('test')

    def tearDown(self):
        os.remove(get_storage_path('test'))

    def test_pull(self):
        os.system(f'echo "something: 1" > {get_storage_path()}')
        self.assertEqual(self.storage('something').pull(), 1)
        self.assertEqual(self.storage('another_thing').pull(), None)

    def test_push(self):
        os.system(f'echo "something: 1" > {get_storage_path()}')
        self.assertEqual(self.storage('something').push(), True)
        self.assertEqual(self.storage('another_thing').push(), True)

        with open(get_storage_path('test')) as f:
            self.assertEqual(dict(something=True, another_thing=True), yaml.safe_load(f))

    def test_put(self):
        os.system(f'echo "something: 1" > {get_storage_path()}')
        self.assertEqual(self.storage('something').put(), 1)
        self.assertEqual(self.storage('another_thing').put(), True)

        with open(get_storage_path('test')) as f:
            self.assertEqual(dict(something=1, another_thing=True), yaml.safe_load(f))
