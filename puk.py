import db
import requests

API_URL = "https://api.telegram.org"

token = "6680899279:AAErsnZiHy8rUTaQLbJDcM3kvKYTQT4614c"
get_updates = "getUpdates"
send_message = "sendMessage"

getting_updates = requests.get(f"{API_URL}/bot{token}/{get_updates}")
offset = getting_updates.json()["result"][-1]["update_id"]
getting_updates = requests.get(
    f"{API_URL}/bot{token}/{get_updates}?offset={offset}"
)


def get_message(chat_id, i,message_may):
    requests.get(f"https://api.telegram.org/bot{token}/{send_message}?chat_id={chat_id}&text={message_may}")
    return i["update_id"]+1


    


while True:
    getting_updates = requests.get(f"{API_URL}/bot{token}/{get_updates}")

    for i in getting_updates.json()["result"]:
        chat_id = i["message"]["chat"]["id"]

        if "message" in i and i["update_id"] == offset:
            surname = str(i["message"]["from"]["first_name"])
            # name=str(i["message"]["from"]["last_name"])
            message = str(i["message"]["text"])
            massage_may=db.date_base(chat_id, surname, message)
            offset = get_message(chat_id, i, massage_may)
