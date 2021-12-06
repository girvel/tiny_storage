import yaml
from .internals import pull, get_storage_path


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
