from fastapi import Depends,FastAPI


app = FastAPI()

async def base_name(name: str):
    return {"name":name}

@app.get("/name/{name}")
async def get_name(name_dict :dict = Depends(base_name)):
    return name_dict

# 子依赖

async def extar_action(name: str=None):
    return name

async def get_info_base(name=Depends(extar_action),age :int=None):
    return {"name":name,"age":age}

@app.get("/info/{name}/{age}")
async def get_info(info=Depends(get_info_base),flag :str=None):
    if info['name'] is None:
        return {"flag":flag}
    else:
        return info