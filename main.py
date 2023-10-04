from fastapi import FastAPI, HTTPException
from models import User, Police, Role, Position
from uuid import UUID
from typing import Optional, List


app = FastAPI()
db: List[User] = [
]

db2:List[Police]=[
    Police(
        id="4ea5f847-3007-4bac-80fa-0bf443efa33a",
        posicao=Position.executivo,
        name="Marcos"
    )
]

@app.get("/")
def root():
    return {"Ola": "Mundo"}

@app.get("/api/v1/users")
async def fetch_users():
    return db

@app.get("/api/v1/users/{user_id}")
async def get_user_by_id(user_id:UUID):
    for user in db:
        if(user.id==user_id):
            return user

@app.post("/api/v1/users")
async def post_users(user:User):
    db.append(user)
    return{"id":user.id}

@app.delete("/api/v1/users/{user_id}")
async def delete_user_by_id(user_id:UUID):
    for user in db:
        if(user.id==user_id):
            db.remove(user)
            return 
    raise HTTPException(
        status_code=404,
        detail=f"User with id: {user_id} was not found "
    )

@app.get("/api/v1/polices")
async def get_policies():
    return db2

@app.put("/api/v1/polices/{police_id}")
async def update_police(policeUpdate:Police, police_id:UUID):
    for police in db2:
        if (police.id==police_id):
            if(policeUpdate.name is not None):
                police.name=policeUpdate.name
            if(policeUpdate.posicao is not None):
                police.posicao=policeUpdate.posicao
            return {"Update feito com sucesso"}
        
    raise HTTPException(
        status_code=404,
        detail=f"Police with id: {police_id} was not found "
    )