#!/usr/bin/env python3
# encoding: utf-8
'''
@author: hzj
@file: 01_pathParameter.py
@time: 2020/3/14 6:07 下午
'''


from fastapi import  FastAPI

app  = FastAPI()

static_url = "http://127.0.0.1:8000{0}"

@app.get("/")
async def root():
    return {
        "path1":static_url.format("/name/me"),
        "path":static_url.format("/name/{you can input something}")
    }
@app.get("/name/me")
async def return_name():
    return {"name":"this name is me "}

@app.get("/name/{name}")
async def return_name(name:str):
    return {"name":"you  input name is {}".format(name)}
