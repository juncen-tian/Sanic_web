# -*- coding: utf-8 -*-

from sqlalchemy.orm import sessionmaker
from server import sqlite_engine
from model.model_user import User
from common.decorator import db_exception


class BizUser(object):
    def __init__(self):
        try:
            self.session = sessionmaker(sqlite_engine)()
        except Exception as e:
            print('connect database failure', e)

    def __del__(self):
        self.session.close()

    @db_exception()
    def insert_user(self, username: str, password: str, user_type: int, equipment: str, data_tagging: str,
                    model_build: str, model_check: str) -> int:
        user_info = User(username=username, password=password, user_type=user_type, equipment=equipment,
                         data_tagging=data_tagging, model_build=model_build, model_check=model_check)
        self.session.add(user_info)
        self.session.commit()
        return user_info.id

    @db_exception()
    def update_user(self, user_id: int, user_type: int, **kwargs) -> bool:
        res = self.session.query(User).filter(User.id == user_id, User.user_type == user_type).update(kwargs)
        self.session.commit()
        if res:
            return True
        else:
            return False

    @db_exception()
    def delete_user(self, user_id: int) -> bool:
        res = self.session.query(User).filter(User.id == user_id).delete()
        self.session.commit()
        if res:
            return True
        else:
            return False

    @db_exception()
    def get_user_by_username_and_password(self, username: str, password: str):
        return self.session.query(User).filter(User.username == username, User.password == password).first()

    @db_exception()
    def get_user_by_user_id(self, user_id: int):
        return self.session.query(User).filter(User.id == user_id).first().to_dict()

    @db_exception()
    def get_user_pagination(self, offset=0, limit=10):
        ret = self.session.query(User).filter(User.user_type == 1).offset(offset).limit(limit).all()
        result = []
        if ret:
            for i in ret:
                result.append(i.to_dict_password())
        return result

    # @db_exception()
    # def get_equipment_pagination(self, offset=0, limit=10):
    #     ret = self.session.query(Equipment).offset(offset).limit(limit).all()
    #     result = []
    #     if ret:
    #         for i in ret:
    #             json_data = i.to_json()
    #             result.append(json_data)
    #     return result
    #
    # @db_exception()
    # def insert_equipment(self, name: str, ip: str, desc: str) -> int:
    #     equipment_info = Equipment(name=name, ip=ip, desc=desc)
    #     self.session.add(equipment_info)
    #     self.session.commit()
    #     return equipment_info.id
    #
    # @db_exception()
    # def update_equipment(self, equipment_id: int, **kwargs) -> bool:
    #     res = self.session.query(Equipment).filter(Equipment.id == equipment_id).update(kwargs)
    #     self.session.commit()
    #     if res:
    #         return True
    #     else:
    #         return False
    #
    # @db_exception()
    # def delete_equipment(self, equipment_id: int) -> bool:
    #     res = self.session.query(Equipment).filter(Equipment.id == equipment_id).delete()
    #     self.session.commit()
    #     if res:
    #         return True
    #     else:
    #         return False
