import os
from dotenv import load_dotenv

load_dotenv()

API_URL = "https://api.telegram.org"
TOKEN = os.getenv("TOKEN")

GET_UPDATES = "getUpdates"
SEND_MESSAGE = "sendMessage"

GET_URL = f"{API_URL}/bot{TOKEN}"
SEND_MESSAGE_URL = f"{GET_URL}/{SEND_MESSAGE}?chat_id="
GET_UPDATES_URL = f"{GET_URL}/{GET_UPDATES}"
