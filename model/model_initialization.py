from sqlalchemy import Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy import create_engine
import os
import platform

Base = declarative_base()
PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

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

sqlite_engine = create_engine('sqlite:///' + system, encoding='utf-8')


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
        return True


# class Equipment(Base):
#     __tablename__ = 'Equipment'
#     __table_args__ = {'extend_existing': True}
#
#     id = Column('ID', Integer, primary_key=True, autoincrement=True)
#     name = Column('NAME', String(length=255), nullable=False)
#     ip = Column('IP', String(length=255), nullable=False)
#     desc = Column('DESC', Text, nullable=False)
#
#
# class User(Base):
#     __tablename__ = 'User'
#     __table_args__ = {'extend_existing': True}
#
#     id = Column('ID', Integer, primary_key=True, autoincrement=True)
#     username = Column('USERNAME', String(length=255), nullable=False, unique=True)
#     password = Column('PASSWORD', String(length=255), nullable=False)
#     equipment_id = Column('EQUIPMENT_ID', Integer, ForeignKey("Equipment.ID"), nullable=True)
#     user_type = Column('USER_TYPE', Integer, nullable=False)
#     equipment = relationship("Equipment", backref="user_of_equipment")
#     data_tagging = Column('DATA_TAGGING', String(length=255), nullable=True)
#     model_build = Column('MODEL_BUILD', String(length=255), nullable=True)
#     model_check = Column('MODEL_CHECK', String(length=255), nullable=True)
#
#     @staticmethod
#     def create_database_table():
#         Base.metadata.create_all(sqlite_engine)
#         print('CREATE TABLE User SUCCESS')
#         return True


if __name__ == '__main__':
    Base.metadata.drop_all(sqlite_engine)
    # Equipment.create_database_table()
    create = User.create_database_table()
    if create:
        session = sessionmaker(sqlite_engine)()
        user_info = User(username='admin', password='admin', user_type=0)
        session.add(user_info)
        session.commit()
        session.close()
        print('初始化用户成功')
