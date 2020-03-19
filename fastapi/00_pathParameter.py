#!/usr/bin/env python3
# encoding: utf-8
'''
@author: hzj
@file: 00_pathParameter.py
@time: 2020/3/14 11:58 下午
'''

from fastapi import FastAPI
app = FastAPI()
@app.get("/")
# 使用异步请求
async def root():
    return {
        "message":"hello world"
    }

# 路径参数
# @app.get('/items/{item_id}')
# async def get_single_item(item_id):
#     return {
#         "item_id" : item_id
#     }

# 路径参数+ 参数类型限制
# @app.get('/items/{item_str}')
# async def get_str_item(item_str:str):
#     return {
#         "item_str": item_str
#     }

# 参数类型限制表示，你在url中输入的内容是string类型的，他会自动帮你转换其他类型的，比如说这里的 string - > int
# @app.get('/items/{item_number}')
# async def get_number_item(item_number:int):
#     return {
#         "item_number": item_number
#     }

# 路径参数的默认值
@app.get('/items/{item_number}')
async def get_number_item(item_number: int=1):
    message = "这是默认的"
    if item_number == 1:
        message = "你输出了默认的参数值 1"
    else:
        message = "你输出了其他的参数{}".format(item_number)

    return {
        "message":message

    }
