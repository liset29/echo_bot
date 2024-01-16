import requests
from demo_bots import data_base
import config as con
import functions as func

getting = requests.get(f"{con.GET_UPDATES_URL}?offset=-1").json()
update_id = requests.get(f"{con.GET_UPDATES_URL}?offset=-1").json()["result"][0]["update_id"]
send_message =con.SEND_MESSAGE_URL

while True:
    getting_updates = requests.get(f"{con.GET_UPDATES_URL}?offset={update_id + 1}").json()
    if len(getting_updates["result"]) != 0:

        if "message" in getting_updates["result"][0]:
            chat_id = getting_updates["result"][0]["message"]["chat"]["id"]
            commands = {"/delete": func.delete_message, "/start": func.send_hello, "/my_inf": func.send_users_inf,
                        "/for_danil": func.send_boss,
                        "/my_message": func.send_all_message}

            if "text" in getting_updates["result"][0]["message"]:

                message = getting_updates["result"][0]["message"]["text"]
                surname = getting_updates["result"][0]["message"]["from"]["first_name"]

                data_base.add_inf(chat_id, surname, message)

                if message in commands:
                    commands[message](chat_id)
                    update_id += 1

                else:
                    func.send_meow_message(chat_id, message)
                    update_id += 1
            else:
                func.send_danil(chat_id)
                update_id += 1

        else:
            update_id += 1
