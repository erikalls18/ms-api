from sqlalchemy import Boolean, Column, Integer, String , ForeignKey, Enum as SQLAlchemyEnum
from sqlalchemy.orm import relationship
from ..db_setup import Base 
from .microservice import Microservice
from .deploy import Deploy 
from enum import Enum


class EnvironmentType(str, Enum):
    dev = "dev"
    prod = "prod"
   


class Environment(Base):
    __tablename__ = 'environment'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(SQLAlchemyEnum(EnvironmentType), nullable=False)
    #defining Foreign key 
    microservice_id = Column(Integer, ForeignKey('microservice.id'), nullable=False)

    # Relation with microservice and deploy tables
    microservice = relationship('Microservice', back_populates='environment')
    deploy = relationship('Deploy', back_populates='environment')