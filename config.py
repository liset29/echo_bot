import os
from dotenv import load_dotenv

load_dotenv()
API_URL = "https://api.telegram.org"

TOKEN = os.getenv("TOKEN")
HOST = os.getenv("HOST")
USER = os.getenv("USER")
PASSWORD = os.getenv("PASSWORD")
DATABASE = os.getenv("DATABASE")
PORT_ORM=os.getenv("PORT_ORM")
PHOTO_BOSS = os.getenv("PHOTO_BOSS")
PHOTO_NO_BOSS = os.getenv("PHOTO_NO_BOSS")

GET_UPDATES = "getUpdates"
SEND_MESSAGE = "sendMessage"

GET_URL = f"{API_URL}/bot{TOKEN}"
SEND_MESSAGE_URL = f"{GET_URL}/{SEND_MESSAGE}?chat_id="
GET_UPDATES_URL = f"{GET_URL}/{GET_UPDATES}"

RHOST = os.getenv("REDIS_HOST")
PORT = os.getenv("PORT")
DB = os.getenv("DB")
