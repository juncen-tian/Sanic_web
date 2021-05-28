# -*- coding: utf-8 -*-

import re
import os
from sanic import Blueprint

dir_path = os.listdir(os.path.dirname(__file__))
api_files = [x for x in dir_path if re.findall('handler_[A-Za-z]\w+\.py$', x)]
blue_prints = []
for api_file in api_files:
    model_name = api_file[:-3]
    a = __import__(model_name, globals(), locals(), [model_name], 1)
    blue_prints.extend([getattr(a, item) for item in dir(a) if isinstance(getattr(a, item, None), Blueprint)])

blue_print_group = Blueprint.group(*blue_prints, url_prefix='/panel')
