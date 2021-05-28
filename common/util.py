# -*- coding: utf-8 -*-

import time as t
import traceback
import hashlib
import random
from io import BytesIO

from PIL import Image, ImageDraw, ImageFont
import base64

"""英文title_hash值"""


def track():
    return str(traceback.format_exc())


def time():
    '''计算毫秒值'''
    return int(t.time() * 1000)


def time_to_timestamp(rtime):
    try:
        timeArray = t.strptime(rtime, "%Y-%m-%d %H:%M:%S")
        timeStamp = int(t.mktime(timeArray)) * 1000
        return timeStamp
    except:
        return False


def md5(text=str(time()), bits=32):
    md5_func = hashlib.md5()
    md5_func.update(bytes(str(text), encoding='utf-8'))
    if bits == 16:
        return md5_func.hexdigest()[8: -8]
    else:
        return md5_func.hexdigest()


def get_random_color():
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))


def get_valid_code_img():
    img = Image.new('RGB', (167, 67), color=(255, 255, 255))
    draw = ImageDraw.Draw(img)
    kumo_font = ImageFont.truetype('./static/font/KumoFont.ttf', size=30)

    valid_code_str = ''
    for i in range(5):
        random_num = str(random.randint(0, 9))
        random_low_alpha = chr(random.randint(97, 122))
        random_high_alpha = chr(random.randint(65, 90))
        random_char = random.choice([random_num, random_low_alpha, random_high_alpha])
        draw.text((i * 32 + 10, 17), random_char, get_random_color(), font=kumo_font)

        # 保存验证码字符串
        valid_code_str += random_char

    # 噪点噪线
    width = 167
    height = 67
    for i in range(5):
        x1 = random.randint(0, width)
        x2 = random.randint(0, width)
        y1 = random.randint(0, height)
        y2 = random.randint(0, height)
        draw.line((x1, y1, x2, y2), fill=get_random_color())

    for i in range(5):
        draw.point([random.randint(0, width), random.randint(0, height)], fill=get_random_color())
        x = random.randint(0, width)
        y = random.randint(0, height)
        draw.arc((x, y, x + 4, y + 4), 0, 90, fill=get_random_color())

    f = BytesIO()  # 用完之后，BytesIO会自动清掉
    img.save(f, 'png')
    data = f.getvalue()
    base64_data = 'data:image/png;base64,' + str(base64.b64encode(data), 'utf-8')

    return dict(valid_code=valid_code_str, img=base64_data)


if __name__ == '__main__':
    # print(sha256())
    # print(get_day_time(n=-1))
    # time_str = '2020-09-14T16:18:15+08:00'
    # print(format_time(time_str))
    pass
