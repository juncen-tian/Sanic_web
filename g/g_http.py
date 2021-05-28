# -*- coding: utf-8 -*-

from .g_env import ENUM


class HTTP_STATUS(ENUM):
    status_200 = 200
    status_500 = 500
    status_400 = 400
    status_404 = 404
    status_403 = 403
    status_405 = 405
    status_400_list = [status_400, status_404, status_403, status_405]
    status_500_list = [status_500]


class HTTP_METHOD(ENUM):
    get = 'get'
    post = 'post'
    options = 'options'


class PARAM(ENUM):
    '''请求参数的'''
    pass
