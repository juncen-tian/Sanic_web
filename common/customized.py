# -*- coding: utf-8 -*-

from enum import Enum


class ENUM(Enum):

    @classmethod
    def values(cls):
        return [item.value for item in cls._value2member_map_.values() if item]

    @classmethod
    def translate(cls, value):
        pass


class Dict(dict):
    def __init__(self, defaults: dict = {}):
        super().__init__({**defaults})

    def __getattr__(self, attr):
        try:
            return self[attr]
        except KeyError as ke:
            raise AttributeError("Config has no '{}'".format(ke.args[0]))

    def __setattr__(self, attr, value):
        self[attr] = value


if __name__ == '__main__':
    class ASK_MEDICAL_INTENT(ENUM):
        '''ai itent'''
        disease = 'disease'  # 疾病
        symptom = 'symptom'  # 症状
        medical_qa = 'medical_qa'  # 医疗问答
        authority = 'authority'  # 权威信息
        experience = 'experience'  # 健康经验


    print(dir(ASK_MEDICAL_INTENT))
    print(getattr(getattr(ASK_MEDICAL_INTENT, 'authority'), 'value'))
