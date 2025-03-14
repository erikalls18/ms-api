from pydantic import BaseModel
from enum import Enum
from db.models.environment  import EnvironmentType
from datetime import datetime
from typing import List, Optional
from pydantic_squemas.deploy_squema import DeployResponse

class EnvironmentBase(BaseModel):
    env: EnvironmentType
    microservice_id: int 

    class Config:
        from_attributes  = True

class EnvironmentCreate(EnvironmentBase):

    ...
    class Config:
        from_attributes  = True

class EnvironmentResponse(BaseModel):
    id: int
    env: EnvironmentType
    created_at: datetime
    deploy: Optional[List[DeployResponse]] = None
  

    class Config:
        from_attributes = True

class EnvironmentResponsewithMicroservice(BaseModel):
    id: int
    env: EnvironmentType
    created_at: datetime
    microservice_id: int 

    class Config:
        from_attributes = True
