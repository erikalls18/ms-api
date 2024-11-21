from pydantic import BaseModel

class MicroservicesBase(BaseModel):
    name: str
    image: str
    owner: str 

class MicroservicesCreate(MicroservicesBase):
    ...

class MicroservicesUpdat(BaseModel):
    id: int
    name: str
    image: str
    owner: str 
    
    class Config:
        orm_mode = True
