from sqlalchemy.orm import Session 
from pydantic_squemas.deploy_squema import DeployCreate
from db.models.deploy import Deploy
from db.models.microservice import Microservice 
from db.models.environment import Environment
from sqlalchemy.orm import joinedload


def get_deploys(db:Session):
    results = db.query(Deploy).all()
    return results

def get_deploy_by_id(db: Session, deploy_id: int):
    return db.query(Deploy).filter(Deploy.id == deploy_id).first()

def create_new_deploy(db: Session, deploy: DeployCreate):
    db_deploy = Deploy(
        version = deploy.version,
        command = deploy.command,
        microservice_id = deploy.microservice_id,
        environment_id = deploy.environment_id
    )
    db.add(db_deploy)
    db.commit()
    db.refresh(db_deploy)
    
    return db_deploy

def delete_deploy(db: Session, deploy_id: int):
    db_deploy = db.query(Deploy).filter(Deploy.id == deploy_id).first()
    db.delete(db_deploy)
    db.commit()
    return {"detail": "Deploy deleted successfully"}
