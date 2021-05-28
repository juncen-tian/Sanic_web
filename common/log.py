# -*- coding: utf-8 -*-

import g
import ujson
from config import config
from loguru import logger
from sanic.handlers import ErrorHandler
from common.handler import Handler
from common import util
import info

logger.configure(**config.LOG)


def log(request, status=g.HTTP_STATUS.status_200.value, message=''):
    if config.LOG_SERIALIZE:
        info = dict(
            spent_time=request.get('spent_time', 0),
            ip=str(request.get_header('X-Real-IP') or request.get_header('X-Forwarded-For') or request.ip),
            headers=dict(request.headers),
            method=request.method,
            path=request.path,
            status=status,
            query_string=request.query_string,
            form=request.form,
            userid=request.get('userid')
        )
        return ujson.dumps(info)
    else:
        info = list()
        # info.append(str(request.get('spent_time', 0)))
        info.append(str(request.path))
        info.append(str(request.method))
        info.append(str(status))
        info.append(str(request.query_string))
        info.append(str(request.form))
        info.append(str(dict(request.headers)))
        if not request.files:
            info.append(request.body.decode().replace('\n', '').replace('\r', ''))
        else:
            info.append('')
        info.append(str(message))
        return ' || '.join(info)


class CustomErrorHandler(ErrorHandler):
    def default(self, request: Handler, exception):
        status = getattr(exception, 'status_code', None) or g.HTTP_STATUS.status_500.value
        resp = request.error(msg=str(exception.args), status=status)
        if status not in g.HTTP_STATUS.status_400_list.value:
            logger.error('\n' + str(util.track()))
        logger.error(log(request, status=status, message=info.page_no_found))
        return resp
