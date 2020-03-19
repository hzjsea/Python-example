#!/usr/bin/env python3
# encoding: utf-8
'''
@author: hzj
@file: 03_queryParameters.py
@time: 2020/3/15 12:13 上午
'''

from fastapi import  FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"speak":"helloworld"}

# #无查询参数
# @app.get("/name/")
# async def get_name():
#     return {"name":"hzj"}

# # 查询可选参数
# @app.get("/name/")
# async def  get_age(age :int=None ):
#     message = "his age is {}"
#     if age is None:
#         message = "he dont have age"
#     else:
#         message = message.format(age)
#     return {
#         "message":"his name is and {}".format(message)
#     }

# #查询必选参数
# @app.get("/name/")
# async def  get_age_one(age :int ):
#     return {
#         "message":"his name is  and his age is {0}".format(age)
#     }

# # 查询必须参数默认
# @app.get("/name/")
#
# async def  get_age_one(age :int=20 ):
#     return {
#         "message":"his name is and his age is {0}".format(age)
#     }
#
