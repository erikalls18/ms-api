import fastapi
from sqlalchemy.orm import Session 
from db.db_setup import get_db
from fastapi import Depends, HTTPException 
from typing import Optional, List 
from pydantic import BaseModel 
from pydantic_squemas.deploy_squema import DeployCreate, DeployResponse, DeployResponsewithIDs
from api.controllers.deploy_controller import get_deploys, create_new_deploy, get_deploy_by_id, delete_deploy
from typing import List 
from services.kube import create_deploy_k8s
from services.auth import verify_token

router_dp = fastapi.APIRouter()

@router_dp.get("/deploy", response_model= List[DeployResponse])
async def get_all_deploys(db: Session = Depends(get_db), payload: dict = Depends(verify_token)):
    return get_deploys(db=db)

@router_dp.get("/deploy/{deploy_id}", response_model= DeployResponsewithIDs)
async def get_deploy(deploy_id: int, db: Session = Depends(get_db), payload: dict = Depends(verify_token) ):
    db_deploy= get_deploy_by_id(db=db, deploy_id=deploy_id)
    if not db_deploy: 
        raise HTTPException(status_code=404, detail= "Deploy not found")
    return db_deploy

@router_dp.post("/deploy", response_model = DeployResponse)
async def create_deploy(deploy: DeployCreate, db: Session = Depends(get_db), payload: dict = Depends(verify_token)):
    db_deploy= create_new_deploy(db=db, deploy=deploy)
    '''microservice_data = get_data_microservices(db, db_deploy.microservice_id)
    if microservice_data:
        print(f"Microservice Name: {microservice_data.name}")  '''
    
    create_deploy_k8s(db_deploy)
    return db_deploy

@router_dp.delete("/deploy/{deploy_id}")
async def delete_deploys(deploy_id: int, db: Session = Depends(get_db), payload: dict = Depends(verify_token)):
    db_deploy = get_deploy_by_id(db= db, deploy_id = deploy_id)
    if db_deploy is None: 
        raise HTTPException(status_code= 404, detail = "Deploy not found")
    return delete_deploy(db=db, deploy_id= deploy_id)
    