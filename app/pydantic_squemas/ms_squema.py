from pydantic import BaseModel

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
    
    class Config:
        orm_mode = True

