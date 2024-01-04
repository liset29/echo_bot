import requests
from demo_bots import data_base

API_URL = "https://api.telegram.org"

token = "6773930324:AAEDAk5APfsCNxmU0dVW7cgG-lKCHz6vf1Q"
get_updates = "getUpdates"
send_message = "sendMessage"

getting = requests.get(f"{API_URL}/bot{token}/{get_updates}?offset=-1").json()
update_id = requests.get(f"{API_URL}/bot{token}/{get_updates}?offset=-1").json()["result"][0]["update_id"]
send_mes = f"https://api.telegram.org/bot{token}/{send_message}?chat_id="


def say_hy(chat_id):
    requests.get(f"{send_mes}{chat_id}&text=Привет, напиши что нибудь")


def send_message(chat_id, message):
    requests.get(f"{send_mes}{chat_id}&text={message} мяу")


def send_delete(chat_id):
    data_base.delete_inf(chat_id)
    requests.get(f"{send_mes}{chat_id}&text=Твои данные удалены")


def send_inf(chat_id):
    mess = data_base.my_inf(chat_id)
    requests.get(f"{send_mes}{chat_id}&text=Фамилия: {mess[0]}, ИМЯ: {mess[1]}, сообщение: {mess[2]}")


def send_boss(chat_id):
    caption = "страшно"
    photo_path = r'C:\Users\Тимур\danil.jpg'
    url = f'https://api.telegram.org/bot{token}/sendPhoto'
    files = {'photo': open(photo_path, 'rb')}
    params = {'chat_id': chat_id, 'caption': caption}
    response = requests.post(url, params=params, files=files)


def send_danil(chat_id):
    caption = "босс"
    photo_path = r'C:\Users\Тимур\danil2.jpg'
    url = f'https://api.telegram.org/bot{token}/sendPhoto'
    files = {'photo': open(photo_path, 'rb')}
    params = {'chat_id': chat_id, 'caption': caption}
    response = requests.post(url, params=params, files=files)


def send_all_message(chat_id, ):
    all_message = data_base.all_message(chat_id)
    requests.get(f"{send_mes}{chat_id}&text=Твои сообщения: {all_message}")


while True:
    getting_updates = requests.get(f"{API_URL}/bot{token}/{get_updates}?offset={update_id + 1}").json()
    if len(getting_updates["result"]) != 0:

        if "message" in getting_updates["result"][0]:
            commands = {"/delete": send_delete, "/start": say_hy, "/my_inf": send_inf, "/for_danil": send_boss,
                        "/my_message": send_all_message}
            if "text" in getting_updates["result"][0]["message"]:

                chat_id = getting_updates["result"][0]["message"]["chat"]["id"]
                message = getting_updates["result"][0]["message"]["text"]
                surname = getting_updates["result"][0]["message"]["from"]["first_name"]

                data_base.add_inf(chat_id, surname, message)

                if message in commands:
                    commands[message](chat_id)
                    update_id += 1

                else:
                    send_message(chat_id, message)
                    update_id += 1
            else:
                send_danil(chat_id)
                update_id += 1

        else:
            update_id += 1

    else:
        pass
