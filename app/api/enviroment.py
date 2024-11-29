import fastapi
from typing import Optional, List 
from pydantic import BaseModel 
from db.db_setup import get_db
from fastapi import Depends, HTTPException 
from sqlalchemy.orm import Session 
from pydantic_squemas.enviroment_squema import EnvironmentCreate, EnvironmentBase, EnvironmentResponse, EnvironmentResponsewithMicroservice
from api.controllers.enviroment_controller import get_environment_by_id, get_environment_by_env, get_all_environments, create_environment, delete_environment, get_environment_for_microservice
from db.models.environment import EnvironmentType

router_env= fastapi.APIRouter()

@router_env.get("/environment", response_model = List[EnvironmentResponsewithMicroservice])
async def get_list_enviroment(db: Session = Depends(get_db)):
    query_result = get_all_environments(db=db)
  
    return query_result

@router_env.get("/environment/type/{env}", response_model= List[EnvironmentResponsewithMicroservice])
async def get_environment_by_type( env: EnvironmentType, db: Session = Depends(get_db)):
    db_env = get_environment_by_env(db=db, env = env)
    if not db_env:
        raise HTTPException(status_code= 404, detail = "Environments not found")
    return db_env


@router_env.get("/environment/{env_id}", response_model= EnvironmentResponsewithMicroservice)
async def get_env_by_id(env_id:int , db: Session = Depends(get_db)):
    environment = get_environment_by_id(db=db, env_id=env_id)
    if not environment:
        raise HTTPException(status_code=404, detail="Environment not found")
    return environment

@router_env.post("/environment", response_model= EnvironmentResponse, status_code = 201 )
async def create_new_environment(environment: EnvironmentCreate, db: Session = Depends(get_db)):
    db_env = get_environment_for_microservice(db=db, env=environment.env, microservice_id= environment.microservice_id)
    if db_env:
        raise HTTPException(status_code= 400, detail= "Environment already exists for this microservice")
    return create_environment(db=db, environment = environment)

@router_env.delete("/environment/{env_id}")
async def delete_environments(env_id:int, db: Session = Depends(get_db) ):
    db_env = get_environment_by_id(db= db, env_id = env_id)
    if db_env is None: 
        raise HTTPException(status_code= 404, detail = "Environment not found")
    return delete_environment(db=db, env_id = env_id)

    