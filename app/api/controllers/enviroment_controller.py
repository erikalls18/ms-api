from sqlalchemy.orm import Session 
from db.models.environment import Environment, EnvironmentType
from pydantic_squemas.enviroment_squema import EnvironmentCreate
from enum import Enum
from db.models.microservice import Microservice



def get_environment_by_id(db:Session , env_id:int):
    return db.query(Environment).filter(Environment.id == env_id).first()

def get_environment_by_env(db:Session , env:EnvironmentType):
    return db.query(Environment).filter(Environment.env == env).all()

def get_all_environments(db:Session ):
    results = db.query(Environment).all()
    return results

def get_environment_for_microservice(db: Session, env: EnvironmentType, microservice_id: int):
    return db.query(Environment).filter(
        Environment.env == env,
        Environment.microservice_id == microservice_id
    ).first()

def create_environment(db:Session, environment: EnvironmentCreate):
    db_env = Environment(
        env=environment.env,
        microservice_id =environment.microservice_id
        
    )
    db.add(db_env)

    db.commit()
    db.refresh(db_env)
    return db_env



def delete_environment(db:Session , env_id:int):
    db_env= db.query(Environment).filter(Environment.id == env_id).first()
    db.delete(db_env)
    db.commit()
    return {"detail": "Environment deleted successfully"}