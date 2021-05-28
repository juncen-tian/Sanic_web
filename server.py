# -*- coding: utf-8 -*-

import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import platform

# 查看系统类型
platform_ = platform.system()
system = 'windows'
if platform_ == "Windows":
    # system = f'D:\\zy-panel-api\\database\\windows\\panel.db'
    system = os.path.join(PROJECT_DIR, "\\zy-panel-api\\database\\windows", 'panel.db')
elif platform_ == "Linux":
    # system = f'zy-panel-api/database/linux'
    system = '/usr/local/bin/panel.db'
elif platform_ == "Mac":
    # system = '/usr/local/bin/panel.db'
    system = os.path.join(PROJECT_DIR, "\\zy-panel-api\\database\\macos", 'panel.db')

sqlite_engine = create_engine('sqlite:///' + system,
                              encoding='utf-8')


async def init_db(loop):
    '''初始化数据库'''
    pass


async def init_connect(loop):
    '''初始化连接'''
    init_result = True
    try:
        # session = sessionmaker(sqlite_engine)()
        # session.close()
        ...
    except Exception as e:
        init_result = False
        print('connect database failure', e)
    # try:
    #     ...
    # except:
    #     init_result = False
    #     logger.error(f'Redis连接错误')
    #     logger.error(str(util.track()))
    return init_result


async def init(app, loop):
    '''服务初始化'''
    init_result = True
    if not await init_connect(loop):
        init_result = False

    await init_db(loop)
    return init_result


if __name__ == '__main__':
    print(os.path.join(PROJECT_DIR, f'zy-panel-api\\database\\{system}', 'panel.db'))
