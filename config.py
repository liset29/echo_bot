import os
from dotenv import load_dotenv
name=3124
load_dotenv()
API_URL = "https://api.telegram.org"

TOKEN = os.getenv("TOKEN")
HOST = os.getenv("HOST")
USER = os.getenv("USER")
PASSWORD = os.getenv("PASSWORD")
DATABASE = os.getenv("DATABASE")

GET_UPDATES = "getUpdates"
SEND_MESSAGE = "sendMessage"

GET_URL = f"{API_URL}/bot{TOKEN}"
SEND_MESSAGE_URL = f"{GET_URL}/{SEND_MESSAGE}?chat_id="
GET_UPDATES_URL = f"{GET_URL}/{GET_UPDATES}"
