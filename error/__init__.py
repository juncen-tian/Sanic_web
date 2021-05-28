# -*- coding: utf-8 -*-

ERROR_CODE_F1 = -1
ERROR_CODE_0 = 0
ERROR_CODE_1003 = 1003  # 用户名或者密码错误
ERROR_CODE_1004 = 1004  # 参数错误特殊码
ERROR_TOKEN_CODE_1005 = 1005  # token错误
ERROR_PERMISSION_CODE_1006 = 1006  # 没有访问权限
ERROR_NO_TOKEN_1007 = 1007  # 需要token参数
ERROR_VALID_ERROR_1008 = 1008  # 需要token参数

# 错误信息在此集中定义，方便后期维护和国际化
error_code = {
    ERROR_CODE_F1: '未知错误',
    ERROR_CODE_0: '成功',
    ERROR_CODE_1003: '用户名或者密码错误',
    ERROR_CODE_1004: '参数错误',
    ERROR_TOKEN_CODE_1005: '无效的token',
    ERROR_PERMISSION_CODE_1006: '没有访问权限',
    ERROR_NO_TOKEN_1007: '需要token参数',
    ERROR_VALID_ERROR_1008: '验证码输入错误'
}


class Successs(object):
    def __new__(cls, *args, **kwargs):
        if not kwargs.get('data'):
            kwargs['data'] = {}
        if not kwargs.get('msg'):
            kwargs['msg'] = error_code[ERROR_CODE_0]
        return dict(
            code=ERROR_CODE_0,
            msg=kwargs['msg'],
            data=kwargs['data']
        )


class Error(object):
    def __new__(cls, *args, **kwargs):
        return dict(
            code=kwargs['code'],
            msg=kwargs.get('msg') or error_code.get(kwargs['code']) or '',
            data=kwargs.get('data', {})
        )


class Error_500(object):
    '''http 500 错误'''

    def __new__(cls, *args, **kwargs):
        return dict(
            code=kwargs['code'],
            msg=kwargs.get('msg') or error_code.get(kwargs['code']) or '',
            error_msg=kwargs.get('error_msg', ''),
            data=kwargs.get('data', {})
        )
