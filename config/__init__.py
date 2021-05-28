# -*- coding: utf-8 -*-

import os
import sys
import json
from common.command_line import command

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


class config(object):
    ROOT = ROOT
    LOCALE_PATH = os.path.join(ROOT, 'translations')


with open(os.path.join(ROOT, f'config/{command.args.env.strip()}.json')) as config_file:
    conf = json.load(config_file)
    for key, value in conf.items():
        setattr(config, key, value)
LOG = {
    "handlers": [
        {
            'sink': sys.stdout,
            'format': '{message}',
            'serialize': config.LOG_SERIALIZE
        }
    ]
}
setattr(config, "LOG", LOG)
