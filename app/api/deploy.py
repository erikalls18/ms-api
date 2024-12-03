import fastapi
from sqlalchemy.orm import Session 
from db.db_setup import get_db
from fastapi import Depends, HTTPException 
from typing import Optional, List 
from pydantic import BaseModel 
from pydantic_squemas.deploy_squema import DeployCreate, DeployResponse, DeployResponsewithIDs
from api.controllers.deploy_controller import get_deploys, create_new_deploy, get_deploy_by_id, delete_deploy
from typing import List 

router_dp = fastapi.APIRouter()

@router_dp.get("/deploy", response_model= List[DeployResponse])
async def get_all_deploys(db: Session = Depends(get_db)):
    return get_deploys(db=db)

@router_dp.get("/deploy/{deploy_id}", response_model= DeployResponsewithIDs)
async def get_deploy(deploy_id: int, db: Session = Depends(get_db) ):
    db_deploy= get_deploy_by_id(db=db, deploy_id=deploy_id)
    if not db_deploy: 
        raise HTTPException(status_code=404, detail= "Deploy not found")
    return db_deploy

@router_dp.post("/deploy", response_model = DeployResponse)
async def create_deploy(deploy: DeployCreate, db: Session = Depends(get_db)):
    db_deploy= create_new_deploy(db=db, deploy=deploy)
    return db_deploy

@router_dp.delete("/deploy/{deploy_id}")
async def delete_deploys(deploy_id: int, db: Session = Depends(get_db)):
    db_deploy = get_deploy_by_id(db= db, deploy_id = deploy_id)
    if db_deploy is None: 
        raise HTTPException(status_code= 404, detail = "Deploy not found")
    return delete_deploy(db=db, deploy_id= deploy_id)
    