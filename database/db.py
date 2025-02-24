import os
from azure.cosmos import CosmosClient
from dotenv import dotenv_values

config = dotenv_values(".env")
COSMOS_DB = "ap-physics-nipun-db"
USER_CONTAINER = "users"
QUESTIONS_CONTAINER = ""

def create_db_instance():
    client = CosmosClient(config["AZURE_COSMOS_URL"], credential=config["AZURE_COSMOS_KEY"])
    database = client.get_database_client(COSMOS_DB)
    container = database.get_container_client(USER_CONTAINER)
    return client, database, container

client, database, container = create_db_instance()
