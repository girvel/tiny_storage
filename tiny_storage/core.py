import yaml
from .internals import pull, push, get_storage_path


class Storage:
    def __init__(self, name):
        self.name = name

    def __call__(self, key):
        return Entry(self.name, key)


class Entry:
    def __init__(self, name, key):
        self.name = name
        self.key = key

    def _act(self, function, value):
        path = get_storage_path(self.name)

        if path.exists():
            with open(path, 'r') as f:
                data = yaml.safe_load(f)
        else:
            data = {}

        was_modified, result = function(data, self.key.split('.'), value)

        if was_modified:
            with open(path, 'w') as f:
                yaml.safe_dump(data, f)

        return result

    def pull(self, value=None):
        return self._act(pull, value)

    def push(self, value=True):
        return self._act(push, value)
