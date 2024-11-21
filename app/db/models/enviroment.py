from sqlalchemy import Boolean, Column, Integer, String , ForeignKey
from sqlalchemy.orm import relationship
from ..db_setup import Base 
from .microservice import Microservice
from .deploy import Deploy 

class Environment(Base):
    __tablename__ = 'environment'
    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String, nullable=False)
    
    #defining Foreign key 
    microservice_id = Column(Integer, ForeignKey('microservice.id'), nullable=False)

    # Relation with microservice and deploy tables
    microservice = relationship('Microservice', back_populates='environment')
    deploys = relationship('Deploy', back_populates='environment')