import fastapi
from typing import Optional, List 
from pydantic import BaseModel 

router = fastapi.APIRouter()

@router.get("/services")
async def get_services():
    return "Hi"