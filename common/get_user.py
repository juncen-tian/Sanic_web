from functools import wraps
from common.handler import Handler
from common.jwt_func import decode_jwt
import error
from typing import List


def get_user(user_type: List[int]):
    """校验token和访问权限的装饰器"""

    def decorator(func):
        @wraps(func)
        async def wrapper(r: Handler, *args, **kwargs):
            # 检查登录状态
            token = r.get_header('token')
            if not token:
                return r.error(code=error.ERROR_NO_TOKEN_1007,
                               msg=error.error_code.get('ERROR_NO_TOKEN_1007'))
            user_info = decode_jwt(token)
            if not user_info:
                return r.error(code=error.ERROR_TOKEN_CODE_1005,
                               msg=error.error_code.get('ERROR_TOKEN_CODE_1005'))
            if user_info.get('user_type') not in user_type:
                return r.error(code=error.ERROR_PERMISSION_CODE_1006,
                               msg=error.error_code.get('ERROR_PERMISSION_CODE_1006'))
            r.ctx.__setattr__('user_info', user_info)
            return await func(r, *args, **kwargs)

        return wrapper

    return decorator
