#!/usr/bin/env python3
# encoding: utf-8
'''
@author: hzj
@file: 02_enumeration.py
@time: 2020/3/14 9:51 下午
'''

from fastapi import  FastAPI
from enum import  Enum

class Set_Enum(int,Enum):
    id = 1,
    age = 2,
    speak = 3,

app = FastAPI()

@app.get("/")
async def root():
    return {"speak":"hello world "}

@app.get("/id/{index}")
async def get_index(index: int):
    if index == Set_Enum.age:
        return {"index":Set_Enum.age}
    elif index == Set_Enum.id:
        return {"index":Set_Enum.speak}
