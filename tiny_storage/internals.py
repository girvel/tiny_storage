import os
from pathlib import Path


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
