from pydantic import BaseModel
from pydantic_squemas.enviroment_squema import EnvironmentResponse
from typing import List, Optional
from datetime import datetime
from pydantic_squemas.deploy_squema import DeployResponse

class MicroservicesBase(BaseModel):
    name: str
    image: str
    team: str 

    class Config:
        from_atrributes = True

class MicroservicesCreate(MicroservicesBase):

    ...
    class Config:
        from_atrributes = True
class MicroservicesUpdate(BaseModel):
    image: str
    team: str 
    
    class Config:
        from_atrributes = True

class MicroservicesResponse(BaseModel):
    id: int
    name: str
    image: str
    team: str 
    created_at: datetime
    updated_at: datetime
    environment: Optional[List[EnvironmentResponse]] = None
    
    class Config:
        from_attributes = True

