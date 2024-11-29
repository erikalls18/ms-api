
from sqlalchemy import Boolean, Column, Integer, String , ForeignKey
from sqlalchemy.orm import relationship
from ..db_setup import Base 


'''class Microservice(Base):
    __tablename__= "microservice"

    id = Column(Integer, primary_key = True , index= True)
    name = Column(String(100), unique=True, index= True, nullable=False)
    image = Column(String(100), nullable=False)
    owner =Column(String(100),index= True, nullable=False)

    environment = relationship('Environment', back_populates='microservice')
    deploy = relationship('Deploy', back_populates='microservice')'''

class Microservice(Base):
    __tablename__= "microservice"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), unique=True, index=True, nullable=False)
    image = Column(String(100), nullable=False)
    owner = Column(String(100), index=True, nullable=False)

    environment = relationship('Environment', back_populates='microservice') 
    deploy = relationship('Deploy', back_populates='microservice')  # Relación con Deploy
