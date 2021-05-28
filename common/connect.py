# -*- coding: utf-8 -*-

from functools import wraps

def singleten(cls):
    _instances = {}

    @wraps(cls)
    def instance(*args, **kw):
        if cls.__name__ not in _instances:
            _instances[cls.__name__] = cls(*args, **kw)
        return _instances[cls.__name__]

    return instance