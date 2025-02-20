from fastapi import APIRouter
import json
from models.questions import Question

router = APIRouter()

@router.get("/get-ques-u")
def read_ques():
    with open("./MOCK_QUES U.json", 'r') as obj:
        data = json.load(obj)
    return data

@router.get("/get-ques-s")
def read_ques():
    with open("./MOCK_QUES S.json", 'r') as obj:
        data = json.load(obj)
    return data

@router.get("/get-ques-by-id/{quesID}")
async def get_ques(quesID: str):
    with open("./MOCK_QUES U.json", 'r') as obj:
        data = json.load(obj)
        for d in data:
            question=Question(**d)
            if question.quesID == quesID:
                return d
    return {}