import os
from pathlib import Path

import yaml

from tiny_storage import Storage
import unittest


class TinyStorageCase(unittest.TestCase):
    def setUp(self):
        self.storage = Storage('test')

    def tearDown(self):
        os.remove(os.getenv('HOME') / Path('.test.yaml'))

    def test_pull(self):
        os.system(r'echo "something: 1" > ~/.test.yaml')
        self.assertEqual(self.storage('something').pull(), 1)
        self.assertEqual(self.storage('another_thing').pull(), None)

    def test_push(self):
        os.system(r'echo "something: 1" > ~/.test.yaml')
        self.assertEqual(self.storage('something').push(), True)
        self.assertEqual(self.storage('another_thing').push(), True)

        with open(os.getenv('HOME') / Path('.test.yaml')) as f:
            self.assertEqual(dict(something=True, another_thing=True), yaml.safe_load(f))

    def test_put(self):
        os.system(r'echo "something: 1" > ~/.test.yaml')
        self.assertEqual(self.storage('something').put(), 1)
        self.assertEqual(self.storage('another_thing').put(), True)

        with open(os.getenv('HOME') / Path('.test.yaml')) as f:
            self.assertEqual(dict(something=1, another_thing=True), yaml.safe_load(f))
