# -*- coding: utf-8 -*-

import g
import server

from config import config
from common import util
from common.handler import Handler
from common.log import logger, CustomErrorHandler, log
from sanic import Sanic, response
from sanic.response import HTTPResponse
from sanic.request import Request

# from sanic_session import Session, InMemorySessionInterface

sanic_app = Sanic(name=config.SERVER_NAME, request_class=Handler, strict_slashes=True,
                  error_handler=CustomErrorHandler(),
                  configure_logging=False
                  )


# session = Session(sanic_app, interface=InMemorySessionInterface())


@sanic_app.middleware('request')
async def add_start_time(request: Handler):
    # request['start_time'] = util.time()
    ...


@sanic_app.middleware('response')
async def access_log(r: Handler, response: HTTPResponse):
    # response.headers['Access-Control-Allow-Origin'] = '*'
    # response.headers['Access-Control-Allow-Methods'] = 'GET, POST, OPTIONS, HEAD, CONNECT, PUT, DELETE, TRACE, PATCH'
    # response.headers['Access-Control-Allow-Headers'] = '*, Origin, X-Requested-With, Content-Type, Accept, token'
    # response.headers['Timing-Allow-Origin'] = '*'
    if response.status == g.HTTP_STATUS.status_200.value:
        # r['spent_time'] = util.time() - r['start_time']
        logger.success(log(request=r, status=response.status, message=''))


@sanic_app.listener('before_server_start')
async def before_server_start(sanic: Sanic, loop):
    stop = False
    try:
        if not await server.init(app=sanic, loop=loop):
            stop = True
    except Exception as e:
        stop = True
        logger.error(util.track())
    import handler
    sanic.blueprint(handler.blue_print_group)
    if stop:
        sanic.stop()
        logger.error('Server stop failed!!!!')


@sanic_app.listener('after_server_start')
async def after_server_start(app, loop):
    logger.info('server started on port %d' % config.SERVER_PORT)


class Result(object):

    def __new__(cls, *args, **kwargs):
        return dict(
            code=kwargs.get('code', -1),
            msg=kwargs.get('msg', ''),
            data=kwargs.get('data', {})
        )


@sanic_app.route('/check', methods=['GET'])
async def check(r: Request):
    return response.json(dict(code=0, msg='success'))


if __name__ == '__main__':
    for item in dir(config):
        if not item.startswith('__'):
            logger.info(str(item) + ' : ' + str(getattr(config, item)))
    sanic_app.run(host='0.0.0.0', port=config.SERVER_PORT)
