
from sqlalchemy import Boolean, Column, Integer, String , ForeignKey,  DateTime
from sqlalchemy.orm import relationship
from ..db_setup import Base 
from datetime import datetime

class Microservice(Base):
    __tablename__= "microservice"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), unique=True, index=True, nullable=False)
    image = Column(String(100), nullable=False)
    team = Column(String(100), index=True, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)

    #Relationships with environment and deploy entities
    environment = relationship('Environment', back_populates='microservice', cascade="all, delete-orphan") 
    deploy = relationship('Deploy', back_populates='microservice', cascade="all, delete-orphan") 
