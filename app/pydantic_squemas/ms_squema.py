from pydantic import BaseModel
from pydantic_squemas.enviroment_squema import EnvironmentResponse
from typing import List, Optional

class MicroservicesBase(BaseModel):
    name: str
    image: str
    owner: str 

    class Config:
        orm_mode = True

class MicroservicesCreate(MicroservicesBase):

    ...
    class Config:
        orm_mode = True
class MicroservicesUpdate(BaseModel):
    image: str
    owner: str 
    
    class Config:
        orm_mode = True

class MicroservicesResponse(BaseModel):
    id: int
    name: str
    image: str
    owner: str 
    environment: Optional[List[EnvironmentResponse]] = None
    
    class Config:
        orm_mode = True

