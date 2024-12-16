from typing import List
from uuid import UUID
from fastapi import FastAPI

from modles import Gender, Roles, User

app = FastAPI()

db:List[User]=[
    User(id=UUID("4a779a09-bfd5-42ac-8351-8faf89a1b824"),first_name="Ashar",last_name="Malik",gender=Gender.male,roles=[Roles.student]),
    User(id=UUID("4a779a09-bfd5-42ac-8351-8faf89a1b825"),first_name="Alex",last_name="Malik",gender=Gender.male,roles=[Roles.admin])

]


@app.get("/")
async def root():
    return {"Hello": "world"}

@app.get("/api/v1/users") 
async def fetch_Users():
    return db

@app.post("/api/v1/users")
async def register_Users(user:User):
    db.append(user)
    return {"id": user.id}
    

@app.delete("/api/v1/users/{user_id}")
async def delete_Users(user_id:UUID):
    for user in db:
        if(user_id==user.id):
            db.remove(user)
            return
