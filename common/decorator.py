# -*- coding: utf-8 -*-

from functools import wraps
from common.handler import Handler
from common.log import logger
from common import util


# 装饰器

def auth():
    """校验token和访问权限的装饰器"""

    def decorator(func):
        @wraps(func)
        async def wrapper(r: Handler, *args, **kwargs):
            if r.method == 'OPTIONS':
                return r.text('')
            else:
                return await func(r, *args, **kwargs)

        return wrapper

    return decorator


def db_exception():
    """校验token和访问权限的装饰器"""

    def decorator(func):
        @wraps(func)
        def wrapper(r: Handler, *args, **kwargs):
            try:
                return func(r, *args, **kwargs)
            except:
                logger.error(util.track())
                return None

        return wrapper

    return decorator



