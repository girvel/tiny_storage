import os
from pathlib import Path


def pull(data, path, value):
    if data is None:  # FIXME value should go instead of undefined value, not None
        return value

    if len(path) == 0:
        return data

    if isinstance(data, dict):
        return pull(data.get(path[0]), path[1:], value)

    return value


def push(data, path, value):
    if len(path) == 0:
        return data

    assert isinstance(data, dict), "you can push value only into dict"  # FIXME there

    if path[0] in data:
        return push(data[path[0]], path[1:], value)

    if len(path) == 1:
        data[path[0]] = value
        return value

    data[path[0]] = {}
    return push(data[path[0]], path[1:], value)


def get_storage_path(name):
    return os.getenv('HOME') / Path(f".{name}.yaml")
