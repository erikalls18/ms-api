from sqlalchemy.orm import Session 

from db.models.microservice import Microservice
from pydantic_squemas.ms_squema import MicroservicesCreate, MicroservicesUpdate

def get_ms_by_id(db:Session , ms_id:int):
    return db.query(Microservice).filter(Microservice.id == ms_id).first()

def get_ms_by_name(db:Session , ms_name:str):
    return db.query(Microservice).filter(Microservice.name == ms_name).first()

def get_all_ms(db:Session ,  limit: int =100):
    return db.query(Microservice).limit(limit).all()

def create_ms(db:Session, microservice: MicroservicesCreate):
    db_ms = Microservice(
        name=microservice.name,
        image=microservice.image,
        owner=microservice.owner
    )
    db.add(db_ms)
    db.commit()
    db.refresh(db_ms)
    return db_ms 

def update_ms(db:Session , ms_id:int, microservice: MicroservicesUpdate):
    db_ms= db.query(Microservice).filter(Microservice.id == ms_id).first()
  
    db_ms.image = microservice.image
    db_ms.owner = microservice.owner 
   
    db.commit()
    db.refresh(db_ms)
    return db_ms 

def delete_ms(db:Session , ms_id:int):
    db_ms= db.query(Microservice).filter(Microservice.id == ms_id).first()
    db.delete(db_ms)
    db.commit()
    return {"detail": "Microservice deleted successfully"}