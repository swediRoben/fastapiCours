from fastapi import FastAPI,HTTPException,status,Depends
from pydantic import BaseModel
from typing import Optional,Annotated
import models.myModels
from sqlalchemy.orm import Session
from db.dbConnect import engine,Sessionmeker
import uvicorn

app=FastAPI()
models.myModels.Base.metadata.create_all(bind=engine)

class cours(BaseModel):
    titre:str

def get_db():
    db=Sessionmeker()
    try:
        yield db
    finally:
        db.close()
        
db_depandance=Annotated[Session,Depends(get_db)]

app.post("/create/",status_code=status.HTTP_201_CREATED)
def create_cour(cour:cours,db:db_depandance):
    cour_db=models.myModels.cour(**cour.dict())
    db.add(cour_db)
    db.commit()

app.get("/{id}",status_code=status.HTTP_200_OK)
def get_cour(id:int,db:db_depandance):
    user=db.query(models.myModels.cour).filter(models.myModels.cour.id==id).first()
    if user is None:
        raise HTTPException(status_code=status.HTTP_204_NO_CONTENT,detail="pas de donnees")
    return user