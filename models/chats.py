from pydantic import BaseModel

class Chat(BaseModel):
    role: str | None = None
    content: str
    timestamp: str | None = None