from fastapi import APIRouter
import json
from schemas import Chat
from utils.time_funcs import get_current_time

router = APIRouter()

@router.get("/get-chats")
def read_chats():
    with open("./MOCK_CHAT.json", 'r') as obj:
        data = json.load(obj)
    return data

@router.get("/get-chat/{chatId}")
def get_chat(chatId: str):
    with open("./MOCK_CHAT.json", 'r') as obj:
        data = json.load(obj)
        for d in data:
            if d["chatId"] == chatId:
                return d
    return {}

@router.post("/send-chat/{chatId}")
async def send_chat(chat: Chat, chatId: str):
    try:
        with open("./MOCK_CHAT.json", 'r') as obj:
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
        with open("./MOCK_CHAT.json", 'w') as f:
            json.dump(data, f, indent=4)
        return {"message": "Chat sent"}
    
    return {"message": "Chat not found"}