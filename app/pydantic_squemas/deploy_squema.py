from pydantic import BaseModel
#from db.models.deploy import Deploy
from datetime import datetime


class DeployBase(BaseModel):
    version: str
    command: str 
    microservice_id: int
    environment_id: int

    class Config:
        from_attributes  = True

class DeployCreate(DeployBase):
    ...
    class Config:
        from_attributes  = True

class DeployResponse(BaseModel):
    id: int 
    version: str
    command: str 
    status: str
    created_at: datetime

    class Config:
        from_attributes  = True


class DeployResponsewithIDs(BaseModel):
    id: int 
    version: str
    command: str 
    status: str
    microservice_id: int
    environment_id: int
    created_at: datetime

    class Config:
        from_attributes = True