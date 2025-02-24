from pydantic import BaseModel

class UserCreate(BaseModel):
    name: str
    email: str
    password: str

class UserLogin(BaseModel):
    email: str
    password: str

class Chat(BaseModel):
    role: str | None = None
    content: str
    timestamp: str | None = None