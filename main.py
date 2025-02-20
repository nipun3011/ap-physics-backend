from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
# from routes import ml, users
import json
from dotenv import dotenv_values
from azure.cosmos.aio import CosmosClient
from azure.cosmos import PartitionKey, exceptions
from contextlib import asynccontextmanager
import pytz
from routes import chats, questions, users

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

app.include_router(chats.router)
app.include_router(questions.router)

# Initialize the Cosmos client
@asynccontextmanager
async def get_client():
    app.client = CosmosClient(config["COSMOS_ENDPOINT"], credential=config["COSMOS_KEY"])
    database = app.client.get_database_client(DATABASE_NAME)
    container = database.get_container_client(CONTAINER_NAME)
    yield container
    app.client.close()

@app.get("/")
def read_root():
    return {"message": "Welcome to the backend"}





