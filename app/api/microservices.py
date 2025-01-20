import fastapi
from typing import Optional, List 
from api.controllers.ms_controller import get_ms_by_id, get_ms_by_name, get_all_ms, create_ms, update_ms, delete_ms
from db.db_setup import get_db
from fastapi import Depends, HTTPException 
from sqlalchemy.orm import Session 
from pydantic_squemas.ms_squema import MicroservicesCreate, MicroservicesBase, MicroservicesResponse,  MicroservicesUpdate

router = fastapi.APIRouter()

#parameter + model that the endpoint need to use 
@router.get("/services", response_model= List[MicroservicesResponse])
async def get_list_services( limit: int =100, db: Session = Depends(get_db)):
    microservices= get_all_ms(db, limit=limit)
    return microservices

@router.get("/services/{ms_id}", response_model= MicroservicesResponse)
async def get_services(  ms_id:int , db: Session = Depends(get_db)):
    
    db_ms= get_ms_by_id(db= db, ms_id= ms_id)
    if db_ms is None: 
        raise HTTPException(status_code= 404, detail = "Microservice not found")

    return db_ms
    

@router.post("/services", response_model = MicroservicesResponse, status_code = 201)
async def create_microservice(ms:MicroservicesCreate, db: Session = Depends(get_db) ):
    db_ms = get_ms_by_name(db=db, ms_name = ms.name)
    if db_ms:
        raise HTTPException(status_code= 400, detail= "Microservice already exists")
    return create_ms(db=db, microservice=ms)

@router.patch("/services/{ms_id}", response_model = MicroservicesResponse)
async def update_microservice(ms_id: int, microservice: MicroservicesUpdate, db: Session = Depends(get_db)):
    
    db_ms= get_ms_by_id(db= db, ms_id= ms_id)

    if db_ms is None: 
        raise HTTPException(status_code= 404, detail = "Microservice not found")

    return update_ms(db=db, ms_id= ms_id, microservice=microservice)

@router.delete("/services/{ms_id}")
async def delete_microservices(ms_id: int, db: Session = Depends(get_db)):
    
    db_ms= get_ms_by_id(db= db, ms_id= ms_id)

    if db_ms is None: 
        raise HTTPException(status_code= 404, detail = "Microservice not found")

    return delete_ms(db=db, ms_id = ms_id)

    

