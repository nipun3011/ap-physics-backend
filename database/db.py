# import os
# from azure.cosmos import CosmosClient
# from dotenv import load_dotenv

# load_dotenv()
# cosmos_url = os.getenv("AZURE_COSMOS_CONNECTION_STRING")

# client = CosmosClient(cosmos_url)
# database = client.create_database_if_not_exists("UserDatabase")
# users_container = database.create_container_if_not_exists(id="Users", partition_key="/id")
