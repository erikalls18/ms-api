import fastapi
from typing import Optional, List 
from pydantic import BaseModel 
from db.db_setup import get_db
from fastapi import Depends, HTTPException 
from sqlalchemy.orm import Session 
from pydantic_squemas.enviroment_squema import EnvironmentCreate, EnvironmentBase, EnvironmentResponse
from api.controllers.enviroment_controller import get_environment_by_id, get_environment_by_name, get_all_environments, create_environment, delete_environment
from db.models.environment import EnvironmentType

router_env= fastapi.APIRouter()

@router_env.get("/environment", response_model = List[EnvironmentResponse])
async def get_list_enviroment(db: Session = Depends(get_db)):
    query_result = get_all_environments(db=db)
    print(query_result)
    return query_result

@router_env.get("/environment/type/{name}", response_model= List[EnvironmentResponse])
async def get_environment_by_type( name: EnvironmentType, db: Session = Depends(get_db)):
    return get_environment_by_name(db=db, name = name)


@router_env.get("/environment/{env_id}", response_model= EnvironmentResponse)
async def get_env_by_id(env_id:int , db: Session = Depends(get_db)):
    environment = get_environment_by_id(db=db, env_id=env_id)
    if not environment:
        raise HTTPException(status_code=404, detail="Environment not found")
    return environment

@router_env.post("/environment", response_model= EnvironmentResponse )
async def create_new_environment(environment: EnvironmentCreate, db: Session = Depends(get_db)):
    return create_environment(db=db, environment = environment)



'''@router_env.delete("/enviroment/{env_id}")
async def delete_environment(db: Session = Depends(get_db), env_id:int ):

    db_env= get_environment_by_id(db= db, env_id = env_id)

    if db_env is None: 
        raise HTTPException(status_code= 404, detail = "Microservice not found")

    return delete_ms(db=db, ms_id = ms_id)'''

    