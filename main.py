import requests
import config as con
import functions as func
import comands as com
import time

getting = requests.get(f"{con.GET_UPDATES_URL}?offset=-1").json()
update_id = requests.get(f"{con.GET_UPDATES_URL}?offset=-1").json()["result"][0]["update_id"]
com.setMyCommands()

while True:
    getting_updates = requests.get(f"{con.GET_UPDATES_URL}?offset={update_id + 1}").json()
    if len(getting_updates["result"]) == 0:
        continue

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

    if message == "/start":
        func.start(chat_id, first_name, last_name)
        update_id += 1
        continue

    func.add_message(chat_id, time_mes, message)

    if message in com.commands:
        com.commands[message](chat_id)
        update_id += 1
        continue
    else:
        func.send_meow_message(chat_id, message)
        update_id += 1
