from sqlalchemy import Boolean,Column,Integer,String,Float,Double,BigInteger,ForeignKey
from sqlalchemy.orm import Relationship
from db.dbConnect import Base

class cour(Base):
    __tablename__="cours"
    
    id=Column(Integer,primary_key=True,index=True,autoincrement=True)
    titre=Column(String(44))
    
class eleve(Base):
    __tablename__="eleves"
    
    id=Column(Integer,primary_key=True,index=True,autoincrement=True)
    nom=Column(String(44))
    prenom=Column(String(44))
    
    
class classe(Base):
    __tablename__="classes"
    
    id=Column(Integer,primary_key=True,index=True,autoincrement=True)
    nom=Column(String(44)) 
    type=Column(String(1))

class note(Base):
    __tablename__="notes"
    
    id=Column(Integer,primary_key=True,index=True,autoincrement=True)
    point=Column(String(44)) 
    periode=Column(String(1))
