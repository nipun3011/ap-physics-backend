from fastapi import APIRouter
import requests
import os
from dotenv import load_dotenv

load_dotenv()

router = APIRouter()

ML_API_URL = os.getenv("AZURE_ML_API_URL")

@router.post("/predict/")
def get_prediction(data: dict):
    response = requests.post(ML_API_URL, json=data)
    return response.json()
