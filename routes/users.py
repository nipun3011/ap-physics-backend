from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from schemas import UserCreate, UserLogin
from database.db import container
from models.users import User
from utils.pwd_context import get_hashed_pass
import uuid
from services.auth import create_access_token, verify_password, get_current_user

router = APIRouter()

@router.post("/register")
def register_user(user: UserCreate):

    #verify existing user
    query = f"SELECT * FROM c WHERE c.email = '{user.email}'"
    existing_user = list(container.query_items(query, enable_cross_partition_query=True))
    if existing_user:
        raise HTTPException(status_code=400, detail="User already exists")

    #storing new user
    user_data = User(
        id= str(uuid.uuid4()),
        name=user.name,
        email=user.email,
        password=get_hashed_pass(user.password)
    )
    container.create_item(body=user_data.model_dump())
    return {"msg": "User registered successfully"}

@router.post("/login")
def login(user: OAuth2PasswordRequestForm=Depends()):
    query = f"SELECT * FROM c WHERE c.email = '{user.username}'"
    db_user = list(container.query_items(query, enable_cross_partition_query=True))

    if not db_user or not verify_password(user.password, db_user[0]["password"]):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    token = create_access_token({"sub": user.username})
    return {"access_token": token, "token_type": "bearer"}


@router.get("/protected")
def protected_route(user: dict = Depends(get_current_user)):
    return {"msg": "Access granted", "user": user}