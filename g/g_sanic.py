# -*- coding: utf-8 -*-

from .g_env import *


class SANIC_METHOD(ENUM):
    get = ['GET', 'OPTIONS']
    post = ['POST', 'OPTIONS']
    get_post = ['GET', 'POST', 'OPTIONS']
