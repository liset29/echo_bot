import requests
import config as con
import functions as func
import comands as com
import database
import time

getting = requests.get(f"{con.GET_UPDATES_URL}?offset=-1").json()
update_id = requests.get(f"{con.GET_UPDATES_URL}?offset=-1").json()["result"][0]["update_id"]
com.setMyCommands()

while True:
    getting_updates = requests.get(f"{con.GET_UPDATES_URL}?offset={update_id + 1}").json()
    if len(getting_updates["result"]) != 0:

        if "message" not in getting_updates["result"][0]:
            update_id += 1
            continue

        chat_id = getting_updates["result"][0]["message"]["chat"]["id"]

        if "text" not in getting_updates["result"][0]["message"]:
            func.send_danil(chat_id)
            update_id += 1
            continue

        seconds = time.time()
        time_mes = time.ctime(seconds)
        message = getting_updates["result"][0]["message"]["text"]
        first_name = getting_updates["result"][0]["message"]["from"]["first_name"]
        last_name = False if "last_name" not in getting_updates["result"][0]["message"]["from"] else \
            getting_updates["result"][0]["message"]["from"]["last_name"]
        database.main(chat_id, first_name, last_name, message, time_mes)

        if message in com.commands:
            com.commands[message](chat_id)
            update_id += 1

        else:
            func.send_meow_message(chat_id, message)
            update_id += 1
