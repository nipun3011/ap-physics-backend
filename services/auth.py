import os
from msal import ConfidentialClientApplication
from dotenv import load_dotenv

load_dotenv()

TENANT_ID = os.getenv("AZURE_TENANT_ID")
CLIENT_ID = os.getenv("AZURE_CLIENT_ID")
CLIENT_SECRET = os.getenv("AZURE_CLIENT_SECRET")

AUTHORITY = f"https://login.microsoftonline.com/{TENANT_ID}"
APP = ConfidentialClientApplication(CLIENT_ID, CLIENT_SECRET, authority=AUTHORITY)

def get_access_token():
    token_response = APP.acquire_token_for_client(scopes=["https://graph.microsoft.com/.default"])
    return token_response.get("access_token", None)
