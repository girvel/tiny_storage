from ._version import __version__
from .core import Storage, Entry

__all__ = [e.__name__ for e in (Storage, Entry)]
