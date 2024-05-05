from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

url="mysql+pymysql://pma:11111@localhost:3306/noteclasse"
engine=create_engine(url)
Sessionmeker=sessionmaker(autoflush=False,bind=engine)
Base=declarative_base() 