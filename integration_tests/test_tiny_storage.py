import os
import sys
from pathlib import Path

import yaml

from tiny_storage import Unit, SafetyException
import unittest


def get_storage_path(name):
    if sys.platform.startswith("linux"):
        return os.getenv("HOME") / Path(f".{name}.yaml")

    if sys.platform.startswith("win"):
        return os.getenv("APPDATA") / Path(f"{name}/{name}.yaml")

    raise Exception(f"Platform {sys.platform} is not supported.")


class DataFileExistsCase(unittest.TestCase):
    def setUp(self):
        self.unit = Unit("test")
        path = get_storage_path("test")
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text("something: 1")

    def tearDown(self):
        os.remove(get_storage_path("test"))

    def test_pull(self):
        self.assertEqual(self.unit("something").pull(), 1)
        self.assertEqual(self.unit("another_thing").pull(), None)

    def test_push(self):
        self.assertEqual(self.unit("something").push(), True)
        self.assertEqual(self.unit("another_thing").push(), True)

        with open(get_storage_path("test")) as f:
            self.assertEqual(
                dict(something=True, another_thing=True), yaml.safe_load(f)
            )

    def test_push(self):
        class UnsafeType:
            pass

        self.assertRaises(
            SafetyException, lambda: self.unit("something").push(UnsafeType())
        )

    def test_put(self):
        self.assertEqual(self.unit("something").put(), 1)
        self.assertEqual(self.unit("another_thing").put(), True)

        with open(get_storage_path("test")) as f:
            self.assertEqual(dict(something=1, another_thing=True), yaml.safe_load(f))
