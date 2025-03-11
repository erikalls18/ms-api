from sqlalchemy.orm import Session
from db.db_setup import engine, Base, SessionLocal
from db.models.deploy import Deploy
from db.models.microservice import Microservice 
from db.models.environment import Environment, EnvironmentType
from datetime import datetime
from sqlalchemy import text
from db.db_setup import engine, Base


def drop_tables_if_exist(db: Session):
    try:
        db.execute(text("TRUNCATE TABLE deploy, microservice, environment RESTART IDENTITY CASCADE"))
        db.commit()
        print("Tables truncated successfully.")
    except Exception as e:
        db.rollback()
        print(f"Error truncating tables: {e}")


def insert_data(db):

    try:
        #Insert microservices
        microservice1 = Microservice(name="api-test", image="alpine", team="data")
        microservice2 = Microservice(name="api-auth", image="ubuntu", team="devops")
        db.add_all([microservice1, microservice2])
        db.commit()

        # Insert environments
        env1 = Environment(env=EnvironmentType.dev, microservice_id=microservice1.id)
        env2 = Environment(env=EnvironmentType.prod, microservice_id=microservice2.id)
        
        db.add_all([env1, env2])
        db.commit()
        
        # Insert deploys
        deploy1 = Deploy(version="latest", command="deploy.sh", status="Deployed", microservice_id=microservice1.id, environment_id=env1.id)
        deploy2 = Deploy(version="latest", command="deploy.sh", status="Deployed", microservice_id=microservice2.id, environment_id=env2.id)
        
        db.add_all([deploy1, deploy2])
        db.commit()
        
        print("Data inserted succesfully.")
    except Exception as e:
        db.rollback()
        print(f"Error while inserting data: {e}")
    finally:
        db.close()

if __name__ == "__main__":
    Base.metadata.create_all(bind=engine)
    db: Session = SessionLocal()
    drop_tables_if_exist(db)
    insert_data(db)