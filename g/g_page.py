# -*- coding: utf-8 -*-

from .g_env import ENUM


class PAGENUM(ENUM):
    common = 10  # 通用
    large = 20


class PAGE_DIRECTION(ENUM):
    next = 'next'  # 获取下一页
    prev = 'prev'  # 获取上一页
