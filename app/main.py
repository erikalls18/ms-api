from fastapi import FastAPI
import uvicorn
from api.microservices import router
from api.enviroment import router_env
from api.deploy import router_dp
from db.db_setup import engine, Base
from db.models import  microservice, enviroment, deploy 

Base.metadata.create_all(bind=engine)
app = FastAPI()

@app.get("/")
async def root():
    return "The app is running"

app.include_router(router)
app.include_router(router_env)
app.include_router(router_dp)


'''if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0")'''

#uvicorn main:app --host 0.0.0.0 --port 8005 --reload

