from fastapi import APIRouter
from database.db import users_container

router = APIRouter()

@router.post("/add/")
def add_user(user: dict):
    users_container.upsert_item(user)
    return {"message": "User added"}
