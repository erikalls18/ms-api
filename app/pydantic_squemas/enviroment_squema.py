from pydantic import BaseModel
from enum import Enum
from db.models.environment  import EnvironmentType

class EnvironmentBase(BaseModel):
    name: EnvironmentType
    microservice_id: int 

    class Config:
        orm_mode = True

class EnvironmentCreate(EnvironmentBase):

    ...
    class Config:
        orm_mode = True

class EnvironmentResponse(BaseModel):
    id: int
    name: EnvironmentType
    microservice_id: int 
   
    
    class Config:
        orm_mode = True