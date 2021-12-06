from pathlib import Path

import yaml
import os


class Storage:
    def __init__(self, name):
        self.name = name

    def __call__(self, key):
        return Entry(self.name, key)


class Entry:
    def __init__(self, name, key):
        self.name = name
        self.key = key

    def pull(self, value=None):
        path = get_storage_path(self.name)

        if not path.exists():
            return value

        with open(path, 'r') as f:
            data = yaml.safe_load(f)

        return pull(data, self.key.split('.'), value)


def pull(data, path, value):
    if data is None:
        return value

    if len(path) == 0:
        return data

    if isinstance(data, dict):
        return pull(data.get(path[0]), path[1:], value)

    return value


def get_storage_path(name):
    return os.getenv('HOME') / Path(f".{name}.yaml")
