from sqlalchemy.orm import Session 
from db.models.environment import Environment, EnvironmentType
from pydantic_squemas.enviroment_squema import EnvironmentCreate
from enum import Enum
from db.models.microservice import Microservice



def get_environment_by_id(db:Session , env_id:int):
    return db.query(Environment).filter(Environment.id == env_id).first()

def get_environment_by_name(db:Session , name:EnvironmentType):
    return db.query(Environment).filter(Environment.name == name).all()

def get_all_environments(db:Session ):

    results = (
        db.query(Environment, Microservice.id.label("microservice_id"))
        .join(Microservice, Environment.microservice_id == Microservice.id)
        .all()
    )

    return [
        {
            "id": env.id,
            "name": env.name,
            "microservice_id": microservice_id,
        }
        for env, microservice_id in results
    ]
def create_environment(db:Session, environment: EnvironmentCreate):
    db_env = Environment(
        name=environment.name,
        microservice_id =environment.microservice_id
        
    )
    db.add(db_env)
    db.commit()
    db.refresh(db_env)
    return db_env



def delete_environment(db:Session , ms_id:int):
    db_env= db.query(Environment).filter(Environment.id == ms_id).first()
    db.delete(db_env)
    db.commit()
    return {"detail": "Environment deleted successfully"}