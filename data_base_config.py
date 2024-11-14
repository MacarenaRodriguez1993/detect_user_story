from sqlalchemy.ext.declarative import  declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

from config_env import settings


engine = create_engine(settings.DATABASE_URL, echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal() 
    try:
        yield db
    finally:
        db.close()
        
        
        
