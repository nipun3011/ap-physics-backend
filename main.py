from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
# from routes import ml, users
import json
from azure.cosmos import PartitionKey, exceptions
from routes import chats, questions, users
from database.db import create_db_instance

# Initialize the Cosmos client
create_db_instance()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(chats.router)
app.include_router(questions.router)
app.include_router(users.router)



@app.get("/")
def read_root():
    return {"message": "Welcome to the backend"}





