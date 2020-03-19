#!/usr/bin/env python3
# encoding: utf-8
'''
@author: hzj
@file: 04_request_body.py
@time: 2020/3/15 12:30 上午
'''

from fastapi import FastAPI,Body
from pydantic import BaseModel

class Item(BaseModel):
    name: str
    description: str = None
    price: float
    tax: float = None

class User(BaseModel):
    username: str
    full_name: str = None


app = FastAPI()


# @app.post("/items/")
# async def create_item(item: Item,user: User,another_name :str = Body(...)):
#     return {"item":item,"User":user,"another_name":another_name}


@app.post("/items/")
async def create_item(item: Item,user: User):
    return {"item":item,"User":user}





# @app.post("/items/")
# async def create_item(item: Item):
#     item_dict = item.dict()
#     if item.tax:
#         price_with_tax = item.price + item.tax
#         item_dict.update({"price_with_tax": price_with_tax})
#     return item_dict