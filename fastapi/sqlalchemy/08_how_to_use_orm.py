#!/usr/bin/env python3
# encoding: utf-8

"""
@author: hzj
@file: 08_how_to_use_orm.py
@time: 2020/3/13 8:54 下午
"""


# how to use https://www.sqlalchemy.org/
from sqlalchemy import  create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import  Column,Integer,String
# from sqlalchemy import create_engine
engine = create_engine('sqlite:///:memory:', echo=True)
Base = declarative_base()
class User(Base):
    __tablename__ = 'users'

    id = Column(Integer,primary_key=True)
    name = Column(String)
    fullname = Column(String)
    nickname = Column(String)


    def __repr__(self):
        return "<User(name='%s', fullname='%s', nickname='%s')>" % (self.name, self.fullname, self.nickname)
