from sqlalchemy.ext.declarative import declarative_base

from server import sqlite_engine
from sqlalchemy import Column, Integer, String

Base = declarative_base()


# class Equipment(Base):
#     __tablename__ = 'Equipment'
#     __table_args__ = {'extend_existing': True}
#
#     id = Column('ID', Integer, primary_key=True, autoincrement=True)
#     name = Column('NAME', String(length=255), nullable=False)
#     ip = Column('IP', String(length=255), nullable=False)
#     desc = Column('DESC', Text, nullable=False)
#
#     @staticmethod
#     def create_database_table():
#         Base.metadata.create_all(sqlite_engine)
#         print('CREATE TABLE Equipment SUCCESS')
#
#     def to_json(self):
#         dict = self.__dict__
#
#         if "_sa_instance_state" in dict:
#             del dict["_sa_instance_state"]
#
#         return dict


class User(Base):
    __tablename__ = 'User'
    __table_args__ = {'extend_existing': True}

    id = Column('ID', Integer, primary_key=True, autoincrement=True)
    username = Column('USERNAME', String(length=255), nullable=False, unique=True)
    password = Column('PASSWORD', String(length=255), nullable=False)
    user_type = Column('USER_TYPE', Integer, nullable=False)
    equipment = Column('EQUIPMENT', String(length=255), nullable=True)
    data_tagging = Column('DATA_TAGGING', String(length=255), nullable=True)
    model_build = Column('MODEL_BUILD', String(length=255), nullable=True)
    model_check = Column('MODEL_CHECK', String(length=255), nullable=True)

    @staticmethod
    def create_database_table():
        Base.metadata.create_all(sqlite_engine)
        print('CREATE TABLE User SUCCESS')

    def to_json(self):
        dict = self.__dict__

        if "_sa_instance_state" in dict:
            del dict["_sa_instance_state"]

        return dict

    def to_dict(self):
        return dict(
            id=self.id,
            username=self.username,
            user_type=self.user_type,
            data_tagging=self.data_tagging,
            model_build=self.model_build,
            model_check=self.model_check,
            equipment=self.equipment
        )

    def to_dict_password(self):
        return dict(
            id=self.id,
            username=self.username,
            password=self.password,
            user_type=self.user_type,
            data_tagging=self.data_tagging,
            model_build=self.model_build,
            model_check=self.model_check,
            equipment=self.equipment
        )


if __name__ == '__main__':
    Base.metadata.drop_all(sqlite_engine)
    # Equipment.create_database_table()
    User.create_database_table()
