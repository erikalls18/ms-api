from sqlalchemy import Boolean, Column, Integer, String , ForeignKey
from sqlalchemy.orm import relationship
from ..db_setup import Base 
from .microservice import Microservice

class Deploy(Base):
    __tablename__ = 'deploy'
    id = Column(Integer, primary_key=True, autoincrement=True)
    microservice_id = Column(Integer, ForeignKey('microservice.id'), unique=True, nullable=False)
    environment_id = Column(Integer, ForeignKey('environment.id'), unique=True, nullable=False)

    # Relación uno a uno con Microservicio y Environment
    microservice = relationship('Microservice', back_populates='deploy')
    environment = relationship('Environment', back_populates='deploy')

  