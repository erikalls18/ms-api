from pydantic import BaseModel

class MicroservicesBase(BaseModel):
    id:int
    name: str
    image: str
    owner: str 

    #class Config:
        #orm_mode = True

class MicroservicesCreate(MicroservicesBase):

    ...
    class Config:
        orm_mode = True
class MicroservicesUpdate(BaseModel):
    id: int
    name: str
    image: str
    owner: str 
    
    class Config:
        orm_mode = True
