from pydantic import BaseModel

class Question(BaseModel):
    userID: str
    quesID: str
    topic: str
    description: str
    options: list[str]
    response: int | None = None
