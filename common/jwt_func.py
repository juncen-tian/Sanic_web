import time
import jwt


def generate_jwt(user_id: int, user_name: str, user_type: int) -> str:
    # payload
    payload = {'iat': int(time.time()), 'username': user_name, 'user_id': user_id,
               'exp': int(time.time()) + 60 * 60 * 24, 'user_type': user_type}
    """payload 中一些固定参数名称的意义, 同时可以在payload中自定义参数"""
    # exp 【expiration】 该jwt销毁的时间；unix时间戳
    # iat   【issued at】 该jwt的发布时间；unix 时间戳

    # headers
    headers = {
        'alg': "HS256",  # 声明所使用的算法
    }

    secret = 'HN^k1M31udP*t%!E#BX^0OzXclHii#'

    jwt_token = jwt.encode(payload, secret, algorithm="HS256", headers=headers)

    return jwt_token


def decode_jwt(token):
    data = None
    secret = 'HN^k1M31udP*t%!E#BX^0OzXclHii#'
    try:
        data = jwt.decode(token, secret, algorithms=['HS256'])
    except Exception as e:
        print(e)
    return data


if __name__ == '__main__':
    user_id = 1
    user_name = 'name'
    token = generate_jwt(user_id, user_name)
    print(token)
    data = decode_jwt(token)
    print(data)
