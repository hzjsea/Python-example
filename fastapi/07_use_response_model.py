# 定义一个post实例
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class UserIn(BaseModel):
    username: str
    password: str
    email: str
    full_name: str = None


class UserOut(BaseModel):
    username: str
    email: str
    full_name: str = None


@app.post("/user/", response_model=UserOut)
async def create_user(*, user: UserIn):
    return user