# -*- coding: utf-8 -*-

import re
import error
import g
from sanic.request import Request
from sanic import response
import ujson


class Handler(Request):
    method_get = 'get'
    method_post = 'post'

    def get_method(self):
        return self.method.lower()

    async def template(self, tpl, **kwargs):
        env = self.app.jinja_env
        template = env.get_template(tpl)
        return response.html(await template.render_async(**kwargs))

    def _bool(self, value):
        '''
        转成布尔值
        :param value:
        :return:
        '''
        if value in ['true', 'false', 'undefined', 'null']:
            return {'true': True, 'false': False, 'undefined': False, 'null': False}[value]
        else:
            return bool(int(value))

    def get_int(self, key, data={}, default=None):
        try:
            return int(self.args.get(key) or self.form.get(key) or data.get(key, default))
        except:
            return default

    def get_obj(self, key, data={}, default={}):
        try:
            return ujson.loads(self.args.get(key) or self.form.get(key) or data.get(key, default))
        except:
            return default

    def get_json(self, default={}):
        try:
            return self.json
        except:
            return default

    def get_email(self, key, data={}, default=''):
        try:
            r_str = self.get_str(key, data=data)
            if r_str:
                return self.re_matten(r_str, g.Re.email.value)
            return default
        except:
            return default

    def get_url(self, key, data={}, default=''):
        try:
            r_str = self.get_str(key, data=data)
            if r_str:
                return self.re_matten(r_str, g.Re.url.value)
            return default
        except:
            return default

    def get_str(self, key, data=dict(), default=''):
        try:
            return str(self.args.get(key) or self.form.get(key) or data.get(key, default)).strip()
        except:
            return default

    def get_dict(self, key, data=dict(), default={}):
        try:
            return dict(data.get(key, default))
        except:
            return default

    def get_list(self, key, data=dict(), default=[]):
        try:
            return list(self.args.get(key) or self.form.get(key) or data.get(key, default))
        except:
            return default

    def get_bool(self, key, default=False):
        '''适配True、true、False、false'''
        try:
            temp = self.get_str(key).lower()
            return self._bool(temp)
        except:
            return default

    def get_float(self, key, data=dict(), default=None):

        try:
            return float(self.args.get(key) or self.form.get(key) or data.get(key, default))
        except:
            return None

    def re_matten(self, test_str, re_str, default=''):
        """
        正则验证
        :param test_str: 待测试字符串
        :param re_str: 正则表达式
        :return:
        """
        if re.match(re_str, str(test_str)):
            return test_str
        else:
            return default

    def get_file(self, key, default=None):
        try:
            file_metas = self.files.get(key, default)
            if not file_metas:
                return None
            return file_metas
        except Exception as e:
            return None

    def get_header(self, key, default=None):
        try:
            return self.headers.get(key, default)
        except:
            return default

    def success(self, data: dict = {}, msg: str = '', headers: dict = None) -> str:
        return response.json(error.Successs(data=data, msg=msg), headers=headers)

    def html(self, data, headers: dict = None):
        return response.html(data, headers=headers)

    def error(self, code=error.ERROR_CODE_F1, msg="", data={}, status=g.HTTP_STATUS.status_200.value):
        return response.json(error.Error(code=code, msg=msg or error.error_code.get(code), data=data), status=status)

    def login_error(self):
        return response.json(error.Error(code=error.ERROR_CODE_1003,
                                         msg=error.error_code.get('ERROR_CODE_1003')))

    def param_error(self, msg):
        """
        提示客户端参数错误
        :param desc:
        :return:
        """
        return response.json(error.Error(code=error.ERROR_CODE_1004,
                                         msg=msg))

    def text(self, data=''):
        return response.text(data)

    def redirect(self, url):
        return response.redirect(url)

    def valid_code_image(self, valid_code, image):
        resp = response.json(error.Successs(data={'image': image}, msg=''))
        resp.cookies['valid_code'] = valid_code
        return resp
