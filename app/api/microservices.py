import fastapi
from typing import Optional, List 
from api.utils.ms_utils import get_ms_by_id, get_ms_by_name, get_all_ms, create_ms
from db.db_setup import get_db
from fastapi import Depends, HTTPException 
from sqlalchemy.orm import Session 

from pydantic_squemas.ms_squema import MicroservicesCreate, MicroservicesBase

router = fastapi.APIRouter()

@router.get("/services", response_model= List[MicroservicesBase])
async def get_list_services( limit: int =100, db: Session = Depends(get_db)):
    microservices= get_all_ms(db, limit=limit)
    return microservices

@router.get("/services/{id}")
async def get_services(id: int):
    pass

@router.post("/services")
async def create_microservice():
    pass

@router.put("/services/{id}")
async def update_microservices():
    pass

@router.delete("/services/{id}")
async def delete_microservices():
    pass

