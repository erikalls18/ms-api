import fastapi
from typing import Optional, List 
from pydantic import BaseModel 

router_env= fastapi.APIRouter()

@router_env.get("/enviroment")
async def get_list_enviroment():
    return "Hi"

@router_env.get("/enviroment/{id}")
async def get_enviroment(id: int):
    pass

@router_env.post("/enviroment")
async def create_enviroment():
    pass



@router_env.delete("/enviroment/{id}")
async def delete_enviroment():
    pass