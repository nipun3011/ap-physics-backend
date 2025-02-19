from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
# from routes import ml, users
import uvicorn
import json
from dotenv import dotenv_values
from azure.cosmos.aio import CosmosClient
from azure.cosmos import PartitionKey, exceptions
from contextlib import asynccontextmanager
from datetime import datetime
import pytz
from models.chat import Chat

from datetime import datetime
import pytz

from datetime import datetime

def get_current_time():
    """Returns the current UTC time in ISO 8601 format without timezone information."""
    current_time_utc = datetime.utcnow()
    iso_format = current_time_utc.replace(microsecond=0).isoformat()
    return iso_format

config = dotenv_values(".env")

app = FastAPI()
DATABASE_NAME = "todo-db"
CONTAINER_NAME = "todo-items"

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize the Cosmos client
@asynccontextmanager
async def get_client():
    app.client = CosmosClient(config["COSMOS_ENDPOINT"], config["COSMOS_KEY"])
    database = app.client.get_database_client(DATABASE_NAME)
    container = database.get_container_client(CONTAINER_NAME)
    yield container
    app.client.close()

@app.get("/")
def read_root():
    return {"message": "Welcome to the backend"}

@app.get("/get-ques-u")
def read_ques():
    with open("MOCK_QUES U.json", 'r') as obj:
        data = json.load(obj)
    return data

@app.get("/get-ques-s")
def read_ques():
    with open("MOCK_QUES S.json", 'r') as obj:
        data = json.load(obj)
    return data

@app.get("/get-chats")
def read_chats():
    with open("MOCK_CHAT.json", 'r') as obj:
        data = json.load(obj)
    return data

@app.get("/get-chat/{chatId}")
def get_chat(chatId: str):
    with open("MOCK_CHAT.json", 'r') as obj:
        data = json.load(obj)
        for d in data:
            if d["chatId"] == chatId:
                return d
    return {}

@app.post("/send-chat/{chatId}")
async def send_chat(chat: Chat, chatId: str):
    try:
        with open("MOCK_CHAT.json", 'r') as obj:
            data = json.load(obj)
    except FileNotFoundError:
        return {"error": "Chat file not found"}
    
    chat.timestamp = get_current_time()
    chat.role = "user"
    
    chat_found = False
    for d in data:
        if d["chatId"] == chatId:
            d["messages"].append(chat.model_dump())
            chat_found = True
            break  # No need to loop further

    if chat_found:
        with open("MOCK_CHAT.json", 'w') as f:
            json.dump(data, f, indent=4)
        return {"message": "Chat sent"}
    
    return {"message": "Chat not found"}

