# -*- coding: utf-8 -*-

import argparse


class command(object):
    args = None

    def __new__(cls, *args, **kwargs):
        if not command.args:
            command_args = argparse.ArgumentParser(prog='Haxitag task lets')
            command_args.add_argument('-e', '--env', required=False, action='store', type=str, default='other',
                                      help='运行环境')
            command.args = command_args.parse_args()
        return command.args


command()
