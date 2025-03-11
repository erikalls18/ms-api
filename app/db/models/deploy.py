from sqlalchemy import Boolean, Column, Integer, String , ForeignKey, DateTime
from sqlalchemy.orm import relationship
from ..db_setup import Base 
from .microservice import Microservice
from datetime import datetime

class Deploy(Base):
    __tablename__ = 'deploy'
    id = Column(Integer, primary_key=True, autoincrement=True)
    version = Column(String(100), nullable=False)
    command= Column(String(200), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)
    status= Column(String(100), default= 'Creating', nullable=False)
    microservice_id = Column(Integer, ForeignKey('microservice.id'), nullable=False)
    environment_id = Column(Integer, ForeignKey('environment.id'),  nullable=False)

    # Define the relationship one to one with Microservice and  Environment
    microservice = relationship('Microservice', back_populates='deploy')
    environment = relationship('Environment', back_populates='deploy')

