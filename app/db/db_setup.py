from sqlalchemy import create_engine
#from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, declarative_base
DATABASE_URL = "postgresql+psycopg2://postgres:admin@db:5432/microservices"

#postgresql://user:password@localhost:5432/nombre_base_datos"

engine = create_engine(
    DATABASE_URL, connect_args={}, future = True
    )

# Crear una sesión
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine, future = True )


Base = declarative_base()

#
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()