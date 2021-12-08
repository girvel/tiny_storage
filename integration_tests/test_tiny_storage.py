import os
from pathlib import Path

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
