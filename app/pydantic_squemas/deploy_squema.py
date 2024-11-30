from pydantic import BaseModel
#from db.models.deploy import Deploy
from datetime import datetime


class DeployBase(BaseModel):
    version: str
    command: str 
    microservice_id: int
    environment_id: int

    class Config:
        orm_mode = True

class DeployCreate(DeployBase):
    ...
    class Config:
        orm_mode = True

class DeployResponse(BaseModel):
    id: int 
    version: str
    command: str 
    status: str

    class Config:
        orm_mode = True


class DeployResponsewithIDs(BaseModel):
    id: int 
    version: str
    command: str 
    status: str
    microservice_id: int
    environment_id: int

    class Config:
        orm_mode = True