import fastapi
from typing import Optional, List 
from pydantic import BaseModel 

router_dp = fastapi.APIRouter()

@router_dp.get("/deploy")
async def get_list_deploy():
    return "Hi"

@router_dp.get("/deploy/{id}")
async def get_deploy(id: int):
    pass

@router_dp.post("/deploy")
async def create_deploy():
    pass

@router_dp.delete("/deploy/{id}")
async def delete_deploy():
    pass